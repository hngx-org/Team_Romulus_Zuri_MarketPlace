<!--- Provide a general summary of your changes in the Title above -->
​
## Description
Model Definition: In the models.py file, a Wishlist model is defined. It includes fields for the user who owns the wishlist and a many-to-many relationship with products. Each wishlist entry is associated with a timestamp indicating when the product was added.

Serializer Configuration: The serializers.py file defines a serializer class, WishlistSerializer, which handles the serialization and deserialization of wishlist data. It specifies the model and fields to include in the serialized data.

View for Adding Products: The main functionality is in the view function add_to_wishlist located in the views.py file. This view accepts HTTP POST requests and expects a list of product IDs in the request data. It retrieves or creates the user's wishlist and adds the specified products to it. The view then serializes the updated wishlist data and returns it in the response.

URL Pattern: The urls.py file defines a URL pattern that maps the /wishlist/add/ endpoint to the add_to_wishlist view. Users can make POST requests to this endpoint to add products to their wishlist.
​
## Related Issue (Link to linear ticket)
https://linear.app/zuri-project-backend/issue/MAR-26/add-to-wishlist
​
## Motivation and Context
This change enables users to add products to their wishlist directly from, improving the user experience by allowing them to save and organize products they're interested in for future reference or potential purchase. This aligns with common e-commerce practices, enhancing the application's functionality.
​
## How Has This Been Tested?
I extensively tested these changes using Postman. I created test cases to cover various scenarios,
including adding products to the wishlist, verifying successful additions, handling errors, and checking the response format. I tested with different user IDs to ensure it works for multiple users. The goal was to confirm that the endpoint functions correctly, handles errors appropriately, and provides the expected JSON responses
​
## Screenshots (if appropriate - Postman, etc):


![Screenshot 2023-10-08 145451](https://github.com/hngx-org/Team_Romulus_Zuri_MarketPlace/assets/62937590/77e2abd7-bacc-452f-b38f-dc7fbf542ec7)

![Screenshot 2023-10-08 145451](https://github.com/hngx-org/Team_Romulus_Zuri_MarketPlace/assets/62937590/9401270f-2a6a-4cd0-bb8f-19705baad431)



## Types of changes
- [ ] New feature (non-breaking change which adds functionality)

​
## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're here to help! -->
- [ ] My code follows the code style of this project.
- [ ] My change requires a change to the documentation.
- [ ] I have updated the documentation accordingly.
- [ ] I have read the **CONTRIBUTING** document.
- [ ] I have added tests to cover my changes.
- [ ] All new and existing tests passed.
