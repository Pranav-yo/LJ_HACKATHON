# AI Finance Assistant 💰

## Overview
This project is a prototype of an AI-powered personal finance assistant using **Gemini 2.0 API**.

It allows users to:
- Chat with AI about finances
- Control data permissions (assets, liabilities, transactions, EPF, credit score, investments)
- Get actionable financial insights

## Files
- `App.py` → Main Streamlit application
- `finance.json` → Mock financial dataset
- `requirements.txt` → Python dependencies

## Setup
```bash
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
streamlit run App.py
```

## Note
Replace `YOUR_GEMINI_API_KEY` in `App.py` with your actual API key.
