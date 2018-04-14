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

# def main(args):
  
#   service = build("customsearch", "v1",
#             developerKey="AIzaSyBtpmrsNZdsdk3IB5mQ-XUzl1zwDRz1Zek")

#   res = service.cse().list(
#       q=args.desc,
#       cx='007857100306810506245:nvw7hhb25r0',
#     ).execute()
#   #pprint.pprint(res['items'][0]['link'])
#   link = res['items'][0]['link']
#   f = urllib.request.urlopen(link) 
#   soup = BeautifulSoup(f)
#  # print(soup)
#   form = soup.find('form')
#   inputs = form.find_all('input')
#   pairs=[]
#   for each in inputs:
#      name=each.get('name')
#      val=each.get('value')
#      typ=each.get('type')
#   #   print(sentence(name,val,typ))
#      pairs.append([name,typ,val])

#   #print(pairs)
#   #print(getpair(pairs,1))
#   answers=[]

#   if(args.query.lower().find('Fill')):
#   	print(query(pairs,index,args.query,answers))
#   if(args.query.lower().find('What')):
#     print(getpair(pairs,index))
#   return pairs

# #  print('RESULT',res['items'])
# #  for result in res:
#     #if result.find('<form'):
#      #  print(result)
#  #    print(res['items'])
# def getpair(pairs,index):
# 	return sentence(pairs[index])

# def query(pairs,index,q,answers):
# 	if q.lower().find('fill'):
# 		pair = getpair(pairs,index)
# 		answers.append((pair[0],q))

# def sentence(pairs):
# 	name,val,typ = pairs
# 	if(name is None):
# 		name=''
# 	if(typ is None):
# 		typ=''
# 	return ('Name is '+name+', Type '+typ)
# def response(field,res,reses):
# 	reses.append((field,res))

# if __name__ == '__main__':
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('desc', type=str,
#                     help='Description')
# 	parser.add_argument('query', type=str,
#                     help='Query')
# 	args = parser.parse_args()
# 	print('ARGS',args.query)

# 	main(args)



# # from bs4 import BeautifulSoup

# # def get_labels(filename)
# # with open(filename) as f:
# # soup=BeautifulSoup(f)
# # # form=soup.find('form')
# # # inputs=form.find_all('input')
# # form=soup.find('form')
# # inputs=form.find_all('input')
# # pairs=[]
# # for each in inputs:
# # name=each.get('name')
# # val=each.get('value')
# # typ=each.get('type')
# # pairs.append([name,typ,val])

# # print(pairs)

# # get_labels("index.html")

#######################

def firstget(args,pairs):
  
  service = build("customsearch", "v1",
            developerKey="AIzaSyBtpmrsNZdsdk3IB5mQ-XUzl1zwDRz1Zek")

  res = service.cse().list(
      q=args,
      cx='007857100306810506245:nvw7hhb25r0',
    ).execute()
  for i in range(len(res['items'])):
  #pprint.pprint(res['items'][0]['link'])
    link = res['items'][i]['link']
    title = res['items'][i]['title']
    if(link.find('.pdf')):
       f = urllib.request.urlopen(link)
       print(f)
       break

 # print(soup)
  # form = soup.find('form')
  # inputs = form.find_all('input')
  
  # for each in inputs:
  #    name=each.get('name')
  #    val=each.get('value')
  #    typ=each.get('type')
  # #   print(sentence(name,val,typ))
  #    pairs.append([name,typ,val])
  # if(len(pairs))
  #print(pairs)
  #print(getpair(pairs,1))
  # answers=[]

  # if(args.query.lower().find('Fill')):
  #   print(query(pairs,index,args.query,answers))
  # if(args.query.lower().find('What')):
  #   print(getpair(pairs,index))
  return f,title

#  print('RESULT',res['items'])
#  for result in res:
    #if result.find('<form'):
     #  print(result)
 #    print(res['items'])
def getpair(pairs,index):
    return sentence(pairs[index])

def query(pairs,index,q,answers):
    if q.lower().find('fill'):
        pair = getpair(pairs,index)
        answers.append((pair[0],q))

def sentence(pairs):
    name,val,typ = pairs
    if(name is None):
        name=''
    if(typ is None):
        typ=''
    return ('Name is '+name+', Type '+typ)
def response(field,res,reses):
    reses.append((field,res))
