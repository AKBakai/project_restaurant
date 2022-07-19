from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe

from abouts.models import AboutUs, WhyChoiceUs, Chef

@register(AboutUs)
class AboutUsAdmin(ModelAdmin):
    list_display = ('title', 'content', 'image')

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" heigth="110">')

    get_image.short_description = "Image"


@register(WhyChoiceUs)
class WhyChoiceUsAdmin(ModelAdmin):
    list_display = ('title', 'content')


@register(Chef)
class ChefAdmin(ModelAdmin):
    list_display = ('name', 'subtitle', 'bio', 'image')

    read_only = (
        'get_image',
    )

    def get_image(self, obj):
        return mark_safe(f'<img src= {obj.image.url} width="100" heigth="110">')

    get_image.short_description = "Image"
