from django.shortcuts import render

def index(request):
    context = {
        'title':'PP.MQ',
        'heading':'PONPES. MIFTAHUL QULUB',
        'subheading':'Jln.masaran, Polagan Tengah, Polagan, Kec. Galis, Kab. Pamekasan, JATIM 69382',
    }
    return render(request,'index.html',context)