# API Keys Setup Guide

## 1. Hugging Face Token 🤗

### Cara Mendapatkan:
1. Buka https://huggingface.co/
2. Register/Login akun
3. Klik avatar (kanan atas) → **Settings**
4. Pilih **Access Tokens** di sidebar
5. Klik **New token**
6. Beri nama (contoh: "review-analyzer")
7. Pilih role: **Read**
8. Klik **Generate token**
9. **COPY token yang muncul** (hf_xxxxxxxxxx)

### Model yang Digunakan:
- `distilbert-base-uncased-finetuned-sst-2-english`
- Pre-trained untuk sentiment analysis
- Return: POSITIVE/NEGATIVE dengan confidence score

---

## 2. Google Gemini API Key 🔮

### Cara Mendapatkan:
1. Buka https://makersuite.google.com/app/apikey
2. Login dengan Google account
3. Klik **Create API Key**
4. Pilih/buat Google Cloud Project
5. **COPY API key yang muncul** (AIzaSy_xxxxxxxxxx)

### Model yang Digunakan:
- `gemini-1.5-flash`
- Untuk extract key points dari review
- Return: Bullet points summary

---

## 3. Setup di Aplikasi

### Edit file `.env`
```bash
cd backend/backend_ai
nano .env  # atau buka dengan text editor
```

### Paste API Keys:
```bash
HF_TOKEN=hf_your_actual_token_paste_here
GEMINI_KEY=AIzaSy_your_actual_key_paste_here
```

**PENTING:** Jangan commit file `.env` ke Git!

---

## 4. Verifikasi API Keys

### Test Hugging Face:
```python
import requests

HF_TOKEN = "hf_your_token"
HF_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

response = requests.post(HF_API_URL, headers=headers, json={"inputs": "I love this product!"})
print(response.json())
# Expected: [{"label": "POSITIVE", "score": 0.9998}]
```

### Test Gemini:
```python
import google.generativeai as genai

GEMINI_KEY = "AIzaSy_your_key"
genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Extract 3 bullet points: Great phone but expensive")
print(response.text)
# Expected: Bullet points output
```

---

## 5. Free Tier Limits

### Hugging Face Free:
- 30,000 requests/month
- Rate limit: ~1 request/second
- Cukup untuk development & testing

### Gemini Free:
- 60 requests/minute
- 1500 requests/day
- Unlimited untuk low-volume usage

**Untuk production dengan traffic tinggi, pertimbangkan upgrade.**

---

## Troubleshooting

### Error: "Invalid token" (Hugging Face)
- Cek token masih valid: https://huggingface.co/settings/tokens
- Pastikan format: `hf_xxxxx` (ada prefix `hf_`)
- Generate token baru jika expired

### Error: "API key not valid" (Gemini)
- Cek API key: https://makersuite.google.com/app/apikey
- Pastikan Google Cloud project sudah dibuat
- Enable Gemini API di Google Cloud Console

### Error: "Model is loading"
- Model Hugging Face perlu warm-up pertama kali (~20 detik)
- Coba request lagi setelah beberapa detik
- Ini normal untuk free tier

---

## Alternatif Models (Optional)

### Hugging Face Alternatives:
- `cardiffnlp/twitter-roberta-base-sentiment` (Twitter sentiment)
- `nlptown/bert-base-multilingual-uncased-sentiment` (1-5 stars)

### Gemini Alternatives:
- `gemini-1.5-pro` (lebih akurat, lebih lambat)
- OpenAI GPT-4 (perlu payment)
- Anthropic Claude (perlu API key)

Ganti di file `views/default.py` jika ingin eksperimen.
