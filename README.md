Deboss Footwear

A Django-powered e-commerce platform for footwear and fashion accessories, including shoes, belts, and more.

Deboss Footwear allows customers to browse products, explore categories, view product details, manage shopping carts, and place orders online using Pay on Delivery.

🌐 Live Demo: https://deboss-footwear.onrender.com

Screenshots

Homepage Preview

"Deboss Footwear Homepage" (homepage.jpg)

Shop Page

"Deboss Footwear Shop" (shop.jpg)

Shopping Cart

"Deboss Footwear Cart" (cart.jpg)

Order History

"Deboss Footwear Order History" (order.jpg)

Custom Order Enquiries

"Deboss Footwear Custom Order" (custom-order.jpg)

Technology Stack

- Backend: Python, Django
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript
- Deployment: Render
- Database Hosting: Neon PostgreSQL
- Media Storage: Cloudinary

Features

Customer Features

- Customer registration, login, and authentication
- Product browsing and category filtering
- Product details with size and variant selection
- Shopping cart management
- Checkout with Pay on Delivery
- Customer order history and order details

Order and Inventory Management

- Inventory and stock management
- Order status management
- Payment status management

Communication

- Custom order enquiries through WhatsApp
- Direct WhatsApp communication for customer enquiries

Admin Features

- Django Admin dashboard for managing products, categories, inventory, and orders

Architecture

Deboss Footwear follows Django's Model-Template-View (MTV) architecture.

- Models: Manage application data, including products, customers, inventory, carts, and orders.
- Views: Handle incoming requests, application logic, and interactions between models and templates.
- Templates: Render the user interface using Django templates.
- Database: PostgreSQL stores production data, while SQLite can be used for local development.

Architecture Diagram

flowchart TD
    A[Customer / Browser] --> B[Django URLs]
    B --> C[Django Views]
    C --> D[Django Models]
    D --> E[(PostgreSQL Database)]
    C --> F[Django Templates]
    F --> A
    C --> G[WhatsApp]
    H[Django Admin] --> D

Local Setup

1. Clone the Repository

git clone https://github.com/corni-codes/shoe-store.git
cd shoe-store

2. Install Dependencies

pip install -r requirements.txt

3. Configure Environment Variables

Create a ".env" file in the project root and configure the required environment variables.

SECRET_KEY=your-generated-secret-key
DEBUG=True

Generate your own Django secret key. Do not use production credentials.

4. Apply Database Migrations

python manage.py migrate

5. Run the Development Server

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

Deployment

The application is deployed on Render, with Neon PostgreSQL providing the production database and Cloudinary handling media storage.

Live URL: https://deboss-footwear.onrender.com

Project Status

Status: Live

The application is deployed and accessible online.

Author

Developed by corni-codes.
