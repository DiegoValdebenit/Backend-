from django import forms
from django_reservas.models import Reservas


class FormReservas(forms.ModelForm):
    ESTADOS = [('reservado','RESERVADO'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')]

    class Meta:
        model = Reservas  # Asegúrate de especificar el modelo aquí
        fields = '__all__'

    responsable = forms.CharField()
    telefono = forms.IntegerField(label='Teléfono')
    fechaReserva=forms.DateField(label='Fecha de Reserva')
    horaReserva=forms.TimeField(label='Hora de Reserva')
    cantidadPersonas = forms.IntegerField(label='Cantidad de Personas')
    email = forms.CharField()
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    observacion = forms.CharField(required=False, label='Observación')

    def clean_responsable(self):
        input_responsable = self.cleaned_data['responsable']
        if len(input_responsable) > 80:
            raise forms.ValidationError("El largo máximo del nombre son 80 caracteres")
        return input_responsable

    def clean_cantidadPersonas(self):
        input_cantidadPersonas = self.cleaned_data['cantidadPersonas']
        if input_cantidadPersonas < 1 or input_cantidadPersonas > 15:
            raise forms.ValidationError("Cantidad de personas incorrecta")
        return input_cantidadPersonas

    def clean_email(self):
        input_email = self.cleaned_data['email']
        if not "@" in input_email:
            raise forms.ValidationError("Correo Electrónico incorrecto")
        return input_email

    #bootstrap
    responsable.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fechaReserva.widget.attrs['class'] = 'form-control'
    horaReserva.widget.attrs['class'] = 'form-control'
    cantidadPersonas.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'
