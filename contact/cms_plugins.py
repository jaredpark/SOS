from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from contact.forms import ContactForm, QuickContactForm

class CMSContactPlugin(CMSPluginBase):
	name = _("Contact Plugin")  # Name of the plugin
	render_template = "contact/contact_plugin.html"  # template to render the plugin with

	def render(self, context, instance, placeholder):
		request = context['request']
		context.update({
			'instance': instance,
			'placeholder': placeholder,
			'contact_form': ContactForm(),
			})
		return context

class CMSQuickContactPlugin(CMSPluginBase):
    name = _("Quick Contact Plugin")  # Name of the plugin
    render_template = "contact/quick_contact_plugin.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        request = context['request']
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'quick_contact_form': QuickContactForm(),
            })
        return context

plugin_pool.register_plugin(CMSQuickContactPlugin)
plugin_pool.register_plugin(CMSContactPlugin)  # register the plugin
