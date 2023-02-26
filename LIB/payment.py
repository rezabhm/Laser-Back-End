import time
import uuid

from Payment import models
from Reserve import models as res_model

from LIB import utils


def delete_off_code(json_data):

    """

    delete off code

    """

    try:

        # get off code
        off_code = models.OffCode.objects.get(code=json_data['off_code'])


        # delete
        off_code.delete()

        return 200, 'successfully ...'

    except:

        return 400, 'wrong code'


def create_off_code(json_data):

    """

    delete off code

    """

    try:

        # get off code
        off_code = models.OffCode.objects.get(code=json_data['off_code'])

        return 400, 'you have used this code'

    except:

        # create new off code

        if (float(json_data['amount']) <= 100.0) and (float(json_data['amount']) > 0.0):

            # create off code
            off_code = models.OffCode()

            # set parameter
            off_code.code = json_data['off_code']
            off_code.amount = json_data['amount']

            # save
            off_code.save()

            return 200, 'successfully ...'

        else:

            return 400, 'your amount must be between 0 and 100'


def off_code_add_reserve(json_data):

    """

    add off code to reserve

    """

    try:

        # get off code
        off_code = models.OffCode.objects.get(code=json_data['off_code'])

        # get reserve
        reserve = res_model.Reserve.objects.get(id=json_data['reserve'])

        if not reserve.used_off_code:

            # add off code
            reserve.off_code = off_code.code
            reserve.total_payment_amount += (off_code.amount / 100) * reserve.total_price_amount
            reserve.used_off_code = True

            # save
            reserve.save()

            return 200, 'successfully'

        else:

            return 400, 'you can"t use off code'

    except:

        return 400, 'wrong off code or reserve id'


def multiple_payment(json_data):

    """

    stor multiple payment

    """

    try:

        # get reserve
        reserve = res_model.Reserve.objects.get(id=json_data['reserve'])

        for pay in json_data['payment_list']:

            # add new payment
            pay_obj = models.Payment()

            # set parameter
            pay_obj.id = str(uuid.uuid4().int)
            pay_obj.price = pay['price']
            pay_obj.payment_time_int = time.time()
            pay_obj.payment_time_str = utils.time_int2str(time.time())
            pay_obj.payment_type = pay['payment_type']
            pay_obj.reserve = reserve
            pay_obj.user = reserve.user

            # save
            pay_obj.save()

            reserve.total_payment_amount += pay['price']

        # save
        reserve.save()

        return 201, 'successfully ...'

    except:

        return 400, 'wrong reserve id'
