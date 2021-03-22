
# make sure this is at the top if it isn't already 
from django import forms

# our new form

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    name = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True,max_length=50)
    subject = forms.CharField(required=True,max_length=100)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'cols':30, 'rows':8}),
        )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Your name"
        self.fields['email'].label = "Your email"
        self.fields['subject'].label = "Subject"
        self.fields['message'].label = "Write your message here!!"
