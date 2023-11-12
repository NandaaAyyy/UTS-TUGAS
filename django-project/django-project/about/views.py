from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'About',
        'heading':'TENTANG',
        'subheading':'PONPES.MIFTAHUL QULUB',
    }
    return render(request, 'about/index.html',context)