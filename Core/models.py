from django.db import models
from Config import config

# Create your models here.


class User(models.Model):

    """

    this table will define system's user and store all user's information

    """

    # user information
    username = models.CharField(default='user', primary_key=True, max_length=50)
    name = models.CharField(default='user', max_length=50)
    last_name = models.CharField(default='user', max_length=50)
    phone_number = models.CharField(default='0989121112244', max_length=13)

    # security information
    password = models.CharField(default='****', max_length=50)

    # this parameter define type of user and it's access
    user_type = models.CharField(max_length=1, choices=config.user_type_tuple)

    def __str__(self):
        return self.username


class Token(models.Model):

    """

    this table store user's token

    """

    # information
    token_code = models.CharField(default='****', max_length=128, primary_key=True)

    # timing information
    token_create_time_int = models.FloatField(default=0.0)
    token_create_time_str = models.CharField(default='-', max_length=25)

    token_expire_time_int = models.FloatField(default=0.0)
    token_expire_time_str = models.CharField(default='-', max_length=25)

    # foreign key
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.token_code


class ForgotPassword(models.Model):

    """

    with this table we can handle forgot password process.
    this table will store code which we send to user via sms.

    """

    # information
    code = models.CharField(default='****', max_length=8, primary_key=True)
    code_generate = models.CharField(default='****', max_length=8, )

    # timing
    expire_time = models.FloatField(default=0.0)

    # status
    proved = models.BooleanField(default=False)
    used = models.BooleanField(default=False)

    # foreign key
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class EmployeeEnterExit(models.Model):

    """

    this table will store all type of user's enter and exit ( to workplace ) history

    """

    # information
    id = models.CharField(max_length=150, primary_key=True)

    # timing
    enter_time_int = models.FloatField(default=0.0)
    enter_time_str = models.CharField(default='-', max_length=25)

    exit_time_int = models.FloatField(default=0.0)
    exit_time_str = models.CharField(default='-', max_length=25)

    # this parameter determine did user loge out from system or didn't or only login to system,
    exited = models.BooleanField(default=False)

    # foreign key
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Customer(models.Model):

    """

    this table belong to customers

    """

    # information
    national_code = models.CharField(max_length=15, primary_key=True)
    address = models.TextField()
    house_number = models.CharField(max_length=15)

    # medical history
    drug_hist = models.BooleanField(default=False)
    decease_hist = models.BooleanField(default=False)
    doctor = models.CharField(max_length=50)
    charge = models.BooleanField(default=False)

    # foreign key
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default='')

    def __str__(self):
        return self.national_code


class Comment(models.Model):

    """

    store user's comment

    """

    # information
    id = models.CharField(max_length=150, primary_key=True)
    comment_text = models.TextField()
    seen = models.BooleanField(default=False)

    # timing information
    create_time_int = models.FloatField(default=0.0)
    create_time_str = models.CharField(default='-', max_length=25)

    # foreign key
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text
