
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.formula(derive=Timesheet.total_amount_billed, as_expression=lambda row: row.billing_rate * row.hours_worked if row.is_billable else 0)
