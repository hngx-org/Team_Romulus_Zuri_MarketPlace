from django.contrib import admin
from MarketPlace.models import *
import django.apps

<<<<<<< HEAD
# Register your models here.
admin.site.register(Product)
=======
models = django.apps.apps.get_models()

for model in models:
	try:
		admin.site.register(model)
	except:
		pass
>>>>>>> 92ec6e7eb7d506979780363fecb52787a30681e3
