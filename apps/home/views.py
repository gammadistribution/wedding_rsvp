from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Render the home page for the site, i.e. get the template home.html and
    render this class based view.
    """
    template_name = "home.html"
