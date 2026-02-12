from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///amazon.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    phone = Column(String)
    alt_phone = Column(String)
    isprime=Column(Boolean)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    category = Column(String)
    stock = Column(Integer)
    image=Column(String)
    size=Column(String)
    color=Column(String)
    brand=Column(String)
    rating=Column(Float)
    reviews=Column(Integer)
    isprime=Column(Boolean)
    taxpersentage=Column(Float)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    total_price = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    payment_type = Column(String)
    payment_status = Column(String)

class cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

class wishlist(Base):
    __tablename__ = 'wishlist'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())  

class product_review(Base):
    __tablename__ = 'product_review'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    review = Column(String)
    rating = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())          

class order_details(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
sample_users = [
    User(name='John Doe', email='[EMAIL_ADDRESS]', password='password'),
    User(name='Jane Smith', email='[EMAIL_ADDRESS]', password='password')
]
session.add_all(sample_users)
session.commit()

sample_products = [
    Product(name='Laptop', price=1000, description='High performance laptop', image_url='https://example.com/laptop.jpg'),
    Product(name='Mouse', price=25, description='Wireless mouse', image_url='https://example.com/mouse.jpg')
]
session.add_all(sample_products)
session.commit()

sample_orders = [
    Order(user_id=1, product_id=1, quantity=1, total_price=1000, order_date='2022-01-01'),
    Order(user_id=2, product_id=2, quantity=2, total_price=50, order_date='2022-01-02')
]
session.add_all(sample_orders)
session.commit()

# Query data
users = session.query(User).all()
products = session.query(Product).all()
orders = session.query(Order).all()

print('Users:', users)
print('Products:', products)
print('Orders:', orders)

session.close()