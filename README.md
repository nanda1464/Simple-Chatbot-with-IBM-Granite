# Simple-Chatbot-with-IBM-Granite

# Simple Chatbot dengan AI IBM Granite 🤖

## 📝 Description

Proyek ini merupakan **aplikasi chatbot sederhana** yang memanfaatkan **model AI IBM Granite** untuk menjawab pertanyaan pengguna secara kontekstual.
Aplikasi dibangun menggunakan **Python, Flask, dan Streamlit**, di mana Streamlit berfungsi sebagai antarmuka pengguna dan Flask sebagai backend API yang menghubungkan chatbot dengan model Granite.
Tujuannya adalah membuat chatbot yang mudah di-deploy, ringan, dan dapat dijadikan dasar untuk pengembangan chatbot AI yang lebih kompleks.

---

## 🧰 Technologies

* **Python 3.10+**
* **Streamlit** – untuk antarmuka web interaktif
* **Flask** – sebagai REST API backend
* **IBM Granite API / Model** – untuk pemrosesan bahasa alami (Natural Language Processing)
* **Requests** – untuk komunikasi antara frontend dan backend
* **HTML & CSS** – untuk styling (custom UI mirip ChatGPT)

---

## ✨ Features

* Chatbot interaktif dengan tampilan bubble chat modern
* Header tetap (sticky) saat scroll
* Komunikasi real-time antara frontend (Streamlit) dan backend (Flask)
* Integrasi AI IBM Granite untuk respons berbasis konteks
* Mudah di-deploy secara lokal
* Dapat diperluas untuk mendukung multiple AI model atau API tambahan

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/username/simple-chatbot-granite.git
cd simple-chatbot-granite
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Backend (Flask)

```bash
python backend.py
```

### 4. Jalankan Frontend (Streamlit)

```bash
streamlit run chatbot_ui.py
```

### 5. Akses di Browser

Buka [http://localhost:8501](http://localhost:8501) untuk menggunakan chatbot.

---

## 🧠 AI Support Explanations

IBM **Granite** merupakan keluarga model **Foundation Model** dari IBM yang dirancang untuk pemahaman bahasa alami (NLP) dan generative tasks.
Dalam proyek ini, Granite digunakan untuk:

* Menganalisis konteks dari pertanyaan pengguna
* Menghasilkan jawaban alami dan relevan
* Memungkinkan pengembangan chatbot yang adaptif dan berbasis pembelajaran kontekstual

Granite AI dapat diintegrasikan melalui **IBM watsonx.ai API**, yang mendukung inference berbasis teks dan multimodal.
Dengan demikian, chatbot ini bukan hanya menjawab secara statis, tetapi dapat beradaptasi dengan konteks percakapan pengguna.

---

📌 *Project ini dapat dijadikan pondasi untuk mengembangkan chatbot AI khusus sesuai domain seperti pendidikan, layanan pelanggan, atau bisnis UMKM.*
