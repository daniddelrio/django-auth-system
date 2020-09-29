from django.contrib.auth import get_user_model

def create_user_account(email, password, **extra_args):
    user = get_user_model().objects.create_user(
		email=email, password=password, **extra_args
    )
    return user