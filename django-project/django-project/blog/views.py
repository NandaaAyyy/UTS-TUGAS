from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Blog',
        'heading':'BLOG',
        'subheading':'PONPES.MIFTAHUL QULUB',
    }
    return render(request, 'blog/index.html',context)