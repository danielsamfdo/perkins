from django_alexa.api import fields, intent, ResponseBuilder
from copy import deepcopy
from .googles import *
import ast
namefields=("Name","Name Field")
phonefields=("Phone Field")
categories=("Hospital","")

pair_examples=[[]]
title=["Dummy"]
curr_index=[0]

class FieldsForFormsSlots(fields.AmazonSlots):
    query = fields.AmazonSearchQuery()
    # query = fields.AmazonLiteral()

class FieldsFillingForms(fields.AmazonSlots):
    searchphrase = fields.AmazonSearchQuery()

@intent
def LaunchRequest(session):
    """
    ---
    launch
    start
    run
    begin
    """
    # return ResponseBuilder.create_response(message="Hello! Let's fill some forms together.",
    #                                       reprompt="What form do you want me to open? It can be a description or a URL.",
    #                                       end_session=False,
    #                                       launched=True)
    return ResponseBuilder.create_response(message="Hi",
                                           reprompt="",
                                           end_session=False,
                                           launched=True)

@intent(slots=FieldsForFormsSlots)
def FillForm(session, query=''):
    """
    ---
    form {query}
    """
 #   global pair_examples
    pair_examples = []
    print(query)
    pair_examples_copy,title_copy=firstget(query,[])
    pair_examples=deepcopy(pair_examples_copy) #pair_examples is a global list
    print(pair_examples) 
#    f = open('/home/perkins/candle/pairs.txt','w')
 #   f.write(str(pair_examples)+'\n')
    title[0]=title_copy #same global thingy
    kwargs = {}
    index_copy=0
    kwargs['attributes']={}
    kwargs['attributes']['pair_examples']=str(pair_examples)
    kwargs['attributes']['curr_index']=str(0)
    kwargs['attributes']['answers']=str([])
    kwargs['message'] = str(title[0])+" form received. Please use the phrase Enter followed by the value, starting with "+str(pair_examples[index_copy][0])
    #curr_index[0]+=1
    #kwargs['end_session']=False
    kwargs['attributes']['new']=False    
    if True or session.get('launched'): 
        print ("ngogoawr")
        session['reprompt'] = "Please mention the phrase for the form."
        session['end_session'] = False
        session['shouldEndSession']=False
        session['launched'] = True #session['launched']
       
        kwargs['reprompt'] = "Please mention the phrase for the form."
        kwargs['end_session'] = False
        kwargs['shouldEndSession']=False
        kwargs['launched'] = True #session['launched']
#    f.close()
    return ResponseBuilder.create_response(**kwargs)

@intent(slots=FieldsFillingForms)
def AddForm(session,searchphrase=''):
    pair_examples=[]
    curr_index=[[]]
#    f = open('/home/perkins/candle/pairs.txt','r')
    #for line in f:
     #   pair_examples[0]=list(line)
 #   pair_examples[0]=list(f.read())
    print('AAATTTRRR!!!!!!',session.keys(),session)
    pair_examples=str(session['attributes']['attributes']['pair_examples'])
    pair_examples=ast.literal_eval(pair_examples)
    answer=ast.literal_eval(str(session['attributes']['attributes']['answers']))
    #pair_examples=[n.strip() for n in pair_examples]
    curr_index[0]=int(session['attributes']['attributes']['curr_index'])
#    ci = open('/home/perkins/candle/curr_index.txt','r')
#    for line in ci:
 #       curr_index[0]=int(line)
 #   curr_index[0]=int(line)
    print ("khgbwygweifgi@@@@@@@@@",pair_examples)
    print ("khhviv%%%%%%%%%%%%%%%%%%",curr_index)
    print(searchphrase)
    kwargs={}
    index_copy=curr_index[0]
    answer.append(searchphrase)
    kwargs['attributes']={}
    kwargs['attributes']['answers']=str(answer)
    if index_copy>=len(pair_examples)-2:
        kwargs['message']=str(pair_examples[index_copy][0])+" has been filled. Form complete."
        kwargs['end_session']=True
        print("uyfyfuy&&&&&&&&&&&&",kwargs['attributes']['answers'])        
    else:
        kwargs['message']=str(pair_examples[index_copy][0])+" has been filled. Next is "+str(pair_examples[index_copy+1][0])
        kwargs['end_session']=False
    curr_index[0]+=1
    #answer.append(searchphrase)
    #kwargs['attributes']={}
    kwargs['attributes']['curr_index']=str(curr_index[0])
    kwargs['attributes']['pair_examples']=str(pair_examples)
    #kwargs['attributes']['answers']=str(answer)
    #kwargs['attributes']['a']
#    cw = open('/home/perkins/candle/curr_index.txt','w')
 #   write(str(curr_index[0])
   # cw.close()
#    ci.close()
    if True or session.get('launched'):
        session['reprompt'] = "Please mention the proper phrases..."
        session['end_session']=False
        session['shouldEndSession']=False
        session['launched']=True #session['launched']

        #kwargs['reprompt'] = "Please mention the phrase for the form."
        #kwargs['end_session'] = False
        kwargs['shouldEndSession']=False
        kwargs['launched'] = True #session['launched']

    return ResponseBuilder.create_response(**kwargs)
