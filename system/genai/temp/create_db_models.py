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
    """description: Table to store client details including contact and budget info."""
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    total_hours = Column(DECIMAL(10, 2), default=0)
    total_amount = Column(DECIMAL(10, 2), default=0)
    budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean)
    invoice_total = Column(DECIMAL(10, 2), default=0)
    payment_total = Column(DECIMAL(10, 2), default=0)

class Project(Base):
    """description: Table to manage projects of clients, tracking hours, budget, and active status."""
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    total_project_hours = Column(DECIMAL(10, 2), default=0)
    total_project_amount = Column(DECIMAL(10, 2), default=0)
    project_budget_amount = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean)
    is_active = Column(Boolean)

class Invoice(Base):
    """description: Stores invoice details for clients including payment tracking."""
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    invoice_date = Column(Date, default=date.today())
    client_id = Column(Integer, ForeignKey('client.id'))
    project_id = Column(Integer, ForeignKey('project.id'))
    invoice_amount = Column(DECIMAL(10, 2), default=0)
    payment_total = Column(DECIMAL(10, 2), default=0)
    invoice_balance = Column(DECIMAL(10, 2), default=0)
    is_paid = Column(Boolean)
    is_ready = Column(Boolean)
    task_count = Column(Integer, default=0)
    completed_task_count = Column(Integer, default=0)

class InvoiceItem(Base):
    """description: Details individual items in an invoice, linking tasks and invoices."""
    __tablename__ = 'invoice_item'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    task_id = Column(Integer, ForeignKey('task.id'))
    task_amount = Column(DECIMAL(10, 2), default=0)
    is_completed = Column(Boolean)

class Task(Base):
    """description: Manage tasks within projects, tracking work and budget allocations."""
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    name = Column(String)
    description = Column(String)
    total_task_hours_worked = Column(DECIMAL(10, 2), default=0)
    total_task_amount_billed = Column(DECIMAL(10, 2), default=0)
    task_budget_hours = Column(DECIMAL(10, 2), default=0)
    is_over_budget = Column(Boolean)
    is_completed = Column(Boolean)

class Person(Base):
    """description: Contains person-specific details, responsible for logging hours billed to clients."""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_hours_entered = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)

class Timesheet(Base):
    """description: Tracks individual time entries and corresponding billing information."""
    __tablename__ = 'timesheet'
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('task.id'))
    person_id = Column(Integer, ForeignKey('person.id'))
    date_worked = Column(Date, default=date.today())
    hours_worked = Column(DECIMAL(10, 2), default=0)
    billing_rate = Column(DECIMAL(10, 2), default=0)
    total_amount_billed = Column(DECIMAL(10, 2), default=0)
    is_billable = Column(Boolean)

