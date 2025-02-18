
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.formula(derive=InvoiceItem.is_completed, as_expression=lambda row: all(item.is_completed for item in row.invoice_items))
