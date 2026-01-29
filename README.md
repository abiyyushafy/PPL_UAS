# PPL_UAS

# 🛡️ Automated OSINT Reconnaissance Tool
**Proyek Ujian Akhir Semester (UAS) - Pemrograman Python Lanjut (TK067)** **Universitas Amikom Yogyakarta | Semester Ganjil TA 2025/2026**

---

## 📝 Deskripsi Proyek
Proyek ini merupakan sebuah alat otomatisasi berbasis Python yang dirancang untuk membantu praktisi keamanan siber dalam melakukan fase pengumpulan informasi (*Reconnaissance*) secara efisien. Alat ini mengintegrasikan berbagai API keamanan untuk mengumpulkan data intelijen dari sumber terbuka (OSINT) hanya dengan satu kali input domain target.

Sesuai dengan tema UAS yaitu **Otomatisasi**, program ini meminimalkan intervensi manual dalam pengumpulan data DNS, informasi kepemilikan domain, hingga deteksi kerentanan server

## 👥 Informasi Kelompok
Proyek ini disusun dan dikembangkan secara berkelompok oleh:
1. **Sarjana Nanda Pamungkas** - 23.83.1028
2. **Abiyyu Shafy Hidayat** - 23.83.1035
3. **Zulfi Rahmad Fathoni** - 23.83.1040

**Dosen Pengampu:** Muhammad Koprawi, S.Kom., M.Eng 

---

## 🚀 Fitur Utama (Otomatisasi)
Alat ini menjalankan beberapa modul investigasi secara otomatis:
* **DNS Reconnaissance**: Mengidentifikasi record A, MX, NS, dan TXT menggunakan library `dnspython`.
* **Subdomain Discovery**: Melakukan pencarian daftar subdomain melalui integrasi API `crt.sh`.
* **Whois Intelligence**: Mengambil data registrasi dan kepemilikan domain melalui library `python-whois`.
* **Server & Vulnerability Intelligence**: Menggunakan **Shodan Developer API** untuk mengidentifikasi port yang terbuka, sistem operasi, serta potensi kerentanan (CVE) pada server target.
* **Auto-Reporting**: Seluruh hasil temuan secara otomatis diekspor ke dalam format file `.csv` di folder `reports/`.

---

## 💻 Panduan Instalasi & Penggunaan

### 1. Prasyarat
Pastikan Anda telah menginstal Python 3.x dan mengaktifkan Virtual Environment (venv).

### 2. Instalasi Library
Gunakan perintah berikut untuk menginstal dependensi yang diperlukan:
```bash
pip install -r requirements.txt
```
3. Konfigurasi API
Masukkan Shodan Developer API Key Anda ke dalam file **modules/shodan_recon.py** pada variabel **SHODAN_API_KEY.**
