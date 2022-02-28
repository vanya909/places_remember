from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.db import models
from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    User = get_user_model()
    user = models.OneToOneField(User, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    avatar_url = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta():
        db_table = 'user_profile'


@receiver(user_signed_up)
def social_login_fname_lname_profilepic(sociallogin, user, **kwargs):
    picture_url = ''
    if sociallogin:
        if sociallogin.account.provider == 'vk':
            user.first_name = sociallogin.account.extra_data['first_name']
            user.last_name = sociallogin.account.extra_data['last_name']
            user.username = sociallogin.account.extra_data['id']
            picture_url = sociallogin.account.extra_data['photo_big']

    user.save()
    profile = UserProfile(user=user, avatar_url=picture_url)
    profile.save()
