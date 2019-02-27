from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime 
from dateutil import relativedelta
from .models import *

def med_dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:

        context={
        'all_children':Dependent.objects.all(),
        'users':User.objects.all()
    }
        return render(request, "meds/med_dashboard.html",context)

def child(request):#add a child on this page



    return render(request,"meds/child.html")


def addchild(request):#button
    #if parent only gives inches, feet will be 0
    feet=request.POST['feet']
    if len(feet)==0:
        feet=0
    else:
        feet=int(feet)
    print(feet)
    print(type(feet))

    #if parent only gives feet, inches will be 0
    inches=request.POST['inches']
    if len(inches)==0:
        inches=0
    else:
        inches=int(inches)
    print(inches)
    print(type(inches))
    #converts height to inches
    height_in=feet* 12 + inches
    
    #add child in database
    user=User.objects.get(id=request.session['user_id'])
    
    this_child=Dependent.objects.create(first_name=request.POST['child_first'], last_name=request.POST['child_last'], dob=request.POST['dob'], gender=request.POST['gender'], height=height_in, weight=request.POST['weight'], blood_type=['blood'], user=user)
    print("///////child added////////")

    

    request.session['dob']=request.POST['dob']
    return redirect('/dashboard')


# def vaccines(request): #button
#     today = datetime.now()
#     dob = datetime(2017,8,15) #POST REQUEST['dob']- session
#     difference = relativedelta.relativedelta(today,dob)
#     request.session["months_old"] = difference.years * 12 + difference.months
    
#     return redirect(request,'/seevaccines')

def seevaccines(request, dependent_id):#page
    the_child=Dependent.objects.get(id=dependent_id)
    context={
        'child_info':the_child
    }
    
    # if request.session["months_old"] == 0:
    
    return render(request, 'meds/vaccinedue.html', context)

def viewvaccine(request, dependent_id): #button
    print("going to see vaccines")
    the_child=Dependent.objects.get(id=dependent_id)
    

    return redirect('/dashboard/seevaccines/'+str(dependent_id))

def delete(request, dependent_id):
    delete_child= Dependent.objects.get(id=dependent_id)
    delete_child.delete()

    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')#main login and reg page