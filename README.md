## 🧱 Xocolatl System

**Xocolatl System** es una aplicación web desarrollada con **Django**.
Este proyecto sirve como base para un sistema web modular, con una aplicación principal llamada `xocolatl_catalogo`.

---

## ⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

* Python 3.10+
* Django (versión recomendada: 5.1+)

Puedes verificar las versiones con:

```bash
python --version
python -m django --version
```

Si no tienes Django instalado, puedes hacerlo con:

```bash
pip install django
```

---

## 🗂️ Estructura del proyecto

```
Xocolatl_System/
│
├── xocolatl_system/               # Configuración principal del proyecto (settings, urls, etc.)
├── xocolatl_catalogo/             # Aplicación Django principal
│   ├── templates/xocolatl_catalogo/   # Archivos HTML (interfaces del sistema)
│   └── static/                        # Archivos estáticos (CSS, JS, imágenes)
├── manage.py                    # Archivo principal de ejecución
└── README.md                    # Este archivo
```

---


##  Cómo ejecutar el proyecto localmente

1️⃣ **Abre una terminal** y navega hasta la carpeta raíz del proyecto (donde está `manage.py`):

```bash
cd Xocolatl_System
```

2️⃣ **Ejecuta el servidor de desarrollo:**

```bash
python manage.py runserver
```

3️⃣ **Abre el navegador** y entra a:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

