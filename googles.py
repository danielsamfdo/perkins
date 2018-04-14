# #from googleapiclient.discovery import build
# #import pprint

# my_api_key = " AIzaSyBtpmrsNZdsdk3IB5mQ-XUzl1zwDRz1Zek"
# my_cse_id = "007857100306810506245:nvw7hhb25r0"

import pprint
import urllib
from urllib import request                                       
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import argparse

def main(args):
  
  service = build("customsearch", "v1",
            developerKey="AIzaSyBtpmrsNZdsdk3IB5mQ-XUzl1zwDRz1Zek")

  res = service.cse().list(
      q=args.desc,
      cx='007857100306810506245:nvw7hhb25r0',
    ).execute()
  #pprint.pprint(res['items'][0]['link'])
  link = res['items'][0]['link']
  f = urllib.request.urlopen(link) 
  soup = BeautifulSoup(f)
  print(soup)
  return soup
#  print('RESULT',res['items'])
#  for result in res:
    #if result.find('<form'):
     #  print(result)
 #    print(res['items'])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('desc', type=str,
                    help='Description')
	args = parser.parse_args()
	main(args)

