from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.LinkList.as_view(), name="link-list"),
    path("add/", views.LinkCreate.as_view(), name="link-add"),
    path("delete/<int:pk>/", views.LinkDelete.as_view(), name="link-delete"),
    path("public/<str:username>/", views.PublicUserLinksView.as_view(), name="public-user-links"),
]
