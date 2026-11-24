from django.contrib import admin
from .models import Genre, Director, Movie, Festival


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "director", "release_year", "age_rating", "is_published")
    list_filter = ("age_rating", "is_published", "director")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}

    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        blank=True,
        verbose_name="ჟანრები",
    )

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Festival)