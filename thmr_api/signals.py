# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from .models import ManagerExtraInfo

# User = get_user_model()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         ManagerExtraInfo.objects.create(user=instance)
#     instance.manager_extra_info.save()