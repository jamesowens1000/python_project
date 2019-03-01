from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime, timezone
from dateutil import relativedelta
from .models import *

#Vaccination.objects.filter(age_groups__min_age=7).distinct()
def med_dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")
    else:

        context={
        'all_children':Dependent.objects.all(),
        'users':User.objects.get(id=request.session['user_id'])
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

    


    return redirect('/dashboard')




def seevaccines(request, dependent_id):#page
    the_child=Dependent.objects.get(id=dependent_id)
    #age_range=Age_group.objects.
    
    today = datetime.now(timezone.utc)
    print('//////////////////////////////')
    print(today)
    dob = the_child.dob
    print(dob)
    difference = relativedelta.relativedelta(today,dob)
    #print(difference)
    months_old = difference.years * 12 + difference.months
    print("The child is " +str(months_old)+ " months old")
    
    child_vac=[]

    if months_old <=1:
        age_grp=Age_Group.objects.get(id=1)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=3:
        age_grp=Age_Group.objects.get(id=2)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=5:
        age_grp=Age_Group.objects.get(id=3)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=8:
        age_grp=Age_Group.objects.get(id=4)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=11:
        age_grp=Age_Group.objects.get(id=5)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=12:
        age_grp=Age_Group.objects.get(id=6)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=14:
        age_grp=Age_Group.objects.get(id=7)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=17:
        age_grp=Age_Group.objects.get(id=8)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=18:
        age_grp=Age_Group.objects.get(id=9)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group
    elif months_old <=23:
        age_grp=Age_Group.objects.get(id=10)# the age group the kid falls into
        child_vac=age_grp.vaccinations.all()#getting vacs for the age group

    length=len(child_vac)
    print("///////////////")
    
    context={
        'child_info':the_child,
        'child_vacs':child_vac,
        'length_vac':length

    }
    


    
    return render(request, 'meds/vaccinedue.html', context)

def viewvaccine(request, dependent_id): #button
    print("going to see vaccines")
    the_child=Dependent.objects.get(id=dependent_id)
    

    return redirect('/dashboard/seevaccines/'+str(dependent_id))

def edit_child(request, dependent_id):#button
    print("!!!!!!!!!!I'm trying to edit a child!!!!!!!!")
    return redirect('/dashboard/edit/'+str(dependent_id))


def editchild_page(request, dependent_id): #display page
    child_to_update=Dependent.objects.get(id=dependent_id)
    
    #converting date to the correct format
    print(child_to_update.dob)
    year = str(child_to_update.dob.year)
    month = str(child_to_update.dob.month)
    if(len(month)==1):
        month = "0"+month
    day = str(child_to_update.dob.day)
    if(len(day)==1):
        day = "0"+day
    dob = year+"-"+month+"-"+day
    print(dob)

    #converting weight to the correct format
    weight=str(child_to_update.weight)
        
    #coverting height to correct format



    context={
        'child_form':child_to_update,
        "dob": dob
    }


    return render(request, 'meds/edit_child.html', context)

def save_child(request, dependent_id): #save new child info button
    child_to_update=Dependent.objects.get(id=dependent_id)

    #saving child info into database
    child_to_update.first_name=request.POST['child_first']
    child_to_update.last_name=request.POST['child_last']
    child_to_update.dob=request.POST['dob']
    print(request.POST['dob'])
    child_to_update.dob=request.POST['dob']
    child_to_update.gender=request.POST['gender']
    child_to_update.height=request.POST['feet']
    child_to_update.height=request.POST['inches']
    child_to_update.weight=request.POST['weight']
    child_to_update.blood_type=request.POST['blood']
    child_to_update.save()

    #saving dob into session -->do I need this?
    request.session['dob'] = child_to_update.dob

    print(request.session['dob'])


    return redirect('/dashboard')

def tips(request):

    return render(request,'meds/tips.html')

def delete(request, dependent_id):
    delete_child= Dependent.objects.get(id=dependent_id)
    delete_child.delete()

    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')#main login and reg page