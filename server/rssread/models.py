from django.db import models

# Create your models here.

class RssSources(models.Model):
    rss_url = models.CharField(null=False)
    user_number = models.IntegerField()


class Posts(models.Model):
    rss_url = models.CharField(null=False)
    post_id = models.CharField(null=False)
    post_author = models.CharField(default = "匿名用户")
    post_title = models.CharField(null=False)
    post_time = models.CharField(null=False) 
    post_content = models.TextField(null=False)
    time_stamp = models.FloatField()