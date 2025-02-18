
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.after_flush_row_event(on_class=Invoice, calling=kafka_producer.send_row_to_kafka, if_condition=lambda row: row.is_ready, with_args={'topic': 'invoice_ready'})
