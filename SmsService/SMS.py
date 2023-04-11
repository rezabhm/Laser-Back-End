import requests

src = 'http://ippanel.com/api/select'
url = 'ادرس سایت'
json_request = {

    'op': 'send',
    'uname': '09104734870',
    'pass': '4400080072',
    # 'message': 'be emad kir kocholo salam bereson',
    'from': '5000125475',
    # 'to': ['09339192819', ],

}


def successfully_reserve_sms(phone_number, name, date, hour):
    message_text = f'نوبت لیزر شما با موفقیت ثبت شد. \n' \
                   f'{name} عزیز نوبت لیزر شما برای تاریخ {date} و ساعت {hour} در کلینیک لیزر لیانا با موفقیت ثبت شد . شما میتوانید از طریق صفحه حساب کاربری اطلاعات نوبت خود را مشاهده کنید .\n' \
                   f'منتظر حضور شما هستیم .\n\n' \
                   f'{url}'

    request_json = json_request
    request_json['message'] = message_text
    request_json['to'] = [phone_number]

    r = requests.post(src, json=json_request)

    if r.status_code == 200:
        return True, r.content
    else:
        return False, r.content


def review_1_day_sms(phone_number, name, date, hour):

    message_text = f'{name} عزیز منتظر حضور شما در تاریخ {date} و ساعت {hour} در کلینیک لیزر لیانا هستیم . شما میتوانید از طریق صفحه حساب کاربری اطلاعات نوبت خود را مشاهده کنید .\n' \
                   f'\n لطفا ۱۵ دقیقه قبل از زمان مقرر شده در کلینیک حضور پیدا کنید .\n\n' \
                   f'{url}'

    request_json = json_request
    request_json['message'] = message_text
    request_json['to'] = [phone_number]

    r = requests.post(src, json=json_request)

    if r.status_code == 200:
        return True, r.content
    else:
        return False, r.content


def cancel_sms(phone_number, name):

    message_text = f'{name} عزیز نوبت شما در کلینیک لیزر لیانا لغو شده است .\n' \
                   f'شما میتوانید از طریق سایت نسبت به دریافت مجدد نوبت اقدام کنید.' \
                   f'\n\n{url}'

    request_json = json_request
    request_json['message'] = message_text
    request_json['to'] = [phone_number]

    r = requests.post(src, json=json_request)

    if r.status_code == 200:
        return True, r.content
    else:
        return False, r.content


def review_1_week_sms(phone_number, name):

    message_text = f'یک هفته تا نوبت شما باقی مانده است .\n\n {name} عزیز نسبت به رزرو نوبت بعدی خود از طریق سایت  کلینیک لیزر لیانا اقدام کنید . نوبت جدید شما مطابق با زمان نوبت قبلی برای شما در حالت  انتظار پرداخت قرار گرفته است لطفا نسبت به تایید  نوبت خود در دو روز آینده اقدام فرمایید .' \
                   f'{url}'

    request_json = json_request
    request_json['message'] = message_text
    request_json['to'] = [phone_number]

    r = requests.post(src, json=json_request)

    if r.status_code == 200:
        return True, r.content
    else:
        return False, r.content


def send_password_code_sms(phone_number, code):

    message_text = f'کد ورود شما : {code} \n\n کلینیک لیزر لیانا ' \
                   f'\n\n{url}'

    request_json = json_request
    request_json['message'] = message_text
    request_json['to'] = [phone_number]

    r = requests.post(src, json=json_request)
    if r.status_code == 200:
        print(json_request)
        return True, r.content
    else:
        return False, r.content


review_1_day_sms('09027235390', 'رضا بهرامی', '1402/11/2', '8:00:00')
review_1_week_sms('09027235390', 'رضا بهرامی')
cancel_sms('09027235390', 'رضا بهرامی')
send_password_code_sms('09027235390', '12248')
