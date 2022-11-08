from django.contrib import admin

from .models import Category, Genre, Title, User, Review, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


class TitleInline(admin.TabularInline):
    model = Title.genre.through


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category')
    inlines = [
        TitleInline,
    ]
    search_fields = ('name',)
    raw_id_fields = ('genre',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'pub_date', 'title', 'score')
    search_fields = ('text',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'pub_date', 'review')
    search_fields = ('text',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
