from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from cmsaloha.models import AlohaFieldPlugin

class AlohaPlugin(CMSPluginBase):
    model = AlohaFieldPlugin
    name = 'aloha text area'
    render_template = 'cmsaloha/aloha.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.body,
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(AlohaPlugin)
