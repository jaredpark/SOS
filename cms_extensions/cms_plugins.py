from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

class CMSYelpPlugin(CMSPluginBase):
	name = _("Yelp Plugin")  # Name of the plugin
	render_template = "cms_extensions/yelp_plugin.html"  # template to render the plugin with

	def render(self, context, instance, placeholder):
		request = context['request']
		context.update({
			'instance': instance,
			'placeholder': placeholder,
			})
		return context

plugin_pool.register_plugin(CMSYelpPlugin)
