# 🔑 Cara Setup API Keys - WAJIB!

## ⚠️ PENTING: Tanpa API Keys, Hasil Akan "Simulasi/Mock"

Aplikasi Anda sudah berjalan, tapi hasil analisis masih **SIMULASI** karena API keys belum dikonfigurasi.

---

## 📝 Langkah-langkah Setup:

### 1️⃣ Dapatkan Hugging Face Token (GRATIS)

**Langkah:**
1. Buka: https://huggingface.co/settings/tokens
2. Login atau Register (gratis)
3. Klik **"New token"**
4. Nama: `review-analyzer`
5. Role: **Read** (sudah cukup)
6. Klik **"Generate a token"**
7. **COPY token** yang muncul (format: `hf_xxxxxxxxxx`)

**Free Tier:** 30,000 requests/month

---

### 2️⃣ Dapatkan Google Gemini API Key (GRATIS)

**Langkah:**
1. Buka: https://makersuite.google.com/app/apikey
2. Login dengan Google Account
3. Klik **"Create API Key"**
4. Pilih atau buat Google Cloud Project
5. **COPY API key** (format: `AIzaSyxxxxxxxxxx`)

**Free Tier:** 60 requests/minute

---

### 3️⃣ Masukkan ke File .env

**BUKA FILE:** `backend/backend_ai/.env`

**ISI DENGAN API KEYS ANDA:**

```env
# Paste token Hugging Face Anda di sini (ganti semua xxx)
HF_TOKEN=hf_paste_token_anda_disini

# Paste API key Gemini Anda di sini (ganti semua xxx)
GEMINI_KEY=AIzaSy_paste_key_anda_disini
```

**CONTOH (dengan key palsu):**
```env
HF_TOKEN=hf_QbRzJmLpWxYgKsVnFcTdMhPqRvXyZaBcDeFgH
GEMINI_KEY=AIzaSyB1234567890abcdefghijklmnopqrstuvwxyz
```

---

### 4️⃣ Restart Backend Server

**Tutup window PowerShell backend** (yang menjalankan `pserve`)

**Buka terminal baru dan jalankan:**
```powershell
cd C:\Users\Arcel\Documents\tugas_ai\backend\backend_ai
pserve development.ini --reload
```

**ATAU klik tombol restart di VS Code terminal**

---

### 5️⃣ Test Aplikasi

1. **Refresh browser** (F5) di `http://localhost:5173`
2. **Input review:**
   - Nama Produk: `iPhone 15 Pro`
   - Review: `Great camera quality but battery drains too fast`
3. **Klik "Analyze Review"**

**Hasil yang BENAR:**
- ✅ Sentiment: POSITIVE atau NEGATIVE (sesuai AI analysis)
- ✅ Confidence: angka realistis (80%-99%)
- ✅ Key Points: bullet points yang relevan dengan review (BUKAN "Poin simulasi")

**Hasil SIMULASI (API key salah):**
- ❌ Key Points: "Poin simulasi 1", "Poin simulasi 2 (Backend Mati)"
- ❌ Ini tandanya API keys tidak valid

---

## 🔍 Troubleshooting

### Problem: Masih muncul "Backend Mati"
**Solusi:**
1. Pastikan file `.env` ada di `backend/backend_ai/.env`
2. Cek API keys tidak ada spasi atau karakter aneh
3. Pastikan format benar: `HF_TOKEN=hf_xxx` (TANPA spasi sebelum/sesudah `=`)
4. Restart backend server

### Problem: Error "Invalid API Key"
**Solusi:**
1. **Hugging Face:** Cek token masih valid di https://huggingface.co/settings/tokens
2. **Gemini:** Cek API key di https://makersuite.google.com/app/apikey
3. Generate token/key baru jika perlu
4. Paste ulang ke `.env`

### Problem: Error "Model is loading"
**Solusi:**
- Model Hugging Face perlu warm-up pertama kali (~20 detik)
- Tunggu sebentar, lalu coba lagi
- Ini normal untuk free tier

---

## ✅ Cara Verifikasi API Keys Bekerja

### Test Manual dengan Python:

```python
# Test Hugging Face
import requests
HF_TOKEN = "hf_your_token_here"
url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}
response = requests.post(url, headers=headers, json={"inputs": "I love this!"})
print(response.json())
# Expected: [{"label": "POSITIVE", "score": 0.9998}]
```

```python
# Test Gemini
import google.generativeai as genai
GEMINI_KEY = "AIzaSy_your_key_here"
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Extract 3 bullet points: Great phone")
print(response.text)
# Expected: Bullet points output
```

---

## 📌 Kesimpulan

**SEBELUM setup API keys:**
- ❌ Hasil: Simulasi/Mock
- ❌ "Backend Mati" muncul
- ❌ Key points: "Poin simulasi 1, 2"

**SETELAH setup API keys:**
- ✅ Hasil: AI analysis sebenarnya
- ✅ Sentiment akurat
- ✅ Key points relevan dengan review

**File .env HARUS diisi dengan API keys yang VALID!**

---

## 🎯 Lokasi File Penting

```
tugas_ai/
└── backend/
    └── backend_ai/
        └── .env          👈 ISI FILE INI!
```

**Setelah diisi, RESTART backend server!**

Selamat mencoba! 🚀
