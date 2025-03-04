# Fast API Project - Cashier Application API

## How to Run This Project

### Server Side (Backend)

First of all, you can clone this project. Then, run this command on your terminal

```bash
    pip install -r requirements.txt
    python populate_database.py
    uvicorn app.main:app --reload
```

If you want to use virtual environment python, you can run this command

```bash
    python3 -m venv venv

    # If you are on windows
    ./venv/Script/activate
    # If you are on Mac or linux
    source venv/bin/activate

    pip install -r requirements.txt
    python populate_database.py
    uvicorn app.main:app --reload
```

The api documentation of this project will serve on http://localhost:8000/docs

### Client Side (Frontend)

To run the frontend, you must run this script

```bash
    cd frontend/

    # If you are not downloaded the package before
    # Run this command
    npm install

    npm run dev
```

The client side will be run on port [5000](http://localhost:5000)

## Initial Database

After you run the `py populate_database.py`, you can find the database file named `cashier-app.db`. In this database, the initial database will look like this

### Users Table

| User ID | Name       | Email                  | Password (Non Hashed) |
| ------- | ---------- | ---------------------- | --------------------- |
| 1       | John Doe   | john.doe@example.com   | `password123`         |
| 2       | Jane Smith | jane.smith@example.com | `password456`         |

### Products Table

| Product ID | Barcode       | Product Name                    | Price   | Quantity | Status       |
| ---------- | ------------- | ------------------------------- | ------- | -------- | ------------ |
| 1          | 1234567890123 | iPhone 15 Pro                   | 999.99  | 100      | In Stock     |
| 2          | 1234567890124 | Samsung Galaxy S23 Ultra        | 1199.99 | 50       | In Stock     |
| 3          | 1234567890125 | Google Pixel 8 Pro              | 899.99  | 25       | In Stock     |
| 4          | 1234567890126 | MacBook Air M2                  | 1299.99 | 0        | Out of Stock |
| 5          | 1234567890127 | Dell XPS 13                     | 1499.99 | 75       | In Stock     |
| 6          | 1234567890128 | Sony WH-1000XM5 Headphones      | 399.99  | 200      | In Stock     |
| 7          | 1234567890129 | Apple Watch Series 9            | 499.99  | 10       | In Stock     |
| 8          | 1234567890130 | Samsung Galaxy Watch 6          | 299.99  | 150      | In Stock     |
| 9          | 1234567890131 | iPad Pro 12.9-inch              | 1099.99 | 0        | Out of Stock |
| 10         | 1234567890132 | Microsoft Surface Laptop 5      | 1299.99 | 60       | In Stock     |
| 11         | 1234567890133 | Bose QuietComfort 45 Headphones | 329.99  | 90       | In Stock     |
| 12         | 1234567890134 | Logitech MX Master 3S Mouse     | 99.99   | 40       | In Stock     |
| 13         | 1234567890135 | Canon EOS R7 Camera             | 1499.99 | 30       | In Stock     |
| 14         | 1234567890136 | Nintendo Switch OLED            | 349.99  | 80       | In Stock     |
| 15         | 1234567890137 | PlayStation 5                   | 499.99  | 20       | In Stock     |

### Transactions Table

| Transaction ID | Operator (User ID) |
| -------------- | ------------------ |
| 1              | 1 (John Doe)       |
| 2              | 2 (Jane Smith)     |

### Transaction Details Table

| Transaction Detail ID | Transaction ID | Product ID                   | Quantity | Price   | Subtotal |
| --------------------- | -------------- | ---------------------------- | -------- | ------- | -------- |
| 1                     | 1              | 1 (iPhone 15 Pro)            | 2        | 999.99  | 1999.98  |
| 2                     | 1              | 2 (Samsung Galaxy S23 Ultra) | 1        | 1199.99 | 1199.99  |
| 3                     | 2              | 3 (Google Pixel 8 Pro)       | 3        | 899.99  | 2699.97  |
| 4                     | 2              | 4 (MacBook Air M2)           | 1        | 1299.99 | 1299.99  |
