# MediTrack
# Medicine Strip Information Extractor

This project extracts structured medicine details from photos of medicine blister packs (medicine strips). It combines state-of-the-art OCR (Optical Character Recognition) using [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) with a local LLM (Mistral) for text understanding and information extraction.

---

## Features

- Extract raw text from medicine strip images via OCR
- Clean up and interpret OCR text using a local LLM
- Return structured JSON containing:
  - Medicine name
  - Manufacturing date (MFD)
  - Expiry date (EXP)

---

## Example Images

This repo has been tested on strips like:

- Ginseng, Multivitamins and Multiminerals Capsules
  - MFD: 09/2024
  - EXP: 08/2026
- Aceclofenac & Paracetamol Tablets
  - MFD: 09/2024
  - EXP: 08/2026

Example strips from Jan Aushadhi (PMBI) are included for testing purposes.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/medicine-strip-extractor.git
cd medicine-strip-extractor




Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\Scripts\activate      # On Windows
Install dependencies
bash
Copy
Edit
pip install paddleocr opencv-python numpy llama-cpp-python
Note:

This project uses PaddleOCR with English language support.

The LLM used is a local model (e.g. Mistral 7B), quantized to fit local hardware constraints.

Usage
Run the main script:

bash
Copy
Edit
python W1.py
This will:

Load the medicine strip image (default: 184.jpg)

Extract text via OCR

Parse it using the local LLM

Print the structured JSON output

File Details
W1.py
Core script containing:

extract_raw_text(image_path)
Reads the image and extracts text using PaddleOCR.

extract_medicine_info(ocr_text)
Feeds OCR text into the Mistral LLM for structured extraction.

Example output:

json
Copy
Edit
{
  "Medicine name": "Ginseng, Multivitamins and Multiminerals Capsules",
  "Manufacturing date": "09/2024",
  "Expiry date": "08/2026"
}
Project Architecture
pgsql
Copy
Edit
Image (.jpg)
   ↓
PaddleOCR → Extract raw text
   ↓
Mistral LLM → Interpret OCR text → Return JSON info
Model Details
OCR → PaddleOCR

LLM → Local Mistral 7B Instruct model:

Model file: mistral-7b-instruct-v0.2.Q4_K_M.gguf

Loaded via llama-cpp-python

Customizing Input
To run the pipeline on your own images, change the following in W1.py:

python
Copy
Edit
image_path = "your_image.jpg"
Limitations
OCR may occasionally misread characters in low-quality images.

The LLM’s accuracy depends on how well the OCR captures the text.

Processing large images or models may require significant RAM.

License
This project is under the MIT License.

Acknowledgements
PaddleOCR

llama-cpp-python

Mistral

Pharmaceuticals & Medical Devices Bureau of India (PMBI)
