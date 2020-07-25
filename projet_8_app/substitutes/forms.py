from django import forms

class SubstituteSearchForm(forms.Form):
    text = forms.CharField(label='Nom du produit', max_length=50,
                                    widget=forms.TextInput(
                                        attrs={'class': 'search-product', 'placeholder': 'Produit',
                                        'name': 'search'}
                                    ))
