from django import template
from django.conf import settings

from django.contrib.contenttypes.models import ContentType

from whereabouts.models import SocialNetworkWidget, SocialNetworkProfile


register = template.Library()

class WidgetNode(template.Node):
    def __init__(self, content_object, widget_slug):
        self.content_object = template.Variable(content_object)
        self.widget_slug = widget_slug
    
    def render(self, context):
        try:
            object_instance = self.content_object.resolve(context)
            content_type = ContentType.objects.get_for_model(object_instance)
            
            widget = SocialNetworkWidget.objects.get(slug=self.widget_slug)
            profile = SocialNetworkProfile.objects.get(
                content_type=content_type,
                object_id=object_instance.id,
                network=widget.network
            )
            
            context_dict = {}
            context_dict["profile"] = profile
            
            if widget.api_key_setting:
                context_dict["api_key"] = getattr(
                    settings,
                    widget.api_key_setting
                )
            
            t = template.Template(widget.widget_template)
            c = template.Context(context_dict)
            
            return t.render(c)
        except:
            return ""


@register.tag
def whereabouts_widget(parser, token):
    args = token.split_contents()
    
    content_object = args[1]
    widget_slug = args[2]
    
    return WidgetNode(content_object, widget_slug)