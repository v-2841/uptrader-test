from django.contrib import admin
from django.contrib.auth.models import Group, User

from menu.models import MenuItem


admin.site.register(MenuItem)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_title = 'Updater test'
admin.site.site_header = 'Updater test'
admin.site.index_title = 'Администрирование сайта'
