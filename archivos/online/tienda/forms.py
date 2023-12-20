from django.forms import ModelForm
from productos.models import Producto



from django import forms

class SearchLibroForm(forms.Form):
    querycom = forms.CharField(label='Ingresar el nombre de libro a buscar', widget=forms.TextInput(attrs={'size': 32, 'class': 'form- control'}))





class CargarForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['producto', 'fecha_publicacion', 'imagen']

    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)