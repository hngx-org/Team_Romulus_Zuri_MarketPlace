from django.contrib import admin
from MarketPlace.models import *
import django.apps

models = django.apps.apps.get_models()

for model in models:
	try:
		admin.site.register(model)
	except:
		pass
