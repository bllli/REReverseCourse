from django.contrib import admin

from .models import Course, Resource


class CourseAdmin(admin.ModelAdmin):
    pass


class ResourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Resource, ResourceAdmin)
