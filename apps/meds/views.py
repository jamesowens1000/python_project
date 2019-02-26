from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime 
from dateutil import relativedelta

def med_dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:
        return render(request, "meds/med_dashboard.html")

def child(request):#add a child on this page
    
    return render(request,"meds/child.html")


def addchild(request):#button
    height_cm=int(request.POST['feet'])*12 +int(request.POST['inches'])#convert height into cm

    #create the child in db
    Dependent.objects.create(first_name=request.POST['child_first'], last_name=request.POST['child_last'], dob=request.POST['dob'], gender=request.POST['gender'], height=height_cm, weight=request.POST['weight'], blood_type=['blood'])

    request.session['dob']=request.POST['dob']
    return redirect('/med_dashboard')


def vaccines(request): #button
    today = datetime.now()
    dob = datetime(2017,8,15) #POST REQUEST['dob']- session
    difference = relativedelta.relativedelta(today,dob)
    request.session["months_old"] = difference.years * 12 + difference.months
    
    return redirect(request,'/seevaccines')

def seevaccines(request):#page
    
    context={
 
    }
    
    # if request.session["months_old"] == 0:
    
    return render(request, 'meds/vaccinedue.html')

def logout(request):
    request.session.clear()
    return redirect('/')#main login and reg page