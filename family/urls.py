from django.urls import path
from .views import PersonDetailView, family_tree_view, FamilyList
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Person
from django.urls import reverse_lazy

urlpatterns = [
    path("", family_tree_view, name="homepage"),
    path(
        "family_list",
        FamilyList.as_view(template_name="family_list.html"),
        name="family_list",
    ),
    path(
        "person/<int:pk>/",
        PersonDetailView.as_view(template_name="person_detail.html"),
        name="person-detail",
    ),
    path(
        "add_person",
        CreateView.as_view(
            model=Person,
            fields="__all__",
            success_url=reverse_lazy("homepage"),
            template_name="generic_update.html",
        ),
        name="add-person",
    ),
    path(
        "person/<int:pk>/edit/",
        UpdateView.as_view(
            model=Person,
            fields="__all__",
            success_url=reverse_lazy("family_list"),
            template_name="generic_update.html",
        ),
        name="update-person",
    ),
    path(
        "person/<int:pk>/delete/",
        DeleteView.as_view(
            model=Person,
            success_url=reverse_lazy("family_list"),
            template_name="generic_delete.html",
        ),
        name="delete-person",
    ),
]
