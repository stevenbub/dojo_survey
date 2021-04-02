from django.shortcuts import render, redirect, HttpResponse
def index(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, 'index.html')
    # if request.method == "POST":
    #     print("a POST request is being made to this route")
    #     return redirect("/")
def create_user(request):
    # name = request.POST['name']
    # location = request.POST['location']
    # language = request.POST['language']
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    return redirect('result.html')
def result(request):
    return render(request, 'result.html')
    # if request.method == "GET":
    #     print(request.GET)
    #     return render(request, 'result.html')
    # if request.method == "POST":
    # request.session['name'] = request.POST['name']
    # request.session['location'] = request.POST['location']
    # request.session['language'] = request.Post['language']
    # return render(request, 'result.html')
