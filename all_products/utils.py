def is_deleted_active(queryset):
	return queryset.filter(is_deleted='active')

def admin_status_approved(queryset):
	return queryset.filter(admin_status='approved')

def admin_approved_shop(queryset):
	return queryset.filter(shop__admin_status='approved')

def shop_not_deleted(queryset):
	return queryset.filter(shop__is_deleted='active')

def shop_not_restricted(queryset):
	return queryset.filter(shop__restricted='no')