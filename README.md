# 🎬 BookMyShow - Movie Ticket Booking System

A full-featured Django web application for booking movie tickets online. Users can browse movies, select theatres and showtimes, choose seats, and make payments through Razorpay integration.

[![Django](https://img.shields.io/badge/Django-5.2.9-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### 🎭 User Features

- **User Authentication**: Register, login, logout, and password reset functionality
- **Movie Browsing**: Browse available movies with images, ratings, cast, and descriptions
- **Genre & Language Filters**: Filter movies by genre and language
- **Theatre Selection**: View available theatres and showtimes for selected movies
- **Seat Selection**: Interactive seat selection with real-time availability
- **Seat Reservation**: Temporary seat hold (5 minutes) during booking process
- **Payment Integration**: Secure payments via Razorpay gateway
- **User Profile**: View and manage user profile and booking history
- **Trailer Preview**: Watch movie trailers directly on the platform

### 👨‍💼 Admin Features

- **Admin Dashboard**: Comprehensive dashboard for managing the system
- **Movie Management**: Add, edit, and delete movies with images and details
- **Theatre Management**: Configure theatres, showtimes, and seat pricing
- **Booking Management**: View and manage all bookings
- **Payment Tracking**: Monitor payment status and transactions
- **User Management**: Manage user accounts and permissions

### 🔐 Security Features

- Password hashing and secure authentication
- Session management
- CSRF protection
- Secure payment processing
- User authorization and permissions

## 🛠️ Tech Stack

### Backend

- **Django 5.2.9**: Python web framework
- **Python 3.9+**: Programming language
- **SQLite**: Development database
- **PostgreSQL**: Production database (via psycopg2-binary)
- **Gunicorn**: WSGI HTTP Server

### Payment Integration

- **Razorpay**: Payment gateway for secure transactions

### Frontend

- **HTML/CSS**: Template rendering
- **Django Templates**: Server-side rendering

### Deployment

- **Vercel**: Cloud platform for deployment
- **dj-database-url**: Database configuration utility

## 📁 Project Structure

```
BookMyShow/
├── BookMyShow/           # Project configuration
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
│
├── users/                # User authentication & profiles
│   ├── models.py         # User models
│   ├── views.py          # User views
│   ├── urls.py           # User URL patterns
│   └── forms.py          # User forms
│
├── movies/               # Movie management
│   ├── models.py         # Movie, Theatre, Seat, Booking models
│   ├── views.py          # Movie browsing & booking views
│   ├── urls.py           # Movie URL patterns
│   └── utils.py          # Helper utilities
│
├── payments/             # Payment processing
│   ├── models.py         # Payment models
│   ├── views.py          # Payment views
│   ├── services.py       # Payment service layer
│   └── urls.py           # Payment URL patterns
│
├── dashboard/            # Admin dashboard
│   ├── views.py          # Dashboard views
│   └── urls.py           # Dashboard URL patterns
│
├── templates/            # HTML templates
│   ├── home.html
│   ├── users/            # User templates
│   ├── movies/           # Movie templates
│   ├── payments/         # Payment templates
│   └── dashboard/        # Dashboard templates
│
├── media/                # User-uploaded files
│   └── movies/           # Movie images
│
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel deployment config
├── db.sqlite3            # SQLite database (development)
└── README.md             # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Manav-Sonawane/BookMySeat.git
cd BookMyShow
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

### Step 5: Collect Static Files

```bash
python manage.py collectstatic
```

### Step 6: Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory (optional):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DATABASE_URL=your-database-url

# Razorpay Configuration
RAZORPAY_KEY_ID=your-razorpay-key-id
RAZORPAY_KEY_SECRET=your-razorpay-key-secret
```

### Django Settings

Update [BookMyShow/settings.py](BookMyShow/settings.py) for production:

- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Update `SECRET_KEY` (use environment variable)
- Configure production database
- Set up static file serving

### Razorpay Setup

1. Sign up at [Razorpay](https://razorpay.com/)
2. Get your API keys from the dashboard
3. Update the keys in your settings or environment variables

## 📖 Usage

### For Users

1. **Register/Login**: Create an account or login
2. **Browse Movies**: View available movies on the homepage
3. **Select Movie**: Click on a movie to view details and available shows
4. **Choose Theatre & Time**: Select preferred theatre and showtime
5. **Select Seats**: Choose your seats from the seating chart
6. **Make Payment**: Complete payment via Razorpay
7. **Confirmation**: Receive booking confirmation

### For Admins

1. **Access Admin Panel**: Navigate to `/admin/`
2. **Login**: Use superuser credentials
3. **Manage Content**:
   - Add/edit movies with images, ratings, and details
   - Configure theatres and showtimes
   - Set seat pricing
   - View bookings and payments
   - Manage users

## 🔗 API Endpoints

### User Endpoints

- `GET /` - Homepage
- `GET /users/register/` - User registration
- `POST /users/register/` - Submit registration
- `GET /users/login/` - Login page
- `POST /users/login/` - Submit login
- `GET /users/logout/` - Logout user
- `GET /users/profile/` - User profile
- `GET /users/password-reset/` - Password reset

### Movie Endpoints

- `GET /movies/` - List all movies
- `GET /movies/<movie_id>/` - Movie details
- `GET /movies/<movie_id>/theatres/` - List theatres for a movie
- `GET /movies/theatre/<theatre_id>/seats/` - Seat selection
- `POST /movies/theatre/<theatre_id>/book/` - Book seats

### Payment Endpoints

- `GET /payments/checkout/` - Checkout page
- `POST /payments/create-order/` - Create Razorpay order
- `POST /payments/verify/` - Verify payment

### Dashboard Endpoints

- `GET /dashboard/` - Admin dashboard
- (Additional admin endpoints as needed)

## 🗄️ Database Models

### User Model

- Built-in Django User model
- Extended with profile information

### Movie Model

- `name`: Movie title
- `image`: Movie poster
- `rating`: Movie rating (1-10)
- `cast`: Cast information
- `description`: Movie description
- `trailer_url`: YouTube/video URL
- `genre`: Many-to-many with Genre
- `language`: Foreign key to Language

### Theatre Model

- `name`: Theatre name
- `movie`: Foreign key to Movie
- `time`: Showtime
- `seat_price`: Ticket price

### Seat Model

- `theatre`: Foreign key to Theatre
- `seat_number`: Seat identifier
- `is_booked`: Booking status
- `reserved_by`: Temporary hold by user
- `reserved_until`: Reservation expiry

### Booking Model

- `user`: Foreign key to User
- `seat`: One-to-one with Seat
- `movie`: Foreign key to Movie
- `theatre`: Foreign key to Theatre
- `booked_at`: Booking timestamp

### Payment Model

- `user`: Foreign key to User
- `theatre`: Foreign key to Theatre
- `razorpay_order_id`: Razorpay order ID
- `razorpay_payment_id`: Razorpay payment ID
- `razorpay_signature`: Payment signature
- `amount`: Payment amount
- `status`: Payment status

## 🌐 Deployment

### Vercel Deployment

The project includes [vercel.json](vercel.json) for easy deployment:

1. Install Vercel CLI:

```bash
npm install -g vercel
```

2. Login to Vercel:

```bash
vercel login
```

3. Deploy:

```bash
vercel
```

4. Follow prompts to complete deployment

### Environment Configuration

Set environment variables in Vercel dashboard:

- `SECRET_KEY`
- `DATABASE_URL`
- `RAZORPAY_KEY_ID`
- `RAZORPAY_KEY_SECRET`

### Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use strong `SECRET_KEY`
- [ ] Set up PostgreSQL database
- [ ] Configure static file serving
- [ ] Set up HTTPS
- [ ] Configure email backend
- [ ] Set up logging
- [ ] Enable security middleware

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Write unit tests for new features

## 🐛 Known Issues

- Seat reservation timeout needs browser-side countdown
- Email notifications not yet implemented
- Mobile responsive design needs improvement

## 🔮 Future Enhancements

- [ ] Email notifications for bookings
- [ ] SMS notifications
- [ ] QR code tickets
- [ ] Movie reviews and ratings by users
- [ ] Social media integration
- [ ] Mobile app development
- [ ] Multiple payment gateway options
- [ ] Booking cancellation feature
- [ ] Loyalty points system
- [ ] Advanced search and filters

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Manav Sonawane**

- GitHub: [@Manav-Sonawane](https://github.com/Manav-Sonawane)
- Repository: [BookMySeat](https://github.com/Manav-Sonawane/BookMySeat)

## 🙏 Acknowledgments

- Django framework and community
- Razorpay for payment integration
- Vercel for hosting platform
- All contributors and supporters

---

⭐ If you find this project helpful, please give it a star on GitHub!

## 📞 Support

For support, email your-email@example.com or open an issue in the GitHub repository.

---

**Happy Booking! 🎬🍿**
