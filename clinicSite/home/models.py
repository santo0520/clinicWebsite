from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey



class HomePage(Page):

    def img_slider1(self):
        gallery_item = self.sliderImage1.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
    def img_slider2(self):
        gallery_item = self.sliderImage2.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
    def img_slider3(self):
        gallery_item = self.sliderImage3.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
    content_panels = Page.content_panels + [

        InlinePanel('sliderImage1', label = "Slider image No.1"),
        InlinePanel('sliderImage2', label = "Slider image No.2"),
        InlinePanel('sliderImage3', label = "Slider image No.3"),


    ]


class HomePageSliderImage1(Orderable):
    page =ParentalKey(HomePage, on_delete=models.CASCADE, related_name='sliderImage1')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        ImageChooserPanel('image'),
    ]

class HomePageSliderImage2(Orderable):
    page =ParentalKey(HomePage, on_delete=models.CASCADE, related_name='sliderImage2')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        ImageChooserPanel('image'),
    ]

class HomePageSliderImage3(Orderable):
    page =ParentalKey(HomePage, on_delete=models.CASCADE, related_name='sliderImage3')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        ImageChooserPanel('image'),
    ]







class AboutPage(Page):
    def img_slider1(self):
        gallery_item = self.sliderImage1.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [

        InlinePanel('sliderImage1', label = "Slider image No.1"),

    ]


class AboutPageSliderImage1(Orderable):
    page =ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='sliderImage1')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        ImageChooserPanel('image'),
    ]



class DepartmentsPage(Page):

    pass


class AppointmentPage(Page):

    pass


class BlogPage(Page):

    pass


class ContactPage(Page):

    pass


class DoctorsPage(Page):

    pass

