import cv2
import numpy as np
from paddleocr import PaddleOCR
from llama_cpp import Llama

# Initialize PaddleOCR once
ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

# Load the local Mistral model
llm = Llama(model_path="mistral-7b-instruct-v0.2.Q4_K_M.gguf", n_ctx=2048, n_threads=12)

def extract_raw_text(image_path):
    """Extracts raw text from image using PaddleOCR"""
    try:
        img = cv2.imread(image_path)
        if img is None:
            return {"error": "Image not found"}
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

        result = ocr.ocr(gray, cls=True)
        text_lines = [line[-1][0] for line in result[0]]
        
        return {"text": "\n".join(text_lines)}
    
    except Exception as e:
        return {"error": str(e)}

def extract_medicine_info(ocr_text):
    """Uses the local LLM to extract structured medicine info"""
    prompt = f"""You are an expert at reading medicine strips. Given the OCR text below its not proper in text so i want you to understand the ocr text and give an proper prediction of that which make scence and correct, extract:
- Medicine name
- Manufacturing date (MFD)
- Expiry date (EXP)

Respond in JSON format.

OCR Text:

\"\"\"
{ocr_text}
\"\"\"
"""
    

    response = llm(
        prompt=prompt,
        max_tokens=512,
        stop=["</s>"]
    )

    return response["choices"][0]["text"].strip()

# Main usage
if __name__ == "__main__":
    image_path = "184.jpg"
    ocr_result = extract_raw_text(image_path)

    if "error" in ocr_result:
        print("Error:", ocr_result["error"])
    else:
        structured_info = extract_medicine_info(ocr_result["text"])
        print(structured_info)
