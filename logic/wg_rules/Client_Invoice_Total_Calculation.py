
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.sum(derive=Client.invoice_total, as_sum_of=Invoice.invoice_amount)
