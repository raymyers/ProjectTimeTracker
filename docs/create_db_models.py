# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Client(Base):
    """description: Represents a client entity in the application."""
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    total_hours = Column(DECIMAL(10, 2), default=0)
    total_amount = Column(DECIMAL(10, 2), default=0)
    budget_amount = Column(DECIMAL(10, 2))
    is_over_budget = Column(Boolean, default=False)

class Project(Base):
    """description: Represents a project linked to a client."""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    total_project_hours = Column(DECIMAL(10, 2), default=0)
    total_project_amount = Column(DECIMAL(10, 2), default=0)
    project_budget_amount = Column(DECIMAL(10, 2))
    is_over_budget = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

class Invoice(Base):
    """description: Represents an invoice related to a project, tracking financials and approval status."""
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date = Column(Date)
    project_id = Column(Integer, ForeignKey('project.id'))
    invoice_amount = Column(DECIMAL(10, 2), default=0)
    payment_total = Column(DECIMAL(10, 2), default=0)
    invoice_balance = Column(DECIMAL(10, 2))
    is_paid = Column(Boolean, default=False)
    is_ready = Column(Boolean, default=False)
    task_count = Column(Integer, default=0)
    completed_task_count = Column(Integer, default=0)

class InvoiceItem(Base):
    """description: Represents an individual item in an invoice, which is derived from a task."""
    __tablename__ = 'invoice_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    task_id = Column(Integer, ForeignKey('task.id'))
    task_amount = Column(DECIMAL(10, 2), default=0)
    is_completed = Column(Boolean, default=False)

class Task(Base):
    """description: Represents a task under a project, measuring progress and budget adherence."""
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    name = Column(String)
    description = Column(String)
    total_task_hours_worked = Column(DECIMAL(10, 2), default=0)
    total_task_amount_billed = Column(DECIMAL(10, 2), default=0)
    task_budget_hours = Column(DECIMAL(10, 2))
    is_over_budget = Column(Boolean, default=False)
    is_completed = Column(Boolean, default=False)

class Person(Base):
    """description: Represents a person associated with a client, who logs time and generates billing amounts."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_hours_entered = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Timesheet(Base):
    """description: Tracks the time worked by a person on a task, used for billing and reporting purposes."""
    __tablename__ = 'timesheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    date_worked = Column(Date)
    hours_worked = Column(DECIMAL(10, 2), default=0)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)
    is_billable = Column(Boolean, default=False)

class Payment(Base):
    """description: Represents a payment made against an invoice, logging the payment amounts and dates."""
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    amount = Column(DECIMAL(10, 2), default=0)
    payment_date = Column(Date)
    notes = Column(String)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    test_client_1 = Client(name="Client A", email="clienta@example.com", phone="123-456-7890", total_hours=100.00, total_amount=2000.00, budget_amount=3000.00, is_over_budget=False)
    test_client_2 = Client(name="Client B", email="clientb@example.com", phone="234-567-8901", total_hours=150.00, total_amount=3000.00, budget_amount=3000.00, is_over_budget=False)
    test_client_3 = Client(name="Client C", email="clientc@example.com", phone="345-678-9012", total_hours=120.00, total_amount=3500.00, budget_amount=3000.00, is_over_budget=True)
    test_client_4 = Client(name="Client D", email="clientd@example.com", phone="456-789-0123", total_hours=50.00, total_amount=1000.00, budget_amount=2000.00, is_over_budget=False)
    test_project_1 = Project(client_id=1, name="Project X", total_project_hours=80.00, total_project_amount=1600.00, project_budget_amount=2000.00, is_over_budget=False, is_active=True)
    test_project_2 = Project(client_id=2, name="Project Y", total_project_hours=90.00, total_project_amount=1800.00, project_budget_amount=2000.00, is_over_budget=False, is_active=True)
    test_project_3 = Project(client_id=3, name="Project Z", total_project_hours=60.00, total_project_amount=2000.00, project_budget_amount=1800.00, is_over_budget=True, is_active=True)
    test_project_4 = Project(client_id=4, name="Project W", total_project_hours=30.00, total_project_amount=600.00, project_budget_amount=1000.00, is_over_budget=False, is_active=True)
    test_invoice_1 = Invoice(invoice_date=date(2023, 6, 1), project_id=1, invoice_amount=400.00, payment_total=200.00, invoice_balance=200.00, is_paid=False, is_ready=False, task_count=2, completed_task_count=1)
    test_invoice_2 = Invoice(invoice_date=date(2023, 6, 5), project_id=2, invoice_amount=500.00, payment_total=500.00, invoice_balance=0.00, is_paid=True, is_ready=True, task_count=3, completed_task_count=3)
    test_invoice_3 = Invoice(invoice_date=date(2023, 6, 10), project_id=3, invoice_amount=400.00, payment_total=100.00, invoice_balance=300.00, is_paid=False, is_ready=False, task_count=1, completed_task_count=0)
    test_invoice_4 = Invoice(invoice_date=date(2023, 6, 15), project_id=4, invoice_amount=200.00, payment_total=200.00, invoice_balance=0.00, is_paid=True, is_ready=True, task_count=2, completed_task_count=2)
    
    
    
    session.add_all([test_client_1, test_client_2, test_client_3, test_client_4, test_project_1, test_project_2, test_project_3, test_project_4, test_invoice_1, test_invoice_2, test_invoice_3, test_invoice_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
