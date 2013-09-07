from django.http import HttpResponse
from django_twilio.client import twilio_client
from django.shortcuts import render_to_response

import json

def call(request):
    twilio_client.calls.create(
        to="+15154512927",
        from_="+13198048229",
        url="http://kara-ok.herokuapp.com/response/"
    )
    return HttpResponse(json.dumps({"success": True}), content_type="application/json")

def response(request):
    return render_to_response("xml/response.xml", mimetype="application/xhtml+xml")
