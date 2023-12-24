# Django Email Sender

A Django project for sending emails using Django's email functionalities.

## Overview

This Django project facilitates the sending of emails through Django's email backend. It provides an API endpoint to send emails by accepting JSON data containing email, subject, and body.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/popeyewrener/django_email_sender.git
   cd django_email_sender

2. Install dependencies:
    ```bash
    pip install -r requirements.txt


3.  Set up environment variables:

  Create a .env file based on .env.example and fill in your email configuration details.
  Ensure the .env file is in the project's root directory.
    
4. Usage
To start the Django server, run the following command:
    ```bash
    python manage.py runserver
5. API Endpoint
  POST /api/send-email/ 
  Payload format:

  ```bash
  {
    "email": "recipient@example.com",
    "subject": "Your Subject",
    "body": "Your Email Body"
}

    

