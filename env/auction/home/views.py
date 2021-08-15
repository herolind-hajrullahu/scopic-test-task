from django.shortcuts import render
from django.http import HttpResponse
import json
import jwt
import requests

with open('home\items.json') as f:
    items = json.load(f)
    

with open('home\\users.json') as file:
    users = json.load(file)
 
def auto_bidding(name):
    pass


def home(request):
    return HttpResponse(json.dumps(items), content_type="application/json")


def item_details_page(request, title):
    for item in items:
        for k in item:
            if k == 'image' or k == 'description' or k == 'price':
                continue
            
            if item[k] == title:
                return HttpResponse(json.dumps(item), content_type="application/json")

    return HttpResponse(json.dumps({'message':'No Item Found!!'}), content_type="application/json")


def login(request):
    
    req_body = request.body.decode('utf-8')
    body = json.loads(req_body)
    for user in users:
        if user['username'] == body['username'] and user['password'] == body['password'] :
            encoded_jwt = jwt.encode({"username": body['username'], "password": body['password']}, "secret", algorithm="HS256")
            return HttpResponse(json.dumps({"message": "Authorized!"}),status=200)

    return HttpResponse(status=401)


def search(request):
    req_body = request.body.decode('utf-8')
    body = json.loads(req_body)
    
    filtered_items = []
    
    for item in items:
        print(item)
        for k in item:
            if k == 'image':
                continue
            if body['filter'] in str(item[k]):
                filtered_items.append(item)
    
    sorted_items = sorted(filtered_items, key=lambda k: k['price'])
    
    return HttpResponse(json.dumps(sorted_items), content_type="application/json")

def bid(request, title):
    authorization = request.headers["Authorization"]
    authorization_key = authorization.split(' ')[1]
    payload = jwt.decode(authorization_key, "secret", algorithms="HS256")

    for item in items:
        if title == item['title']:
            if item['highest_bid'] == 0:
                item['highest_bid'] = item['price'] + 1 
                item['highest_bidder'] = payload['username']
            else:
                item['highest_bid'] = item['highest_bid'] + 1
                item['highest_bidder'] = payload['username']

            if item['highest_bidder'] != item['auto_bidder'] and item['highest_bidder'] != "":
                item['highest_bid'] = item['highest_bid'] + 1
                item['highest_bidder'] = item['auto_bidder']
                
                print(item['highest_bid'])
            
            for user in users:
                if item['highest_bidder'] == user['username']:
                    if item['highest_bid'] > user['auto_bid']['max_bid']:
                        print(11122)
                        item['auto_bidder'] = ""
                        user['auto_bid'] = {}


    return HttpResponse(status=200)
    

def auto_bid(request, title, max_bid):
    authorization = request.headers["Authorization"]
    authorization_key = authorization.split(' ')[1]
    payload = jwt.decode(authorization_key, "secret", algorithms="HS256")

    for user in users:
        if payload['username'] == user['username']:
            user['auto_bid']['title'] = title
            user['auto_bid']['max_bid'] = max_bid
    
    for item in items:
        if title == item['title']:
            item['auto_bidder'] = payload['username']
    

    content = requests.get(url='http://127.0.0.1:8000/bid/vase', headers={
        'Authorization':  'Bearer ' + authorization_key
    }
    )

    return HttpResponse(status=content.status_code)

    
