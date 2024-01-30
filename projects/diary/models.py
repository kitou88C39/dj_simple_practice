from django.db import models
from django.utils import timezone

class Day(models.Model):
    title=models.CharField('タイトル',max_length=200)