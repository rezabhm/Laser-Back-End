from django.conf import settings
import requests
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from . import models
from Reserve import models as res_model

# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/zarin/pall/verify/'
SuccessFull_Redirect_url = 'http://127.0.0.1:8000/'
UnSuccessFull_Redirect_url = ''


@csrf_exempt
def send_request(request):

    try:
        reserve = res_model.Reserve.objects.get(id=request.POST['reserve'])

    except:

        return JsonResponse({

            'Status':False,
            'Description': 'wrong reserve id'
        })

    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": float(request.POST['amount']),
        "Description": 'kk;;',
        "Phone": '',
        "CallbackURL": CallbackURL,

    }

    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}

    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:

            response = response.json()

            if response['Status'] == 100:

                zarin_payment = models.ZarinPall()

                zarin_payment.authority = response['Authority']
                zarin_payment.amount = float(request.POST['amount'])
                zarin_payment.reserve = reserve

                zarin_payment.save()

                return JsonResponse({'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                        'authority': response['Authority']})

            else:
                return JsonResponse({'status': False, 'code': str(response['Status'])})

        return JsonResponse(response)

    except requests.exceptions.Timeout:
        return JsonResponse({'status': False, 'code': 'timeout'})

    except requests.exceptions.ConnectionError:
        return JsonResponse({'status': False, 'code': 'connection error'})


def verify(request):

    try:

        zarin_payment = models.ZarinPall.objects.get(authority=request.GET['Authority'])

    except:

        return JsonResponse({'status':False, 'description':'wrong reserve id'})

    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": zarin_payment.amount,
        "Authority": request.GET['Authority'],
    }

    data = json.dumps(data)

    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()

        if response['Status'] == 100:

            zarin_payment.ref_id = response['RefID']
            zarin_payment.status = 'Successfully'
            zarin_payment.save()

            reserve = zarin_payment.reserve
            reserve.total_payment_amount += zarin_payment.amount
            reserve.save()

            return HttpResponseRedirect(SuccessFull_Redirect_url)

        else:

            zarin_payment.status = 'Fail'
            zarin_payment.save()

            response['Status'] = False
            return JsonResponse({'status': False, 'code': str(response['Status'])})

    return JsonResponse(response)
