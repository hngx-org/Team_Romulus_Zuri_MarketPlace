from rest_framework import serializers
from MarketPlace.models import Product

# class ProductViewSerializer(serializers.ModelSerializer):
#     # sorting_option = serializers.ChoiceField(
#     #     choices=[
#     #         (SortingOptions.NAME_ASC, 'Name (A-Z)'),
#     #         (SortingOptions.NAME_DESC, 'Name (Z-A)'),
#     #         (SortingOptions.DATE_CREATED_ASC, 'Date Created (Oldest first)'),
#     #         (SortingOptions.DATE_CREATED_DESC, 'Date Created (Newest first)'),
#     #         (SortingOptions.RATING_ASC, 'Rating (Lowest first)'),
#     #         (SortingOptions.RATING_DESC, 'Rating (Highest first)'),
#     #         (SortingOptions.PRICE_ASC, 'Price (Lowest first)'),
#     #         (SortingOptions.PRICE_DESC, 'Price (Highest first)'),
#     #     ],
#     #     write_only=True,
#     #     required=False,
#     # )

#     class Meta:
#         model = ProductView
#         fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
