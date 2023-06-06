from django.contrib import admin
from .models import Task, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Photo)
