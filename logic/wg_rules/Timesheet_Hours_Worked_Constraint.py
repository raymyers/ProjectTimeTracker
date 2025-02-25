
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.constraint(validate=Timesheet, as_condition=lambda row: 0 < row.hours_worked < 15, error_msg="Hours worked must be greater than 0 and less than 15")
