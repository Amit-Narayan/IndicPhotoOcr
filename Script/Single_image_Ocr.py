from IndicPhotoOCR.ocr import OCR

# Initialize OCR system
ocr_system = OCR(verbose=True, identifier_lang="auto", device="cpu")
words = ocr_system.ocr("c:/Users/User/Downloads/IndicPhotoOcr/img.jpg")
print(words)