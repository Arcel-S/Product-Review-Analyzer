# 🚀 Backend - Product Review Analyzer

Backend API untuk sentiment analysis dan key points extraction menggunakan Pyramid Framework.

## 📋 Struktur Backend

```
backend/
└── backend_ai/
    ├── backend_ai/              # Aplikasi utama
    │   ├── __init__.py          # App initialization + CORS
    │   ├── routes.py            # Route configuration
    │   ├── views/
    │   │   ├── default.py       # API endpoints & AI logic ⭐
    │   │   └── notfound.py
    │   ├── models/
    │   │   ├── mymodel.py       # Review model ⭐
    │   │   └── meta.py
    │   ├── scripts/
    │   │   └── initialize_db.py # Database initialization
    │   ├── alembic/             # Database migrations
    │   ├── static/              # CSS files
    │   └── templates/           # HTML templates
    ├── tests/                   # Unit tests
    ├── .env                     # API keys (JANGAN COMMIT!) ⭐
    ├── development.ini          # Development config
    ├── setup.py                 # Dependencies
    └── pytest.ini               # Test config
```

## 🔧 Setup

### 1. Install Dependencies
```bash
cd backend/backend_ai
pip install -e .
```

### 2. Configure API Keys
Edit `.env` file:
```env
HF_TOKEN=your_huggingface_token_here
GEMINI_KEY=your_gemini_api_key_here
```

Dapatkan dari:
- **Hugging Face:** https://huggingface.co/settings/tokens
- **Gemini:** https://makersuite.google.com/app/apikey

### 3. Initialize Database
```bash
initialize_backend_db development.ini
```

### 4. Run Backend Server
```bash
pserve development.ini
```

✅ Backend akan berjalan di: **http://localhost:6543**

---

## 📡 API Endpoints

### POST `/api/analyze-review`
Analyze review dan simpan ke database

**Request:**
```json
{
  "product_name": "Infinix Note 60",
  "review_text": "Baterainya boros dan gampaing panas"
}
```

**Response:**
```json
{
  "id": 1,
  "product_name": "Infinix Note 60",
  "review_text": "Baterainya boros dan gampaing panas",
  "sentiment": "NEGATIVE",
  "confidence": 0.84,
  "key_points": "- Baterainya boros\n- Gampaing panas",
  "created_at": "2025-12-14"
}
```

### GET `/api/reviews`
Ambil semua review

**Response:**
```json
[
  {
    "id": 1,
    "product_name": "Infinix Note 60",
    "review_text": "Baterainya boros dan gampaing panas",
    "sentiment": "NEGATIVE",
    "confidence": 0.84,
    "key_points": "...",
    "created_at": "2025-12-14"
  }
]
```

---

## 🧠 AI Integration

### Sentiment Analysis
- **Provider:** Keyword-based (Indonesian & English)
- **Model:** Custom sentiment keywords
- **Output:** POSITIVE / NEGATIVE / NEUTRAL + confidence score
- **File:** `backend_ai/views/default.py` (lines 21-55)

**Keywords Detection:**
- Positive: `baik`, `bagus`, `hebat`, `cepat`, `lancar`, dll
- Negative: `jelek`, `buruk`, `boros`, `panas`, `lambat`, dll

### Key Points Extraction
- **Provider:** Google Gemini AI
- **Model:** `gemini-1.5-flash`
- **Fallback:** Extract dari sentences review
- **File:** `backend_ai/views/default.py` (lines 62-74)

---

## 💾 Database

### Model: Review
```python
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    review_text = Column(Text, nullable=False)
    sentiment = Column(String(50))          # POSITIVE/NEGATIVE/NEUTRAL
    confidence = Column(Float)              # 0-1
    key_points = Column(Text)               # Extracted points
    created_at = Column(DateTime)           # Timestamp
```

### Database Options

**Development (SQLite):**
```ini
sqlalchemy.url = sqlite:///%(here)s/review.sqlite
```

**Production (PostgreSQL):**
```ini
sqlalchemy.url = postgresql://user:password@localhost:5432/review_db
```

---

## 🛠️ Development

### Auto-reload pada perubahan code
```bash
pserve development.ini --reload
```

### Running Tests
```bash
pytest
```

### Database Migrations
```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head
```

---

## 🔒 Security Notes

1. **API Keys:**
   - Store di `.env` file
   - JANGAN commit ke git
   - Add `.env` to `.gitignore`

2. **CORS:**
   - Already configured for localhost:5173
   - Change di `__init__.py` untuk production

3. **Database:**
   - Use strong password untuk PostgreSQL
   - Regular backup untuk production

---

## 🐛 Troubleshooting

### Backend tidak start
```bash
# Check port sudah digunakan?
netstat -ano | findstr :6543

# Kill existing process
taskkill /F /IM python.exe

# Restart
pserve development.ini
```

### API Keys error
- Verify token/key di file `.env`
- Check token masih valid di provider
- Generate token/key baru jika perlu

### Database error
```bash
# Re-initialize
initialize_backend_db development.ini

# Or manual
rm review.sqlite
initialize_backend_db development.ini
```

---

## 📚 File Penting

| File | Deskripsi |
|------|-----------|
| `.env` | API keys (RAHASIA) |
| `setup.py` | Dependencies |
| `development.ini` | Config development |
| `views/default.py` | Business logic utama |
| `models/mymodel.py` | Database model |

---

## 🚀 Deploy ke Production

1. Change database ke PostgreSQL
2. Update API keys di environment variables
3. Use `production.ini` instead of `development.ini`
4. Deploy dengan Gunicorn/uWSGI
5. Setup reverse proxy (Nginx)

---

## 📞 Support

Lihat dokumentasi utama: [../README.md](../README.md)
