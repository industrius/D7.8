from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Author, Book, Publisher, Profile

@admin.register(Author)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("full_name", "birth_year", "country")
    list_display_links = ("full_name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("get_image", "title", "author" , "year_release", "copy_count")
    list_display_links = ("title",)
    list_filter = ("author",)
    search_fields = ("title", "author")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100"')

admin.site.register(Publisher)
admin.site.register(Profile)

admin.site.site_title = "books:shelf"
admin.site.site_header = "books:shelf"