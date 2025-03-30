# OCR Image Processing Tool

## Description
This Python script performs Optical Character Recognition (OCR) on an image file. It includes advanced image preprocessing techniques to enhance text recognition accuracy using OpenCV and Tesseract OCR.

## Features
- Image preprocessing pipeline including:
  - Denoising
  - Contrast enhancement (CLAHE)
  - Adaptive thresholding
  - Morphological operations
  - Sharpening
- OCR text extraction using Tesseract
- Processed image preview
- Error handling for file operations

## Requirements
- Python 3.x
- Required packages:
  - Pillow (PIL)
  - pytesseract
  - pyttsx3
  - numpy
  - opencv-python (cv2)

## Installation
1. Install Tesseract OCR on your system:
   - Windows: Download from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Mac: `brew install tesseract`
   - Linux: `sudo apt-get install tesseract-ocr`

2. Install Python dependencies:
   ```bash
   pip install pillow pytesseract pyttsx3 numpy opencv-python
   ```

3. Set the Tesseract path in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = 'path_to_tesseract_executable'
   ```

## Usage
1. Place your image file (named `ocr.png`) in the same directory as the script
2. Run the script:
   ```bash
   python projectFirstStepDone.py
   ```
3. The script will:
   - Process the image
   - Display the processed image in a window
   - Print the extracted text to the console
   - Save the processed image to `~/place_to_save/place_to_save(file)/ocr_result.png`

## Notes
- The default input image name is `ocr.png` - change the `image_path` variable in the `main()` function to use a different file
- For best results, use high-quality images with clear text
- The script creates necessary directories automatically for output files

## Troubleshooting
- If you get file not found errors, verify:
  - The input image exists in the correct location
  - You have write permissions for the output directory
- For Tesseract errors, ensure:
  - Tesseract is properly installed
  - The path in `pytesseract.tesseract_cmd` is correct
