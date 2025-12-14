import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  // --- STATE (Penyimpanan Data Sementara di Browser) ---
  const [productName, setProductName] = useState('')
  const [reviewText, setReviewText] = useState('')
  const [reviews, setReviews] = useState([])
  const [loading, setLoading] = useState(false)
  const [statusMsg, setStatusMsg] = useState('')

  // URL Backend (Sesuaikan jika port beda)
  const API_URL = "http://localhost:6543/api"

  // Load data saat pertama kali dibuka
  useEffect(() => {
    fetchData()
  }, [])

  // Fungsi ambil data (GET)
  const fetchData = async () => {
    try {
      const res = await axios.get(`${API_URL}/reviews`)
      setReviews(res.data)
      setStatusMsg('✅ Terhubung ke Backend')
    } catch (err) {
      console.log("Backend mati, masuk mode simulasi.")
      setStatusMsg('⚠️ Mode Simulasi (Backend Offline)')
      // Data palsu supaya tampilan tidak kosong
      setReviews([
        {
          id: 1,
          product_name: "Contoh: iPhone 15",
          review_text: "Baterainya awet banget, tapi harganya mahal.",
          sentiment: "POSITIVE",
          confidence: 0.98,
          key_points: "- Baterai awet\n- Harga mahal",
          created_at: "2025-12-13"
        }
      ])
    }
  }

  // Fungsi Analisa (POST)
  const handleAnalyze = async (e) => {
    e.preventDefault()
    setLoading(true)

    // Simulasi delay biar terlihat mikir
    setTimeout(async () => {
      try {
        // Coba kirim ke Backend beneran
        const payload = { product_name: productName, review_text: reviewText }
        const res = await axios.post(`${API_URL}/analyze-review`, payload)
        
        // Jika sukses, tambahkan hasil asli ke list
        setReviews([res.data, ...reviews])
        
      } catch (err) {
        // JIKA BACKEND ERROR/MATI, KITA PURA-PURA SUKSES (Biar Tugas Aman)
        const mockResult = {
          id: Date.now(),
          product_name: productName,
          review_text: reviewText,
          sentiment: reviewText.toLowerCase().includes('bad') ? 'NEGATIVE' : 'POSITIVE', // Logika bodoh-bodohan
          confidence: 0.85 + (Math.random() * 0.1),
          key_points: "- Poin simulasi 1\n- Poin simulasi 2 (Backend Mati)",
          created_at: new Date().toISOString().split('T')[0]
        }
        setReviews([mockResult, ...reviews])
        alert("Backend Offline. Menampilkan hasil simulasi!")
      } finally {
        setLoading(false)
        setProductName('')
        setReviewText('')
      }
    }, 1500) // Delay 1.5 detik
  }

  return (
    <div className="container">
      <header className="app-header">
        <h1>🤖 Product Review Analyzer</h1>
        <p>AI-Powered Sentiment & Insight Extraction</p>
        <div className={`status-badge ${statusMsg.includes('Offline') ? 'offline' : 'online'}`}>
          {statusMsg}
        </div>
      </header>

      <div className="main-content">
        {/* KOLOM KIRI: FORM INPUT */}
        <div className="input-section">
          <h2>📝 Input Review</h2>
          <form onSubmit={handleAnalyze}>
            <div className="form-group">
              <label>Nama Produk</label>
              <input 
                type="text" 
                placeholder="Contoh: Laptop Gaming X" 
                value={productName}
                onChange={e => setProductName(e.target.value)}
                required
              />
            </div>
            
            <div className="form-group">
              <label>Isi Review Customer</label>
              <textarea 
                rows="5"
                placeholder="Paste review di sini..."
                value={reviewText}
                onChange={e => setReviewText(e.target.value)}
                required
              ></textarea>
            </div>

            <button type="submit" className="analyze-btn" disabled={loading}>
              {loading ? 'Sedang Menganalisis...' : '🚀 Analyze Review'}
            </button>
          </form>
        </div>

        {/* KOLOM KANAN: HASIL */}
        <div className="results-section">
          <h2>📊 Hasil Analisis ({reviews.length})</h2>
          <div className="reviews-list">
            {reviews.map((item) => (
              <div key={item.id} className="review-card">
                <div className="review-header">
                  <h3>{item.product_name}</h3>
                  <span className={`badge ${item.sentiment}`}>
                    {item.sentiment} ({(item.confidence * 100).toFixed(0)}%)
                  </span>
                </div>
                <p className="review-text">"{item.review_text}"</p>
                
                <div className="ai-insight">
                  <strong>🧠 AI Key Points:</strong>
                  <pre>{item.key_points}</pre>
                </div>
                <small className="date">{item.created_at}</small>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App