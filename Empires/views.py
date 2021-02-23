from django.shortcuts import render
from .models import AgeofEmpries
from rest_framework import viewsets
from Empires.serializer import EmpriesSerializer
# Create your views here.




def index(requset):
    return render(requset, 'index.html')


def all_data(request):
    alldata = AgeofEmpries.objects.all()
    return render(request, 'all_data.html' ,{'alldata':alldata})

MAX_RETRIES = 5
def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        data = AgeofEmpries.objects.filter(age__icontains=q)
        context = {'query': q,
                'data': data}
        template = 'search.html'
    else:
        attempt_num = 0
        while attempt_num < MAX_RETRIES :
            r = request.get("https://age-of-empires-2-api.herokuapp.com/docs/", timeout=10)
            if r.status_code == 200:
                data = r.json()
                return data
            else:
                attempt_num += 1
                time.sleep(5)
            return {'error': 'data cant be fetch'}
        template = 'search.html'
        context = {}
    return render(request, template, context)



class EmpriesViewSet(viewsets.ModelViewSet):
    queryset = AgeofEmpries.objects.all()
    serializer_class = EmpriesSerializer


