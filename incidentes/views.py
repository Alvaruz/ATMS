from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import TicketForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.core import serializers

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



# def estadisticas(request):
# 	return render(request, 'estadisticas_prueba.html', {})



def apimes(request):
    data = Ticket.objects.all() \
        .extra(select={'month': connections[Ticket.objects.db].ops.date_trunc_sql('month', 'fecha')}) \
        .values('month') \
        .annotate(count_items=Count('id'))
    return JsonResponse(list(data), safe=False)


def estadisticas(request): 
    # data = serializers.serialize("json", Ticket.objects.only("categoria").annotate(Count('id')))

    #--CATEGORIA---
    mantenimiento = Ticket.objects.only("categoria").filter(categoria=1).count()
    vehiculo_mal_estacionado = Ticket.objects.only("categoria").filter(categoria=2).count()
    vehiculo_descompuesto = Ticket.objects.only("categoria").filter(categoria=3).count()
    manifestacion = Ticket.objects.only("categoria").filter(categoria=4).count()
    cierre_de_calle = Ticket.objects.only("categoria").filter(categoria=5).count()
    accidente = Ticket.objects.only("categoria").filter(categoria=6).count()
    obras = Ticket.objects.only("categoria").filter(categoria=7).count()
    obstaculo = Ticket.objects.only("categoria").filter(categoria=8).count()
    congestionamiento = Ticket.objects.only("categoria").filter(categoria=9).count()

    #--GRUPO---
    sistemas = Ticket.objects.only("grupo_destino").filter(grupo_destino=1).count()
    redes = Ticket.objects.only("grupo_destino").filter(grupo_destino=2).count()
    pmt_atms = Ticket.objects.only("grupo_destino").filter(grupo_destino=3).count()
    pmt_otros = Ticket.objects.only("grupo_destino").filter(grupo_destino=4).count()
    operadores = Ticket.objects.only("grupo_destino").filter(grupo_destino=5).count()
    tecnicos = Ticket.objects.only("grupo_destino").filter(grupo_destino=6).count()
    administrativa = Ticket.objects.only("grupo_destino").filter(grupo_destino=7).count()
    jefatura = Ticket.objects.only("grupo_destino").filter(grupo_destino=8).count()

    #--ESTADO--
    pendiente = Ticket.objects.only("estado").filter(estado=1).count()
    cerrado = Ticket.objects.only("estado").filter(estado=2).count()
    atendido = Ticket.objects.only("estado").filter(estado=3).count()
    vencido = Ticket.objects.only("estado").filter(estado=4).count()


    data = {
        "mantenimiento": mantenimiento,
        "vehiculo_mal_estacionado": vehiculo_mal_estacionado,
        "vehiculo_descompuesto": vehiculo_descompuesto,
        "manifestacion": manifestacion,
        "cierre_de_calle": cierre_de_calle,
        "accidente": accidente,
        "obras": obras,
        "obstaculo": obstaculo,
        "congestionamiento": congestionamiento,

        "pmt_otros": pmt_otros,
        "sistemas": sistemas,
        "redes": redes,
        "pmt_atms": pmt_atms,
        "operadores": operadores,
        "tecnicos": tecnicos,
        "administrativa": administrativa,
        "jefatura": jefatura,


        "pendiente": pendiente,
        "cerrado": cerrado,
        "atendido": atendido,
        "vencido": vencido,
        }

    return render(request, 'estadisticas_prueba.html', {'data':data})





# Mcal. López
mcal_lopez = Ticket.objects.filter(ubicacion__contains='cal')


Ticket.objects.select_related('grupo_destino').filter(grupo_destino=3).count() # PMT Atms
Ticket.objects.select_related('grupo_destino').filter(grupo_destino=4).count() # PMT Otros