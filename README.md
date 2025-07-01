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


