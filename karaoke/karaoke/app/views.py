from django.http import HttpResponse
from django_twilio.client import twilio_client
import json

def call(request):
    twilio_client.calls.create(
        to="+15154512927",
        from_="+13198048229",
        url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"
    )
    return HttpResponse(json.dumps({"success": True}), content_type="application/json")
