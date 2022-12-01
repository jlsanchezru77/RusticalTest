from django import forms


class UsuarioFormulario(forms.Form):
    Nombre=forms.CharField(max_length=40)
    Apellidos=forms.CharField(max_length=40)
    Edad=forms.IntegerField()

class CompraFormulario(forms.Form):
    Peso=forms.IntegerField()
    Unidades=forms.IntegerField()    


STATUS =(
    ("Compra", "Me interesa adquirir Orellanas"),
    ("Cultivo", "Me interesa cultivar Orellanas"),
)
  
# creating a form 
class InteresFormulario(forms.Form):
    Interes_ = forms.ChoiceField(choices = STATUS) 

    