from django_alexa.api import fields, intent, ResponseBuilder

namefields=("Name","Name Field")
phonefields=("Phone Field")
categories=("Hospital","")


class FieldsForFormsSlots(fields.AmazonSlots):
    NameField=fields.AmazonCustom(label="NameField", choices=namefields)
    PhoneField=fields.AmazonCustom(label="PhoneField",choices=phonefields)
    Category=fields.AmazonCustom(label="Category",choices=categories)
    query = fields.AmazonSearchQuery()

@intent
def LaunchRequest(session):
    """
    ---
    launch
    start
    run
    begin
    open
    """
    return ResponseBuilder.create_response(message="Hello! Let's fill some forms together.",
                                           reprompt="What form do you want me to open? It can be a description or a URL.",
                                           end_session=False,
                                           launched=True)

@intent(slots=FieldsForFormsSlots)
def FillForm(session,query):
    print query
    return ResponseBuilder.create_response(message="",
                                           reprompt="What house would you like to give points to?",
                                           end_session=False,
                                           launched=True)



