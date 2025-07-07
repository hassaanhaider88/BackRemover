# 🖼️ Back Remover – AI Background Remover (Flask App)

Back Remover is a free, open-source web app that removes image backgrounds using AI, just like [remove.bg](https://www.remove.bg). Built with Python, Flask, and the `rembg` library, it runs locally and can be deployed online easily.

> ⚡ Upload any image and download a transparent background version instantly!

---

## 🚀 Features

- ✅ Upload any `.jpg`, `.png`, etc.
- ✅ Background removal using `rembg` (ONNX + U2Net)
- ✅ Real-time preview of original and transparent images
- ✅ Download final result in `.png` format
- ✅ Mobile responsive UI with Tailwind CSS
- ✅ Clean routing and templating via Flask

---

## 📸 Demo

![screenshot](https://your-screenshot-url-if-any.com)  
🔗 Live Demo (if deployed): [https://back-remover.onrender.com](https://back-remover.onrender.com)

---

## 📦 Installation (Local)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/back-remover.git
cd back-remover

## Run the app
```
python app.py


# Then open your browser:
👉 http://127.0.0.1:5000


```
back-remover/
│
├── app.py
├── requirements.txt
├── Procfile               # for Render deployment
├── static/
│   ├── favicon.ico
│   └── uploads/           # image upload output
├── templates/
│   ├── index.html
│   ├── result.html
│   └── about.html
└── README.md



---

Let me know if you want me to generate a matching:
- `requirements.txt`
- `Procfile`
- `.gitignore`

Or if you'd like me to prepare a `.zip` you can upload straight to GitHub.
