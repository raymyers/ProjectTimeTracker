
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.formula(derive=Task.is_over_budget, as_expression=lambda row: row.total_task_hours_worked > row.task_budget_hours)
