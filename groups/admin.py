from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline): #this helps to edit groupmember when editing group
    model = models.GroupMember

admin.site.register(models.Group)
