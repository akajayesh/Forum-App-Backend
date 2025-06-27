# Forum-App-Backend

A clean and scalable discussion forum backend built with Django .  
Supports threaded conversations, user authentication, post voting, moderation tools, and search functionality .

---

## ✨ Features

- Threaded posts with support for nested replies 
- User registration, login, logout, and profile handling
- Create, view, and manage categories, threads, and posts 
- Report inappropriate posts and lock threads for moderation 
- Upvote [👍] and downvote [👎] individual posts 
- Search threads and post content in real time 
- Admin panel for full control over content and users 

---

## ⚙️ Requirements

- Python 3.10+ 
- Django 4.x 
- Gunicorn (for deployment) 
- PostgreSQL or SQLite (default for development) 
- Render (or any WSGI-compatible platform for deployment) 


🧪 Local Setup
1. Clone the repo

git clone https://github.com/YOUR_USERNAME/Forum-App-Backend.git

cd Forum-App-Backend

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

3. Install Dependencies by
pip install -r requirements.txt

4. Apply Migrations by
python manage.py migrate

5. Run Deployment server by
python manage.py runserver

And after all this , Visit http://127.0.0.1:8000/ to explore the app locally


For Video Explanation , checkout -
https://drive.google.com/file/d/1lM8pSsOFrYwJCf15Jqh1JsqOxtRvu3jM/view?usp=sharing

https://drive.google.com/file/d/1yWER3fxkhbkjSP_9LkSpi1mNknTM8vaM/view?usp=sharing
