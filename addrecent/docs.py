from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

product_by_list_body =openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'product_ids': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format=openapi.FORMAT_UUID,
                description="A list of product ids, all of which MUST be a valid uuid")
            )
        }
    )

product_by_list_resonses = {
    200: openapi.Response('Request was successful without errors', schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description="Message response from server"),
                    'success': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="true"),
                    'count':  openapi.Schema(type=openapi.TYPE_INTEGER, description="Number of products that were returned"),
                    'data':  openapi.Schema(type=openapi.TYPE_OBJECT, description="Products objects from the database")
                }
    )),


    500: openapi.Response('Internal server error ', schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description="Message response from server"),
                    'success': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="true or false"),
                    'count':  openapi.Schema(type=openapi.TYPE_INTEGER, description="Number of products that were returned"),
                    'data':  openapi.Schema(type=openapi.TYPE_OBJECT, description="Products objects from the database")
                },
                description= "This means a server error occured hint: might occur as a result of an invalid uuid in the list"
    )),
}