
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.formula(derive=Project.is_over_budget, as_expression=lambda row: row.total_project_amount > row.project_budget_amount)
