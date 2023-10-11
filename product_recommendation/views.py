from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from MarketPlace.models import Product, UserProductRating, Shop
from MarketPlace.serializers import ProductSerializer

# Create your views here.

from django.db.models import F
from django.db.models import FloatField
from django.db.models import Min
from django.db.models import Avg
from django.db.models import Value
from django.db.models import Count

class ProductRecommendationView(APIView):
    def get(self, request):
        try:
            # Retrieve products with the highest quantity
            highest_quantity_products = Product.objects.order_by('-quantity')[:20]

            # Retrieve products with the highest discount price
            highest_discount_products = Product.objects.order_by('-discount_price')[:20]

            # Retrieve products with the highest rating
            highest_rated_products = Product.objects.filter(
                rating_id__isnull=False
            ).annotate(
                avg_rating=Avg('rating_id__rating', output_field=FloatField())
            ).order_by('-avg_rating')[:20]

            # Retrieve products that have been reviewed
            reviewed_products = Product.objects.filter(rating_id__isnull=False).annotate(
                num_reviews=Count('rating_id')
            ).order_by('-num_reviews')[:20]

            # Retrieve products with the lowest tax
            lowest_tax_products = Product.objects.annotate(
                lowest_tax=Min('tax')
            ).filter(
                tax=F('lowest_tax')
            )[:20]

            # Combine the recommendations without duplicates
            recommended_products = list(
                set(
                    highest_quantity_products |
                    highest_discount_products |
                    highest_rated_products |
                    reviewed_products |
                    lowest_tax_products
                )
            )[:20]

            # Serialize the recommended products
            serializer = ProductSerializer(recommended_products, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 
 











# # Import necessary modules and functions at the beginning of your views.py file
# from django.db.models import Avg

# # Import UserProductInteraction model if not already imported
# from MarketPlace.models import UserProductInteraction, User

# # Import the necessary serializers
# from MarketPlace.serializers import ProductSerializer

# Add the missing imports and make necessary modifications to the code
# ...

# class PersonalizedRecommendationView(APIView):
#     def get(self, request, user_id):
#         try:
#             # Retrieve the user's profile
#             user = User.objects.get(id=user_id)

#             # Calculate user's content-based preferences
#             user_preferences = self.calculate_user_preferences(user)

#             # Get product recommendations based on content-based filtering
#             recommended_products = self.get_content_based_recommendations(user_preferences)

#             # Serialize the recommended products
#             serializer = ProductSerializer(recommended_products, many=True)

#             return Response(serializer.data, status=status.HTTP_200_OK)

#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def calculate_user_preferences(self, user):
#         # Initialize preference values
#         total_price_preference = 0
#         total_category_preference = 0

#         # Get all user interactions with products
#         interactions = user.userproductinteraction_set.all()

#         # Calculate preferences based on interactions
#         for interaction in interactions:
#             product = interaction.product
#             # Example: Calculate price preference based on ratings
#             total_price_preference += interaction.rating * product.price

#             # Example: Calculate category preference based on the category of the product
#             total_category_preference += interaction.rating * product.category.id

#         # Calculate average preferences
#         num_interactions = len(interactions)
#         if num_interactions > 0:
#             average_price_preference = total_price_preference / num_interactions
#             average_category_preference = total_category_preference / num_interactions
#         else:
#             # Handle cases where the user has no interactions
#             average_price_preference = 0
#             average_category_preference = 0

#         user_preferences = {
#             'price_preference': average_price_preference,
#             'category_preference': average_category_preference,
#         }

#         return user_preferences


#     def get_content_based_recommendations(self, user_preferences):
#         # Implement your content-based filtering logic to recommend products
#         # You can query products based on their attributes that match user preferences

#         price_preference = user_preferences['price_preference']
#         category_preference = user_preferences['category_preference']

#         # Filter products based on user preferences
#         recommended_products = Product.objects.filter(
#             price__lte=price_preference * 1.2,  # You can adjust the tolerance as needed
#             category__id=category_preference
#         ).order_by('-quantity')[:10]

#         return recommended_products

# h


















# class PopularityBasedRecommendationView(APIView):
#     def get(self, request):
#         try:
#             # Retrieve popular products (e.g., top 10 products based on quantity)
#             popular_products = Product.objects.order_by('-quantity')[:10]
            
#             # Serialize the recommended products
#             serializer = ProductSerializer(popular_products, many=True)
            
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
