from django.http import HttpResponse  # this is neccesary learn it
from django.shortcuts import render
import datetime  # for e.g we perform date operation and at last we append it in httpresponse in string


def home(request):  # calls the method and prints message below
    date = datetime.datetime.now()
    # return HttpResponse("<h1>Hello this is index page</h1>"+str(date))#this 'HttpResponse'is used for sending this message  to client
    # on running this in new terminal you get your port in the last which can be run on browser


#dyanamic values
    isActive=True
    name="Dharmesh"
    list_of_programs=[
        'JAI shree ram',
        'Jai bajarang bali',
        'Har Har Mahadev',
        'Jai shri Krishna'
    ]

    student={
    'student_name':"Nannu",
    'student_college':"JECRC",
    'student_city':"Jaipur"
    }
    data={
    'date':date,
    'isActive':isActive,
    'name':name,
    'list_of_programs':list_of_programs,
    'student_data':student
    }
    return render(request, "home.html",data)


# another method for about section below
def about(request):
    # return HttpResponse("<h1>This is about Page</h1>")
    return render(request, "about.html", {})


# services page
def services(request):
    # return HttpResponse("<h1>This is services section</h1>")
    return render(request, "services.html", {})
