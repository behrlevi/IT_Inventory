from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, EditEquipmentForm, EquipmentFormSet, DeleteEquipmentForm
from .models import Record, Equipment
from django.forms import modelformset_factory
from django.utils import timezone
from django.db.models import Count


def home(request):
	records = Record.objects.all()

	#Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in.")
			return redirect('home')
		else:
			messages.success(request, "Incorrect username or password.")
			return redirect ('home')
	else:
		return render(request, 'home.html', {'records':records})

def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out.")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You have successfully registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
	if request.user.is_authenticated:
		#Look up records
		customer_record=Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You must be logged in to view this page.")
		return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        # Check if there are any related Equipment objects for the Record
        record_exists = Record.objects.filter(id=pk).annotate(equipment_count=Count('equipment')).first()
        
        if record_exists and record_exists.equipment_count > 0:
            # Equipment objects are associated with the Record, don't allow deletion
            messages.error(request, "Cannot delete this record because it has associated equipment.")
        else:
            # No Equipment objects associated, proceed with deletion
            record_to_delete = Record.objects.filter(id=pk).first()
            if record_to_delete:
                record_to_delete.delete()
                messages.success(request, "Record deleted successfully.")
    
    else:
        messages.success(request, "You must be logged in to delete records.")
    
    return redirect('home')

def add_record(request):
	form=AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method=="POST":
			if form.is_valid():
				add_record=form.save()
				messages.success(request, "Record added")
				return redirect('home')
		return render(request, 'add_record.html', {'form': form})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')

def edit_equipment(request, pk):
	if request.user.is_authenticated:
		user_record = get_object_or_404(Record, pk=pk)
		user_equipment = Equipment.objects.filter(record=user_record)
		EquipmentFormSet = modelformset_factory(Equipment, form=EditEquipmentForm, extra=len(user_equipment))

		if request.method=='POST':
			formset=EquipmentFormSet(request.POST, queryset=user_equipment)
			if formset.is_valid():
				formset.save()
				messages.success(request, "Equipment list has been updated.")
				return redirect('home')
			else:
				print(formset.errors)
		else:
			formset = EquipmentFormSet(queryset=user_equipment)

			
			for form in formset:
				form.fields['hwtype'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['vendor'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['model'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['stag'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['location'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['status'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['pdate'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['licence'].widget.attrs.update({'class': 'form-control form-control-sm'})
				form.fields['company'].widget.attrs.update({'class': 'form-control form-control-sm'})
				

		context = {
        	'user_record': user_record,
        	'formset': formset,
    	}
		return render(request, 'edit_equipment.html', context)
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')

def list_equipment(request, pk):
	record = Record.objects.get(id=pk)
	equipments = Equipment.objects.filter(record=record)
	return render(request, 'equipment.html', {'equipments': equipments, 'record': record})

def add_equipment(request, pk):
	if request.user.is_authenticated:
		user_record = get_object_or_404(Record, pk=pk)
		user_equipment = Equipment.objects.filter(record=user_record)
		EquipmentFormSet = modelformset_factory(Equipment, form=EditEquipmentForm, extra=1)

		if request.method=='POST':
			formset=EquipmentFormSet(request.POST, queryset=user_record.equipment_set.all())
			if formset.is_valid():
				formset.save()
				messages.success(request, "New equipment has been added.")
				return redirect('home')
			else:
				print(formset.errors)
		else:
			# Set the initial value for the record field to the primary key (pk) of user_record
			initial_data = [{ 'company':'ROSSI', 'pdate':timezone.now(), 'record': user_record.pk}]
			formset = EquipmentFormSet(None, queryset=Equipment.objects.none(), initial=initial_data)

		context = {
			'user_record': user_record,
			'formset': formset,
			}
		return render(request, 'add_equipment.html', context)
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')

def delete_equipment(request, pk):
	if request.user.is_authenticated:
		item = get_object_or_404(Equipment,pk=pk)
		if request.method == 'POST':
			item.delete()
			messages.success(request, "Item deleted successfully.")
			return redirect('home')
	else:
		messages.success(request, "You must be logged in to delete items.")
		return redirect('home')
