class PrimaryRouter:
	def db_for_read(self, model, **hints):
		return 'primary'

	def db_for_write(self, model, **hints):
		return 'primary'

	def allow_relation(self, obj1, obj2, **hints):
		return True

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		return False

class DefaultRouter:
	route_app_labels = ['auth', 'contenttypes', 'admin', 'sessions', 'messages', 'staticfiles', 'rest_framework']

	def db_for_read(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'default'

	def db_for_write(self, model, **hints):
		if model._meta.app_label in self.route_app_labels:
			return 'default'

	def allow_relation(self, obj1, obj2, **hints):
		if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
			return True

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		return True