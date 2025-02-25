
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.constraint(validate=Person, as_condition=lambda row: 0 < row.billing_rate < 200, error_msg="Billing rate must be greater than 0 and less than 200")
