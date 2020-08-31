from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import braintree
# Create your views here.


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="dzk57fd7wg9tg7fn",
        public_key="2bn3wkd8by2kfhzs",
        private_key="090bcb852ef5823c48a510cf8ec08d97s"
    )
)

def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user  = UserModel.objects.get(id = id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid session please login again'})
    return JsonResponse({"token" : gateway.client_token.generate()})


@csrf_exempt
def process_transaction(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid session please login again'})

    nonce_from_the_client = request.POST['clientNonce']
    amount_from_client = request.POST['amount']

    result = gateway.transaction.sale({
    "amount": amount_from_client,
    "payment_method_nonce": nonce_from_the_client,
    "options": {
      "submit_for_settlement": True}
    })

    if result.is_success:
        return JsonResponse({
        'success': result.is_success,
        'transaction' : {
            'id' : result.transaction.id,
            'amount' : result.transaction.amount,
        }
        })
    return JsonResponse({'error': True})