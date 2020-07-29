from django import forms

class SubstituteSearchForm(forms.Form):
    product = forms.CharField(label='', max_length=100,
                                    widget=forms.TextInput(
                                        attrs={'class': 'search-product', 'placeholder': 'Recherche...',
                                        'name': 'search'}
                                    ))
