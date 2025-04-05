from django.views import generic

from blossom.models.ShowModel import Show

class IndexView(generic.ListView):
    template_name = "blossom/index.html"
    context_object_name = "active_show_list"

    def get_queryset(self):
        return Show.objects.all().filter(active=True)