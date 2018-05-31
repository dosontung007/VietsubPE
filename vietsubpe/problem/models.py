from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    solved_by = models.IntegerField(default=0)

    def __str__(self):
        return self.title