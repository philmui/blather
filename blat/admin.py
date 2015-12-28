from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from blat.models import Blat, Profile

# Register your models here.
class BlatAdmin(admin.ModelAdmin):
	list_display = ('text', 'created_on', 'total_likes', 'created_by')
	list_filter = ['created_on']
	search_fields = ['text']

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (ProfileInline, )

admin.site.register(Blat, BlatAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)