from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import JSONParser

from LIB import utils
from . import models

# Create your views here.


class OperatorProgram(generics.ListCreateAPIView):

    def post(self, request, *args, **kwargs):

        # parse input json
        json_data = JSONParser().parse(request)

        # get input data
        date = json_data['date']
        date_int = utils.cvt_str2int_time(date)

        # query to database
        operator_program_list = models.OperatorProgram.objects.filter(date_int=date_int)
