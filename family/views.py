from django.views.generic import ListView
from .models import Person
from django.shortcuts import render


class FamilyList(ListView):
    def get_queryset(*args, **kwargs):
        return Person.objects.all()

    def get_context_data(self, family_list=None, **kwargs):
        queryset = family_list or self.object_list
        return super().get_context_data(family_list=queryset, **kwargs)


def family_tree_view(request):
    return render(request, "homepage.html")


class PersonDetailView(ListView):
    model = Person

    def get_context_data(self, **kwargs):
        person = Person.objects.get(pk=self.kwargs["pk"])
        return super().get_context_data(person=person, **kwargs)
