
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.count(derive=Invoice.completed_task_count, as_count_of=InvoiceItem, where=lambda row: row.is_completed is True)
