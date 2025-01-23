# Django Social Media Project

- This is a social media web application built using **Django** and **Bootstrap**. The project includes core features such as user authentication, profile management, and CRUD operations for posts and comments.

## 🚀 Features

- **User Authentication:**
  - User signup
  - User login/logout
  - Password reset functionality

- **User Profile:**
  - Profile image upload
  - Edit profile details

- **Posts Management:**
  - Add new posts
  - Edit existing posts
  - Delete posts
  - View all posts

- **Comments System:**
  - Add comments to posts
  - View comments under each post

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django database)

## 📂 Installation

1. Clone the repository:
   ```bash
   
   git clone https://github.com/JanhaviGanorkar/pro2-master
   cd pro2-master

   ```
2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\\Scripts\\activate`
   ```
3. Install dependencies:

``` bash
pip install -r requirements.txt
```
4. Apply database migrations:
```bash
python manage.py migrate
   ```

5. Create a superuser:

```bash
python manage.py createsuperuser
   ```
6. Run the development server:

```bash 
python manage.py runserver
```

7. Open the project in the browser:

```bash
http://127.0.0.1:8000/
```

📁 Project Structure

```bash

|-- social_media_project/
    |-- api/                  # User authentication app
    |-- media/                # Uploaded media files (profile images)
    |-- myapp/                # app functionality
    |-- static/               # Static files (CSS, JS, images)
    |-- templates/            # HTML templates
    |-- db.sqlite3            # SQLite database
    |-- manage.py             # Django project management script
    |-- requirements.txt      # Project dependencies
```

## 🧰 Usage

- Sign up for an account and log in to create and manage your posts.

- Add comments to other users' posts.


- Upload and update your profile image.

- Edit and delete your posts anytime.

## 🔮 Future Enhancements

- Friend Request functionality.

- Follow/Unfollow functionality.

- Improved UI with more Bootstrap components.

- Chat with friends.

## 📜 License

- This project is open-source and available under the MIT License.

## Developed by Janhavi
