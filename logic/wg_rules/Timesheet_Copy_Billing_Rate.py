
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.copy(derive=Timesheet.billing_rate, from_parent=Person.billing_rate)
