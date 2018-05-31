from django.shortcuts import render,redirect

from django.http import HttpResponse

# Create your views here.


def login(request):


    return render(request,'app01/login.html')




def index(request):


    if request.session.get('is_login',None):

        name = request.session.get('user',None)

        return render(request, 'app01/index.html', locals())


    # if request.COOKIES.get('name',None):
    #
    #     name = request.COOKIES.get('name')
    #     return render(request,'app01/index.html',locals())

    else:

        return redirect("/app01/login/")

def login_handle(request):


    print("COOKIE",request.COOKIES)  #{}

    print("SESSION",request.session)

    if request.method == 'POST':

        name = request.POST.get("name")
        pwd = request.POST.get("pwd")


        if name=='liubin' and pwd=='123456':

            #cookie
            # ret = redirect("/app01/index/")
            #
            # ret.set_cookie('name',name)
            #
            # return ret

    #cookie session

            request.session['is_login'] = True
            request.session['user'] = name

            return redirect("/app01/index/")







    return render(request,'app01/login.html')