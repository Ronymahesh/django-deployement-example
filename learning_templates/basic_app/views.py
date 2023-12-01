from django.shortcuts import render


# Create your views here.
def index(request):
    my_dic = {'text':'hello world','number':100}
    return render(request,'basic_app\index.html',my_dic)

def other(request):
    return render(request,'basic_app\other.html')

def maheshtemplates(request):
    return render(request,'basic_app\maheshtemplates.html')

    # Note: Please dont use Relative or Templates builtin names
