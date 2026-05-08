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
## 📌 Crear Plato (POST)
![](./pruebas/POST.png)
## 📌 JSON de creación de Plato
![](./pruebas/json.png)

## 📌 Segundo JSON / detalle de Plato
![](./pruebas/json2.png)

## 📌 Listado general de Platos (GET)
![](./pruebas/GET.png)

## 📌 JSON listado de Platos
![](./pruebas/json_platos.png)

## 📌 Vista visual de Platos
![](./pruebas/platos.png)

## 📌 Búsqueda de Plato por nombre
![](./pruebas/lomo_nombre.png)

## 📌 Búsqueda de Plato por categoría
![](./pruebas/categoria.png)

## 📌 Actualización de Plato
![](./pruebas/actualizar_plato.png)

## 📌 Eliminación de Plato
![](./pruebas/delete.png)

## 📌 Resultado eliminación de Plato
![](./pruebas/delete_visual_json.png)

## 📌 Crear Pedido (POST)
![](./pruebas/POST_crear_pedido.png)

## 📌 JSON creación de Pedido
![](./pruebas/json_pedidos.png)

## 📌 Listado general de Pedidos (GET)
![](./pruebas/GET_Listar_pedidos.png)

## 📌 JSON listado de Pedidos
![](./pruebas/pedidos_json.png)

## 📌 GET adicional de Pedidos
![](./pruebas/get_.png)

## 📌 Búsqueda de Pedido por estado
![](./pruebas/pendiente.png)

## 📌 Búsqueda de Pedido por plato
![](./pruebas/Busqueda_pedido.png)

## 📌 Búsqueda de Pedido por categoría
![](./pruebas/Busqueda_bebida.png)

## 📌 Actualización de Pedido
![](./pruebas/PUT_Actualizar_pedido.png)

## 📌 Eliminación de Pedido
![](./pruebas/DELETE_pedido1.png)

## 📌 Pedido eliminado visualmente
![](./pruebas/pedido_eliminado.png)

## 📌 Resultado final de eliminación de Pedido
![](./pruebas/resultado_pedido_eliminado.png)