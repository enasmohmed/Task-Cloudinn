from django.shortcuts import render
from .models import AgeofEmpries
from rest_framework import viewsets
from Empires.serializer import EmpriesSerializer
from django.http import HttpResponse

# Create your views here.




def index(requset):
    return render(requset, 'index.html')


def all_data(request):
    alldata = AgeofEmpries.objects.all()
    return render(request, 'all_data.html' ,{'alldata':alldata})


MAX_RETRIES = 5
def search(request):

    if 'q' in request.data:
        q = request.GET.get('q')
        data = AgeofEmpries.objects.filter(age__icontains=q)
        template = 'search.html'
        context = {}
        if data.length:
            # found item in local db
            context = {'query': q,
                'data': data}
        else:
            # fetch data from api endpoint
            data = fetch_data()
            context = {'query': q,
                'data': data}

    return render(request, template, context) # return empty template


def fetch_data():
    attempt_num = 0
    while attempt_num < MAX_RETRIES :
        r = request.get("https://tasks.cloudinn.net/docs/", timeout=10)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            attempt_num += 1
            time.sleep(5)
            return {'error': 'data cant be fetch'}

class EmpriesViewSet(viewsets.ModelViewSet):
    queryset = AgeofEmpries.objects.all()
    serializer_class = EmpriesSerializer


