from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created
from .models import UniwareMaster, UniwareDimension, Inbound



@receiver(post_save, sender=UniwareMaster)
def at_ending_save(sender, instance, created, **kwargs):
 if created:
  print("----------------------------")
  print("Post Save Signal...")
  print("New Record")
  print("Sender:", sender)
  print("Instance:", instance)
  print("Created:", created)
  print(f'Kwargs: {kwargs}')
  input_data = UniwareDimension(uniware = instance, length = 10, width = 10, height = 10)
  input_data.save()
 else:
  print("----------------------------")
  print("Post Save Signal...")
  print("Update")
  print("Sender:", sender)
  print("Instance:", instance)
  print("Created:", created)
  print(f'Kwargs: {kwargs}')