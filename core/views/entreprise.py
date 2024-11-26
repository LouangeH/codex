from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from core.models.business import Business
from core.forms.business_form import BusinessForm

class BusinessDetailView(DetailView):
    model = Business
    template_name = 'core/business_detail.html'
    context_object_name = 'business'

class BusinessCreateView(CreateView):
    model = Business
    form_class = BusinessForm
    template_name = 'core/business_form.html'
    success_url = reverse_lazy('core:business_list')
