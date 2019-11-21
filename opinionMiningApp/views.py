from django.shortcuts import render
from opinionMiningApp.models import OpinionMiningResult
from opinionMiningApp.models import Product
from django.http import HttpResponse
import json


#Greetings page
def index(request):
    if request.method == "GET" or request.method == "POST":
        #First all device list is taken from MongoDB
        #(İleride kullanici hesabi ile girildiginde companyName kullanici hesabindan alinabilir)
        deviceCollection = Product.objects.filter(companyName="Casper")
        deviceList = []

        for device in deviceCollection:
            deviceList.append(device.deviceName)

        if request.method == "GET":
            #The last analysis is sent to the client for displaying
            #ONEMLI: Ileride baska sirketler ile calisilirsa, bu kisimda Casper vermek yerine mevcut kullanicidan companyName cekilebilir
            last_object = OpinionMiningResult.objects.filter(companyName="Casper").latest('_id')
        else:
            #Getting the device client requested
            device = request.POST.get('device_list')
            #The last analysis is sent to the client for displaying
            #ONEMLI --> User authentication sistemi geldiginde Casper yazılı kisma mevcut kullanicinin companyName i yazilmali
            last_object = OpinionMiningResult.objects.filter(companyName="Casper", deviceName=device).latest('_id')


        template_values_curr = {
            "deviceName":last_object.deviceName,
            "reportDate":last_object.reportDate,
            "textCount":last_object.textCount,
            "aspectStats":last_object.aspectStats,
            "deviceList":deviceList
        }
        return render(request, 'opMiningApp/home.html',{"template_values_curr":template_values_curr})
