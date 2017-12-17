import uuid
from datetime import datetime, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from webServer.models import Post



def index(request):

    
    #posts = list(Post.objects.filter(date_created__gte=t1)) 

    print("index !!")

    return TemplateResponse(request, "index.html")