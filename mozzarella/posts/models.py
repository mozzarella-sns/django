from django.db import models
from mozzarella.users.models import User


class Post(models.Model):
    class Meta:
        db_table = 'post'

    user_id = models.ForeignKey(User, verbose_name="投稿者ID", on_delete=models.SET_NULL)
    post_text = models.CharField(max_length=1000)
    created_date = models.DateTimeField()
