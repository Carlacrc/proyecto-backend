# proyecto-backend

ENTORNO VIRTUAL

> python -m venv venv

[GIT]

VER RAMAS 
git branch -a

CREAR RAMA
git branch feature/NOMBRE_RAMA 

CAMBIARSE A LA RAMA CREADA
git checkout feature/NOMBRE_RAMA

REALIZAR EL MERGE (EN LA RAMA DE TRABAJO ACTUAL)
git merge master

ELIMINAR RAMA LOCAL
git branch -d 'NombreRama'

ELIMINAR RAMA REMOTA
git push origin --delete 'NombreRama'


COMANDOS
[+] Para iniciar un proyecto en Django: django-admin startproject 'nombreProyecto'
[+] Para iniciar nuestro projecto web: python manage.py runserver
[+] Para crear una App dentro de nuestro projecto: python manage.py startapp 'nombreApp'
[+] Para agregar una App a nuestro projecto Django ir a 'settings.py' -> Sección: INSTALLED_APPS -> Agregar " 'nombreApp', "
	[-] Para verificiar si nuestra App fue agregada: python manage.py check 'nombreApp'

[+] Creación de Base de Datos: python magane.py makemigrations
[+] Generar código de SQL para generar las tablas creadas en 'models.py': python manage.py sqlmigrate 'nombreApp' 'numeroMigración'
	[-] Número de migración  -> gestorPedidos\migrations\0001_initial.py
	[-] Ejemplo: python manage.py sqlmigrate 'nombreApp' '0001'

[+] Crear tablas en la base de datos: python manage.py migrate


BASE DE DATOS
[+] Iniciar shell de nuestro proyecto: python manage.py shell

[+] Manipulación de una tabla (dentro de la shell de python)
	[-] >> from 'nombreApp'.models import 'nombreTabla'
   [-] Insertar un registro dentro de la tabla seleccionada
	*Ejemplo de Articulos*
	[-] >> art=Articulos(nombre='mesa', categoria='decoración', precio=100)
	*Guardar datos*
	[-] >> art.save()

   [-] CREATE: crear un articulo
	[-] >> art2.Articulos.objects.create(nombre='auto', categoria='automovil', precio=200)
   [-] UPDATE: actualizar un articulo
	[-] >> art.precio=200
	[-] >> art.save()
   [-] DELETE: eliminar un articulo
	*Crear variable para guardar el articulo a eliminar*
	[-] >> artEli=Articulos.objecs.get(id=2)
	[-] >> artEli.delete()
   [-] SELECT: consultar una tabla de la db
	*Crear variable para guardar la consulta a realizar*
	[-] >> Lista=Articulos.objects.all()
	*Mostrar lista*
	[-] >> Lista
	[-] >> Lista.query.__str__()

PGADMIN (Postgresql)
[+] Crear una nueva db mediante consola:  Database -> postgres -> Click derecho ( Query Tool )
	[-] create database 'nombreDB' (Ejemplo 'ArticulosClientes') -> Click en RUN!!
	
[+] Conectar Proyecto Django a la base de datos (ArticulosClientes)
	*Instalar psycopg2 * -> *IMPORTANTE* situarse en la ruta donde esta creado el proyecto!!!!
	[-] 'ruta'\'nombreProyecto'> pip install psycopg2

   [-] Cambiando CFG para conectar la base de datos
	* En 'settings.py' editar*
	[-] DATABASES = {
    		'default': {
        			'ENGINE': 'django.db.backends.postgresql_psycopg2',
       			'NAME': 'nombreDB',
        			'USER': 'postgres',
        			'PASSWORD': 'contraseñaSQL',
        			'HOST': 'localhost',
        			'DATABASE_PORT': '5432',
    		}
	}
   [!] Para generar los cambios: python manage.py makemigrations
   [!] Luego realizar la migración: python manage.py migrate

[+] Agregar registros en la base de datos -> Clientes !!

[+] Realizar consultas SQL con clausulas (desde la consola)
	[-] > python manage.py shell
	[-] >> from gestorPedidos.models import Articulos
	*Filtrado por 1 sólo campo, es este caso será a categoria*
	[-] >> Articulos.objects.filter(categoria='decoración')

[!] Para que muestre de forma STR los valores filtrados anteriormente agregar en la Clase que queremos mostrar (models.py):
	[-] Ejemplo en Articulos:
	def __srt__(self):
        		return '[+]Nombre: %s \n [+]Categoria: %s \n [+]Precio: %s' %(self.nombre, self.categoria, self.precio) 

[!] *IMPORTANTE* si se realiza un cambio en models se debe realizar las migraciones nuevamente
	[-] > python manage.py makemigrations
	[-] > python manage.py migrate

[+] Algunas consultas directas en Django (python)
	[-] > python manage.py shell
	[-] >> from gestorPedidos.models import Articulos
	[-] >> Articulos.objects.filter(categoria='decoración', precio__gte=70) 
	[-] >> Articulos.objects.filter(categoria='decoración', precio__lte=200)
	[-] >> Articulos.objects.filter(precio__gte=300).order_by('precio') -> Ascendente
	[-] >> Articulos.objects.filter(precio__gte=300).order_by('-precio') -> Descendiente


PANEL DE ADMINISTRACION DJANGO

[+] Crear un SuperUsuario
	[-] > python manage.py createsuperuser
	*Seguir los pasos correspondientes*
	[!] IMPORTANTE: realizar un "pip install psycopg2==2.8.6" para solucionar el problema de logeo del panel de administración

[+] Manipulación de tablas 
	[!] Dirigirse al archivo 'admin.py' -> importar modelo de la App
	[-] Agregar: admin.site.register(Clientes) | admin.site.register(Articulos)  | admin.site.register(Pedidos) 

[+] Personalización de Panel de Administración
	*Archivo 'models.py'*
	[-] verbose_name -> Sirve para modificar el nombre que aparece en el panel de administración , pero no afecta a la tabla de la db| Se coloca como atributo en la columna a modificar.
	[-] blank -> True (Campo no obligatorio), False (No puede estar en blanco)  | Null -> True (Permite que sea nulo en la db)

	*Archivo 'admin.py'
	[-] Para añadir más columnas al panel
		[-] Crear una clase -> Ej: class ClientesAdmin(admin.ModelAdmin):
					list_display=("nombreColumna")
					search_fields=("nombreColumna") -> Esto permite filtrar en específico por columna, Ej: si se coloca "nombre" se podrá filrar sólo por nombres, si se trata de filtrar por dirección no aparecerá nada.
	[-] Agregar filtro -> list_filter=("nombreColumna",) 
	[-] Filtro de fechas -> date_hierarchy="fecha"

