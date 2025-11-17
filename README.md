# AI Auto Parts — Intelligent Auto Spares Platform for Africa

AI Auto Parts is a next-generation automotive parts intelligence platform built for the African market.  
It helps workshops, mechanics, and parts shops **identify, source, and manage spare parts faster** using **AI-powered text, image, and voice recognition**.

Built proudly in **Kasama, Zambia**, designed to scale across Africa.

---

## 🚗 What AI Auto Parts Does

AI Auto Parts helps you:

### ✔ Identify parts instantly  
Search by:
- Text (“radiator for Toyota Vitz 2008”)
- Image (snap a photo of the part)
- Voice (ask the system like a human)

### ✔ Suggest compatible and alternative parts  
AI recommends:
- Compatible vehicles  
- Interchangeable part numbers  
- Reliable brands  
- Better or cheaper alternatives  

### ✔ Manage inventory + POS (offline-first)
Engineered for Africa:
- Works with poor/no internet  
- Mobile-first  
- Offline-first PWA  
- Auto-sync when network returns  

### ✔ Serve customers on WhatsApp  
Your customers can send:
- A text  
- A picture  
- A voice note  

The bot instantly finds the right part.

### ✔ Build African-language automotive intelligence (KUPIYA)
The platform learns how people across Africa:
- Describe parts  
- Use slang  
- Mix languages  
- Ask for help  

This becomes the **first African-trained auto parts model**.

---

## 🔥 Key Features

| Feature | Status |
|--------|--------|
| Text-based part search | ✅ Live |
| Category & part database | ✅ Live |
| Semantic embeddings for AI search | 🚧 In progress |
| Image-based recognition (CLIP) | ❌ Planned |
| Voice-based recognition (Whisper) | ❌ Planned |
| WhatsApp integration (Meta API) | ❌ Planned |
| Offline POS (React PWA + IndexedDB) | ❌ Planned |
| Supplier integration | ❌ Planned |
| Data consent & privacy system | ❌ Planned |

---

## 🧠 How the AI Works

**Text search:**  
Uses Sentence Transformers to convert part names, brands, and descriptions into vector embeddings for semantic matching.

**Image search:** (future)  
CLIP model encodes images and matches them against known parts.

**Voice search:** (future)  
Whisper transcribes customer audio for the search engine.

**African Language Learning (KUPIYA):**  
The system continuously learns:
- Regional slang  
- Vernacular expressions  
- Code-switching patterns  
- Mechanic-style descriptions  

---

## 🧩 Tech Stack Overview

### Backend
- Django  
- Django REST Framework  
- SQLite (development) → PostgreSQL (production)  
- Sentence Transformers (ML)  

### Frontend (future)
- React  
- Offline-first PWA  
- TailwindCSS  
- IndexedDB caching  

### Messaging
- WhatsApp Cloud API  

### Storage
- AWS S3 or Cloudinary  

### CI/CD
- GitHub Actions  

---

## 📸 Screenshots  
*(Coming soon)*

---

## 📍 Roadmap

### **v0.1.0 — Core Backend**
- Part & category models  
- Semantic embeddings  
- Basic search API  
- Admin configuration  

### **v0.2.0 — WhatsApp Assistant**
- Handle text, images, and voice  
- Intelligent part suggestions  
- Push to checkout  

### **v0.3.0 — POS + Inventory**
- Offline-first PWA  
- Stock management  
- Transaction history  
- Supplier pricing  

### **v1.0.0 — Full AI Auto Parts Platform**
- Advanced recognition  
- Compatibility engine  
- AI-powered mechanic assistant  

---

## 🔒 Privacy & Data Usage

AI Auto Parts follows strict policies:
- No images/audio stored without explicit opt-in  
- Users can revoke or delete their data  
- PII is minimized and anonymized  
- Data is never sold  

---

## 🛠️ Local Development Setup

```bash
git clone <repo-url>
cd ai-auto-parts

python -m venv .venv
. .venv/Scripts/Activate.ps1

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 🤝  Contributing
We welcome contributions!
See CONTRIBUTING.md and COMMIT_GUIDELINES.md.

## 📧 Contact
For business inquiries:
kugrow.enterprises@gmail.com
