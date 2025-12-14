# 🤖 Product Review Analyzer

**AI-Powered Sentiment Analysis & Insight Extraction System**  
**✅ STATUS: APLIKASI LENGKAP & SIAP DIGUNAKAN!**

Proyek Tugas AI - Pengembangan Aplikasi Web Berbasis AI  
Menggunakan: Pyramid Framework (Backend) + React + Vite (Frontend) + Hugging Face + Google Gemini AI

---

## ✅ Fitur yang Sudah Lengkap

- [x] **User dapat input product review (text)** - Form input di frontend
- [x] **Analyze sentiment (positive/negative/neutral)** - Hugging Face DistilBERT
- [x] **Extract key points** - Google Gemini AI (gemini-1.5-flash)
- [x] **Display hasil analysis di React frontend** - Modern UI dengan real-time updates
- [x] **Save results ke database** - SQLite (dev) / PostgreSQL (production)

**SEMUA FITUR SUDAH TERIMPLEMENTASI!** 🎉

---

## 🏃‍♂️ Quick Start (2 Menit)

### 1. Setup Backend
```bash
cd backend/backend_ai
pip install -e .

# Edit .env dengan API keys Anda:
# HF_TOKEN=your_huggingface_token
# GEMINI_KEY=your_gemini_key

initialize_backend_db development.ini
pserve development.ini
```

### 2. Setup Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Buka Browser
```
http://localhost:5173
```

**Status akan menampilkan ✅ Terhubung ke Backend**

---

## 📋 Deskripsi Proyek

Aplikasi web yang menganalisis review produk secara otomatis menggunakan teknologi AI untuk:
- ✅ **Sentiment Analysis** (Positive/Negative) menggunakan Hugging Face Transformers
- 🧠 **Key Points Extraction** (Poin penting dari review) menggunakan Google Gemini AI
- 📊 **Visualisasi hasil analisis** dengan confidence score
- 💾 **Penyimpanan data** review dan hasil analisis ke database

---

## 🛠️ Teknologi yang Digunakan

### Backend
- **Framework:** Pyramid Web Framework (Python)
- **Database:** SQLite (dev) / PostgreSQL (production)
- **ORM:** SQLAlchemy
- **AI Services:**
  - Hugging Face API (Sentiment Analysis)
  - Google Gemini 1.5 Flash (Key Points)

### Frontend
- **Framework:** React 19
- **Build Tool:** Vite 7
- **HTTP Client:** Axios
- **Styling:** Custom CSS

---

## 📦 Prerequisites

Pastikan sudah terinstall:
- **Python 3.8+**
- **Node.js 18+** & npm
- **Git** (untuk version control)

---

## 🔧 Setup Backend (Detailed)

### Step 1: Navigasi ke folder backend
```bash
cd backend/backend_ai
```

### Step 2: Buat Virtual Environment (Opsional tapi recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### Step 3: Install Dependencies
```bash
pip install -e .
```

Dependencies yang terinstall:
- `requests` - HTTP client untuk Hugging Face API
- `google-generativeai` - Gemini AI SDK
- `psycopg2-binary` - PostgreSQL driver
- `python-dotenv` - Environment variables
- `pyramid` - Web framework
- `sqlalchemy` - ORM database

### Step 4: Konfigurasi API Keys

**Edit file `.env`:**
```bash
# Hugging Face Token
# Dapatkan dari: https://huggingface.co/settings/tokens
HF_TOKEN=hf_your_actual_token_here

# Google Gemini API Key
# Dapatkan dari: https://makersuite.google.com/app/apikey
GEMINI_KEY=AIzaSy_your_actual_key_here
```

**Cara Mendapatkan API Keys:**

**Hugging Face (Gratis):**
1. Buka https://huggingface.co/settings/tokens
2. Klik "New token"
3. Beri nama: `review-analyzer`
4. Pilih role: **Read**
5. Klik "Generate token"
6. **COPY** token (`hf_xxxxxxxxxx`)

**Google Gemini (Gratis):**
1. Buka https://makersuite.google.com/app/apikey
2. Login dengan Google Account
3. Klik "Create API Key"
4. **COPY** API key (`AIzaSyxxxxxxxxxx`)

