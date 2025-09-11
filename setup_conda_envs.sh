#!/bin/bash
# setup_conda_envs.sh

echo "Creating Python Main environment (3.12)..."
conda create -n python_main python=3.12 -y
conda activate python_main
conda install numpy pandas matplotlib seaborn jupyter notebook scipy scikit-learn requests beautifulsoup4 -y
pip install openai langchain streamlit gradio transformers torch fastapi uvicorn sqlalchemy pydantic-settings
conda deactivate

echo "Creating OCR Projects environment (3.9)..."
conda create -n ocr_projects python=3.9 -y
conda activate ocr_projects
conda install opencv pillow numpy matplotlib -y
pip install pytesseract easyocr paddlepaddle paddleocr tensorflow torch torchvision
conda deactivate

echo "All environments created successfully!"
echo ""
echo "사용법:"
echo "- 파이썬 기초/심화/챗봇/FastAPI: conda activate python_main"
echo "- OCR 기초/심화: conda activate ocr_projects"
