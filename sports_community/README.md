# 🏟️ Sports Arena – Online Community for Sports Enthusiasts

A **Django-based web application** designed for sports fans to connect, discuss, and share their passion for sports. This platform allows users to create posts, comment, explore categories, and engage with an active sports community.

## 📖 Overview

**Sports Arena** serves as a social hub for sports lovers. It provides a user-friendly interface for creating, managing, and discussing sports-related posts, complete with user profiles, categories, and interaction features.

## 🎯 Objectives

* Build an interactive community for sports enthusiasts.
* Enable users to create, edit, and delete posts easily.
* Support category-based filtering, commenting, and post sorting.
* Provide a clean, responsive, and user-friendly design.
* Offer administrative capabilities for user and content moderation.

## ⚙️ Features

* ✅ **User Authentication** – Register, login, logout
* ✅ **CRUD Operations** – Create, edit, and delete posts
* ✅ **Comment System** – Add or remove comments on posts
* ✅ **User Profiles** – Track user stats and posts
* ✅ **Category Filtering** – Browse posts by sport type (Football, Basketball, Soccer, Tennis, Other)
* ✅ **Search & Sorting** – Find posts and sort by newest, oldest, or most commented
* ✅ **Pagination** – Seamless browsing through multiple post pages
* ✅ **Post View Counter** – Track post popularity
* ✅ **Activity Feed** – See recent user actions
* ✅ **Flash Messages** – Feedback for user actions
* ✅ **Custom Error Pages** – 404 and 500 error handling
* ✅ **Responsive Design** – Works on mobile, tablet, and desktop

## 🧮 Technologies Used

| Category           | Technology                            |
| ------------------ | ------------------------------------- |
| **Backend**        | Django 5.2.6, Python 3.10             |
| **Frontend**       | HTML5, CSS3 (custom, no frameworks)   |
| **Database**       | SQLite (development)                  |
| **Authentication** | Django built-in authentication system |

## 🚀 Installation & Setup

### 🥉 Prerequisites

Ensure you have the following installed:

* Python 3.8+
* pip
* virtualenv (recommended)

### 🧺 Step-by-Step Setup

1. **Clone the Repository**

   ```bash
   git clone <your-repo-url>
   cd sports_community
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

   **Activate it:**

   * On **Windows**:

     ```bash
     venv\Scripts\activate
     ```
   * On **Mac/Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install django
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   * Homepage: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 🗂️ Project Structure

```
sports_community/
├── manage.py
├── sports_community/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── community/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── static/
│   └── css/
│       └── styles.css
└── templates/
    ├── home.html
    ├── post_detail.html
    ├── create_post.html
    ├── edit_post.html
    ├── delete_confirm.html
    ├── user_profile.html
    ├── activity_feed.html
    ├── 404.html
    ├── 500.html
    └── registration/
        ├── login.html
        └── register.html
```

## 👥 Usage Guide

### 🔸 For Users

* Register or log in to your account
* Browse posts by category or search by keywords
* Create new posts and share your thoughts about your favorite sports
* Comment on posts and engage in discussions
* View user profiles and activity history

### 🔸 For Administrators

* Access the **Admin Panel** at `/admin/`
* Manage users, posts, and comments
* Moderate content and maintain community integrity

## ⚙️ Configuration

### 🕐 Timezone

Edit your timezone in `settings.py`:

```python
TIME_ZONE = 'Africa/Lagos'
```

### 🗃️ Database

The project uses **SQLite** by default.
For production, configure **PostgreSQL** or another supported database in `settings.py`.

## 🔮 Future Enhancements

* 👍 Post voting (likes/upvotes)
* 🌼 User badges and achievements
* 📧 Email notifications
* 📝 Rich text editor for posts
* 🖼️ Image uploads for posts
* 💬 Real-time chat system
* 📱 Dedicated mobile app
* 🔗 Social media sharing

## 🤝 Contributing

This is a **student project** created for learning purposes.
Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit a pull request.

## 🪪 License

This project was created for **educational purposes**.
You are free to use and modify it with appropriate attribution.

## 📬 Contact

Created as part of a Django learning project.
For inquiries or collaboration, reach out via GitHub or email (if applicable).

## 🙏 Acknowledgments

* [Django Documentation](https://docs.djangoproject.com/)
* Inspiration from open-source sports communities
* The global open-source developer community

**⭐ If you like this project, consider giving it a star on GitHub!**
