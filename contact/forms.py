from django import forms

class ContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='Your First Name', required=True)
	last_name = forms.CharField(label='Your Last Name', required=False)
	address = forms.CharField(label='Street Address', required=False)
	zipcode = forms.IntegerField(label='Zip Code', required=False)
	inquiry_type = forms.MultipleChoiceField(label='What types of services do you need?', choices=(('Pool Repair','Pool Repair'), ('Pool Cleaning Service', 'Pool Cleaning Service'), ('Other', 'Other')),
		widget = forms.CheckboxSelectMultiple(), required=True)
	phone = forms.CharField(label='Your Phone Number (optional)', required=False)
	email = forms.EmailField(label='Your Email Address', required=True)
	preferred_contact = forms.ChoiceField(label='Preferred contact', choices=(('email', 'email'), ('phone', 'phone')), required=False)
	availability = forms.MultipleChoiceField(label='When are you available?', choices=(('Evening', '4pm to 8pm'), ('Afternoon', 'noon to 4pm'), ('Morning', '8am to noon')),
		widget = forms.CheckboxSelectMultiple(), required=False)
	permission = forms.BooleanField(label="Do you want to know the 5 things your pool guy hasn't told you?", required=False, initial=True)
	subject = forms.CharField(label='Subject', initial='Request an estimate',required=False)
	message = forms.CharField(label='Extra information about your request (optional)', max_length=400, initial='Please provide any additional information about your needs.', required= False,
		widget = forms.Textarea())

class QuickContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='Your First Name', required=True)
	inquiry_type = forms.MultipleChoiceField(label='What types of service/s do you need?', choices=(('Pool Repair','Pool Repair'), ('Pool Cleaning Service', 'Pool Cleaning Service'), ('Other', 'Other')),
		widget = forms.CheckboxSelectMultiple(), required=True)
	email = forms.EmailField(label='Your Email Address', required=True)
	phone = forms.CharField(label='Your Phone Number (optional)', required=False)

class CouponForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='First Name', required=True)
	last_name = forms.CharField(label='Last Name', required=True)
	zipcode = forms.IntegerField(label='Zip Code', required=True)
	email = forms.EmailField(label='Email Address', required=True)
	phone = forms.CharField(label='Phone Number', required=True)
	permission = forms.BooleanField(label="Do you want to know the 5 things your bug guy hasn't told you?", required=False, initial=True)