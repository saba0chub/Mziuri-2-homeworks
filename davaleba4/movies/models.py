from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="janri")

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="saxeli")
    birth_year = models.IntegerField(null=True, blank=True, verbose_name="dabadebis weli")
    bio = models.TextField(blank=True, verbose_name="biografia")

    def __str__(self):
        return self.name


class Movie(models.Model):
    class AgeRating(models.TextChoices):
        G = 'G', 'yvelastvis'
        PG = 'PG', 'mshoblis tanxlebit'
        PG13 = 'PG13', '13+'
        R = 'R', '18+'

    title = models.CharField(max_length=200, verbose_name="satauri")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="agwera")
    release_year = models.PositiveIntegerField(verbose_name="gamoshvebis weli")
    duration_minutes = models.PositiveIntegerField(verbose_name="xangrdzlivoba")
    age_rating = models.CharField(
        max_length=10,
        choices=AgeRating.choices,
        default=AgeRating.G,
        verbose_name="asakobrivi reitingi"
    )
    budget = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="biujeti"
    )
    is_published = models.BooleanField(default=False, verbose_name="gamoqveynebulia")
    language = models.CharField(max_length=30, default="qartuli", verbose_name="ena")
    poster_url = models.URLField(blank=True, verbose_name="posteris URL")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="sheqmnis tarigi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="ganaxlebis tarigi")

    class Meta:
        ordering = ['-release_year']
        verbose_name = "filmi"
        verbose_name_plural = "filmebi"

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Festival(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="festivalis saxeli")
    city = models.CharField(max_length=100, verbose_name="qalaqi")
    start_date = models.DateField(verbose_name="dawyebis tarigi")
    end_date = models.DateField(verbose_name="dasrulebis tarigi")
    website = models.URLField(blank=True, null=True, verbose_name="website")
    contact_email = models.EmailField(blank=True, null=True, verbose_name="e-mail")
    is_international = models.BooleanField(default=True, verbose_name="saertashorisoa")

    class Meta:
        ordering = ['start_date']
        verbose_name = "festivali"
        verbose_name_plural = "festivalebi"

    def __str__(self):
        return f"{self.name} ({self.city})"