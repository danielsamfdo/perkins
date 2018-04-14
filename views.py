# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def main(request):
    return HttpResponse("Welcome to the Candle Amazon Alexa skill")

def alexa(request):
    url = 'https://wordsmith.org/words/today.html'
    s = BeautifulSoup(requests.get(url).text)
    word = s.find('h3').text.strip()
    text = "Today's word is %s. " % word
    meanings = ''
    etymology = ''
    usage = ''
    quote = ''
    divs = s.findAll('div')
    for div in divs:
        if 'meaning' in div.text.lower():
            meanings = div.findNext('div')
            if meanings.findChild('table'):
                # multiple meanings
                pass
            else:
                meaning = meanings.text.strip().split(':')
                if len(meaning) == 2:
                    meanings = 'A %s; it means: "%s". ' % tuple(meaning)
                else:
                    meanings = 'It means: "%s". ' % meaning
    text += meanings
            
    d = {
      "uid": word,
      "updateDate": datetime.now(pytz.timezone('UTC')).isoformat(),
      "titleText": "Wordsmith.org: Today's Word",
      "mainText": text,
      "redirectionUrl": url
    }
    return HttpResponse(json.dumps(d), content_type="application/json; charset=utf-8")
