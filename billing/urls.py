from django.urls import path
from billing.views.facture import InvoiceListView, InvoiceCreateView, InvoiceUpdateView, InvoiceDeleteView
from billing.views.rapport import RapportMensuelView
from billing.views.export import ExportFacturesCSVView, ExportFacturesPDFView

app_name = 'billing'

urlpatterns = [
    # Factures
    path('factures/', InvoiceListView.as_view(), name='invoice_list'),
    path('factures/ajouter/', InvoiceCreateView.as_view(), name='invoice_create'),
    path('factures/<int:pk>/modifier/', InvoiceUpdateView.as_view(), name='invoice_update'),
    path('factures/<int:pk>/supprimer/', InvoiceDeleteView.as_view(), name='invoice_delete'),
    # Rapports
    path('rapports/mensuel/', RapportMensuelView.as_view(), name='rapport_mensuel'),
    # Export
    path('export/csv/', ExportFacturesCSVView.as_view(), name='export_csv'),
    path('export/pdf/', ExportFacturesPDFView.as_view(), name='export_pdf'),
]
