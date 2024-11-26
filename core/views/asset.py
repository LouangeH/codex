from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from core.models.asset import Asset
from core.forms.asset_form import AssetForm

class AssetsNonOperationnelsView(ListView):
    model = Asset
    template_name = 'core/assets_non_operationnels.html'
    context_object_name = 'assets'

    def get_queryset(self):
        return Asset.objects.filter(status='non_operational')

class SignalementPerteView(UpdateView):
    model = Asset
    fields = ['status']
    template_name = 'core/signalement_perte.html'
    success_url = reverse_lazy('core:assets_non_operationnels')

class AssetStatusUpdateView(UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = 'core/asset_status_form.html'
    success_url = reverse_lazy('core:asset_list')

    def form_valid(self, form):
        # Ajouter une logique pour alerter le gérant si nécessaire
        return super().form_valid(form)
    
class AssetListView(ListView):
    model = Asset
    template_name = 'core/asset_list.html'
    context_object_name = 'assets'

    def get_queryset(self):
        # Filtrer les actifs selon le statut passé dans l'URL
        statut = self.kwargs.get('status')
        return Asset.objects.filter(status=statut)