from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegistroForm

def home(request):
        if request.method == "POST":
            form = RegistroForm(request.POST)
            if form.is_valid():
                registro = form.save()
                return render(request, 'registro/thank_you.html', {})
            else:
                return render(request, 'registro/error.html', {'form': form})
        else:
            form = RegistroForm()
        return render(request, 'registro/index.html', {})

def thank_you(request):
        return render(request, 'registro/thank_you.html', {})
