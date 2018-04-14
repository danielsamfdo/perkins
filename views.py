# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
from django.views.decorators.csrf import csrf_exempt
import redis as r
from urllib.parse import parse_qs

redis = r.StrictRedis()


def main(request):
    return HttpResponse("Welcome to the Candle Amazon Alexa skill")

@csrf_exempt
def alexa(request):
    url = 'https://wordsmith.org/words/today.html'
    text = "hello"
    print("Here")
    d = {
      "uid": 42,
      "updateDate": datetime.now(pytz.timezone('UTC')).isoformat(),
      "titleText": "Wordsmith.org: Today's Word",
      "mainText": text,
      "redirectionUrl": url
    }
    return HttpResponse(json.dumps(d), content_type="application/json; charset=utf-8")

@csrf_exempt
def plugin(request):
    if request.method == 'POST':
        print(parse_qs(request.body.decode('utf-8')))
        redis.set("form", request.body['form'])
        return HttpResponse(json.dumps({'saved': True}),
            content_type="application/json; charset=utf-8")
    
    elif request.method == 'GET':
        if not redis.exists('filled_form'):
            return HttpResponse(json.dumps({'ready': False}),
                content_type="application/json; charset=utf-8")


def render_test_html_form(request):
    return render(request, "form.html")

