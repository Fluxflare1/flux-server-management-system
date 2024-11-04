import datetime
from .models import BillingCycle, Invoice

def generate_billing_cycle():
    today = datetime.date.today()
    last_billing_cycle = BillingCycle.objects.last()
    if last_billing_cycle.end_date < today:
        new_cycle = BillingCycle.create_new_cycle(today)
        Invoice.generate_invoices_for_cycle(new_cycle)
