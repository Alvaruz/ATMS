from django import forms
from incidentes.models import Ticket

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         widgets = {
#         'password': forms.PasswordInput(),
#     }


class TicketForm(forms.ModelForm):

	class Meta:
		model = Ticket


		fields = [
			'codigo', 		# nuevo
			'categoria',
			'ubicacion',
			'usuario',
			'grupo_destino',
			'detalle',
			'equipo',
			'fecha',
			'fecha_fin', 	# nuevo
			'estado',
			'editado_por', 	# nuevo
			'imagen',		# nuevo
		]
		labels = {
			'codigo': 'Código',						# nuevo
			'categoria': 'Categoría',
			'ubicacion': 'Nombre/Dirección',
			'usuario': 'Generador Por',
			'grupo_destino': 'Remitir A',
			'detalle': 'Detalle',
			'equipo': 'Equipo (si corresponde)',
			'fecha': 'Fecha (dd/mm/aaa hh:mm)',
			'fecha_fin': 'Editado/Cerrado- Fecha:',	# nuevo
			'estado': 'Estado Ticket',
			'editado_por': 'Editado/Cerrado- Por:', # nuevo
			'imagen': 'Adjuntar Imagen',			# nuevo
		}
		widgets = {
			'codigo': forms.TextInput(attrs={'class':'form-control'}), 		# nuevo
			'categoria': forms.Select(attrs={'class':'form-control'}),
			'ubicacion': forms.TextInput(attrs={'class':'form-control'}),
			'usuario': forms.Select(attrs={'class':'form-control'}),
			'grupo_destino': forms.Select(attrs={'class':'form-control'}),
			'detalle': forms.Textarea(attrs={'class':'form-control'}),
			# 'equipo': forms.CheckboxSelectMultiple(),
			'equipo': forms.Select(attrs={'class':'form-control'}),
			'fecha': forms.DateTimeInput(),
			'fecha_fin': forms.DateTimeInput(),	# nuevo
			'estado': forms.Select(attrs={'class':'form-control'}),
			'editado_por': forms.Select(attrs={'class':'form-control'}),	# nuevo
			'imagen': forms.FileInput(attrs={'class':'container'}),			# nuevo
		}