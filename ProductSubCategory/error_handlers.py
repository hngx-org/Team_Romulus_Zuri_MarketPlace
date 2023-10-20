# from django.shortcuts import render
# from django.http import Http404
# from rest_framework.response import Response


# class CustomErrorHandlingMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_exception(self, request, exception):
#         if isinstance(exception, Http404):
#             # Handle 404 error
#             return self.handle_404(request, exception)
#         else:
#             # Handle other exceptions (500 error)
#             return self.handle_500(request, exception)

#     def handle_404(self, request, exception):
#         # Customize the 404 error response
#         return Response({
#             "status": 404,
#             "success": False,
#             "message": f"Therequested resource can not be found: {exception}"
#         })

#     def handle_500(self, request, exception):
#         # Customize the 500 error response
#         return Response({
#             "status": 500,
#             "success": False,
#             "message": f"There is an intenal server error: {exception}"
#         })
