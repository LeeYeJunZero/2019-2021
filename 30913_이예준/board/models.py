from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(
        max_length=255,
    )
    content = models.TextField()
    create_date = models.DateTimeField(
        auto_now_add=True,
    )
    update_date = models.DateTimeField(
        auto_now=True
    )

    objects = models.Manager()

    def __str__(self):
        return(
            f"[{self.pk}]  {self.title}"
            f"{self.create_date}"
        )