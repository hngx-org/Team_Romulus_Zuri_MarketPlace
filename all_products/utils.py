from MarketPlace.models import Product


def is_deleted_active(queryset):
	return queryset.filter(is_deleted='active')