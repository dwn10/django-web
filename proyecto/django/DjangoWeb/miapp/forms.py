from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': ' Introduce el titulo',
                'class': 'titulo_form_article'
            }
        )
    ),
    validators=[
        validators.MinLengthValidator(4, 'Título demasiado corto'),
        validators.RegexValidator('^[A-Za-z0-9]*$', 'Título mal formado', 'invalid_title')
    ]

    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea
    )

    content.widget.attrs.update({
        'placeholder': ' Introduce el contenido',
        'class': 'contenido_form_article',
        'id': 'contenido _form'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "Publicado?",
        choices = public_options
    )