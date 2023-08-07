from celery import shared_task
from django.core.mail import send_mail
from .models import FriendRequest, User

@shared_task
def friend_request_sent(from_username, to_username):
    """Task to send an e-mail notification when a user receives a friend
    request."""
    from_user = User.objects.get(username=from_username)
    to_user = User.objects.get(username=to_username)
    user = FriendRequest.objects.get(from_user=from_user, to_user=to_user)
    subject = f'You have received a friend request'
    message = f'Dear {user.to_user.first_name}, \n\n You have received a friend request from {user.from_user.first_name}. \n\n Login to your account to accept your friend request.'
    mail_sent = send_mail(subject,
                          message,
                          'jobhdezlara93@gmail.com',
                          [user.to_user.email])
    return mail_sent
