import datetime
import time
import json

import jdatetime


def ad2solar(year, month, day, week_day):

    """
    convert AD datetime to solar time
    """

    month2int = {

        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12,

    }

    week = {

        'Sat': 'شنبه',
        'Sun': 'یکشنبه',
        'Mon': 'دوشنبه',
        'Tue': 'سه شنبه',
        'Wed': 'چهارشنبه',
        'Thu': 'پنج شنبه',
        'Fri': 'جمعه',

    }

    time_ = jdatetime.date.fromgregorian(year=year, month=month2int[month], day=day)
    return time_.year, time_.month, time_.day, week[week_day]


def solar2ad(year, month, day):

    """
    convert solar datetime to ad datetime
    """

    time_ = jdatetime.date(year, month, day).togregorian()
    return time_.year, time_.month, time_.day


def sale_status(status):

    """
        return summarize of sale live weighbridge level to persian word
    """

    dict_status = {

        'en': 'ورود',
        'w1': 'وزن کشی مرحله اول',
        'w': 'وزن کشی باسکول ۱ تنی',
        'w2': 'وزن کشی مرحله آخر',
        'ex': 'خروج',
        'fi': 'اتمام',
        'fin': 'اتمام',

    }

    return dict_status[status]


def cvt_str2int_time(year, month, day):

    # convert
    string = f'{day}/{month}/{year}'
    time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

    return time_filter


def split_date(date):

    # split date
    year, month, day = date.split('/')

    return int(year), int(month), int(day)


def decode_reqeust_json(request):

    json_unicode = request.body.decode('utf-8')
    json_data = json.loads(json_unicode)

    return json_data


def cvt_solar_date2ad_int(date):

    year, month, day = split_date(date)
    year, month, day = solar2ad(year, month, day)
    date_int = cvt_str2int_time(year, month, day)

    return date_int

