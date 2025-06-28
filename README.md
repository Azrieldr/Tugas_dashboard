# Dashboard Analisis Penerimaan Mahasiswa Yale University

Dashboard interaktif untuk menganalisis data penerimaan mahasiswa Yale University menggunakan Streamlit.

## 📂 Persiapan File

Pastikan Anda memiliki file berikut dalam satu folder:
- `dashboard.py` (file aplikasi utama)
- `YaleAdmits.csv` (file data)

## ⚙️ Install Dependencies

Buka terminal atau command prompt, kemudian jalankan perintah berikut:

```bash
pip install streamlit pandas plotly
```

## 🚀 Menjalankan Dashboard

1. Navigasikan file exporer ke folder yang berisi `dashboard.py`, lalu buka terminal dengan meng-enter "cmd" di address bar file explorer.
2. Jalankan aplikasi dengan perintah berikut:

```bash
streamlit run dashboard.py
```

## 🌐 Akses Dashboard

- Dashboard akan otomatis terbuka di browser.
- Jika tidak terbuka secara otomatis, buka browser dan kunjungi:

```
http://localhost:8501
```

## 🧭 Cara Menggunakan

1. Gunakan **slider** di sidebar untuk memilih rentang tahun.
2. Lihat **metrik utama** di bagian atas.
3. Analisis **grafik tren penerimaan** dan **skor SAT**.
4. Centang **"Tampilkan Data Mentah"** untuk melihat dataset lengkap.

## 🛠️ Troubleshooting

### ❗ File tidak ditemukan
- Pastikan file `YaleAdmits.csv` berada di folder yang sama dengan `dashboard.py`.

### ❗ Dashboard tidak terbuka
- Coba jalankan dengan port berbeda:

```bash
streamlit run dashboard.py --server.port 8502
```