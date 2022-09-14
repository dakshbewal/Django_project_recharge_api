from django.shortcuts import render, get_object_or_404
from . models import *
import requests
import json
from math import ceil
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import PlanSerializer


#function to get data from Airtel Api and store in our database
#Click once only to avoid to store dublicate data

def index1(request):

    url = "https://assets.airtel.in/static-assets/myplan-infinity-ui/static/js/main~01e7b97c.359e33ff.js"

    response = requests.get(url=url)
    resjson = response.text.split("{e.exports=JSON.parse('")[1].split("'")[0]

    # convert Json to dictionary to Target each plan data using for loop
    aDict = json.loads(resjson)

    for plans in aDict["staticPlanData"]:
        planId = plans["planId"]
        bplInventoryItemId = plans["bplInventoryItemId"]
        billPlanName = plans["billPlanName"]
        freebieCount = plans["freebieCount"]
        pricePoint = plans["pricePoint"]
        billPlanCategory = plans["billPlanCategory"]
        planComponents = plans["planComponents"]
        queryset = Plan.objects.create(planId= planId, bplInventoryItemId=bplInventoryItemId, billPlanName=billPlanName, freebieCount=freebieCount, pricePoint=pricePoint, billPlanCategory=billPlanCategory, planComponents=planComponents)
        queryset.save()
    object=Plan.objects.all()
    return HttpResponse("hello")


# function to get data from our database and show them in our Webpage
def plan(request):
    plans = Plan.objects.all()
    allplans = []
    catplan = Plan.objects.values("pricePoint", "id")
    cats = {item["pricePoint"] for item in catplan}
    print(catplan)
    print(cats)

    for cat in cats:
        plan = Plan.objects.filter(pricePoint=cat)
        n = len(plans)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allplans.append([plan, range(1, nSlides), nSlides])
    params = {'allplans': allplans}

    return render(request, "plan.html", params)


# to make api to fetch data from our website
class planList(APIView):

    def get(self, request):
        plan1 = Plan.objects.all()
        serializer = PlanSerializer(plan1, many= True)
        return Response(serializer.data)

    def post(self):
        pass

#Important note: Our Website Api is http://127.0.0.1:8000/planlist