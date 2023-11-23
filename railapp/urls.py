"""
URL configuration for railapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
import requests

url = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"



headers = {
	"X-RapidAPI-Key": "8f030e4789mshaba39a7ae8cc09ep125e86jsnffefa141efcf",
	"X-RapidAPI-Host": "irctc1.p.rapidapi.com"
}


def firstpage(request):
    if(request.method=="POST"):
        url = "https://irctc1.p.rapidapi.com/api/v1/searchTrain"
        querystring = {"query":"190"}
        headers = {"X-RapidAPI-Key": "8f030e4789mshaba39a7ae8cc09ep125e86jsnffefa141efcf","X-RapidAPI-Host": "irctc1.p.rapidapi.com"}
        querystring["query"]=request.POST['trainNo']
        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())
        train_data=response.json()['data']
        # train_number=[]
        # train_name=[]
        train_details=[]
        for i in train_data:
            info={}
            info['train_name']=i['train_name']
            info['train_number']=i['train_number']
            
            train_details.append(info)
        
        return render(request,'index2.html',{'Train_details':train_details})


        

    return render(request,'index2.html')

def runningstatus(request):
   
    if(request.method=="POST"):
        
        querystring = {"fromStationCode":"BVI","toStationCode":"NDLS","dateOfJourney":"<REQUIRED>"}
        querystring["fromStationCode"]=request.POST['source']
        querystring["toStationCode"]=request.POST['destination']
        querystring["dateOfJourney"]=request.POST['date']
        print(querystring["dateOfJourney"])
        response = requests.get(url, headers=headers, params=querystring)
        print(response)

        train_data=response.json()['data']
        train_name=[]
        train_number=[]
        train_time=[]
        train_details=[]
        for i in train_data:
            info={}
            info['train_name']=i['train_name']
            info['train_number']=i['train_number']
            info['train_time']=i['from_std']
            train_details.append(info)
           
        return render(request,'runningstatus.html' ,{'Train_details':train_details})
    return render(request,'runningstatus.html')
    
    
def pnrstatus(request):
    if(request.method=='POST'):

        url = "https://irctc1.p.rapidapi.com/api/v2/getPNRStatus"
        querystring = {"pnrNumber":"<REQUIRED>"}
        querystring["pnrNumber"]=request.POST['pnrno']
        headers = {
	                       "X-RapidAPI-Key": "8f030e4789mshaba39a7ae8cc09ep125e86jsnffefa141efcf",
	                                 "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
        }
         
        
        response = requests.get(url, headers=headers, params=querystring)
        print(response.json())
        trainNo=response.json()['data']['train_number']
        trainName=response.json()['data']['train_name']
        BoardingDate=response.json()['data']['date']
        From=response.json()['data']['source_station']['station_code']
        to=response.json()['data']['reservation_upto']['station_code']
        class1=response.json()['data']['class']
        data_details={}
        data_details['train_number']=trainNo
        data_details['train_name']= trainName
        data_details['date']=BoardingDate
        data_details['source_station']=From
        data_details['reservation_upto']=to
        data_details['class']=class1
        print("data_details:",data_details)
        passenger_serial_number=[]
        passenger_booking_status=[]
        passenger_details=[]
        for i in response.json()['data']['passenger']:
            passenger_detail={}
            passenger_detail['passengerSerialNumber']=i['passengerSerialNumber']
            if(i['bookingStatus']=='CNF'):
                bookingDetails=[]
                bookingDetails.append(i['bookingStatus'])
                bookingDetails.append(i['bookingCoachId'])
                bookingDetails.append(i['bookingBerthNo'])
                s="/"
                bookingDetails_details=s.join(bookingDetails)
                passenger_detail['bookingStatus']=bookingDetails_details
            else:
                passenger_detail['bookingStatus']=i['bookingStatus']
            passenger_detail['currentStatus']= i['currentStatus']
            passenger_details.append(passenger_detail)
            print("PassengerDetils:",passenger_details)
        
      
            




        return render(request,'pnrstatus.html',{'data':data_details,'passenger_details': passenger_details})


    return render(request,'pnrstatus.html')



    
# def view_form(request):
#     return render(request,'simpleform.html')
from django.shortcuts import render
from rail.forms import InputForm
from rail.models import  Member
# Create your views here.
def view_form(request):
    context ={}
    context['form']= InputForm()
    if(request.method=='POST'):
        print(request.POST)
        full_name=request.POST['firstname']
        last_name=request.POST['lastname']
        #email=request.POST['email']
        age=request.POST['age']
        sex=request.POST['sex']
        print(sex)
        print(age)
        Berth_Choices=request.POST['berth_choice']
        contact=Member.objects.create(firstname=full_name, lastname=last_name,age=age,sex=sex,berth_choice=Berth_Choices)
        #context['form']= InputForm(request.method,instance=contact)

    return render(request, "simpleform.html", context)
    
def showlist(request):
    mydata= Member.objects.all()
    #print(mydata)
    context = {
    'mymembers': mydata,}
    return render(request,"showlist.html",context)
def destroy(request, id):  
    employee = Member.objects.get(id=id)  
    employee.delete()  
    mydata= Member.objects.all()
    #print(mydata)
    context = {
    'mymembers': mydata,}
    return render(request,"showlist.html",context)  

def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = Member.objects.get(id=id)
    print(obj)
    #form = InputForm(request.POST or None)

# Creating a form to change an existing article.
    article = Member.objects.get(id=id)
    #form =InputForm(instance=article)
    # pass the object as instance in form
    #form = InputForm( instance=obj)
    #print(form)
    form= InputForm(request.POST or None,instance=article)
    print(form)
    print(request.POST,"hello bhai")
    # save the data from the form and
    # redirect to detail_view
    #print(form)
    
    # add form dictionary to context
    context["form"] = form
    #print(form.errors())
    if(form.is_valid()):
        form.save()
        print("iske andar")
        mydata= Member.objects.all()
    #print(mydata)
        context = {
        'mymembers': mydata,}
        return render(request,"showlist.html",context)  
    return render(request, "updateform.html",context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstpage,name="homeview"),
    path('index/',runningstatus,name="index"),
    path('pnrst/',pnrstatus,name="pnrst"),
    path('my_view1/',view_form,name="viewform"),
    path('show_list/',showlist,name="showlist"),
    path('delete/<int:id>',destroy,name="delete"),
    path('edit/<int:id>',update_view,name="edit")

    
    ]
