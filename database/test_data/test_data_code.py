import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not -4964743300991021066 in succeeded_hashes:  # avoid duplicate inserts
            instance = client1 = Client(id=1, name="Client A", email="clienta@example.com", phone="111-222-3333", total_hours=120.0, total_amount=6000.0, budget_amount=5000.0, is_over_budget=True, invoice_total=6500.0, payment_total=5500.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4964743300991021066)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4799867558745225057 in succeeded_hashes:  # avoid duplicate inserts
            instance = client2 = Client(id=2, name="Client B", email="clientb@example.com", phone="555-666-7777", total_hours=80.0, total_amount=3200.0, budget_amount=3500.0, is_over_budget=False, invoice_total=3000.0, payment_total=3100.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4799867558745225057)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8173033074833372143 in succeeded_hashes:  # avoid duplicate inserts
            instance = client3 = Client(id=3, name="Client C", email="clientc@example.com", phone="888-999-0000", total_hours=200.0, total_amount=10000.0, budget_amount=9500.0, is_over_budget=True, invoice_total=10200.0, payment_total=10200.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8173033074833372143)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6832047148819756541 in succeeded_hashes:  # avoid duplicate inserts
            instance = client4 = Client(id=4, name="Client D", email="clientd@example.com", phone="333-444-5555", total_hours=150.0, total_amount=7000.0, budget_amount=7500.0, is_over_budget=False, invoice_total=7000.0, payment_total=6800.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6832047148819756541)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8414937780956836187 in succeeded_hashes:  # avoid duplicate inserts
            instance = project1 = Project(id=1, client_id=1, name="Alpha Project", total_project_hours=100.0, total_project_amount=5000.0, project_budget_amount=4500.0, is_over_budget=True, is_active=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8414937780956836187)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -527311253696278487 in succeeded_hashes:  # avoid duplicate inserts
            instance = project2 = Project(id=2, client_id=2, name="Beta Project", total_project_hours=50.0, total_project_amount=2000.0, project_budget_amount=2500.0, is_over_budget=False, is_active=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-527311253696278487)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1696257055264884666 in succeeded_hashes:  # avoid duplicate inserts
            instance = project3 = Project(id=3, client_id=3, name="Gamma Project", total_project_hours=60.0, total_project_amount=3000.0, project_budget_amount=3000.0, is_over_budget=False, is_active=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1696257055264884666)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3694024706194982442 in succeeded_hashes:  # avoid duplicate inserts
            instance = project4 = Project(id=4, client_id=4, name="Delta Project", total_project_hours=130.0, total_project_amount=6500.0, project_budget_amount=6800.0, is_over_budget=False, is_active=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3694024706194982442)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4633717106347164062 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice1 = Invoice(id=1, invoice_date=date(2023, 8, 15), client_id=1, project_id=1, invoice_amount=2500.0, payment_total=2000.0, invoice_balance=500.0, is_paid=False, is_ready=False, task_count=3, completed_task_count=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4633717106347164062)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1316824161334870975 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice2 = Invoice(id=2, invoice_date=date(2023, 7, 10), client_id=2, project_id=2, invoice_amount=1500.0, payment_total=1600.0, invoice_balance=-100.0, is_paid=True, is_ready=True, task_count=5, completed_task_count=5)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1316824161334870975)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5650177291741140814 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice3 = Invoice(id=3, invoice_date=date(2023, 9, 20), client_id=3, project_id=3, invoice_amount=3200.0, payment_total=3100.0, invoice_balance=100.0, is_paid=False, is_ready=True, task_count=4, completed_task_count=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5650177291741140814)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6285468726278498779 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice4 = Invoice(id=4, invoice_date=date(2023, 6, 5), client_id=4, project_id=4, invoice_amount=2000.0, payment_total=1800.0, invoice_balance=200.0, is_paid=False, is_ready=False, task_count=2, completed_task_count=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6285468726278498779)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4501115619753084786 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_item1 = InvoiceItem(id=1, invoice_id=1, task_id=1, task_amount=2500.0, is_completed=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4501115619753084786)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2531733829193010144 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_item2 = InvoiceItem(id=2, invoice_id=2, task_id=2, task_amount=1000.0, is_completed=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2531733829193010144)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 916307872482822626 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_item3 = InvoiceItem(id=3, invoice_id=3, task_id=3, task_amount=2000.0, is_completed=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(916307872482822626)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4324128817674855132 in succeeded_hashes:  # avoid duplicate inserts
            instance = invoice_item4 = InvoiceItem(id=4, invoice_id=4, task_id=4, task_amount=1800.0, is_completed=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4324128817674855132)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7611265697691996612 in succeeded_hashes:  # avoid duplicate inserts
            instance = task1 = Task(id=1, project_id=1, name="Design Task", description="Design Phase", total_task_hours_worked=50.0, total_task_amount_billed=2500.0, task_budget_hours=40.0, is_over_budget=True, is_completed=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7611265697691996612)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 592182001734822478 in succeeded_hashes:  # avoid duplicate inserts
            instance = task2 = Task(id=2, project_id=2, name="Development Task", description="Development Phase", total_task_hours_worked=80.0, total_task_amount_billed=3200.0, task_budget_hours=90.0, is_over_budget=False, is_completed=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(592182001734822478)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3170252414168413724 in succeeded_hashes:  # avoid duplicate inserts
            instance = task3 = Task(id=3, project_id=3, name="Testing Task", description="Testing Phase", total_task_hours_worked=60.0, total_task_amount_billed=3000.0, task_budget_hours=60.0, is_over_budget=False, is_completed=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3170252414168413724)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5042372373994494956 in succeeded_hashes:  # avoid duplicate inserts
            instance = task4 = Task(id=4, project_id=4, name="Deployment Task", description="Deployment Phase", total_task_hours_worked=40.0, total_task_amount_billed=2000.0, task_budget_hours=50.0, is_over_budget=False, is_completed=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5042372373994494956)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7324173097862789180 in succeeded_hashes:  # avoid duplicate inserts
            instance = person1 = Person(id=1, client_id=1, name="Alice", email="alice@example.com", phone="123-456-7890", billing_rate=100.0, total_hours_entered=60.0, total_amount_billed=6000.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7324173097862789180)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2241226910645634112 in succeeded_hashes:  # avoid duplicate inserts
            instance = person2 = Person(id=2, client_id=2, name="Bob", email="bob@example.com", phone="987-654-3210", billing_rate=150.0, total_hours_entered=40.0, total_amount_billed=6000.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2241226910645634112)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4526774478068794657 in succeeded_hashes:  # avoid duplicate inserts
            instance = person3 = Person(id=3, client_id=3, name="Charlie", email="charlie@example.com", phone="567-890-1234", billing_rate=75.0, total_hours_entered=100.0, total_amount_billed=7500.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4526774478068794657)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2565686104882479281 in succeeded_hashes:  # avoid duplicate inserts
            instance = person4 = Person(id=4, client_id=4, name="Diana", email="diana@example.com", phone="321-654-9870", billing_rate=125.0, total_hours_entered=80.0, total_amount_billed=10000.0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2565686104882479281)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4560623664933051923 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet1 = Timesheet(id=1, task_id=1, person_id=1, date_worked=date(2023, 8, 1), hours_worked=5.0, billing_rate=100.0, total_amount_billed=500.0, is_billable=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4560623664933051923)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4632102701666427385 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet2 = Timesheet(id=2, task_id=1, person_id=2, date_worked=date(2023, 8, 2), hours_worked=2.0, billing_rate=150.0, total_amount_billed=300.0, is_billable=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4632102701666427385)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3939910105021103522 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet3 = Timesheet(id=3, task_id=2, person_id=3, date_worked=date(2023, 8, 3), hours_worked=10.0, billing_rate=75.0, total_amount_billed=750.0, is_billable=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3939910105021103522)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6943173997453793324 in succeeded_hashes:  # avoid duplicate inserts
            instance = timesheet4 = Timesheet(id=4, task_id=2, person_id=4, date_worked=date(2023, 8, 4), hours_worked=8.0, billing_rate=125.0, total_amount_billed=1000.0, is_billable=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6943173997453793324)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4690170423060680508 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment1 = Payment(id=1, client_id=1, invoice_id=1, amount=2000.0, payment_date=date(2023, 8, 10), notes="Partial payment received")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4690170423060680508)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7765275160901534845 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment2 = Payment(id=2, client_id=2, invoice_id=2, amount=1600.0, payment_date=date(2023, 7, 15), notes="Full payment")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7765275160901534845)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8512778438143966689 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment3 = Payment(id=3, client_id=3, invoice_id=3, amount=3100.0, payment_date=date(2023, 9, 25), notes="Payment for invoice 3")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8512778438143966689)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5868110494389469064 in succeeded_hashes:  # avoid duplicate inserts
            instance = payment4 = Payment(id=4, client_id=4, invoice_id=4, amount=1800.0, payment_date=date(2023, 6, 10), notes="Final payment for invoice")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5868110494389469064)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
