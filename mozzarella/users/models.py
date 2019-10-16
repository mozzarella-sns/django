from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    thumbnail_img = ImageField(verbose_name='サムネイル画像')
    

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
