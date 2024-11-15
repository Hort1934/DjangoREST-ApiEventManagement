from django.core.mail import send_mail
from django.conf import settings

def send_registration_email(user, event):
    subject = f"Registration Confirmation for {event.title}"
    message = f"Hello {user.username},\n\nYou have successfully registered for the event '{event.title}' on {event.date} at {event.location}.\n\nThank you for registering!\n\nBest regards,\nEvent Management Team"
    recipient_list = [user.email]
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
