
# this parameter define different type of users
user_type_tuple = (

    ('a', 'admin'),
    ('r', 'reception'),
    ('o', 'operator'),
    ('c', 'customer'),

)

user_type_dict = {

    'a': 'admin',
    'r': 'reception',
    'o': 'operator',
    'c': 'customer',

}

# determine all type of payment
payment_type_tuple = (

    ('ca', 'cash'),
    ('cr', 'credit card'),
    ('ch', 'check'),

)

# blew attribute determine all type of reservation
reservation_type_tuple = (

    ('co', 'complete'),          # it means customer finish operate and pay all salary
    ('do', 'done'),              # it means customer finish operate but didn't pay all salary
    ('ca', 'cancel'),            # it means customer cancel reservation
    ('pe', 'pending'),           # it means reservation is in the pending time and didn't register
    ('wa', 'waiting'),            # it means reservation registered but customer waiting for his turn
    ('sc', 'system cancel')      # it means customer didn't register reserve and system cancel pending

)
