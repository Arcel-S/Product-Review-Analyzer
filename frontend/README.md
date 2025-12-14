# 🎨 Frontend - Product Review Analyzer

Frontend React + Vite untuk Product Review Analyzer dengan modern UI dan real-time updates.

## 📋 Struktur Frontend

```
frontend/
├── src/
│   ├── App.jsx              # Main component ⭐
│   ├── App.css              # Styling ⭐
│   ├── main.jsx             # Entry point
│   ├── index.css            # Global CSS
│   └── assets/              # Images, icons
├── index.html               # HTML template
├── vite.config.js           # Vite configuration
├── eslint.config.js         # ESLint rules
├── package.json             # Dependencies ⭐
├── .gitignore               # Git ignore rules
└── public/                  # Static assets
```

## 🔧 Setup

### 1. Install Dependencies
```bash
cd frontend
npm install
```

Dependencies:
- **React 19** - UI library
- **Vite 7** - Build tool (ultra-fast)
- **Axios** - HTTP client

### 2. Run Development Server
```bash
npm run dev
```

✅ Frontend akan berjalan di: **http://localhost:5173**

### 3. Build for Production
```bash
npm run build
```

Output: `dist/` folder (siap di-deploy)

---

## 🎯 Features

### Input Review Form
- **Nama Produk:** Text input
- **Review Text:** Textarea (5 rows)
- **Submit Button:** "Analyze Review"
- **Validation:** Required fields

### Results Display
- **Product Name:** Bold heading
- **Sentiment Badge:** 
  - 🟢 GREEN untuk POSITIVE
  - 🔴 RED untuk NEGATIVE
  - 🟡 YELLOW untuk NEUTRAL
- **Confidence Score:** Percentage display
- **Key Points:** Formatted bullet list
- **Timestamp:** Created date

### History
- **All Reviews:** Automatically loaded
- **Latest First:** Newest reviews di atas
- **Auto Update:** Setiap kali analyze

---

## 🌐 API Integration

### Base URL
```javascript
const API_URL = "http://localhost:6543/api"
```

### Endpoints Used
- **POST `/api/analyze-review`** - Analyze review
- **GET `/api/reviews`** - Get all reviews

---

## ⚠️ Offline Mode

Jika backend tidak tersedia, aplikasi tetap berfungsi dengan simulasi data.

---

## 📦 Scripts

```bash
npm run dev          # Start dev server
npm run build        # Build untuk production
npm run preview      # Preview build
npm run lint         # Check code dengan ESLint
```

---

## 🚀 Deploy

1. Build: `npm run build`
2. Upload folder `dist/` ke hosting
3. Update API_URL di App.jsx untuk production

Lihat [../README.md](../README.md) untuk dokumentasi lengkap.
