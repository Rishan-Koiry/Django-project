# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("email")
        massage= request.POST.get("message")
        with open("userinfo.txt", "a") as file:
            file.write(f"Name: {name},email:{number}\nMessage: {massage}")
        return HttpResponse("""
            <h1 style='color: green; font-family: Arial, sans-serif; animation: fadeIn 2s;'>Your Data has been Saved Successfully!</h1>
            <style>
            body{
                background-color: #222831;
                font-family: Arial, sans-serif;
                color: #00ADB5;
                text-align: center;
                margin: 0;
                padding: 20px;
                margin-top: 500px;
            }
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
            </style>
        """)
    context = {"username": "Rishan"}
    return render(request, "userinfo/index.html", context)