### Step 5: Setup Database

**Untuk Development (SQLite - default):**
```bash
initialize_backend_db development.ini
```

**Untuk Production (PostgreSQL):**
```bash
# 1. Create database
CREATE DATABASE review_db;

# 2. Edit development.ini - uncomment & update:
sqlalchemy.url = postgresql://postgres:your_password@localhost:5432/review_db

# 3. Initialize
initialize_backend_db development.ini
```

### Step 6: Jalankan Backend Server
```bash
pserve development.ini
```

✅ Server akan berjalan di: **http://localhost:6543**

---

## 🎨 Setup Frontend (Detailed)

### Step 1: Navigasi ke folder frontend
```bash
cd frontend
```

### Step 2: Install Dependencies
```bash
npm install
```

Dependencies:
- React 19 - UI library
- Vite 7 - Ultra-fast build tool
- Axios - HTTP client

### Step 3: Jalankan Development Server
```bash
npm run dev
```

✅ Frontend akan berjalan di: **http://localhost:5173**

---

## 🚀 Cara Menggunakan Aplikasi

1. **Pastikan Backend dan Frontend berjalan** (2 terminal berbeda)
2. Buka browser ke **http://localhost:5173**
3. Status "✅ Terhubung ke Backend" akan muncul jika koneksi sukses
4. **Input review:**
   - Masukkan nama produk (contoh: "iPhone 15 Pro")
   - Paste review customer
   - Klik tombol "🚀 Analyze Review"
5. **Hasil analisis akan muncul** dengan:
   - Sentiment (POSITIVE/NEGATIVE)
   - Confidence score (persentase akurasi)
   - Key points (poin penting dari AI)
   - Timestamp (tanggal analisis)

---

## 📁 Struktur Proyek

```
tugas_ai/
├── .gitignore                      # Git ignore (API keys safe)
├── README.md                       # File ini (dokumentasi)
├── backend/
│   └── backend_ai/
│       ├── .env                    # API keys (JANGAN commit!)
│       ├── .gitignore              # Backend ignore rules
│       ├── development.ini         # Server config
│       ├── setup.py                # Dependencies list
│       ├── backend_ai/
│       │   ├── __init__.py         # CORS & app config
│       │   ├── routes.py           # Route definitions
│       │   ├── views/
│       │   │   └── default.py      # API endpoints logic ⭐
│       │   ├── models/
│       │   │   └── mymodel.py      # Review model (SQLAlchemy)
│       │   ├── static/
│       │   ├── templates/
│       │   └── alembic/            # Database migrations
│       ├── tests/
│       └── review.sqlite           # Database (auto-generated)
│
├── frontend/
│   ├── .gitignore                  # Frontend ignore
│   ├── package.json                # Dependencies
│   ├── vite.config.js              # Vite config
│   ├── index.html                  # HTML entry
│   └── src/
│       ├── App.jsx                 # Main component ⭐
│       ├── App.css                 # Styling
│       ├── main.jsx                # React init
│       ├── index.css               # Global CSS
│       └── assets/                 # Images, icons
│
└── README.md                       # File ini (DOKUMENTASI LENGKAP)
```

---

## 🔌 API Endpoints (Detailed)

### POST `/api/analyze-review` - Analyze & Save Review
Analyze sentimen dan extract key points dari review, kemudian simpan ke database.

**Request:**
```json
{
  "product_name": "iPhone 15 Pro",
  "review_text": "Kameranya sangat bagus dan baterainya tahan lama, tapi harganya terlalu mahal"
}
```

**Response (Success - 200):**
```json
{
  "id": 1,
  "product_name": "iPhone 15 Pro",
  "review_text": "Kameranya sangat bagus dan baterainya tahan lama, tapi harganya terlalu mahal",
  "sentiment": "POSITIVE",
  "confidence": 0.87,
  "key_points": "- Kamera berkualitas premium\n- Durasi baterai lebih lama\n- Harga premium/mahal",
  "created_at": "2025-12-13"
}
```

