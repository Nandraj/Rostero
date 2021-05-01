from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Category': '/category/',
        'Product': '/product/'
    }
    return Response(api_urls)
