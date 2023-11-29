from django.shortcuts import render, redirect
from django_reservas.models import Reservas
from django_reservas.forms import FormReservas

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoReservas(request):
    reservas = Reservas.objects.all()
    data = {'reserva': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    if request.method == 'POST':
        form = FormReservas(request.POST)
        if form.is_valid():
            print("FORMULARIO OK!!")
            print("Responsable: ", form.cleaned_data.get('responsable'))
            form.save()
            return redirect('/reservas')
        else:
            print("FORMULARIO NO VÁLIDO")
    else:
        form = FormReservas()

    data = {'form': form}
    return render(request, 'agregar.html', data)

def eliminarReserva(request, IN_id):
    reserva = Reservas.objects.get(id = IN_id)
    reserva.delete()
    return redirect('/reservas')

def modificarReserva(request, IN_id):
    reserva = Reservas.objects.get(id = IN_id)
    form = FormReservas(instance=reserva)

    if (request.method == 'POST'):
        form = FormReservas(request.POST, instance=reserva)
        if (form.is_valid()):
            form.save()
        return redirect('/reservas')
  
    data = {'form': form}
    return render (request, 'agregar.html', data)