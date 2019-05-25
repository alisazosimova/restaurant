from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from app.core.models import MenuItem
from app.core.models import Image


class Index(TemplateView):
    """
    Display index.html page
    """

    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.filter(is_available=True)
        menu_items_images = Image.objects.filter(menu_item_id__is_available=True)
        # import ipdb; ipdb.set_trace()
        context = {
            'menu_items': menu_items,
            'menu_items_images': menu_items_images,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        return redirect('thanks')
