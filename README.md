# E-Commerce Hub (Django)

A full-featured starter e-commerce website built with Django. It includes product browsing, category filtering, a session-backed cart, and a checkout-ready layout.

## Features

- Product catalog with categories and featured products
- Session cart with add/remove flows
- Checkout screen template for order capture
- Django admin configuration for product management

## Getting started

1. Install dependencies

   ```
   pip install -r requirements.txt
   ```

2. Run migrations

   ```
   python ecommerce/manage.py migrate
   ```

3. Create a superuser (optional, for admin access)

   ```
   python ecommerce/manage.py createsuperuser
   ```

4. Start the development server

   ```
   python ecommerce/manage.py runserver
   ```

5. Visit the site at `http://127.0.0.1:8000/` and add products in the admin at `http://127.0.0.1:8000/admin/`.
