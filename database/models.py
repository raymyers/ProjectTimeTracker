# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DECIMAL, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  February 18, 2025 14:53:09
# Database: sqlite:////tmp/tmp.kwRU9Ssoos-01JMCRP6RTCT32TMNM2532VCN2/ProjectTracker/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Client(Base):  # type: ignore
    """
    description: Represents a client entity in the application.
    """
    __tablename__ = 'client'
    _s_collection_name = 'Client'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    total_hours : DECIMAL = Column(DECIMAL(10, 2))
    total_amount : DECIMAL = Column(DECIMAL(10, 2))
    budget_amount : DECIMAL = Column(DECIMAL(10, 2))
    is_over_budget = Column(Boolean)

    # parent relationships (access parent)

    # child relationships (access children)
    PersonList : Mapped[List["Person"]] = relationship(back_populates="client")
    ProjectList : Mapped[List["Project"]] = relationship(back_populates="client")



class Person(Base):  # type: ignore
    """
    description: Represents a person associated with a client, who logs time and generates billing amounts.
    """
    __tablename__ = 'person'
    _s_collection_name = 'Person'  # type: ignore

    id = Column(Integer, primary_key=True)
    client_id = Column(ForeignKey('client.id'))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    billing_rate : DECIMAL = Column(DECIMAL(10, 2))
    total_hours_entered : DECIMAL = Column(DECIMAL(10, 2))
    total_amount_billed : DECIMAL = Column(DECIMAL(10, 2))

    # parent relationships (access parent)
    client : Mapped["Client"] = relationship(back_populates=("PersonList"))

    # child relationships (access children)
    TimesheetList : Mapped[List["Timesheet"]] = relationship(back_populates="person")



class Project(Base):  # type: ignore
    """
    description: Represents a project linked to a client.
    """
    __tablename__ = 'project'
    _s_collection_name = 'Project'  # type: ignore

    id = Column(Integer, primary_key=True)
    client_id = Column(ForeignKey('client.id'))
    name = Column(String)
    total_project_hours : DECIMAL = Column(DECIMAL(10, 2))
    total_project_amount : DECIMAL = Column(DECIMAL(10, 2))
    project_budget_amount : DECIMAL = Column(DECIMAL(10, 2))
    is_over_budget = Column(Boolean)
    is_active = Column(Boolean)

    # parent relationships (access parent)
    client : Mapped["Client"] = relationship(back_populates=("ProjectList"))

    # child relationships (access children)
    InvoiceList : Mapped[List["Invoice"]] = relationship(back_populates="project")
    TaskList : Mapped[List["Task"]] = relationship(back_populates="project")



class Invoice(Base):  # type: ignore
    """
    description: Represents an invoice related to a project, tracking financials and approval status.
    """
    __tablename__ = 'invoice'
    _s_collection_name = 'Invoice'  # type: ignore

    id = Column(Integer, primary_key=True)
    invoice_date = Column(Date)
    project_id = Column(ForeignKey('project.id'))
    invoice_amount : DECIMAL = Column(DECIMAL(10, 2))
    payment_total : DECIMAL = Column(DECIMAL(10, 2))
    invoice_balance : DECIMAL = Column(DECIMAL(10, 2))
    is_paid = Column(Boolean)
    is_ready = Column(Boolean)
    task_count = Column(Integer)
    completed_task_count = Column(Integer)

    # parent relationships (access parent)
    project : Mapped["Project"] = relationship(back_populates=("InvoiceList"))

    # child relationships (access children)
    InvoiceItemList : Mapped[List["InvoiceItem"]] = relationship(back_populates="invoice")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="invoice")



class Task(Base):  # type: ignore
    """
    description: Represents a task under a project, measuring progress and budget adherence.
    """
    __tablename__ = 'task'
    _s_collection_name = 'Task'  # type: ignore

    id = Column(Integer, primary_key=True)
    project_id = Column(ForeignKey('project.id'))
    name = Column(String)
    description = Column(String)
    total_task_hours_worked : DECIMAL = Column(DECIMAL(10, 2))
    total_task_amount_billed : DECIMAL = Column(DECIMAL(10, 2))
    task_budget_hours : DECIMAL = Column(DECIMAL(10, 2))
    is_over_budget = Column(Boolean)
    is_completed = Column(Boolean)

    # parent relationships (access parent)
    project : Mapped["Project"] = relationship(back_populates=("TaskList"))

    # child relationships (access children)
    InvoiceItemList : Mapped[List["InvoiceItem"]] = relationship(back_populates="task")
    TimesheetList : Mapped[List["Timesheet"]] = relationship(back_populates="task")



class InvoiceItem(Base):  # type: ignore
    """
    description: Represents an individual item in an invoice, which is derived from a task.
    """
    __tablename__ = 'invoice_item'
    _s_collection_name = 'InvoiceItem'  # type: ignore

    id = Column(Integer, primary_key=True)
    invoice_id = Column(ForeignKey('invoice.id'))
    task_id = Column(ForeignKey('task.id'))
    task_amount : DECIMAL = Column(DECIMAL(10, 2))
    is_completed = Column(Boolean)

    # parent relationships (access parent)
    invoice : Mapped["Invoice"] = relationship(back_populates=("InvoiceItemList"))
    task : Mapped["Task"] = relationship(back_populates=("InvoiceItemList"))

    # child relationships (access children)



class Payment(Base):  # type: ignore
    """
    description: Represents a payment made against an invoice, logging the payment amounts and dates.
    """
    __tablename__ = 'payment'
    _s_collection_name = 'Payment'  # type: ignore

    id = Column(Integer, primary_key=True)
    invoice_id = Column(ForeignKey('invoice.id'))
    amount : DECIMAL = Column(DECIMAL(10, 2))
    payment_date = Column(Date)
    notes = Column(String)

    # parent relationships (access parent)
    invoice : Mapped["Invoice"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)



class Timesheet(Base):  # type: ignore
    """
    description: Tracks the time worked by a person on a task, used for billing and reporting purposes.
    """
    __tablename__ = 'timesheet'
    _s_collection_name = 'Timesheet'  # type: ignore

    id = Column(Integer, primary_key=True)
    task_id = Column(ForeignKey('task.id'))
    person_id = Column(ForeignKey('person.id'))
    date_worked = Column(Date)
    hours_worked : DECIMAL = Column(DECIMAL(10, 2))
    billing_rate : DECIMAL = Column(DECIMAL(10, 2))
    total_amount_billed : DECIMAL = Column(DECIMAL(10, 2))
    is_billable = Column(Boolean)

    # parent relationships (access parent)
    person : Mapped["Person"] = relationship(back_populates=("TimesheetList"))
    task : Mapped["Task"] = relationship(back_populates=("TimesheetList"))

    # child relationships (access children)
