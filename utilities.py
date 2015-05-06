from context_processors import site_settings_processor
from django.core.mail import send_mail, EmailMessage
import datetime, os

from contact.forms import ContactForm

is_production = os.environ.get('IS_PRODUCTION')

def admin_name():
    return site_settings_processor(None)['admin_name']

def ContactFormProcessor(request, context_dictionary):
	context_dictionary['first_name_placeholder'] = 'First Name'
	context_dictionary['email_placeholder'] = 'Email Address'
	context_dictionary['phone_placeholder'] = 'Phone Number (optional)'
	context_dictionary['message_placeholder'] = 'Extra Information (optional)'
	context_dictionary['first_name_value']=context_dictionary['email_value']=context_dictionary['phone_value']=context_dictionary['message_value'] = ''
	context_dictionary['error_fields'] = []
	if request.method == 'POST':
		if 'contact' in request.POST:
			# create a form instance and populate it with data from the request:
			contact_form = ContactForm(request.POST)
			# check whether it's valid:
			if contact_form.is_valid():
				first_name = contact_form.cleaned_data['first_name']
				phone = contact_form.cleaned_data['phone']
				sender = contact_form.cleaned_data['email']
				inquiry_type = contact_form.cleaned_data['inquiry_type']
				message_body = contact_form.cleaned_data['message']
				recipients = [site_settings_processor(request)['site_email'],]
				# from_email = site_settings_processor(request)['site_email']
				from_email = sender
				header = 'First name,' + 'CF[Inquiry Type],' + 'Main Phone,' + 'Email,' + 'CF[Message]\n'
				fullemail = header + first_name + "," + ' - '.join(inquiry_type) + "," + phone + "," + sender + "," + message_body
				time_stamp = str(datetime.datetime.now())
				# email_object = EmailMessage(subject = 'Website Contact Form', body = message_body, from_email = from_email, to = recipients, attachments = [(time_stamp+'.txt',fullemail,),])
				email_object = EmailMessage(subject = 'Website Contact Form', body = fullemail, from_email = from_email, to = recipients, attachments = [(time_stamp+'.txt',fullemail,),])
				email_object.send()
				context_dictionary['first_name'] = first_name
			else:
				context_dictionary['contact_form'] = contact_form
				for field in contact_form:
					context_dictionary[field.name + "_value"] = contact_form[field.name].value
				for field in contact_form.errors:
					error_message = contact_form.errors[field][0]
					context_dictionary[field + "_placeholder"] = error_message
					context_dictionary['error_fields'].append(field)
		else:
			pass
	else:
		contact_form = ContactForm()
		context_dictionary['contact_form'] = contact_form

from django.db.models import ImageField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContentTypeRestrictedImageField(ImageField):
	"""
	Same as ImageField, but you can specify:
	* content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
	* max_upload_size - a number indicating the maximum file size allowed for upload.
	2.5MB - 2621440
	5MB - 5242880
	10MB - 10485760
	20MB - 20971520
	50MB - 5242880
	100MB 104857600
	250MB - 214958080
	500MB - 429916160
	"""
	def __init__(self, *args, **kwargs):
		# self.content_types = kwargs.pop("content_types")
		self.max_upload_size = kwargs.pop("max_upload_size")
		super(ContentTypeRestrictedImageField, self).__init__(*args, **kwargs)
	def clean(self, *args, **kwargs):        
		data = super(ContentTypeRestrictedImageField, self).clean(*args, **kwargs)
		file = data.file
		try:
			# content_type = file.content_type
			# if content_type in self.content_types:
				if file._size > self.max_upload_size:
					raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
			# else:
				# raise forms.ValidationError(_('Filetype not supported.'))
		except AttributeError:
			pass        

		return data

from south.modelsinspector import add_introspection_rules
add_introspection_rules([
	(
		[ContentTypeRestrictedImageField], # Class(es) these apply to
		[],         # Positional arguments (not used)
		{           # Keyword argument
			"max_upload_size": ["max_upload_size", {}],
		},
	),
	], ["^utilities\.ContentTypeRestrictedImageField"])
