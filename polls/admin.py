from django.contrib import admin

from .models import Doctor
from .models import Login
from .models import Heal

admin.site.register(Doctor)
admin.site.register(Login)
admin.site.register(Heal)
# Register your models here.
