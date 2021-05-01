from django import forms

class DocumentTypeForm(forms.Form):
    id = forms.CharField(max_length=2, required=True, label="Id",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Id",
                'class': 'form-control',
            }
        ))
    name = forms.CharField(max_length=80, required=True, label="Nombre",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nombre",
                'class': 'form-control',
            }
        ))
    active = forms.CheckboxInput()

class ThirdForm(forms.Form):
    def __init__(self, *args, document_types_choices=(), **kwargs):
        super(ThirdForm, self).__init__(*args, **kwargs)
        self.fields['document_type'].choices = document_types_choices
    
    identification = forms.CharField(max_length=20, required=True, label="Identificación",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Identificación",
                'class': 'form-control',
            }
        ))

    first_name = forms.CharField(max_length=100, required=True, label="Nombres",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Nombres",
                'class': 'form-control',
            }
        ))

    last_name = forms.CharField(max_length=100, required=False, label="Apellidos",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Apellidos",
                'class': 'form-control',
            }
        ))
    
    phone = forms.CharField(max_length=50, required=True, label="Teléfono",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Teléfono",
                'class': 'form-control',
            }
        ))

    address = forms.CharField(max_length=200, required=False, label="Dirección",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Dirección",
                'class': 'form-control',
            }
        ))

    birthday = forms.DateField( required=False, label="Fecha de Nacimiento",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Fecha de Nacimiento",
                'class': 'form-control',
            }
        ))

    document_type = forms.ChoiceField(
        required=True,
        label="Tipo Documento",
        widget=forms.Select(attrs={
            'class': 'form-control',
        }))


