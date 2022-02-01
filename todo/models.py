from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
#KUllanıcı 1,2,3 girer arkada biz low medium görürürz
    PRIORITY = (
        ("1", "High"),
        ("2", "Medium"),
        ("3", "Low"),
    )
#priority(öncelik) buradaki fieldları PRİORTY den sec choıse o se yarrar
    priority = models.CharField(max_length=50, choices=PRIORITY)
    isDone = models.BooleanField(default=False)
#auto now hergüncellendiğinde yenile auto now add oluşturulduğu tarih
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
