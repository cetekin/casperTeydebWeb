from django.shortcuts import render
from opinionMiningApp.models import OpinionMiningResult
from opinionMiningApp.models import Product
from django.http import HttpResponse
import json
from django.core.exceptions import ObjectDoesNotExist


#Greetings page
def index(request):
    if request.method == "GET" or request.method == "POST":
        error_msg = "no_product"

        #First all device list is taken from MongoDB
        #ONEMLI: (İleride kullanici hesabi ile girildiginde companyName kullanici hesabindan alinabilir)
        deviceCollection = Product.objects.filter(companyName="Casper")
        deviceList = []

        for device in deviceCollection:
            deviceList.append(device.deviceName)

        if deviceList:
            try:
                if request.method == "GET":
                    error_msg = "no_result"

                    #The last analysis is sent to the client for displaying
                    #ONEMLI: Ileride baska sirketler ile calisilirsa, bu kisimda Casper vermek yerine mevcut kullanicidan companyName cekilebilir
                    last_object = OpinionMiningResult.objects.filter(companyName="Casper").latest('_id')
                    error_msg = "no_error"

                else:
                    error_msg = "selected_no_result"

                    #Getting the device client requested
                    device = request.POST.get('device_list')
                    #The last analysis is sent to the client for displaying
                    #ONEMLI --> User authentication sistemi geldiginde Casper yazılı kisma mevcut kullanicinin companyName i yazilmali
                    last_object = OpinionMiningResult.objects.filter(companyName="Casper", deviceName=device).latest('_id')
                    error_msg = "no_error"


            except OpinionMiningResult.DoesNotExist:
                if error_msg == "no_result":
                    template_values_curr = {
                        "error_msg":error_msg
                    }
                elif error_msg == "selected_no_result":
                    last_object = OpinionMiningResult.objects.filter(companyName="Casper").latest('_id')


            #If there is no error result is added to the template_values
            #Also, if there is no op mining result for selected device, lasts result for any device is showed to the client
            if error_msg == "no_error" or error_msg == "selected_no_result":
                #To show the user general opinion mining results (not aspect-based), calculating total positive-negative counts in the object
                aspect_stats = json.loads(last_object.aspectStats)
                general_stats = {
                    "positiveTotalCnt":0,
                    "negativeTotalCnt":0
                }

                for aspect in aspect_stats:
                    general_stats["positiveTotalCnt"] += aspect_stats[aspect]["positiveCnt"]
                    general_stats["negativeTotalCnt"] += aspect_stats[aspect]["negativeCnt"]

                #Transforming results to the percentages
                denominator = general_stats["positiveTotalCnt"] + general_stats["negativeTotalCnt"];
                general_stats["positiveTotalCnt"] *= 100;
                general_stats["positiveTotalCnt"] /= denominator;

                general_stats["negativeTotalCnt"] *= 100;
                general_stats["negativeTotalCnt"] /= denominator;

                general_stats["positiveTotalCnt"] = round(general_stats["positiveTotalCnt"])
                general_stats["negativeTotalCnt"] = round(general_stats["negativeTotalCnt"])


                template_values_curr = {
                    "error_msg":error_msg,
                    "deviceName":last_object.deviceName,
                    "reportDate":last_object.reportDate,
                    "textCount":last_object.textCount,
                    "aspectStats":last_object.aspectStats,
                    "deviceList":deviceList,
                    "generalStats":general_stats
                }

        else:
            template_values_curr = {
                "error_msg":error_msg
            }


        return render(request, 'opMiningApp/home.html',{"template_values_curr":template_values_curr, "error_msg":error_msg})
