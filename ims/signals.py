from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase 
from django.core.mail import send_mail

@receiver(post_save, sender=Purchase)
def after_purchase(sender, instance, **kwargs):
   print("A Purchase created")
   send_mail(
      subject="Purchase Items",
      message="You have purchased items",
      from_email="ims@gmail.com",
      recipient_list=['ram@gmail.com']
   )