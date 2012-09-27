# Create your views here.

from cmsaloha.models import AlohaFieldPlugin
from django.http import HttpResponse

def alohapost(request):
    if request.method == "POST":
        ID = int(request.POST['id'])
        content = request.POST['content']
        obj = AlohaFieldPlugin.objects.get(id=ID)
        obj.body=content
        obj.save()
        return HttpResponse("", mimetype='application/javascript')
        
