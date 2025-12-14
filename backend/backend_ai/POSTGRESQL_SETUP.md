# PostgreSQL Setup Guide

## Langkah-langkah Menggunakan PostgreSQL

### 1. Install PostgreSQL
Download dari: https://www.postgresql.org/download/

### 2. Buat Database
```sql
-- Login ke PostgreSQL
psql -U postgres

-- Buat database baru
CREATE DATABASE review_db;

-- Verifikasi
\l
```

### 3. Update Configuration
Edit file `backend/backend_ai/development.ini`:

```ini
# Uncomment dan sesuaikan credentials:
sqlalchemy.url = postgresql://postgres:your_password@localhost:5432/review_db
```

### 4. Initialize Database
```bash
cd backend/backend_ai
initialize_backend_db development.ini
```

### 5. Verifikasi Tabel
```sql
-- Login ke database
psql -U postgres -d review_db

-- Lihat tabel
\dt

-- Lihat struktur tabel reviews
\d reviews

-- Test insert data
SELECT * FROM reviews;
```

---

## Connection String Format

```
postgresql://username:password@host:port/database_name
```

**Contoh:**
- Local: `postgresql://postgres:123456@localhost:5432/review_db`
- Remote: `postgresql://user:pass@192.168.1.100:5432/review_db`
- Cloud: `postgresql://user:pass@aws-rds-endpoint.com:5432/review_db`

---

## Troubleshooting

### Error: "password authentication failed"
- Cek password PostgreSQL Anda
- Edit `pg_hba.conf` jika perlu (ganti `md5` menjadi `trust` untuk testing)

### Error: "database does not exist"
- Buat database terlebih dahulu: `CREATE DATABASE review_db;`

### Error: "connection refused"
- Pastikan PostgreSQL service berjalan:
  - Windows: Check Services
  - Linux: `sudo systemctl status postgresql`

---

## Keuntungan PostgreSQL vs SQLite

### PostgreSQL ✅
- Production-ready
- Concurrent users support
- Better performance untuk data besar
- Advanced features (JSON, Full-text search, dll)

### SQLite 📁
- Sederhana untuk development
- No installation needed
- Single file database
- Bagus untuk testing

**Rekomendasi:** 
- Development: SQLite (sudah default)
- Production: PostgreSQL

---

## Migrasi dari SQLite ke PostgreSQL

```bash
# 1. Backup data SQLite (optional)
sqlite3 review.sqlite .dump > backup.sql

# 2. Ganti connection string di development.ini
# 3. Re-initialize database
initialize_backend_db development.ini

# 4. Restart backend server
pserve development.ini
```

Data lama di SQLite tidak akan hilang, hanya database engine yang berubah.
