from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .forms import RegForm,DeptForm,Department,ManagerForm,Manager
from .models import Regmodel
# Create your views here.


class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        form_data=RegForm(request.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            name=form_data.cleaned_data.get('name')
            age=form_data.cleaned_data.get('age')
            em=form_data.cleaned_data.get('email')
            ex=form_data.cleaned_data.get('experience')
            Regmodel.objects.create(name=name,age=age,email=em,experience=ex)
            messages.success(request,"Registered succesfully")
            return redirect('reg')
        else:
            messages.error(request,"Registration Failed")
            return render(request,"reg.html",{"form":form_data})    


class Home(View):
    def get(self,request):
        return render(request,"home.html")

class Index(View):
    def get(self,request):
        return render(request,"index.html")        

class ViewEmp(View):
    def get(self,request):
        emp=Regmodel.objects.all()        
        return render(request,"viewemp.html",{"data":emp})     
        
    
class DeleteEmp(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        print(id)
        eob=Regmodel.objects.get(eid=id)
        eob.delete()
        return redirect('vemp')

class EditEmp(View):
    def get(self,request,*args,**kwargs):        
        id=kwargs.get('id')
        emp=Regmodel.objects.get(eid=id)
        form=RegForm(initial={'name':emp.name,'age':emp.age,'email':emp.email,'experience':emp.experience})
        return render(request,"editemp.html",{'form':form})

    def post(self,request,*args,**kwargs):
        form=RegForm(request.POST)
        id=kwargs.get('id')
        if form.is_valid():
            name=form.cleaned_data.get('name')
            age=form.cleaned_data.get('age')
            em=form.cleaned_data.get('email')
            ex=form.cleaned_data.get('experience')
            Regmodel.objects.filter(eid=id).update(name=name,age=age,email=em,experience=ex)
            return redirect('vemp')
        else:
            return redirect('editemp')

class DeptView(View):
    def get(self,request,*args,**kwargs):
        form=DeptForm()
        return render(request,"deptreg.html",{'form':form})
    def post(self,request,*args,**kwargs):
        form_data=DeptForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Department Added")
            return redirect('h')
        else:
            messages.error(request,"Department Adding failed")
            return redirect('dept')
        

class DepRet(View):
    def get(self,request):
        data=Department.objects.all()
        return render(request,"viewdept.html",{"data":data})

class DepDelete(View):
    def get(self,request,*args,**kwargs):
        did=kwargs.get('did')
        dept=Department.objects.get(id=did)
        dept.delete()
        return redirect('depret')

class DeptEdit(View):
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get('did')
        dept=Department.objects.get(id=d_id)
        form=DeptForm(instance=dept)
        return render(request,"editdept.html",{'form':form})
    
    def post(self,request,*args,**kwargs):
        d_id=kwargs.get('did')
        dept=Department.objects.get(id=d_id)
        form_data=DeptForm(request.POST,instance=dept)
        if form_data.is_valid():
            form_data.save()
            return redirect('depret')
        else:
            return redirect('deptedit')


class ManagerReg(View):
    def get(self,request):
        form=ManagerForm()
        return render(request,"addman.html",{'form':form})
    def post(self,request):
        form_data=ManagerForm(request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('h')
        else:
            return redirect('addman')


class ManagerList(View):
     def get(self,request):
         data=Manager.objects.all()
         return render(request,"viewman.html",{'data':data})
     
class DelMang(View):
    def get(self,request,*args,**kwargs):
        mid=kwargs.get('mid')
        manid=Manager.objects.get(id=mid)
        manid.delete()
        return redirect('viewman')

class EditMang(View):
    def get(self,request,*args,**kwargs):
        mid=kwargs.get('mid')
        manid=Manager.objects.get(id=mid)
        form=ManagerForm(instance=manid)
        return render(request,"editmang.html",{'form':form})
    def post(self,request,*args,**kwargs):
        mid=kwargs.get('mid')
        manid=Manager.objects.get(id=mid)
        form_data=ManagerForm(request.POST,files=request.FILES,instance=manid)
        if form_data.is_valid():
            form_data.save()
            return redirect('viewman')
        else:
            return redirect('editman')


