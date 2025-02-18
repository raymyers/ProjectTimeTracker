
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.formula(derive=Invoice.is_paid, as_expression=lambda row: row.invoice_balance <= 0)
