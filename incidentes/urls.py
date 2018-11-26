
from django.urls import path
from . import views
from .views import * 


urlpatterns = [
	path('home/', views.home, name='home'),
	path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('tickets/', views.ticket_home, name='ticket_home'),
    path('tickets/listar', views.tickets, name='ticket_list'),
    path('tickets/nuevo/', TicketAddView.as_view(), name='ticket_add'),
    path('tickets/editar/<int:pk>', TicketEditView.as_view(), name='ticket_edit'), #TicketEditView.as_view()
    path('tickets/eliminar/<int:pk>', TicketDeleteView.as_view(), name='ticket_delete'),
    path('tickets/estadisticas/', views.estadisticas, name='estadisticas'),
]
