from django import forms
from .models import Videojuego

class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ['titulo', 'plataforma', 'precio', 'stock', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Ej: Elden Ring'
            }),
            'plataforma': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Ej: PS5, PC, Switch'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'min': '0.01',
                'step': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'min': '0'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Descripción breve del juego (opcional)',
                'rows': 3
            }),
        }

    # Validación personalizada para el título (mínimo 2 caracteres)
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if len(titulo) < 2:
            raise forms.ValidationError("El título debe tener al menos 2 caracteres.")
        return titulo

    # Validación personalizada para el precio (Mayor que cero)
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor mayor que cero.")
        return precio

    # Validación personalizada para el stock (No negativo)
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser un número negativo.")
        return stock
