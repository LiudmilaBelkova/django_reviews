from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    actors = models.CharField(max_length=200)
    review = models.TextField()
    STARS = (
        ("s", 1),
        ("ss", 2),
        ("sss", 3),
        ("ssss", 4),
    )
    stars = models.CharField(
        max_length=4,
        choices=STARS,
        default=1,
    )

    def __str__(self):
        return self.title
