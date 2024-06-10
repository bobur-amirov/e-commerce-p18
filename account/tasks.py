from django.core.mail import send_mail
from django.conf import settings

from Ecommerce.celery import app



@app.task(bind=True)
def send_email(self, email, code, redirect_url, **kwargs):
    subject = 'Verify your email'
    message = f"Verify your code: {code} Url: {redirect_url}"
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email]
    )