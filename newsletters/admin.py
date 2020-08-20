from django.contrib import admin
from newsletters.models import Newsletter, Vote, Tag
# Register your models here.


admin.site.register(Newsletter)
admin.site.register(Vote)
admin.site.register(Tag)

