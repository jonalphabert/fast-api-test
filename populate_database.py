from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.databases import Base
from app.models import User, Product, Transaction, TransactionDetail

# Database URL (SQLite in this case)
SQLALCHEMY_DATABASE_URL = "sqlite:///./cashier-app.db"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables
Base.metadata.create_all(bind=engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Add dummy users
def create_dummy_users():
    users = [
        User(name="John Doe", email="john.doe@example.com", password="password123"),
        User(name="Jane Smith", email="jane.smith@example.com", password="password456"),
    ]
    db.add_all(users)
    db.commit()
    print("Added 2 dummy users.")

# Add dummy products
def create_dummy_products():
    products = [
        Product(product_barcode="1234567890123", product_name="iPhone 15 Pro", product_price=999.99, product_quantity=100),
        Product(product_barcode="1234567890124", product_name="Samsung Galaxy S23 Ultra", product_price=1199.99, product_quantity=50),
        Product(product_barcode="1234567890125", product_name="Google Pixel 8 Pro", product_price=899.99, product_quantity=25),
        Product(product_barcode="1234567890126", product_name="MacBook Air M2", product_price=1299.99, product_quantity=0),  # Out of stock
        Product(product_barcode="1234567890127", product_name="Dell XPS 13", product_price=1499.99, product_quantity=75),
        Product(product_barcode="1234567890128", product_name="Sony WH-1000XM5 Headphones", product_price=399.99, product_quantity=200),
        Product(product_barcode="1234567890129", product_name="Apple Watch Series 9", product_price=499.99, product_quantity=10),
        Product(product_barcode="1234567890130", product_name="Samsung Galaxy Watch 6", product_price=299.99, product_quantity=150),
        Product(product_barcode="1234567890131", product_name="iPad Pro 12.9-inch", product_price=1099.99, product_quantity=0),  # Out of stock
        Product(product_barcode="1234567890132", product_name="Microsoft Surface Laptop 5", product_price=1299.99, product_quantity=60),
        Product(product_barcode="1234567890133", product_name="Bose QuietComfort 45 Headphones", product_price=329.99, product_quantity=90),
        Product(product_barcode="1234567890134", product_name="Logitech MX Master 3S Mouse", product_price=99.99, product_quantity=40),
        Product(product_barcode="1234567890135", product_name="Canon EOS R7 Camera", product_price=1499.99, product_quantity=30),
        Product(product_barcode="1234567890136", product_name="Nintendo Switch OLED", product_price=349.99, product_quantity=80),
        Product(product_barcode="1234567890137", product_name="PlayStation 5", product_price=499.99, product_quantity=20),
    ]
    db.add_all(products)
    db.commit()
    print("Added 15 dummy products (2 out of stock).")

# Main function to populate the database
def populate_database():
    create_dummy_users()
    create_dummy_products()
    print("Database populated with dummy data.")

# Run the script
if __name__ == "__main__":
    populate_database()