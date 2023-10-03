from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'view/index.html')

def usuario(request):
    data = {"id": "20.733.436-7", "nombre": "Tatiana Campos", "correo": "tatiana.campos03@inacapmail.cl"}
    return render(request, 'view/usuario.html', data)

def libros(request):
    data = {"titulo":"Libros", "foto1":"libros/after.jpg", "foto2":"libros/ciudadesdehumo.jpg", "foto3":"libros/damian.jpg", "foto4":"libros/divergente.jpg", "producto1":"After", "producto2":"Ciudades", "producto3":"Damián", "producto4":"Divergente"}
    return render(request, 'view/producto.html', data)
def canciones(request):
    data = {"titulo":"Canciones", "foto1":"canciones/ferxxo.jpg", "foto2":"canciones/feo.png", "foto3":"canciones/baby.jpg", "foto4":"canciones/vagabundo.jpeg", "producto1":"Ferxxo", "producto2":"Feo", "producto3":"Baby", "producto4":"Vagabundo"}
    return render(request, 'view/producto.html', data)
def peliculas(request):
    data = {"titulo":"Películas", "foto1":"peliculas/elementos.jpeg", "foto2":"peliculas/encantada.jpeg", "foto3":"peliculas/spiderman.jpg", "foto4":"peliculas/thor.jpg", "producto1":"Elementos", "producto2":"Encantada", "producto3":"SpiderMan", "producto4":"Thor"}
    return render(request, 'view/producto.html', data)

def After(request):
    data = {"producto":"After", "imagen":"libros/after.jpg", "descripcion":"Tessa Young acaba de llegar a la universidad, y su estable y ordenada vida da un giro busco al conocer al misterioso Hardin Scott, cuyo pasado es algo oscuro. Aunque de entrada se odian, estos polos opuestos se unirán y nada volverá a ser como antes. Tendrán que enfrentarse amultiples pruebas como la inocencia y el descubrimiento sexual, para poder estar juntos."}
    return render(request, 'view/descripcion.html', data)
def Ciudades(request):
    data = {"producto":"Ciudades", "imagen":"libros/ciudadesdehumo.jpg", "descripcion":"La vida de Alice está a punto de cambiar. Su rutina, que tiene medida al milímetro, y su naturaleza, es un androide, conlleva una reclusión que hoy va a terminar, pero el mundo en el que habita, no es el nuestro, sino uno muy distinto donde androides y humanos están forzados a convivir."}
    return render(request, 'view/descripcion.html', data)
def Damián(request):
    data = {"producto":"Damián", "imagen":"libros/damian.jpg", "descripcion":"Padme ha vivido durante toda su vida en el pueblo de Asfil. Es una chica normal, buena. O eso parece. En el fondo tiene varios secretos, y uno de ellos se llama Damián. Es su peculiar vecino, que siempre le dio la impresión de estar ocultando algo y a quien ella trató de descifrar sin éxito."}
    return render(request, 'view/descripcion.html', data)
def Divergente(request):
    data = {"producto":"Divergente", "imagen":"libros/divergente.jpg", "descripcion":"En una sociedad futura, la gente se divide en facciones según sus virtudes personales. Después de que la joven Tris sea declarada 'divergente' y, por tanto, nunca encajará en ningún grupo, ella descubre un complot para destruir a quienes son como ella."}
    return render(request, 'view/descripcion.html', data)

def Baby(request):
    data = {"producto":"Baby", "imagen":"canciones/baby.jpg", "descripcion":"«Baby» es una canción interpretada por el cantante canadiense Justin Bieber y el rapero estadounidense Ludacris, lanzada originalmente como el primer sencillo de su segundo álbum de estudio, My World 2.0 (2010). Fue escrita por Christopher 'Tricky' Stewart y Terius 'The-Dream' Nash, quienes ya habían trabajado con Bieber en el tema «One Time» y también con la cantante Christina Milian y el rapero Ludacris."}
    return render(request, 'view/descripcion.html', data)
