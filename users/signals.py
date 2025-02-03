from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
@receiver(post_save,sender=User)
def send_activation_email(sender,instance,created,**kwargs):
  if created:
    token = default_token_generator.make_token(instance)
    activation_url = f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}"
    mail_subject ='Activate Your user account'
    message = f'Hi {instance.username},\n\nPlease activate your account by clicking the link below:\n{activation_url}\n\nThank You!'
    recipient_list = [instance.email]
    try:
      send_mail(mail_subject, message, settings.EMAIL_HOST_USER,recipient_list)
      
    except Exception as e:
      print(f"Failed to send email to {instance.email}: {str(e)}")


""" class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
  def _make_hash_value(self, user, timestamp):
    return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)

account_activation_token = AccountActivationTokenGenerator()
 """