from django.contrib import admin
from . models import Signup,Event,Notice,Login

# Register your models here.
admin.site.register(Signup)
admin.site.register(Event)
admin.site.register(Notice)
admin.site.register(Login)