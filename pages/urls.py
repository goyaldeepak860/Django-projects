from django.urls import path
from .views import HomePageView, AboutPageView, VisionPageView, LeadershipPageView, HistoryPageView, ProductPageView, ProductTwoPageView, ProductOnePageView, ProductThreePageView, ContactPageView 

urlpatterns = [
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("product3/", ProductThreePageView.as_view(), name="product3"),
    path("product2/", ProductTwoPageView.as_view(), name="product2"),
    path("product1/", ProductOnePageView.as_view(), name="product1"),
    path("product/", ProductPageView.as_view(), name="product"),
    path("leadership/", LeadershipPageView.as_view(), name="leadership"),
    path("history/", HistoryPageView.as_view(), name="history"),
    path("vision/", VisionPageView.as_view(), name="vision"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]