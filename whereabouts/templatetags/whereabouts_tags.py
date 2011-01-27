from django import template

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from whereabouts.models import SocialNetworkProfile


register = template.Library()


class Whereabouts(template.Node):
    def __init__(self, content_object, var_name):
        self.content_object = template.Variable(content_object)
        self.var_name = var_name
        
    def render(self, context):
        object_instance = self.content_object.resolve(context)
        content_type = ContentType.objects.get_for_model(object_instance)
        whereabouts = SocialNetworkProfile.objects.filter(
            content_type=content_type,
            object_id=object_instance.id
        )
        context[self.var_name] = whereabouts
        return ""


@register.tag
def get_whereabouts(parser, token):
    """
    Get an object's (user, group, site) whereabouts online.
    
    Returns a list of :model:`whereabouts.SocialNetworkProfile`
    
    Syntax::
        {% get_whereabouts [object] as [var_name] %}
        
    Example usage::
        {% get_whereabouts request.user as whereabouts %}
    """
    args = token.split_contents()
    
    var_name = args[-1]
    content_object = args[1]
    
    return Whereabouts(content_object, var_name)