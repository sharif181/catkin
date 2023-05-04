from django.contrib import admin
from .models import TeamMember, Designation

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    pass

