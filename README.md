# Flask URL Shortener

A simple URL shortener web application built with **Flask**.  
It takes a long URL and generates a short link like `http://127.0.0.1:5000/<short-code>` that redirects to the original address.  
The URL mappings are stored **in memory** (resets on application restart).

---

## Steps to Run the Application

1. **Clone the repository**:
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>

2. **Create and activate a virtual environment** (optional but recommended):
   python -m venv venv
   # On Linux/Mac
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate

3. **Install dependencies**:
   pip install -r requirements.txt

4. **Run the application**:
   python -m app.main

5. **Open the application in your browser**:
   http://127.0.0.1:5000

---

## Usage

- Paste your long URL into the input box.
- Click **Shorten**.
- Copy the generated short link.
- Share and use the short link — it will redirect to the original URL.

---

## Example

**Input**:  
https://www.example.com/some/very/long/url/with/parameters?key=value

**Output**:  
http://127.0.0.1:5000/aB3dE1

---

## Limitations

- Data is stored **in memory** only — all shortened URLs are lost when the app restarts.
- No analytics (click tracking) implemented yet.

---

## Future Enhancements

- Persistent storage using SQLite or PostgreSQL.
- User accounts for managing URLs.
- URL analytics (click count, location, etc.).
- Custom short codes.

---
