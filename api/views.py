from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Category': '/category/',
        'Product': '/product/',
        'Customer': '/customer/',
        'Sale': '/sale/',
        'SaleReturn': '/salereturn/',
        'Supplier': '/supplier/',
        'purchase': '/purchase/',
        'PurchaseReturn': '/purchasereturn/',
        'DateFormat': 'YYYY-MM-DDThh:mm'
    }
    return Response(api_urls)
