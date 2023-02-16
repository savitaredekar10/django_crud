from django.shortcuts import render, redirect
from .models import Info
from django.http import HttpResponse
from django.contrib import messages
from .forms import InfoForm, UpdateForm, DeleteForm
from django.urls import reverse

def home(request):
	return render(request, 'home.html')

def insert(request, uid=1):
	if request.method == 'POST':
		inform = InfoForm(request.POST)
		if inform.is_valid():
			inform.save()
			messages.info(request,"Information stored successfully")
			return redirect(reverse("display"))
		else:
			messages.info(request,"Invalid Information")
			return redirect(reverse("insert"))
	else:
		inform=InfoForm()
		return render(request,"insert.html",{'inform':inform})
		
def display(request):
	data=Info.objects.all()
	context={"data":data}
	# return HttpResponse("<br>".join([e.name for e in data ]))
	return render(request, "display.html", context)

def update(request):
	if request.method == 'POST':
		upform = UpdateForm(request.POST)
		if upform.is_valid():
			uid=request.POST.get('uid','')
			new_name=request.POST.get('name','')

			if Info.objects.filter(uid=uid):
				obj=Info.objects.filter(uid=uid)
				obj.update(name=new_name)
				messages.info(request, "Name updated successfully")
				return redirect(reverse("display"))
			else:
				messages.info(request, "Invalid uid, not found in database")
				return redirect(reverse("update"))

		else:
			messages.info(request, "Invalid data")
			return redirect(reverse("update"))
	else:
		upform=UpdateForm()
		return render(request, "update.html",{'upform':upform})

def delete(request):
	if request.method == 'POST':
		delform = DeleteForm(request.POST)
		if delform.is_valid():
			uid=request.POST.get('uid','')

			if Info.objects.filter(uid=uid):
				obj=Info.objects.filter(uid=uid)
				obj.delete()
				messages.warning(request, "Record deleted successfully")
				return redirect(reverse("display"))
			else:
				messages.warning(request, "Invalid uid, not found in database")
				return redirect(reverse("delete"))

		else:
			messages.info(request, "Invalid data")
			return redirect(reverse("delete"))
	else:
		delform=DeleteForm()
		return render(request, "delete.html",{'delform':delform})