
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.sum(derive=Task.total_task_amount_billed, as_sum_of=Timesheet.total_amount_billed)
