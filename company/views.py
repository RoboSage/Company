from django.http import HttpResponse

def home_page(req):
    print("home page requested")
    return HttpResponse("This is Home")