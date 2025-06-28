\# Dashboard Analisis Penerimaan Mahasiswa Yale University



Dashboard interaktif untuk menganalisis data penerimaan mahasiswa Yale University menggunakan Streamlit.



\## Cara Menjalankan Program



\### 1. Persiapan File

Pastikan Anda memiliki file berikut dalam satu folder:

\- `dashboard.py` (file aplikasi utama)

\- `YaleAdmits.csv` (file data)



\### 2. Install Dependencies

Buka terminal/command prompt dan jalankan:

```bash

pip install streamlit pandas plotly

```



\### 3. Jalankan Dashboard

Di terminal, navigasikan ke folder yang berisi file `dashboard.py`, kemudian jalankan:

```bash

streamlit run dashboard.py

```



\### 4. Akses Dashboard

\- Dashboard akan otomatis terbuka di browser

\- Jika tidak terbuka otomatis, buka browser dan kunjungi: `http://localhost:8501`



\### 5. Cara Menggunakan

1\. Gunakan slider di sidebar untuk memilih rentang tahun

2\. Lihat metrik utama di bagian atas

3\. Analisis grafik tren penerimaan dan skor SAT

4\. Centang "Tampilkan Data Mentah" untuk melihat dataset lengkap



\## Troubleshooting



\*\*Jika terjadi error "File tidak ditemukan":\*\*

\- Pastikan file `YaleAdmits.csv` ada di folder yang sama dengan `dashboard.py`



\*\*Jika dashboard tidak terbuka:\*\*

\- Coba jalankan: `streamlit run dashboard.py --server.port 8502`

