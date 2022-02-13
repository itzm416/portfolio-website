from django.contrib import admin
from app.models import Contact, Portfolio, Project

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','desc')
    search_fields = ('title',)

admin.site.register(Portfolio)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
