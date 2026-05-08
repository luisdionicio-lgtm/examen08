# Gestor de Restaurante - Django REST Framework

## Descripción

Este proyecto es una API REST desarrollada con Django y Django REST Framework. Permite administrar los platos de un restaurante y registrar pedidos realizados por los clientes.

El sistema trabaja con dos entidades principales: Platos y Pedidos. Cada pedido puede estar relacionado con uno o más platos.

Importante: no se utiliza Django Admin como interfaz de gestión. Todo el CRUD se realiza mediante endpoints y se prueba con Postman o Thunder Client.

## Tecnologías usadas

- Python
- Django
- Django REST Framework
- SQLite
- Postman / Thunder Client
- Git y GitHub

## Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/luisdionicio-lgtm/examen08.git
cd examen08
Crear entorno virtual:

python -m venv venv
venv\Scripts\activate

Instalar dependencias:

pip install django djangorestframework django-filter

Ejecutar migraciones:

python manage.py makemigrations
python manage.py migrate

Levantar servidor:

python manage.py runserver

URL base:

http://127.0.0.1:8000/api/


##### EJEMPLOS REALIZADOS - EVIDENCIAS REALIZADAS





