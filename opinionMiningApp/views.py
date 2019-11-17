from django.shortcuts import render
from opinionMiningApp.models import OpinionMiningResults
from django.http import HttpResponse
import json


#Greetings page
def index(request):
    if request.method == "GET":
        last_object = OpinionMiningResults.objects.latest('_id')
        #print(last_object[-1].aspectStats)
        template_values_curr = {
            "deviceName":last_object.deviceName,
            "reportDate":last_object.reportDate,
            "textCount":last_object.textCount,
            "aspectStats":last_object.aspectStats
        }
        return render(request, 'opMiningApp/home.html',{"template_values_curr":template_values_curr})
