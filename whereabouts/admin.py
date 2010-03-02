from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from whereabouts.models import SocialNetwork, SocialNetworkProfile, SocialNetworkWidget

WHEREABOUTS_CONTENT_TYPES = getattr(settings, 'WHEREABOUTS_CONTENT_TYPES', ['user', 'site', 'group'])

class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_icon_image_source',)

class SocialNetworkProfileAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'network')
    radio_fields = {'content_type': admin.HORIZONTAL}
    
    def get_form(self, request, obj=None):
        form = super(SocialNetworkProfileAdmin, self).get_form(request, obj)
        form.base_fields["content_type"].queryset = ContentType.objects.filter(name__in=WHEREABOUTS_CONTENT_TYPES)
        return form

admin.site.register(SocialNetwork, SocialNetworkAdmin)
admin.site.register(SocialNetworkProfile, SocialNetworkProfileAdmin)
admin.site.register(SocialNetworkWidget)