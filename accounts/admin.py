from django.contrib import admin

from .models import Teacher, Student, SchoolClass


class TeacherAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class SchoolClassAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)

admin.site.site_header = '翻转课堂管理后台'
