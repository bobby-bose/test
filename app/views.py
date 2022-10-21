from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def first(request):
    print("thakkudu reached")
    if request.method == "POST":
        print("thakkudu reached")
        print(request.POST)
        print(request.POST.get("fname"))
        print(request.POST.get("lname"))
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        if fname == "thakkudu" and lname == "thakkudu":
            return redirect("second")
    return render(request, "home.html")

def second(request):
    context={"message":"Welcome thakkudu"}
    return render(request, "second.html",context)
