from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField , StreamField
from wagtail.core import  blocks
from wagtail.admin.edit_handlers import InlinePanel , FieldPanel , StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey

from wagtail.search import index



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


class BlogIndexPage(Page):

     def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context



class BlogPage(Page):

    def img_main(self):
        gallery_item = self.blogMainImage.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    




    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")    ),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    search_fields = Page.search_fields + [

        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('body'),
        InlinePanel('blogMainImage', label = "Blog Main image"),
    ]




class BlogPageMainImage(Orderable):
    page =ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='blogMainImage')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')

    panels = [
        ImageChooserPanel('image'),
    ]



class ContactPage(Page):

    pass


class DoctorsPage(Page):

    pass

class RadioPage(Page):
    pass


class EecpPage(Page):
    pass


class MenshealthPage(Page):
    pass


class IvsupplementsPage(Page):
    pass



class ProbioticsPage(Page):
    pass




