from django import forms
from flisol.apps.inscripcion.models import InscritoExpo

class addInscritoForm(forms.ModelForm):
	class Meta:
		model 	= InscritoExpo