# 🔗 URL Shortener - Flask App

A simple **Flask-based URL Shortener** that converts long URLs into short, easy-to-share links. The app also redirects short URLs to their original destinations.

---

## 🌟 Features
✔ Shorten long URLs instantly  
✔ Store URLs in an SQLite database  
✔ Redirect short URLs to the original link  
✔ Responsive UI with a background image  
✔ Smooth animations and modern design  

---

## 🛠 Tech Stack
- **Backend:** Flask, Python  
- **Frontend:** HTML, CSS  
- **Database:** SQLite  

---

## 📂 Project Structure
```
URL-Shortener/
│── static/
│   ├── background.jpg   # Background image
│   ├── style.css        # Styling for the UI
│── templates/  
│   ├── index.html       # Main UI page  
│── app.py               # Flask backend  
│── shortener.db         # SQLite database (auto-generated)  
│── requirements.txt     # Dependencies  
│── README.md            # Project documentation  
```

---

## 🚀 Installation & Usage

### 🔹 1. Clone the Repository
```sh
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 🔹 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 🔹 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 4. Run the Flask App
```sh
python app.py
```

### 🔹 5. Open in Browser
Go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  

Enter a long URL and get a short link instantly!

---

## 🎨 UI Preview
- The background image is stored as **`static/background.jpg`**.
- If you want to use an **online image**, edit **`static/style.css`**:
```css
background: url("https://your-image-url.com") no-repeat center center/cover;
```

---

## 📌 How It Works
1. **User enters a long URL.**  
2. **Flask generates a short code** and stores it in the database.  
3. **The user receives a short URL.**  
4. **When accessed, the short URL redirects to the original URL.**  

---

## 🛠 API Endpoints
| Method | Endpoint       | Description                  |
|--------|---------------|------------------------------|
| GET    | `/`           | Home page with form         |
| POST   | `/shorten`    | Generates a short URL       |
| GET    | `/<short_url>` | Redirects to original URL  |

---

## 🏗 Future Enhancements
- ✅ **Custom short links** (User-defined names)
- ✅ **QR Code generation** for shortened URLs
- ✅ **Click tracking & analytics**
- ✅ **User authentication for saved links**

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 💡 Author
👨‍💻 Developed by **Kunal Masurkar**  
🌐 [GitHub](https://github.com/KunalMasurkar) | 🔗 [LinkedIn](https://linkedin.com/in/kunal-masurkar-8494a123a)

---

**📢 Feel free to contribute, raise issues, or suggest improvements! 🚀**
```
