# E-Store

E-Store is a Django-based e-commerce application that allows users to browse products, add them to a cart, and proceed to checkout.

## Features

- Product listing and detail pages
- Shopping cart functionality
- User authentication
- Checkout process with Stripe integration

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/drayerh/estore.git
   cd estore
   ```
2. Create a virtual environment and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   
3. Apply the migrations:

   ```bash
    python manage.py migrate
    ```
4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:

   ```bash
   python manage.py runserver
   ```
6. Open the browser and go to http://127.0.01:8000/.

Running in Production

1. Set the `DEBUG` setting to `False` in settings.py:

   ```python
   DEBUG = False
   ```
2.Configure the `ALLOWED_HOSTS` setting with the domain name of your site:

   ```python
   ALLOWED_HOSTS = ['yourdomain.com']
   ```
3.Set up a production-ready web server (e.g., Nginx, Gunicorn) and a reverse proxy (eg., Nginx).

4. Collect the static files:

   ```bash
   python manage.py collectstatic
   ```
   
5.Ensure that environment variables are set for
    - `DJANGO_SECRET_KEY`
    - `STRIPE_PUBLIC_KEY`
    - `STRIPE_SECRET_KEY`
    - `STRIPE_WEBHOOK_SECRET`

6. Start the Gunicorn server:

    ```bash
    gunicorn estore.wsgi:application
    ```
7.Configure Nginx to serve the static files and forward requests to the Gunicorn server.