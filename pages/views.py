from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "aboutus.html"

class VisionPageView(TemplateView):
    template_name = "vision.html"
    
class LeadershipPageView(TemplateView):
    template_name = "leadership.html"
    
class HistoryPageView(TemplateView):
    template_name = "history.html"

class ProductPageView(TemplateView):
    template_name = "product.html"
    
class ProductOnePageView(TemplateView):
    template_name = "product1.html"

class ProductTwoPageView(TemplateView):
    template_name = "product2.html"

class ProductThreePageView(TemplateView):
    template_name = "product3.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

