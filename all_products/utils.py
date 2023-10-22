from MarketPlace.models import Product


def is_deleted_active(queryset):
	return queryset.filter(is_deleted='active')

def admin_status_approved(queryset):
	return queryset.filter(admin_status='approved')