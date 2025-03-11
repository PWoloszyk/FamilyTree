from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to="images/", null=True, blank=True)
    father = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="father_of",
    )
    mother = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mother_of",
    )
    partners = models.ManyToManyField(
        "self", blank=True, symmetrical=True, related_name="partners"
    )
    root = models.BooleanField("root", default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
