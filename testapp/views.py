from tempfile import template

from django.shortcuts import render
import datetime

# def wish(request):
#     return render(request,'testapp/wish.html ')


def wish(request):
    date=datetime.datetime.now()
    name="saurabh"
    marks=80
    rollno=1
    my_dict={'insert_date':date,'insert_name':name,'insert_marks':marks,'insert_rollno':rollno}
    return render(request,'testapp/wish.html',my_dict)
