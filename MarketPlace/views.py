from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, UserProfile, UserProductInteraction
from .serializers import ProductSerializer
import random
from django.db.models import Q



class SimilarProductView(APIView):
    @staticmethod
    def get(request, product_id):
        try:
            current_product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        similar_products = Product.objects.filter(category=current_product.category).exclude(id=product_id)

        similar_products = list(similar_products)
        random.shuffle(similar_products)

        recommended_products = similar_products[:4]

        serializer = ProductSerializer(recommended_products, many=True)

        return Response({'similar_products': serializer.data}, status=status.HTTP_200_OK)
    
class FilterProductView(APIView):
    def get(self, request):
        # Parameters from request
        discount = self.request.query_params.get('discount')
        category = self.request.query_params.get('category')
        keywords = self.request.query_params.get('keywords')

        products = Product.objects.all()

        if discount:
            products = products.filter(discount_price__lte=discount)
        
        if category:
            products = products.filter(category=category)

        if keywords:
            products = products.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords))

        serializer = ProductSerializer(products, many=True)

        return Response({'products': serializer.data}, status=status.HTTP_200_OK)
    



class RecommendationView(APIView):
    def get(self, request, user_id):
        try:
            # Retrieves the user's profile and interaction history
            user_profile = UserProfile.objects.get(user_id=user_id)
            user_interactions = UserProductInteraction.objects.filter(user_id=user_id)

            # Implemented the recommendation logic 
            recommended_products = self.get_recommendations(user_profile, user_interactions)

            # Serialized the recommended products
            serializer = ProductSerializer(recommended_products, many=True)

            return Response(serializer.data)

        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found"}, status=404)

    def get_recommendations(self, user_profile, user_interactions):
        # Implemented the recommendation logic 
        # This is a simplified example using content-based filtering

        # Getting user's profile attributes (e.g., age, gender, etc.)
        user_attributes = {
            "age": user_profile.age,
            "gender": user_profile.gender,
        }

        # Initialize a dictionary to store product scores
        product_scores = {}

        # Loop through user interactions to calculate scores
        for interaction in user_interactions:
            product = interaction.product

            # Example: Calculate a score based on product attributes and user profile
            # You should replace this with your actual recommendation algorithm
            score = self.calculate_product_score(product, user_attributes)

            # Store the score for this product
            product_scores[product.id] = score

        # Sort products by their scores in descending order
        sorted_product_scores = sorted(product_scores.items(), key=lambda x: x[1], reverse=True)

        # Get the top recommended products (you can adjust the number as needed)
        top_recommendations = [Product.objects.get(id=product_id) for product_id, _ in sorted_product_scores[:10]]

        return top_recommendations

    def calculate_product_score(self, product, user_attributes):
        # Implement your scoring logic here
        # This is a simplified example; replace with your own algorithm
        # You can calculate a score based on product attributes and user attributes
        score = 0

        # Example: Give higher score to products in the same category as the user's gender
        if product.category == user_attributes["gender"]:
            score += 1

        # Add more scoring rules as needed based on product attributes and user attributes

        return score

