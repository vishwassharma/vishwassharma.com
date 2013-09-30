from copy import deepcopy
from django.contrib import admin
from django import forms
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "choose_template")


class TemplateForm(forms.ModelForm):
    MY_CHOICES = (
        (1, 'Without Images'),
        (2, 'With Big Image'),
        (3, 'With Side Image'),
        (4, 'Tweet and Comment Template'),
    )

    choose_template = forms.ChoiceField(choices=MY_CHOICES)

    class Meta:
        model = BlogPost

class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets
    form = TemplateForm

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)