def Feo(request):
    data = {"producto":"Feo", "imagen":"canciones/feo.png", "descripcion":"La canción 'Feo' de Morat cuenta la historia de una persona que se siente atraída por alguien a quien considera increíblemente hermoso/a, al mismo tiempo que reconoce sus propias imperfecciones físicas. Las letras expresan los pensamientos y sentimientos internos del narrador mientras observa a la persona que le atrae."}
    return render(request, 'view/descripcion.html', data)
def Ferxxo(request):
    data = {"producto":"Ferxxo", "imagen":"canciones/ferxxo.jpg", "descripcion":"«Ferxxo 100» es una canción que fue grabada e interpretada por el cantautor colombiano Feid. Fue lanzado el jueves 2 de junio de 2022 a través de Universal Music Latino, como tercer sencillo de su sexto álbum de estudio, Feliz cumpleaños, Ferxxo, te pirateamos el álbum (2022). Su significado es que es su canción número 100 que Feid ha escrito como artista."}
    return render(request, 'view/descripcion.html', data)
def Vagabundo(request):
    data = {"producto":"Vagabundo", "imagen":"canciones/vagabundo.jpeg", "descripcion":"«Vagabundo» es una canción interpretada por los cantantes colombianos Sebastián Yatra, Manuel Turizo y Beéle. Fue publicada el 11 de mayo de 2023 a través de Universal Music Latino. La canción es un homenaje de los artistas a los ritmos tradicionales como el merengue que es característico de su país natal."}
    return render(request, 'view/descripcion.html', data)

def Elementos(request):
    data = {"producto":"Elementos", "imagen":"peliculas/elementos.jpeg", "descripcion":"Elemental (titulada Elementos en Hispanoamérica) es una película de fantasía romántica animada por computadora estadounidense producida por Walt Disney Pictures y Pixar Animation Studios y distribuida por Walt Disney Studios Motion Pictures. Dirigida por Peter Sohn y producida por Denise Ream y Ricardo Arnaiz a partir de un guion de Brenda Hsueh, cuenta con Leah Lewis y Mamoudou Athie en los papeles principales de voz. La película describe el vínculo entre Ember (Lewis), un elemento fuego, y Wade (Athie), que no pueden tocarse; pero descubre cuánto tienen en común."}
    return render(request, 'view/descripcion.html', data)
def Encantada(request):
    data = {"producto":"Encantada", "imagen":"peliculas/encantada.jpeg", "descripcion":"Giselle, la princesa de un cuento de hadas, es desterrada por una reina malvada y termina en el Manhattan moderno, en donde la música, la magia y los finales felices no son muy frecuentes. Giselle se siente extraña en su nuevo mundo, hasta que un abogado divorciado llega para ayudarla. Giselle empieza a enamorarse de su benefactor, pero el romance de su libro de cuentos se complica más cuando un príncipe de su mundo llega a rescatarla."}
    return render(request, 'view/descripcion.html', data)
def SpiderMan(request):
    data = {"producto":"SpiderMan", "imagen":"peliculas/spiderman.jpg", "descripcion":"Tras descubrirse la identidad secreta de Peter Parker como Spider-Man, la vida del joven se vuelve una locura. Peter le pide ayuda al Doctor Strange para recuperar su vida, pero algo sale mal y provoca una fractura en el multiverso."}
    return render(request, 'view/descripcion.html', data)
def Thor(request):
    data = {"producto":"Thro", "imagen":"peliculas/thor.jpg", "descripcion":"Tras desatar una antigua guerra, el codicioso guerrero Thor es desterrado a la Tierra por su padre para que viva entre los hombres y descubra así el verdadero sentido de la humildad. Allí, sin sus poderes, Thor deberá enfrentarse a las fuerzas más oscuras que su mayor enemigo le enviará desde Asgard."}
    return render(request, 'view/descripcion.html', data)
