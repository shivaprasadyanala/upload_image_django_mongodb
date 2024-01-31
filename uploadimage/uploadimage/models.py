from django.db import models

class Test(models.Model):
    # image_file = models.FileField(upload_to='images/')
    image_file = models.FileField(upload_to='images/')
