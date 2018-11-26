from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import TicketForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def home(request):
	return render(request, "index2.html", {})

def base(request):
	return render(request, "base.html", {})

def ticket_list(request):
	return render(request, "ticket_list.html", {})

def ticket_home(request):
	return render(request, "tickets2.html", {})

def login(request):
	return render(request, "login.html", {})

def tickets(request):
	ticket = Ticket.objects.order_by('-fecha')
	# tk_vencido = Ticket.objects.order_by('fecha')

	template = loader.get_template('ticket_list.html')
	context = {
		'ticket': ticket,
		'categoria': ticket,
		'grupo_destino': ticket,
		'fecha': ticket, 
		'estado': ticket, 

	}

	return HttpResponse(template.render(context, request))


def ticket_view(request):
	if request.method == 'POST':
		form = TicketForm(request.POST)
		if form.is_valid():
			form.save()
			print("formulario guardado")
		return redirect('tickets')
	else:
		form = TicketForm()
	return render(request, 'ticket_form.html', {'form':form})



# version de prueba class

class TicketListView(ListView):
	template_name = 'tickets2.html'
	model = Ticket
	# listado_tickets = Tickets.objects.all()
	# paginator = Paginator(listado_tickets, 10) # Muestra 10 elementos por página.

	# pagina = request.GET.get('page')
 #    pagina_actual = paginator.get_page(page)
 #    return render(request, 'list.html', {'pagina_actual': pagina_actual}) 



class TicketAddView(CreateView):
	model = Ticket
	template_name = 'ticket_form2.html'
	form_class = TicketForm
	success_url = reverse_lazy('ticket_list')

	def form_valid(self, form):
		form.save()
		return super(TicketAddView, self).form_valid(form)


def ticket_edit(request, pk):
	ticket = Ticket.objects.get(id=pk)
	if request.method == 'GET':
		form = TicketForm(instance=ticket)
	else:
		form = TicketForm(request.POST, instance=ticket)

		f = open('wtf.txt','w')
		f.write(form)
		f.close()

		print(form)
		if form.is_valid():
			form.save()
		return redirect('ticket_list')
	return render(request, 'ticket_form2.html',{'form':form})


class TicketEditView(UpdateView):
	model = Ticket
	template_name = 'ticket_form2.html'
	form_class = TicketForm
	success_url = reverse_lazy('ticket_list')

	# def form_valid(self, form):
	# 	form.save()
	# 	return super(TicketEditView, self).form_valid(form)


class TicketDeleteView(DeleteView):
	model = Ticket
	template_name = 'ticket_delete2.html'
	form_class = TicketForm
	success_url = reverse_lazy('ticket_list')





def estadisticas(request):
	return render(request, 'estadisticas.html', {})



# Mcal. López
mcal_lopez = Ticket.objects.filter(ubicacion__contains='cal')


Ticket.objects.select_related('grupo_destino').filter(grupo_destino=3).count() # PMT Atms
Ticket.objects.select_related('grupo_destino').filter(grupo_destino=4).count() # PMT Otros