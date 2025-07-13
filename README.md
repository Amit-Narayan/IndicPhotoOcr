# IndicPhotoOCR

**IndicPhotoOCR** is a multilingual scene-text recognition system built for extracting text from natural scene images in Indian languages, such as Hindi and English.  
This project was developed during my internship under the guidance of **Mr. Anik De**.

---

## 📁 Project Structure

IndicPhotoOCR/
├── Annotated_Dataset/ # JSON annotations with polygon coordinates and language labels
├── Annotated_images/ # Images with polygon-marked text regions
├── Evaluation/ # Contains evaluation scripts and data
├── Ocr_result/ # Output JSON/CSV from OCR
├── Raw_images/ # Raw input images
├── Script/ # Core OCR and analysis scripts
├── LICENSE # MIT License
├── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Features

- ✅ Script-aware text recognition for Indian languages (e.g., Hindi, English)
- ✅ Word-wise OCR with bounding polygon detection
- ✅ Auto language/script detection for each text region
- ✅ Results exported in JSON and CSV format
- ✅ Evaluation metrics included (WRR, Accuracy)

---

## ⚙️ Installation

```bash
git clone https://github.com/Amit-Narayan/IndicPhotoOcr
cd IndicPhotoOCR
pip install -r requirements.txt
🛠️ Usage
Run OCR on a single image:

python
Copy
Edit
from IndicPhotoOCR.ocr import OCR

ocr_system = OCR(verbose=True, identifier_lang="auto", device="cpu")
words = ocr_system.ocr("c:/Users/User/Downloads/IndicPhotoOcr/img.jpg")
Batch OCR over a folder:

bash
Copy
Edit
python run_on_folder.py

📊 Results and Analysis
The OCR system was evaluated on a set of annotated images across multiple scripts.

Language	Recognition Accuracy	Word Recognition Rate (WRR)
Hindi	      73.9%	                 0.737
English	      77.5%	                 0.775
Overall	      77.7% 	             0.757

🔍 Observations
Hindi script detection was also effective despite script complexity.

WRR shows the system's ability to match ground truth at word level across both languages.

🙏 Acknowledgements
Internship Guide: Mr. Anik De
Annotation Platform: Label Studio

📄 License
This project is licensed under the MIT License

🔗 Repository Link
🔗 GitHub: https://github.com/Bhashini-IITJ/IndicPhotoOCR