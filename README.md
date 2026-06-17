# Tomato-Offline-delivery-system-NO-GUI
Tomato Offline delivery system NO GUI is a offline sql based commerce platform

# Tomato Delivery Platform (CLI Edition)

A command-line food ordering and delivery platform built using **Python** and **MySQL**. The project simulates a food delivery service where users can register, log in, browse restaurants, order food, apply discount coupons, view restaurant ratings, and place orders through a terminal-based interface. :contentReference[oaicite:0]{index=0}

---

## Features

### User Authentication
- User Registration
- User Login
- MySQL Database Integration
- Username Validation

### Restaurant Management
- Browse 10 Restaurants
- Multiple Cuisine Categories
- Dynamic Menu Display
- Restaurant Rating System

### Cart Management
- Add Food Items to Cart
- Automatic Quantity Updates
- Remove Items from Cart
- Real-Time Bill Calculation

### Coupon System

Supported Coupons:

| Coupon Code | Discount |
|------------|-----------|
| FOOD10 | 10% Off |
| SAVE50 | ₹50 Off |
| DINNER30 | 30% Off (Max ₹100) |

### Checkout System
- Delivery Address Input
- Coupon Validation
- Discount Calculation
- Order Confirmation
- Random Delivery ETA Generation

### Ratings System
- Restaurant Rating Display
- 1-Star to 5-Star Vote Distribution
- Randomized Ratings for Demonstration

---

## Tech Stack

- Python
- MySQL
- mysql-connector-python

---

## Database Schema

### Users Table

```sql
CREATE DATABASE tomato_app;

USE tomato_app;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/tomato-delivery-platform.git
cd tomato-delivery-platform
```

### Install Dependencies

```bash
pip install mysql-connector-python
```

### Configure Database

Update the database credentials in:

```python
connect_db()
```

```python
host="localhost"
user="root"
password="1234"
database="tomato_app"
```

### Run Application

```bash
python main.py
```

---

## Application Flow

```text
Start
 │
 ├── Login
 │
 ├── Register
 │
 └── Exit
      │
      ▼
User Dashboard
 │
 ├── View Restaurants
 │      │
 │      ├── Browse Menu
 │      ├── Add Items
 │      └── View Ratings
 │
 ├── View Cart
 │
 ├── Checkout
 │
 └── Logout
```

---

## Core Components

### Database Functions

- `connect_db()`
- `register_user()`
- `check_login()`

Responsible for:
- Database Connectivity
- User Registration
- User Authentication

### Coupon Engine

- `apply_coupon()`

Handles:
- Percentage Discounts
- Flat Discounts
- Maximum Discount Caps

### Ratings Engine

- `get_ratings()`

Provides:
- Restaurant Rating Distribution
- Random Vote Generation
- Session-Based Rating Storage

### Cart System

Features:
- Item Addition
- Quantity Management
- Item Removal
- Price Calculation

---

## Project Structure

```text
tomato-delivery-platform/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Sample Features Demonstrated

- Command-Line Interface Design
- Database Connectivity with MySQL
- Authentication Systems
- Cart and Order Management
- Coupon Processing Logic
- Menu Driven Programming
- Data Persistence
- Modular Programming

---

## Current Limitations

- Passwords stored in plain text
- Orders are not stored in the database
- Ratings are randomly generated
- No order history functionality
- No admin dashboard
- No payment gateway integration

---

## Future Improvements

- Password Hashing
- Order History Storage
- Database-Backed Ratings & Reviews
- Restaurant Search & Filters
- Payment Gateway Integration
- Admin Management Panel
- Inventory Management System
- Real-Time Order Tracking

---

## Author

**Bhaskar Negi**

Python Developer • Cybersecurity Enthusiast • AI Explorer

---

## License

This project is intended for educational and academic purposes.
