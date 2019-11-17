from django.shortcuts import render
from opinionMiningApp.models import OpinionMiningResults
from django.http import HttpResponse


#Greetings page
def index(request):
    if request.method == "GET":
        all_results = OpinionMiningResults.objects.all().reverse()
        #print(all_results[-1].aspectStats)
        return render(request, 'opMiningApp/home.html',{"user":request.user})
        #return HttpResponse(all_results[0].aspectStats + all_results[0].reportDate)
