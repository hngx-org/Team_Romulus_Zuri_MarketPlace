"""
from django.http import Http404, JsonResponse
from rest_framework.response import Response


'''
def custom_404_handler(request, exception):
    return JsonResponse({'error': 'Not Found'}, status=404)

def custom_500_handler(request):
    return JsonResponse({'error': 'Internal Server Error'}, status=500)
'''

def handle_404(request, exception):
    # Customize the 404 error response
    return JsonResponse({
        "status": 404,
        "success": False,
        "message": f"Therequested resource can not be found: {exception}"
        })

def handle_500(request):
    # Customize the 500 error response
    return JsonResponse({
        "status": 500,
        "success": False,
        "message": f"There is an internal server error: "
        })

"""
