from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.conf import settings

def send_verification_email(user, email):
	mail_subject = 'Verify your email.'
	message = render_to_string('webapp/acc_active_email.html', {
		'user' : user,
		'default_domain' : settings.DEFAULT_DOMAIN,
		'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
		'token' : account_activation_token.make_token(user),
	})
	email_body = EmailMessage(mail_subject, message, to=[email])
	email_body.send()

def create_user_account(email, password, **extra_args):
    user = get_user_model().objects.create_user(
		email=email, password=password, is_active=False, **extra_args
    )
    return user