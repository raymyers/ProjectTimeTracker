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
        if not 8234592712602685094 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_client_1 = Client(name="Client A", email="clienta@example.com", phone="123-456-7890", total_hours=100.00, total_amount=2000.00, budget_amount=3000.00, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8234592712602685094)
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
        if not 5521430949967034031 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_client_2 = Client(name="Client B", email="clientb@example.com", phone="234-567-8901", total_hours=150.00, total_amount=3000.00, budget_amount=3000.00, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5521430949967034031)
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
        if not -2546576329115396799 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_client_3 = Client(name="Client C", email="clientc@example.com", phone="345-678-9012", total_hours=120.00, total_amount=3500.00, budget_amount=3000.00, is_over_budget=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2546576329115396799)
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
        if not 5087563242095191018 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_client_4 = Client(name="Client D", email="clientd@example.com", phone="456-789-0123", total_hours=50.00, total_amount=1000.00, budget_amount=2000.00, is_over_budget=False)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5087563242095191018)
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
        if not 1734288307868340513 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_project_1 = Project(client_id=1, name="Project X", total_project_hours=80.00, total_project_amount=1600.00, project_budget_amount=2000.00, is_over_budget=False, is_active=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1734288307868340513)
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
        if not -4850258805797078655 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_project_2 = Project(client_id=2, name="Project Y", total_project_hours=90.00, total_project_amount=1800.00, project_budget_amount=2000.00, is_over_budget=False, is_active=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4850258805797078655)
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
        if not -3106720034176892657 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_project_3 = Project(client_id=3, name="Project Z", total_project_hours=60.00, total_project_amount=2000.00, project_budget_amount=1800.00, is_over_budget=True, is_active=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3106720034176892657)
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
        if not 3177011567453580015 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_project_4 = Project(client_id=4, name="Project W", total_project_hours=30.00, total_project_amount=600.00, project_budget_amount=1000.00, is_over_budget=False, is_active=True)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3177011567453580015)
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
        if not 3767269279502158749 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_invoice_1 = Invoice(invoice_date=date(2023, 6, 1), project_id=1, invoice_amount=400.00, payment_total=200.00, invoice_balance=200.00, is_paid=False, is_ready=False, task_count=2, completed_task_count=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3767269279502158749)
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
        if not 6209439216381248573 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_invoice_2 = Invoice(invoice_date=date(2023, 6, 5), project_id=2, invoice_amount=500.00, payment_total=500.00, invoice_balance=0.00, is_paid=True, is_ready=True, task_count=3, completed_task_count=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6209439216381248573)
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
        if not -4918390176270808298 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_invoice_3 = Invoice(invoice_date=date(2023, 6, 10), project_id=3, invoice_amount=400.00, payment_total=100.00, invoice_balance=300.00, is_paid=False, is_ready=False, task_count=1, completed_task_count=0)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4918390176270808298)
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
        if not 1904492869102465764 in succeeded_hashes:  # avoid duplicate inserts
            instance = test_invoice_4 = Invoice(invoice_date=date(2023, 6, 15), project_id=4, invoice_amount=200.00, payment_total=200.00, invoice_balance=0.00, is_paid=True, is_ready=True, task_count=2, completed_task_count=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1904492869102465764)
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
