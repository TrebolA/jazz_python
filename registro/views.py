from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from .forms import RegistroForm
from django.shortcuts import redirect
from registro.models import Registro
from django.http import HttpResponse
import random
import csv


def home(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            inscrito = form.save(commit=False)
            listCodigos = []
            numAlea = random.randrange(1000)
            #f = open('/opt/python/current/app/registro/codigos.txt')
            f = open('/home/pruebasBrageanth/jazz_python/registro/codigos.txt')
            linea = f.readline()
            while linea != "":
                listCodigos.append(linea)
                linea = f.readline()
            darCodigo = listCodigos.pop(numAlea)
            inscrito.codigo = darCodigo
            inscrito.save()
            subject = 'Codigo de descuento Silencio Jazz Club'
            text_content = 'Tu codigo para recibir beneficios para Silencio Jazz Club es : '+inscrito.codigo
            html_content = "<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Jazz</title><base href='/'><meta name='viewport' content='width=device-width, initial-scale=1'><link rel='icon' type='image/x-icon' href='favicon.ico'><link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css' integrity='sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO' crossorigin='anonymous'><link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.3.1/css/all.css' integrity='sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU' crossorigin='anonymous'><link rel='stylesheet' href='{% static 'css/style.css' %}'><script src='https://unpkg.com/scrollreveal'></script><style media='screen'>body {background-color: #000;}.text-rosado{color: #c24776;}.btn-rosado{background: #c24776;}.bg-gris{background: #333;}.border-gris{border-color: #555;}</style></head><body class='p-0 m-0'><table class='container-fluid m-0 p-0 text-center'><tr class='row'><td class='col p-0'><img src='https://paramobucket.s3.amazonaws.com/static/img/untitled.png' class='img-fluid w-100' alt=''></td></tr><tr class='row'><td class='col p-0'><img src='https://paramobucket.s3.amazonaws.com/static/img/untitled1.png' class='img-fluid w-100' alt=''></td></tr><tr class='row'><td class='col p-0 text-rosado'><h2 class='font-weight-bold'>"+inscrito.nombre+"</h2></td></tr><tr class='row'><td class='col p-0 text-rosado'><h3 class='font-weight-bold'>LA LEYENDA MÁS GRANDE DEL JAZZ LLEGA A COLOMBIA</h3></td></tr><tr class='row'><td class='col-sm-2'></td><td class='col-lg-8 p-0 text-white'><p class='text-justify'>Silencio Jazz Club 2018 trae a uno de los músicos más importantes de la historia del Jazz, Herbie Hancock. No sólo se considera uno de los artistas más importantes del Jazz, sino que perteneció, durante cinco años, a la banda de Miles Davis, quizás la figura más grande del Jazz de todos los tiempos, ayudando a definir y a redefinir el género desde sus inicios.</p></td><td class='col-sm-2'></td></tr><tr class='row'><td class='col-sm-2'></td><td class='col-lg-8 p-0 text-white'><p class='text-justify'>Por habernos acompañado en Silencio Jazz Club 2017 con Gregory Porter, queremos darle la oportunidad de adquirir sus entradas en la <span class='font-weight-bold'>PREVENTA EXCLUSIVA CON UN 20% DE DESCUENTO.</span></p></td><td class='col-sm-2'></td></tr><tr class='row'><td class='col-lg-12 p-0 text-white'><h4 class='font-weight-bold'>SU CÓDIGO DE DESCUENTO</h4></td></tr><tr class='row'><td class='col p-0 text-rosado'><h2 class='font-weight-bold'>"+inscrito.codigo+"</h2></td></tr><tr class='row'><td class='col p-0 text-rosado'><button type='button' class='btn btn-rosado btn-lg text-white mt-4 mb-4'><a href='http://vive.tuboleta.com/' target='_blank' class='text-white'>Comprar Entradas</a></button></td></tr><tr class='row'><td class='col-sm-1'></td><td class='col-lg-10 p-0 text-white'><p class='text-justify' style='font-size:.65em;'>Descuento válido del 13 de septiembre desde las 00:00 h hasta el 19 de septiembre a las 23:59 h o hasta agotar existencias. Descuento no aplica sobre el ticket service o consumos no especificados. Boletas disponibles por localidad: Platino: 92 / Gold: 148 / VIP: 60. Compra máximo de 6 entradas por código.</p></td><td class='col-sm-1'></td></tr><tr class='row'><td class='col p-0'><img src='https://paramobucket.s3.amazonaws.com/static/img/untitled2.png' class='img-fluid w-50' alt=''></td></tr><tr class='row bg-gris pt-3 pb-3 border-bottom border-gris border-5'><td class='col-lg-12 p-0'><a href='https://www.facebook.com/silenciojazzclub'><i class='fab fa-facebook-f text-white mr-2' style='font-size: 1.5em;'></i></a><a href='https://www.instagram.com/silenciojazzclub/'><i class='fab fa-instagram text-white ml-2' style='font-size: 1.5em;'></i></a></td></tr><tr class='row bg-gris pt-3'><td class='col-lg-12 p-0 text-white'><p style='font-size:.85em;'>Copyright © 2018 Trebol Digital, All rights reserved.</p></td></tr></table><script src='https://code.jquery.com/jquery-3.3.1.slim.min.js' integrity='sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo' crossorigin='anonymous'></script><script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js' integrity='sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49' crossorigin='anonymous'></script><script src='https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js' integrity='sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy' crossorigin='anonymous'></script></body></html>"
            from_email = '"10Music" <juan@10music.com>'
            to = inscrito.correo
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            #f1 = open("/opt/python/current/app/registro/codigos.txt", 'w')
            f1 = open('registro/codigos.txt', 'w')
            for x in listCodigos:
                f1.write(x)
            f1.close()
            f.close()
            return redirect('gracias')
    else:
        form = RegistroForm()
    #return render(request, '/opt/python/current/app/registro/templates/registro/home.html', {'form': form})
    return render(request, 'registro/home.html', {'form': form})


def gracias(request):
    #return render(request, '/opt/python/current/app/registro/templates/registro/gracias.html')
    return render(request, 'registro/gracias.html')


def exportCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DB Silencio.csv"'
    writer = csv.writer(response)
    for x in Codigo.objects.all():
        writer.writerow([x.nombre, x.apellido, x.correo, x.celular])
    return response
