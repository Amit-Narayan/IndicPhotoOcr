✅ README.md for IndicPhotoOcr
markdown
Copy
Edit
# IndicPhotoOcr - Scene Text Recognition in Indian Scripts 🇮🇳

This project demonstrates the use of the [IndicPhotoOCR](https://github.com/AI4Bharat/IndicPhotoOCR) pipeline to detect and recognize text in natural scene images containing Indian scripts. It includes annotations, OCR outputs, evaluation, and scripts.

## 🗂️ Project Structure

IndicPhotoOcr/
├── Annotated_Dataset/ # JSON files with polygon annotations & script labels
├── Annotated_images/ # Input images with visual annotation overlays
├── Raw_images/ # Original images without annotation
├── Ocr_result/ # OCR output (results.json, predictions.csv, etc.)
├── Script/ # Python scripts used to run OCR, compare, save outputs
├── Evaluations.xlsx # Evaluation sheet with accuracy, mismatch stats
└── README.md # This file

markdown
Copy
Edit

## 📝 Workflow Summary

1. **Image Collection**  
   Scene images collected locally containing multilingual text (e.g., shop boards, banners).

2. **Annotation**  
   Annotated using Label Studio. Saved polygons and labels in `Annotated_Dataset/`.

3. **OCR Pipeline**  
   Used [IndicPhotoOCR](https://github.com/AI4Bharat/IndicPhotoOCR) to:
   - Detect text regions
   - Identify script
   - Recognize text

4. **Results**  
   OCR output stored in `Ocr_result/` as:
   - `results.json` (script + recognized text per image)
   - `predictions.csv` (optional CSV output)

5. **Evaluation**  
   Compared OCR predictions with ground-truth annotations and compiled stats in `Evaluations.xlsx`.

## 🔁 How to Re-run OCR

1. Place new images in `Raw_images/`
2. Run the script in `Script/`:
   ```bash
   python Script/run_on_folder.py
Output will be saved in Ocr_result/

✅ Example OCR Output Format (JSON)
json
Copy
Edit
{
  "IMG_001.jpg": [
    {
      "script": "Hindi",
      "text": "दक्षिण बिहार ग्रामीण बैंक"
    },
    {
      "script": "English",
      "text": "hostel admission open"
    }
  ]
}
📈 Evaluation
Accuracy and other comparison metrics between predictions and annotations are documented in:

Copy
Edit
Evaluations.xlsx
🧠 Model & Tools Used
Model: IndicPhotoOCR

Annotation: Label Studio

Language Detection: Automatic via built-in script classifier

📌 Credits
IndicPhotoOCR: Developed by AI4Bharat