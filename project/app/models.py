from django.db import models

# Create your models here.
from django.utils.text import slugify


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class VacancyTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Requirement(models.Model):
    requirement = models.CharField(max_length=255)

    def __str__(self):
        return self.requirement


class Job(models.Model):
    title = models.ForeignKey(VacancyTitle, null=True,
                              on_delete=models.SET_NULL)

    company = models.ForeignKey(Company, null=True,
                                on_delete=models.SET_NULL)
    description = models.TextField(null=True)
    salary = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    requirements = models.ManyToManyField(Requirement)

    def __str__(self):
        return f"{self.title} - {self.company} - {self.salary}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.company}-{self.salary}")
        super().save(*args, **kwargs)
