import os
import json
import torch
from IndicPhotoOCR.ocr import OCR

# Initialize OCR system
ocr_system = OCR(verbose=True, identifier_lang="auto", device="cpu")

input_dir = "c:/Users/User/Downloads/IndicPhotoOcr/Annotated_images"
output_json = "results.json"

all_results = {}

# Loop through all images in the directory
for img_name in os.listdir(input_dir):
    if img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_dir, img_name)

        try:
            print(f"\n=== Processing {img_name} ===")
            results = ocr_system.ocr(img_path)

            image_texts = []

            for item in results:
                if isinstance(item, list):
                    image_texts.append(" ".join(item))
                elif isinstance(item, dict):
                    image_texts.append(item.get("txt", ""))

            all_results[img_name] = image_texts
            print(f"[✓] Done: {img_name}")

        except Exception as e:
            print(f"[!] Failed on {img_name}: {e}")

# Save all results to JSON file
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f"\n✅ OCR complete. JSON saved at: {os.path.abspath(output_json)}")
