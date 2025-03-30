from PIL import Image
import pytesseract
import pyttsx3
import os
import numpy as np
import cv2

pytesseract.pytesseract.tesseract_cmd = 'tesseract_path'

def preprocess_image_with_cv2(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"{image_path} file did not found")

    denoised = cv2.fastNlMeansDenoising(img, h=10, templateWindowSize=7, searchWindowSize=21)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrast_enhanced = clahe.apply(denoised)

    thresh = cv2.adaptiveThreshold(contrast_enhanced, 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2)
    kernel = np.ones((1,1), np.uint8)
    processed = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    gaussian = cv2.GaussianBlur(processed, (0,0), 3.0)
    sharpened = cv2.addWeighted(processed, 1.5, gaussian, -0.5, 0)

    output_path = os.path.join(os.path.expanduser('~'), 'place_to_save', 'place_to_save(file)', 'ocr_result.png')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, sharpened)
    return sharpened

def main():
    image_path = 'ocr.png'#test_image

    try:

        processed_img = preprocess_image_with_cv2(image_path)

        text = pytesseract.image_to_string(processed_img)

        print("Tanınan Metin:\n", text)

        cv2.imshow('Processed Image', processed_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error Happened: {str(e)}")

if __name__ == "__main__":
    main()