# Proyecto de Tienda con Sistema de Autenticación y Avatares Personalizables

Este proyecto es una aplicación web en Django que permite a los usuarios registrarse, iniciar sesión y personalizar un avatar mediante la integración de **Ready Player Me**. La aplicación está dividida en dos módulos principales:

1. **usuarios**: Módulo que maneja el registro, inicio de sesión y cierre de sesión de los usuarios.
2. **avatar**: Módulo que permite a los usuarios crear y personalizar su avatar en 3D.

## Estructura del Proyecto

```
mi_proyecto/
├── avatar/
│   ├── migrations/
│   ├── templates/
│   │   └── avatar/
│   │       └── crear_avatar.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── usuarios/
│   ├── migrations/
│   ├── templates/
│   │   └── usuarios/
│   │       ├── iniciar_sesion.html
│   │       ├── registro.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── templates/
│   └── base.html
├── mi_proyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

## Instalación y Configuración

### Requisitos

- Python 3.12.6 o superior
- Django 5.1.3
- SQLite (o cualquier base de datos compatible con Django)

### Pasos de Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd mi_proyecto
   ```

2. **Crear un Entorno Virtual**

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instalar las Dependencias**

   ```bash
   pip install django
   ```

4. **Configurar la Base de Datos**

   Ejecuta las migraciones para configurar la base de datos:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Ejecutar el Servidor**

   ```bash
   python manage.py runserver
   ```

6. **Acceder a la Aplicación**

   Abre un navegador y navega a `http://127.0.0.1:8000`.

## Funcionalidades Principales

### Módulo `usuarios`

- **Registro de Usuarios**: Permite a los usuarios crear una cuenta mediante un formulario personalizado.
- **Inicio de Sesión y Cierre de Sesión**: Los usuarios pueden iniciar sesión y cerrar sesión en la aplicación.

### Módulo `avatar`

- **Personalización del Avatar**: Los usuarios pueden crear y personalizar su avatar utilizando **Ready Player Me**. 
- **Guardar URL del Avatar**: La URL del avatar se almacena en la base de datos y se puede recuperar y visualizar.

## Configuración del Avatar

### Integración con Ready Player Me

La aplicación está configurada para interactuar con el creador de avatares de Ready Player Me mediante un iframe. Cuando el usuario finaliza la creación del avatar, el enlace del avatar se guarda en la base de datos.

1. **Abrir el Creador de Avatar**: Al hacer clic en "Iniciar Avatar Creator", el iframe se muestra y permite al usuario personalizar el avatar.
2. **Guardar el Avatar**: La URL del avatar es recibida mediante un mensaje postMessage desde el iframe y se guarda en la base de datos del usuario autenticado.

## Estructura de Base de Datos

### App `usuarios`

**Modelo `Perfil`**:
- **usuario**: Relación uno a uno con el modelo `User` de Django.

### App `avatar`

**Modelo `Avatar`**:
- **usuario**: Relación uno a uno con el modelo `User`.
- **avatar_url**: URL del avatar personalizado generado por Ready Player Me.

## Señales de Django

Las señales `post_save` se utilizan en el modelo `Perfil` en `usuarios/models.py` para crear automáticamente un perfil cuando un nuevo usuario se registra. Esto asegura que cada usuario tenga un perfil asociado.

## Archivos Clave

- **base.html**: Plantilla base que incluye Bootstrap para el diseño de interfaz en colores oscuros.
- **registro.html** y **iniciar_sesion.html**: Formularios de registro e inicio de sesión para la autenticación.
- **crear_avatar.html**: Página que permite al usuario iniciar el creador de avatar y guardar la URL del avatar.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor crea un "fork" y envía un "pull request".

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
