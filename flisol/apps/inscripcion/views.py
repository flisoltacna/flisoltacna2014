from django.shortcuts import render_to_response
from django.template import RequestContext
from flisol.apps.inscripcion.forms import addInscritoForm
from flisol.apps.inscripcion.models import InscritoExpo
from django.http import HttpResponseRedirect

def index_view(request):
	info = "iniciado"
	if request.method == "POST":
		form = addInscritoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('')
	else:
		form = addInscritoForm()
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/index.html',ctx,context_instance = RequestContext(request))