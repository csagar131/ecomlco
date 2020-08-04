from .serializers import OrderSerializer
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Order
from django.views.decorators.csrf import  csrf_exempt
from rest_framework import viewsets
# Create your views here.

def is_user_authenticated(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(id = id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add(request, id, token):
    if not is_user_authenticated(id, token):
        return JsonResponse({"error" : "user is not authenticated"})

    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products =  request.POST['products']

        total_pro = len(products.split(','))

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(id = user_id)
            order = Order.objects.create(user =user, transaction_id = transaction_id, product_names = products, total_products = total_pro, total_amount = amount)
            return JsonResponse({'success':'order placed successfully'})
        except UserModel.DoesNotExist:
            return JsonResponse({'error' : 'Invalid id'})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
