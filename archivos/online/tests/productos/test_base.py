import pytest
from productos.models import Producto
from django.contrib.auth.models import User
import datetime


@pytest.fixture()
def crear_producto():
    mi_producto = Producto(
        producto="Producto 4", fecha_publicacion=datetime.datetime.now()
    )
    mi_producto.save()
    return mi_producto


@pytest.mark.django_db
def test_cambiar_estado(crear_producto):
    print("Cambio de estado de producto")
    assert crear_producto.producto == "Producto 4"


@pytest.mark.django_db
def test_crear_producto():
    mi_producto = Producto(
        producto="Producto 3", fecha_publicacion=datetime.datetime.now()
    )
    mi_producto.save()
    print(mi_producto.producto)
    assert mi_producto.producto == "Producto 3"


@pytest.mark.django_db
def test_cambiar_estado(producto):
    print(producto.estado)
    print(producto.producto)
    assert producto.estado == "Borrador"