**Features:**
- ✅ Accepts JSON payload
- ✅ Validates input (required fields)
- ✅ Calls Hugging Face API for sentiment
- ✅ Calls Gemini AI for key points
- ✅ Saves to database
- ✅ Returns complete result
- ✅ Error handling with status 500

---

### GET `/api/reviews` - Get All Reviews
Ambil semua review yang pernah dianalisis (newest first).

**Request:**
```
GET http://localhost:6543/api/reviews
```

**Response:**
```json
[
  {
    "id": 1,
    "product_name": "iPhone 15 Pro",
    "review_text": "Kameranya sangat bagus dan baterainya tahan lama, tapi harganya terlalu mahal",
    "sentiment": "POSITIVE",
    "confidence": 0.87,
    "key_points": "- Kamera berkualitas premium\n- Durasi baterai lebih lama\n- Harga premium",
    "created_at": "2025-12-13"
  },
  {
    "id": 2,
    "product_name": "Samsung S24",
    "review_text": "Display sangat jelek, build quality buruk sekali",
    "sentiment": "NEGATIVE",
    "confidence": 0.92,
    "key_points": "- Display berkualitas rendah\n- Material murah\n- Tidak recommended",
    "created_at": "2025-12-13"
  }
]
```

**Features:**
- ✅ Returns all reviews
- ✅ Ordered by newest first (DESC)
- ✅ JSON format
- ✅ Complete review objects

---

## 🧪 Testing API (dengan cURL/PowerShell)

### Test Analyze Review:
```bash
curl -X POST http://localhost:6543/api/analyze-review \
  -H "Content-Type: application/json" \
  -d '{"product_name":"Test Product","review_text":"Great product, highly recommend!"}'
```

### Test Get Reviews:
```bash
curl http://localhost:6543/api/reviews
```

---

## 📦 Database Schema (SQLAlchemy)

### Table: `reviews`

```python
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(50))  # POSITIVE/NEGATIVE/NEUTRAL
    confidence = Column(Float)      # 0.0 - 1.0
    key_points = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
```

| Column        | Type      | Description                    |
|---------------|-----------|--------------------------------|
| id            | Integer   | Primary Key (Auto-increment)   |
| product_name  | String    | Nama produk                    |
| review_text   | Text      | Isi review customer            |
| sentiment     | String    | POSITIVE / NEGATIVE / NEUTRAL  |
| confidence    | Float     | Score kepercayaan (0.0 - 1.0)  |
| key_points    | Text      | Poin penting dari AI (bullets) |
| created_at    | DateTime  | Timestamp (Auto-generated)     |

---

## ✅ Requirements Checklist

### Functional Requirements

✅ **1. User dapat input product review (text)**
- [x] Form input di frontend (App.jsx)
- [x] 2 field: product_name & review_text
- [x] Form validation (required fields)
- [x] Modern UI dengan textarea

✅ **2. Analyze sentiment (positive/negative/neutral) dengan Hugging Face**
- [x] Model: distilbert-base-uncased-finetuned-sst-2-english
- [x] API integration dengan requests
- [x] Output: POSITIVE/NEGATIVE + confidence score
- [x] Error handling untuk invalid responses

✅ **3. Extract key points dengan Google Gemini**
- [x] Model: gemini-1.5-flash
- [x] Library: google-generativeai
- [x] Output: Formatted bullet points
- [x] Fallback mechanism jika error

✅ **4. Display hasil analysis di React frontend**
- [x] Real-time display dengan cards
- [x] Sentiment badge (color-coded)
- [x] Confidence percentage
- [x] Key points formatting
- [x] Timestamp tracking
- [x] Modern dark theme UI
- [x] Loading states

✅ **5. Save results ke database**
- [x] SQLAlchemy ORM
- [x] Auto-save setelah analisis
- [x] Support SQLite (dev) & PostgreSQL (prod)
- [x] Auto-migrations dengan Alembic

### Technical Requirements

✅ **API Endpoints**
- [x] POST /api/analyze-review - Working
- [x] GET /api/reviews - Working
- [x] CORS enabled - Working

✅ **Error Handling**
- [x] Try-catch blocks
- [x] HTTP error codes
- [x] Fallback to mock data
- [x] User-friendly messages

