from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegistroForm

def thank_you(request):
        return render(request, 'registro/thank_you.html')

def home(request):
        if request.method == "POST":
            form = RegistroForm(request.POST)
            if form.is_valid():
                registro = form.save()
                return redirect('thank_you')
            else:
                return render(request, 'registro/error.html', {'form': form})
        else:
            form = RegistroForm()
        return render(request, 'registro/thank_you.html', {'form': form})
