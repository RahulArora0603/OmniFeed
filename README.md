# 🚀 OmniFeed – Unified Content Aggregator App

OmniFeed is a powerful **multi-source content aggregator web app** that allows users to search any topic and instantly view relevant content from multiple platforms like **Reddit, News, Research Papers, Medium, and YouTube** — all in one place.

Built using **FastAPI**, **Bootstrap**, **JavaScript**, and API integrations, OmniFeed solves the problem of scattered information by providing a **single unified feed**.

---

## 🌟 Features

✅ Search any topic in real time
✅ Switch between multiple platforms instantly
✅ Live Reddit feed using **PRAW API**
✅ News & articles via **Requests + News APIs**
✅ Research paper feed (arXiv / Semantic Scholar)
✅ Medium & YouTube integration
✅ Clean & responsive **Bootstrap UI**
✅ User authentication & saved posts
✅ Fully API-driven backend with **FastAPI**
✅ Card based Content
✅ Production-ready web architecture (maybe)

---

## 🛠️ Tech Stack

### 🔹 Backend

* **FastAPI** – high-performance Python backend
* **PRAW** – Reddit API wrapper
* **Requests** – external API calls
* **Uvicorn** – ASGI server

### 🔹 Frontend

* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **JavaScript (ES6+)**

### 🔹 Database (Planned in Future)

* SQLite

---


## ⚡ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/omnifeed.git
cd omnifeed
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables (`.env`)

```
REDDIT_CLIENT_ID=your_id
REDDIT_SECRET=your_secret
NEWS_API_KEY=your_key
```

### 5️⃣ Run the App

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🔍 How It Works

1. User searches any topic
2. OmniFeed fetches:

   * Reddit posts using **PRAW**
   * News via **REST APIs**
   * Research papers via scholarly APIs
3. Data is processed using **FastAPI**
4. Results are displayed using **Bootstrap + JS**
5. Users can save, filter, and switch between sources
   
---

## 🎯 Use Cases

* Data Science & AI learners
* Tech enthusiasts
* Research students
* Developers & content creators
* News & knowledge aggregation

---

## 🧠 Future Enhancements (these have nothing to do with my current skills and ground reality :p)

* ✅ Recommendation engine
* ✅ Personalized feed using ML
* ✅ Mobile app version
* ✅ Real-time notifications
* ✅ Trending topic detection
* ✅ Bookmark & sharing system

---

## 👨‍💻 Author

**Rahul Arora**
Certified Data Scientist & AI Developer
📍 India
🔗 LinkedIn | GitHub | Kaggle | Portfolio

---

## ⭐ Support & Contribution

If you like this project, please **give it a star ⭐**
Pull requests and feature suggestions are always welcome!

---

**Github License applies**
