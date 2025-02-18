
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.formula(derive=Person.total_amount_billed, as_expression=lambda row: row.total_hours_entered * row.billing_rate)
