from django.db import models


class TodoData(models.Model):
    title = models.CharField(max_length=205)
    message = models.TextField(max_length=1005)
    email = models.EmailField()
    time = models.DateTimeField()
    complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'time': self.time.strftime("%d %b %Y %H:%M:%S"),
            'complete': self.complete,
            'timestamp': self.timestamp.strftime("%d %b %Y %H:%M:%S"),
        }
