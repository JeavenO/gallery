# Unsplash Gallery — Curated Visuals for the Elite

A Flask web application that integrates with the Unsplash API to deliver a **luxury‑styled photo gallery**. Designed with a millionaire aesthetic: black marble tones, gold accents, curated captions, and a premium layout. This project showcases semantic HTML structure, responsive CSS, and API integration.

---

##  Features
- **Luxury Theme**: Black background, gold gradients, elegant typography.
- **Curated Gallery**: Framed cards with captions, hover glow, consistent sizing.
- **Search Functionality**: Frosted glass search bar to query Unsplash photos.
- **Category Filters**: Quick access to curated topics (Nature, Technology, Food, Travel, People).
- **Responsive Layout**: Works seamlessly across desktop and mobile.
- **Semantic HTML**: Clean structure using `<section>`, `<header>`, `<footer>`.

---

##  Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3 (luxury theme styling)
- **API**: Unsplash API
- **Environment**: VS Code, virtualenv

---

##  Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/unsplash-gallery.git
cd unsplash-gallery

---

####  2. Create and activate a virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

pip install -r requirements.txt

UNSPLASH_ACCESS_KEY=your_unsplash_api_key_here

python app.py

unsplash-gallery/
│
├── static/
│   └── styles.css        # Luxury millionaire theme styling
│
├── templates/
│   ├── base.html         # Semantic structure (header, hero, categories, gallery, footer)
│   ├── index.html        # Homepage
│   └── gallery.html      # Gallery rendering
│
├── app.py                # Flask backend + Unsplash API integration
├── requirements.txt      # Dependencies
└── README.md             # Project documentation


---

 This README is **ready to paste** into your project. It explains the theme, setup, structure, and credits in one cohesive document.  

p

