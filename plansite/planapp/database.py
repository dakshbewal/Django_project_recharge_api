from plansite.planapp.models import Plan
import requests
import json


import sqlite3
# Fetch data From airtel Plan Url using Requests lib

url = "https://assets.airtel.in/static-assets/myplan-infinity-ui/static/js/main~01e7b97c.359e33ff.js"
# db = sqlite3.connect("plansite/db.sqlite3")

response = requests.get(url=url)
resjson = response.text.split("{e.exports=JSON.parse('")[1].split("'")[0]

#convert Json to dictionary to Target each plan data using for loop
aDict = json.loads(resjson)

#database work here
# cursor = db.cursor()
# def create_table():
#     cursor.execute('CREATE TABLE IF NOT EXISTS allPlan(id INTEGER PRIMARY KEY,planId varchar(100) NOT NULL UNIQUE,bplInventoryItemId INTEGER NOT NULL,billPlanName varchar(250), freebieCount INTEGER, pricePoint INTEGER NOT NULL,billPlanCategory varchar(100) NOT NULL,  planComponents varchar(10000) NOT NULL)')

id = 0
for plans in aDict["staticPlanData"]:
            id = id + 1
            planId = plans["planId"]
            bplInventoryItemId = plans["bplInventoryItemId"]
            billPlanName = plans["billPlanName"]
            freebieCount = plans["freebieCount"]
            pricePoint = plans["pricePoint"]
            billPlanCategory = plans["billPlanCategory"]
            planComponents = plans["planComponents"]

            queryset = Plan.objects.create(id=id, planId= planId, bplInventoryItemId=bplInventoryItemId, billPlanName=billPlanName, freebieCount=freebieCount, pricePoint=pricePoint, billPlanCategory=billPlanCategory, planComponents=planComponents)

            # sql_string = f''' "{id}", "{planId}","{bplInventoryItemId}", "{billPlanName}", "{freebieCount}", "{pricePoint}", "{billPlanCategory}","{planComponents}"'''

            # cursor.execute(f"INSERT INTO allPlan VALUES({sql_string})")
            queryset.save()
