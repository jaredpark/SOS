from django import forms

class ContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='First Name', required=True)
	last_name = forms.CharField(label='Last Name', required=True)
	address = forms.CharField(label='Street Address', required=False)
	zipcode = forms.IntegerField(label='Zip Code', required=True)
	inquiry_type = forms.MultipleChoiceField(label='What types of services do you need?', choices=(('Pest Control','General Pest Control'), ('Weed Control', 'Weed Control'), ('Termite Care','Termites'), ('Scorpion Removal', 'Scorpions')),
		widget = forms.CheckboxSelectMultiple(), required=True)
	property_type = forms.ChoiceField(label='Property Type', required=False, choices=(('residential', 'residential'),('commercial', 'commercial'), ('residential multi-family','residential multi-family')))
	square_footage = forms.CharField(label='Approximate Property Size (sq feet or acreage)', required=False)
	phone = forms.CharField(label='Phone Number', required=False)
	email = forms.EmailField(label='Email Address', required=True)
	preferred_contact = forms.ChoiceField(label='Preferred contact', choices=(('email', 'email'), ('phone', 'phone')), required=False)
	availability = forms.MultipleChoiceField(label='When are you available?', choices=(('Evening', '4pm to 8pm'), ('Afternoon', 'noon to 4pm'), ('Morning', '8am to noon')),
		widget = forms.CheckboxSelectMultiple(), required=False)
	permission = forms.BooleanField(label="Do you want to know the 5 things your bug guy hasn't told you?", required=False, initial=True)
	subject = forms.CharField(label='Subject', initial='Request an estimate',required=False)
	message = forms.CharField(label='Message', max_length=400, initial='Please provide any additional information about your needs.', required= False,
		widget = forms.Textarea())

class QuickContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='First Name', required=True)
	last_name = forms.CharField(label='Last Name', required=True)
	zipcode = forms.IntegerField(label='Zip Code', required=True)
	inquiry_type = forms.ChoiceField(label='What type of service?', choices=(('Pest Control','General Pest Control'), ('Weed Control', 'Weed Control'), ('Termite Care','Termites'), ('Scorpion Removal', 'Scorpions')), required = True,
		widget = forms.Select())
	email = forms.EmailField(label='Email Address', required=True)