class Payment(Base):
    """description: Stores payment details for client invoices, linking to those entities."""
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    amount = Column(DECIMAL(10, 2), default=0)
    payment_date = Column(Date, default=date.today())
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
    client1 = Client(id=1, name="Client A", email="clienta@example.com", phone="111-222-3333", total_hours=120.0, total_amount=6000.0, budget_amount=5000.0, is_over_budget=True, invoice_total=6500.0, payment_total=5500.0)
    client2 = Client(id=2, name="Client B", email="clientb@example.com", phone="555-666-7777", total_hours=80.0, total_amount=3200.0, budget_amount=3500.0, is_over_budget=False, invoice_total=3000.0, payment_total=3100.0)
    client3 = Client(id=3, name="Client C", email="clientc@example.com", phone="888-999-0000", total_hours=200.0, total_amount=10000.0, budget_amount=9500.0, is_over_budget=True, invoice_total=10200.0, payment_total=10200.0)
    client4 = Client(id=4, name="Client D", email="clientd@example.com", phone="333-444-5555", total_hours=150.0, total_amount=7000.0, budget_amount=7500.0, is_over_budget=False, invoice_total=7000.0, payment_total=6800.0)
    project1 = Project(id=1, client_id=1, name="Alpha Project", total_project_hours=100.0, total_project_amount=5000.0, project_budget_amount=4500.0, is_over_budget=True, is_active=True)
    project2 = Project(id=2, client_id=2, name="Beta Project", total_project_hours=50.0, total_project_amount=2000.0, project_budget_amount=2500.0, is_over_budget=False, is_active=False)
    project3 = Project(id=3, client_id=3, name="Gamma Project", total_project_hours=60.0, total_project_amount=3000.0, project_budget_amount=3000.0, is_over_budget=False, is_active=True)
    project4 = Project(id=4, client_id=4, name="Delta Project", total_project_hours=130.0, total_project_amount=6500.0, project_budget_amount=6800.0, is_over_budget=False, is_active=True)
    invoice1 = Invoice(id=1, invoice_date=date(2023, 8, 15), client_id=1, project_id=1, invoice_amount=2500.0, payment_total=2000.0, invoice_balance=500.0, is_paid=False, is_ready=False, task_count=3, completed_task_count=1)
    invoice2 = Invoice(id=2, invoice_date=date(2023, 7, 10), client_id=2, project_id=2, invoice_amount=1500.0, payment_total=1600.0, invoice_balance=-100.0, is_paid=True, is_ready=True, task_count=5, completed_task_count=5)
    invoice3 = Invoice(id=3, invoice_date=date(2023, 9, 20), client_id=3, project_id=3, invoice_amount=3200.0, payment_total=3100.0, invoice_balance=100.0, is_paid=False, is_ready=True, task_count=4, completed_task_count=4)
    invoice4 = Invoice(id=4, invoice_date=date(2023, 6, 5), client_id=4, project_id=4, invoice_amount=2000.0, payment_total=1800.0, invoice_balance=200.0, is_paid=False, is_ready=False, task_count=2, completed_task_count=1)
    invoice_item1 = InvoiceItem(id=1, invoice_id=1, task_id=1, task_amount=2500.0, is_completed=False)
    invoice_item2 = InvoiceItem(id=2, invoice_id=2, task_id=2, task_amount=1000.0, is_completed=True)
    invoice_item3 = InvoiceItem(id=3, invoice_id=3, task_id=3, task_amount=2000.0, is_completed=True)
    invoice_item4 = InvoiceItem(id=4, invoice_id=4, task_id=4, task_amount=1800.0, is_completed=False)
    task1 = Task(id=1, project_id=1, name="Design Task", description="Design Phase", total_task_hours_worked=50.0, total_task_amount_billed=2500.0, task_budget_hours=40.0, is_over_budget=True, is_completed=False)
    task2 = Task(id=2, project_id=2, name="Development Task", description="Development Phase", total_task_hours_worked=80.0, total_task_amount_billed=3200.0, task_budget_hours=90.0, is_over_budget=False, is_completed=True)
    task3 = Task(id=3, project_id=3, name="Testing Task", description="Testing Phase", total_task_hours_worked=60.0, total_task_amount_billed=3000.0, task_budget_hours=60.0, is_over_budget=False, is_completed=True)
    task4 = Task(id=4, project_id=4, name="Deployment Task", description="Deployment Phase", total_task_hours_worked=40.0, total_task_amount_billed=2000.0, task_budget_hours=50.0, is_over_budget=False, is_completed=False)
    person1 = Person(id=1, client_id=1, name="Alice", email="alice@example.com", phone="123-456-7890", billing_rate=100.0, total_hours_entered=60.0, total_amount_billed=6000.0)
    person2 = Person(id=2, client_id=2, name="Bob", email="bob@example.com", phone="987-654-3210", billing_rate=150.0, total_hours_entered=40.0, total_amount_billed=6000.0)
    person3 = Person(id=3, client_id=3, name="Charlie", email="charlie@example.com", phone="567-890-1234", billing_rate=75.0, total_hours_entered=100.0, total_amount_billed=7500.0)
    person4 = Person(id=4, client_id=4, name="Diana", email="diana@example.com", phone="321-654-9870", billing_rate=125.0, total_hours_entered=80.0, total_amount_billed=10000.0)
    timesheet1 = Timesheet(id=1, task_id=1, person_id=1, date_worked=date(2023, 8, 1), hours_worked=5.0, billing_rate=100.0, total_amount_billed=500.0, is_billable=True)
    timesheet2 = Timesheet(id=2, task_id=1, person_id=2, date_worked=date(2023, 8, 2), hours_worked=2.0, billing_rate=150.0, total_amount_billed=300.0, is_billable=True)
    timesheet3 = Timesheet(id=3, task_id=2, person_id=3, date_worked=date(2023, 8, 3), hours_worked=10.0, billing_rate=75.0, total_amount_billed=750.0, is_billable=True)
    timesheet4 = Timesheet(id=4, task_id=2, person_id=4, date_worked=date(2023, 8, 4), hours_worked=8.0, billing_rate=125.0, total_amount_billed=1000.0, is_billable=True)
    payment1 = Payment(id=1, client_id=1, invoice_id=1, amount=2000.0, payment_date=date(2023, 8, 10), notes="Partial payment received")
    payment2 = Payment(id=2, client_id=2, invoice_id=2, amount=1600.0, payment_date=date(2023, 7, 15), notes="Full payment")
    payment3 = Payment(id=3, client_id=3, invoice_id=3, amount=3100.0, payment_date=date(2023, 9, 25), notes="Payment for invoice 3")
    payment4 = Payment(id=4, client_id=4, invoice_id=4, amount=1800.0, payment_date=date(2023, 6, 10), notes="Final payment for invoice")
    
    
    
    session.add_all([client1, client2, client3, client4, project1, project2, project3, project4, invoice1, invoice2, invoice3, invoice4, invoice_item1, invoice_item2, invoice_item3, invoice_item4, task1, task2, task3, task4, person1, person2, person3, person4, timesheet1, timesheet2, timesheet3, timesheet4, payment1, payment2, payment3, payment4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
