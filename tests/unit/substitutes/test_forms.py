from django.test import TestCase


from substitutes.forms import SubstituteSearchForm

class SubstituteSearchFormTest(TestCase):
    
    def test_renew_form_date_field_label(self):
        form = SubstituteSearchForm()
        self.assertTrue(form.fields['product'].label == '')
    
    
    