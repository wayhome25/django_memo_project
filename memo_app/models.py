from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Memos(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50, db_column='제목')
    text = models.TextField(max_length = 230, db_column='내용', help_text='메모 내용은 230자 이내로 입력 가능합니다.')
    update_date = models.DateTimeField()
    priority = models.BooleanField(db_column='중요')
    likes = models.ManyToManyField(User, related_name='likes')

    @property
    def total_likes(self):
        return self.likes.count()

    def generate(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s by %s' % (self.title, self.name_id)
