from django import forms


class SubstituteSearchForm(forms.Form):
    product = forms.CharField(label='', 
                                max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control my-0 py-1 lime-border', 
                                        'placeholder': 'Recherche...',
                                        'name': 'search', 'type':'text'}))
