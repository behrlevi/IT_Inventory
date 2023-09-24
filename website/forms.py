from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Equipment
from django.forms import modelformset_factory


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail address'}))
	first_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name','email','password1','password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'



#Create Add Record form

class AddRecordForm(forms.ModelForm):
	first_name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class":"form-control"}), label="")
	last_name=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name","class":"form-control"}), label="")
	company=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Company","class":"form-control"}), label="")
	position=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Position","class":"form-control"}), label="")
	note=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Note","class":"form-control"}), label="")

	class Meta:
		model=Record
		exclude=("user",)


class EditEquipmentForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(EditEquipmentForm, self).__init__(*args, **kwargs)
		self.fields['hwtype'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['vendor'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['model'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['stag'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['location'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['status'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['pdate'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['name'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['licence'].widget.attrs.update({'class': 'form-control form-control-sm'})
		self.fields['company'].widget.attrs.update({'class': 'form-control form-control-sm'})

	class Meta:
		model=Equipment
		fields = '__all__'


EquipmentFormSet = modelformset_factory(
    Equipment,
    form=EditEquipmentForm,
    fields=('hwtype', 'vendor', 'model', 'stag', 'location', 'status', 'pdate', 'name', 'licence', 'company')
)
