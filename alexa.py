from django_alexa.api import fields, intent, ResponseBuilder


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

@intent
def FillForm(session):
    return ResponseBuilder.create_response(message="",
                                           reprompt="What house would you like to give points to?",
                                           end_session=False,
                                           launched=True)

namefields=("Name","Name Field")
phonefields=("Phone Field")
class FieldsForFormsSlots(fields.AmazonSlots):
    NameField=fields.AmazonCustom(label="NameField", choices=namefields)
    PhoneField=fields.AmazonCustom(label="PhoneField",choices=phonefields)
