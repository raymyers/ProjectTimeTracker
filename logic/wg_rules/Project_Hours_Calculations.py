
from logic_bank.logic_bank import Rule
from database.models import *
import integration.kafka.kafka_producer as kafka_producer

def init_rule():
  Rule.sum(derive=Project.total_project_hours, as_sum_of=Task.total_task_hours_worked)
