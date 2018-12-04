
from django.urls import path
from . import views
from .views import * 


urlpatterns = [
	path('home/', views.home, name='home'),
	path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('tickets/', views.ticket_home, name='ticket_home'),
    path('tickets/listar/', views.tickets, name='ticket_list'),
    path('tickets/nuevo/', TicketAddView.as_view(), name='ticket_add'),
    path('tickets/editar/<int:pk>/', TicketEditView.as_view(), name='ticket_edit'), #TicketEditView.as_view()
    path('tickets/eliminar/<int:pk>/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('tickets/estadisticas/', views.estadisticas_main, name='estadisticas_main'),
    path('tickets/estadisticas_dia/', views.estadisticas_dia, name='estadisticas_dia'),
    path('tickets/estadisticas_mes/', views.estadisticas_mes, name='estadisticas_mes'),
    path('tickets/estadisticas_total/', views.estadisticas_total, name='estadisticas_total'),
    path('tickets/estadisticas_versus/', views.global_versus, name='global_versus'),
    path('comunicaciones/estadisticas_dia/', views.comunicaciones_estadisticas_dia, name='comunicaciones_estadisticas_dia'),
    path('comunicaciones/estadisticas_mes/', views.comunicaciones_estadisticas_mes, name='comunicaciones_estadisticas_mes'),
    path('prensa/estadisticas_mes/', views.prensa_estadisticas_mes, name='prensa_estadisticas_mes'),

    # path('tickets/api/estadisticas',views.apimes, name="apimes"),
]