✅ **Loading States**
- [x] Button disabled saat loading
- [x] Text berubah "Sedang Menganalisis..."
- [x] Loading state clear after done

✅ **Security**
- [x] API keys di .env (not hardcoded)
- [x] .gitignore untuk protect secrets
- [x] CORS configuration

---

## 🐛 Troubleshooting

### Backend tidak bisa start?
```bash
# Cek virtual environment aktif
venv\Scripts\activate

# Reinstall dependencies
pip install -e .

# Cek port 6543 tidak digunakan
netstat -ano | findstr :6543
```

### Frontend tidak connect ke backend?
- Pastikan backend running di port 6543
- Cek console browser (F12) untuk error messages
- Verifikasi API URL di App.jsx

### Error "API Keys Invalid"?
```bash
# 1. Verifikasi token Hugging Face
https://huggingface.co/settings/tokens

# 2. Verifikasi Gemini API key
https://makersuite.google.com/app/apikey

# 3. Pastikan .env file exists & readable
```

### Database error saat inisialisasi?
```bash
# Hapus database lama
rm review.sqlite

# Buat ulang
initialize_backend_db development.ini
```

### Port already in use?
```bash
# Kill process di port 6543
netstat -ano | findstr :6543
taskkill /PID <PID> /F

# Atau gunakan port berbeda di development.ini
```

### Mode Simulasi muncul?
- Backend offline/tidak respond
- Frontend auto-fallback ke mock data
- Data tidak tersimpan ke database
- Restart backend untuk normal mode

---

## 📊 Fitur Mode Simulasi

Jika backend offline, frontend otomatis masuk **Mode Simulasi**:
- ⚠️ Warning badge di header
- Data dummy untuk demo
- Sentiment analysis sederhana (keyword-based)
- Tidak ada data yang tersimpan ke database

---

## 🚀 Production Deployment

### Backend Deployment

1. **Switch to PostgreSQL:**
   ```bash
   pip install psycopg2-binary
   # Update development.ini dengan PostgreSQL URL
   ```

2. **Use Production Config:**
   ```bash
   pserve production.ini
   ```

3. **Setup Environment Variables:**
   - HF_TOKEN
   - GEMINI_KEY
   - Database URL (PostgreSQL)

4. **Deploy with Gunicorn/uWSGI:**
   ```bash
   gunicorn --paste production.ini
   ```

### Frontend Deployment

1. **Build for Production:**
   ```bash
   npm run build
   ```

2. **Deploy dist/ folder to hosting:**
   - Vercel
   - Netlify
   - GitHub Pages
   - AWS S3
   - Etc.

3. **Update API_URL in App.jsx** untuk production endpoint

---

## 📚 Additional Resources

- [Hugging Face API Docs](https://huggingface.co/docs/api-inference/en/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Pyramid Framework](https://trypyramid.com/)
- [React Documentation](https://react.dev)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)

---

## 📝 Catatan Pengembang

- Database file (`review.sqlite`) otomatis terbuat saat first run
- API keys bisa disimpan di .env (development) atau environment variables (production)
- Frontend menggunakan Axios untuk HTTP requests
- CORS sudah dikonfigurasi untuk localhost development

---

## 🎓 Tech Insights

### Mengapa Pyramid Framework?
- Lightweight dan fleksibel untuk REST API
- Dukungan SQLAlchemy yang mature
- Mudah konfigurasi CORS untuk SPA

### Mengapa SQLite?
- Zero configuration (auto-create file)
- Cocok untuk development
- Bisa upgrade ke PostgreSQL tanpa ubah kode

### Mengapa React?
- Component-based architecture
- Real-time state management
- Large ecosystem & community

### Mengapa Vite?
- Ultra-fast build tool
- Instant HMR (Hot Module Replacement)
- Production-ready bundling

---

## 📄 License

Proyek ini dibuat untuk keperluan **Tugas Akhir Mata Kuliah AI**.

---

## 👨‍💻 Author

**Arcel** - Tugas AI (Desember 2025)

Jika ada pertanyaan, silakan hubungi atau buat issue.

---

**Built with ❤️ using Python, React, AI, and ☕ Coffee**

