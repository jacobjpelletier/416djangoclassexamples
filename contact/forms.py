from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    '''
    this says for the model of this form, use model = contact
    if you want to select columns for forms, you can:
      fields = ['first_name', 'last_name']
    if you want to include all columns from model:
      fields = '__all__'
    '''
    class Meta:
        model = Contact
        # fields = ['first_name', 'last_name', 'email', 'message'] # individual fields can be included this way as well
        fields = '__all__'  # includes all the fields from the model
        # widget attrs arguments allows us to add attributes (e.g., your own styles, placeholder) to our form input tags
        widgets = {
            # NOTE: must have bootstrap in base template for these attrs to work
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }

        # don't forget, do not rely on client side validation
