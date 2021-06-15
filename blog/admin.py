from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin



class RecipeInLine(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_time', 'cook_time', 'post')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',  'category', 'created_at', 'id')
    inlines = [RecipeInLine]
    save_as = True
    save_on_top = True


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
