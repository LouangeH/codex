import csv
from django.http import HttpResponse
from django.views import View
from billing.models.invoice import Invoice
from django.template.loader import get_template
from xhtml2pdf import pisa

class ExportFacturesCSVView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="factures.csv"'
        writer = csv.writer(response)
        writer.writerow(['Client', 'Montant', 'Statut', 'Date'])
        
        for invoice in Invoice.objects.all():
            writer.writerow([invoice.client_name, invoice.total_amount, invoice.status, invoice.created_at])
        
        return response

class ExportFacturesPDFView(View):
    def get(self, request, *args, **kwargs):
        template = get_template('billing/factures_pdf.html')
        factures = Invoice.objects.all()
        html = template.render({'factures': factures})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="factures.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('Erreur lors de la génération du PDF', status=500)
        return response