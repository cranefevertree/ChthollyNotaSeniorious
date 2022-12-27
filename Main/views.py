from django.shortcuts import render


# Create your views here.
def MainIn(request):
    return render(request, 'Main/MainIndex.html')
