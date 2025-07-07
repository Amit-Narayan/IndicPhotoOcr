from IndicPhotoOCR.ocr import OCR

# Initialize OCR system
ocr_system = OCR(verbose=True, identifier_lang="auto", device="cpu")
words = ocr_system.ocr("c:/Users/User/Downloads/IndicPhotoOcr/Annotated_images/c37e43b7-IMG_20250601_131203.jpg")
print(words)