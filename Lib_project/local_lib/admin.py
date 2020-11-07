from django.contrib import admin
from local_lib import models

class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance
    extra = 1

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('title', 'author', 'genre')
    inlines = [BooksInstanceInline]


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
