from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.description[:30]}..."


class Link(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.SET_NULL, null=True)
    link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.link


class Message(models.Model):
    room = models.ForeignKey(Entry, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body[0:50]
