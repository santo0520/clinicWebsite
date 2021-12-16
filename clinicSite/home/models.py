from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey



class HomePage(Page):
    def main_image(self):
        gallery_item = self.slider_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
    def img_slider1(self):
        gallery_item = self.sliderImage1.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
    content_panels = Page.content_panels + [
        InlinePanel('slider_images', label="Slider images"),
        InlinePanel('sliderImage1', label = "Slider image No.1"),

    ]


class HomePageGalleryImage(Orderable):
    page =ParentalKey(HomePage, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        ImageChooserPanel('image'),
    ]
class HomePageSliderImage1(Orderable):
    page =ParentalKey(HomePage, on_delete=models.CASCADE, related_name='sliderImage1')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        ImageChooserPanel('image'),
    ]
