# 🍷 Entrecopas

Sistema de gestión para una vinoteca desarrollado con **Django**, como trabajo práctico evaluativo de la materia Ingeniería de Software.

---

# 📖 Propósito del proyecto

Entrecopas es una aplicación web que permite administrar una vinoteca mediante una interfaz intuitiva y un panel de administración.

El sistema permite:

* Gestión de vinos.
* Gestión de bodegas.
* Clasificación de vinos por categorías.
* Registro e inicio de sesión de usuarios.
* Administración de permisos mediante grupos.
* Carga y visualización de imágenes.
* Acceso a funcionalidades protegidas según el rol del usuario.

El proyecto fue desarrollado utilizando el framework **Django** y aplicando conceptos de:

* Modelos y relaciones.
* Usuario personalizado.
* CRUDs.
* Templates.
* Context Processors.
* Permisos y grupos.
* Panel de administración.
* Archivos estáticos y multimedia.

---

# 🚀 Instalación y ejecución

## 1. Clonar el repositorio (SSH)

```bash
git clone git@github.com:sgaray512/entrecopas.git
cd entrecopas
```

## 2. Crear entorno virtual

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Instalar dependencias

```bash
pip install django pillow
```

## 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

## 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Luego acceder desde el navegador a:

```text
http://127.0.0.1:8000/
```

---

# 🏗️ Estructura del proyecto

```text
entrecopas/
│
├── entreCopas/
│   ├── settings.py
│   ├── urls.py
│   └── context_processors.py
│
├── pedidos/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── usuarios/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── vinoteca/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── urls.py
│
├── templates/
│   ├── login.html
│   └── register.html
│
├── static/
│
├── media/
│
├── manage.py
│
└── README.md
```

---

# 📸 Capturas del sistema

## Login

<img width="1851" height="1004" alt="Login" src="https://github.com/user-attachments/assets/8da1004f-2c5b-4de2-80ee-08aef42e520b" />

---

## Home

<img width="1851" height="1004" alt="Home" src="https://github.com/user-attachments/assets/5bacd257-3795-4a40-9463-2a8e1bab84ec" />

---

## Vinos

<img width="1851" height="1004" alt="vinos" src="https://github.com/user-attachments/assets/ff0e5fe6-f6b2-4ef4-b5a9-acbab845f1a2" />

---

## Detalle de vino

<img width="1851" height="1004" alt="detalle_vino" src="https://github.com/user-attachments/assets/1be35bce-f3b1-4270-839c-2e552062a6d5" />

---

## Bodegas

<img width="1851" height="1004" alt="bodegas" src="https://github.com/user-attachments/assets/52c476c6-a668-4d89-80b4-a14fff021470" />

---

## Detalle de bodega

<img width="1851" height="1004" alt="detalle_bodega" src="https://github.com/user-attachments/assets/904222f5-7ef5-4775-90f3-37bf98e61ad6" />

---

# 👥 Integrantes

* Matías Ibarra
* Santiago Garay

---

# 🛠️ Tecnologías utilizadas

* Python 3
* Django
* SQLite3
* HTML
* CSS
* GitHub

```
```
