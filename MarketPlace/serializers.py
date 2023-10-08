from rest_framework import serializers


class GetAllCategoriesProductSerializer(serializer.Serializers):
    product_id = serializers.CharField
    title = serializers.CharField(max_length=225, null=False)
    