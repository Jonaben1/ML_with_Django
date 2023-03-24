from django.shortcuts import render
from .prediction import getPrediction

# Create your views here.
def home(request):
    return render(request, 'home.html')


def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPrediction(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)
    return render(request, 'result.html', {'result': result})


