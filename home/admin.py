# home/admin.py
from django.contrib import admin
from .models import HomePage
from .models import ServiceHome
from .models import HomeItem
from .models import HomeImage
from .models import Testimoni


admin.site.register(HomePage)

admin.site.register(ServiceHome)

admin.site.register(HomeItem)

admin.site.register(HomeImage)

admin.site.register(Testimoni)