from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import Event

@receiver(m2m_changed, sender=Event.participant.through)
def send_rsvp_confirmation_email(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            send_mail(
                subject=f"RSVP Confirmation: {instance.name}",
                message=f"Hello {user.first_name},\n\n"
                        f"You have successfully RSVP'd for the event '{instance.name}'.\n\n"
                        f"📅 Date: {instance.date}\n"
                        f"⏰ Time: {instance.time}\n"
                        f"🕸 Location: {instance.location}\n\n"
                        f"Thank you for joining us!\n\nBest,\nEventure Team",
                from_email="zishanahmed344@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,
            )
