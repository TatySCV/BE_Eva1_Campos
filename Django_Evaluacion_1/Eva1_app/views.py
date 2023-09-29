from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'view/index.html')

def usuario(request):
    data = {"titulo":"Usuario"}
    return render(request, 'view/usuario.html', data)
def libros(request):
    data = {"titulo":"Libros", "foto1":"after.jpg", "foto2":"ciudadesdehumo.jpg", "foto3":"damian.jpg", "foto4":"divergente.jpg", "producto1":"After", "producto2":"Ciudades", "producto3":"Damián", "producto4":"Divergente"}
    return render(request, 'view/producto.html', data)
def canciones(request):
    data = {"titulo":"Canciones", "foto1":"", "foto2":"", "foto3":"", "foto4":"", "producto1":"", "producto2":"", "producto3":"", "producto4":""}
    return render(request, 'view/producto.html', data)
def peliculas(request):
    data = {"titulo":"Películas", "foto1":"", "foto2":"", "foto3":"", "foto4":"", "producto1":"", "producto2":"", "producto3":"", "producto4":""}
    return render(request, 'view/producto.html', data)

def After(request):
    data = {"producto":"After", "imagen":"after.jpg", "descripcion":"Tessa Young acaba de llegar a la universidad, y su estable y ordenada vida da un giro busco al conocer al misterioso Hardin Scott, cuyo pasado es algo oscuro. Aunque de entrada se odian, estos polos opuestos se unirán y nada volverá a ser como antes. Tendrán que enfrentarse amultiples pruebas como la inocencia y el descubrimiento sexual, para poder estar juntos."}
    return render(request, 'view/descripcion.html', data)
def Ciudades(request):
    data = {"producto":"Ciudades", "imagen":"ciudadesdehumo.jpg", "descripcion":"La vida de Alice está a punto de cambiar. Su rutina, que tiene medida al milímetro, y su naturaleza, es un androide, conlleva una reclusión que hoy va a terminar, pero el mundo en el que habita, no es el nuestro, sino uno muy distinto donde androides y humanos están forzados a convivir."}
    return render(request, 'view/descripcion.html', data)
def Damián(request):
    data = {"producto":"Damián", "imagen":"damian.jpg", "descripcion":"Padme ha vivido durante toda su vida en el pueblo de Asfil. Es una chica normal, buena. O eso parece. En el fondo tiene varios secretos, y uno de ellos se llama Damián. Es su peculiar vecino, que siempre le dio la impresión de estar ocultando algo y a quien ella trató de descifrar sin éxito."}
    return render(request, 'view/descripcion.html', data)
def Divergente(request):
    data = {"producto":"Divergente", "imagen":"divergente.jpg", "descripcion":"En una sociedad futura, la gente se divide en facciones según sus virtudes personales. Después de que la joven Tris sea declarada 'divergente' y, por tanto, nunca encajará en ningún grupo, ella descubre un complot para destruir a quienes son como ella."}
    return render(request, 'view/descripcion.html', data)
