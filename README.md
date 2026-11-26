
# Deboss Footwear

A Django-powered e-commerce platform for footwear and fashion accessories, including shoes, belts, and more.

The platform allows customers to browse products, explore categories, view product details, manage their shopping carts, and place orders online using Pay on Delivery.

## Homepage Preview

![Deboss Footwear Homepage](homepage.jpg)

### Custom Order Enquiries

![Deboss Footwear Custom Order](custom-order.jpg)

## Technology Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render
- **Database Hosting:** Neon

## Features

- Customer registration, login, and authentication
- Product browsing and category filtering
- Product details with size and variant selection
- Shopping cart management
- Inventory and stock management
- Checkout with Pay on Delivery
- Customer order history and order details
- Order status and payment status management
- **Custom order enquiries through WhatsApp**
- Direct WhatsApp communication for customer enquiries
- Admin dashboard for managing products, inventory, and orders

## Architecture

Deboss Footwear follows Django's Model-Template-View (MTV) architecture.

- **Models:** Handle application data, products, customers, inventory, carts, and orders.
- **Views:** Process requests, apply business logic, and coordinate application operations.
- **Templates:** Render the user interface using Django templates.
- **Database:** PostgreSQL stores production data, while SQLite can be used for local development.

### Architecture Diagram

```mermaid
flowchart TD
    A[Customer / Browser] --> B[Django URLs]
    B --> C[Django Views]
    C --> D[Models]
    D --> E[(Database)]
    C --> F[Templates]
    F --> A
    C --> G[WhatsApp]
    H[Django Admin] --> D
```

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/corni-codes/shoe-store.git
cd shoe-store
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root and add:

```env
SECRET_KEY=your-generated-secret-key
DEBUG=True
```

Generate your own Django secret key. Do not use production credentials.

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Deployment

The application is deployed on Render, with Neon PostgreSQL providing the production database.

## Project Status

**Status:** Live

The application is deployed and accessible online.

## Author

Developed by **corni-codes**.
