def setting_list():

    """
    return list of setting

    """

    with open('morning_time.txt') as fd:
        morning_time = fd.read()

    with open('afternoon_time.txt') as fd:
        afternoon_time = fd.read()

    with open('trust_price.txt') as fd:
        trust_price = fd.read()

    return {

        'trust_price': float(trust_price),
        'afternoon_time': afternoon_time,
        'morning_time': morning_time,

    }
