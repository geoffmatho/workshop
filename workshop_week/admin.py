from django.contrib import admin
from workshop_week.models import Category, School, Workshop, User, Week, Registration

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


class WorkshopAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


class RegistrationAdmin(admin.ModelAdmin):
    pass


class WeekAdmin(admin.ModelAdmin):
    pass

class SchoolAdmin(admin.ModelAdmin):
    pass

    
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(School, SchoolAdmin)
