from  quotes.models import Qoutes
from django.contrib import admin
from  .models import Comments

admin.site.register(Comments)
admin.site.register(Qoutes)
