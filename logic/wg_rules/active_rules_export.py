import logging
from logic_bank.logic_bank import DeclareRule, Rule, LogicBank
from database.models import *
from decimal import Decimal
from datetime import date, datetime
import integration.kafka.kafka_producer as kafka_producer

log = logging.getLogger(__name__)

def declare_logic():
    """
        declare_logic - declare rules
        this function is called from logic/declare_logic.py
    """
    log.info("declare_logic - active rules")
    
    # Exported Rules:
    
# Person Total Hours 
    # Total Hours entered is sum of timesheet hours worked
    Rule.sum(derive=Person.total_hours_entered, as_sum_of=Timesheet.hours_worked)
    
    # Person Total Amount Billed 
    # Total amount billed is total hours entered times billing rate
    Rule.formula(derive=Person.total_amount_billed, as_expression=lambda row: row.total_hours_entered * row.billing_rate)
    
    # Person Billing Rate Constraint 
    # Billing rate must be greater than 0 and less than 200
    Rule.constraint(validate=Person, as_condition=lambda row: 0 < row.billing_rate < 200, error_msg='Billing rate must be between 0 and 200')
    
    # Timesheet Copy Billing Rate 
    # Copy billing rate from Person billing rate
    Rule.copy(derive=Timesheet.billing_rate, from_parent=Person.billing_rate)
    
    # Timesheet Total Amount Billed 
    # If is_billable then total amount billed is billing rate times hours worked
    Rule.formula(derive=Timesheet.total_amount_billed, as_expression=lambda row: row.billing_rate * row.hours_worked if row.is_billable else 0)
    
    # Timesheet Hours Worked Constraint 
    # Hours worked must be greater than 0 and less than 15
    Rule.constraint(validate=Timesheet, as_condition=lambda row: 0 < row.hours_worked < 15, error_msg='Hours worked must be between 0 and 15')
    
    # Task Total Task Hours Worked 
    # Total task hours worked is the sum of the Timesheet hours worked
    Rule.sum(derive=Task.total_task_hours_worked, as_sum_of=Timesheet.hours_worked)
    
    # Task Total Task Amount Billed 
    # Total task amount billed is the sum of the Timesheet total amount billed
    Rule.sum(derive=Task.total_task_amount_billed, as_sum_of=Timesheet.total_amount_billed)
    
    # Task Is Over Budget Formula 
    # Formula: is Over Budget when total task hours worked exceeds task budget hours
    Rule.formula(derive=Task.is_over_budget, as_expression=lambda row: row.total_task_hours_worked > row.task_budget_hours)
    
    # Project Total Project Hours 
    # Total project hours is the sum of Task total task hours worked
    Rule.sum(derive=Project.total_project_hours, as_sum_of=Task.total_task_hours_worked)
    
    # Project Total Project Amount 
    # Total project amount is the sum of Task total amount billed
    Rule.sum(derive=Project.total_project_amount, as_sum_of=Task.total_task_amount_billed)
    
    # Project Is Over Budget Formula 
    # Formula: is Over Budget when total project amount exceeds project budget amount
    Rule.formula(derive=Project.is_over_budget, as_expression=lambda row: row.total_project_amount > row.project_budget_amount)
    
    # Client Total Hours 
    # Total hours is the sum of Project total project hours
    Rule.sum(derive=Client.total_hours, as_sum_of=Project.total_project_hours)
    
    # Client Total Amount 
    # Total amount is the sum of Project total project amount
    Rule.sum(derive=Client.total_amount, as_sum_of=Project.total_project_amount)
    
    # Client Is Over Budget Formula 
    # Formula: is Over Budget equals true when total amount exceeds budget amount
    Rule.formula(derive=Client.is_over_budget, as_expression=lambda row: row.total_amount > row.budget_amount)
    
    # Client Invoice Total Calculation 
    # Calculate total invoice amount for a client
    Rule.sum(derive=Client.invoice_total, as_sum_of=Invoice.invoice_amount)
    
    # Client Payment Total Calculation 
    # Calculate payment total for a client
    Rule.sum(derive=Client.payment_total, as_sum_of=Invoice.payment_total)
    
    # Client Kafka Event 
    # Send client to Kafka when over budget
    Rule.after_flush_row_event(on_class=Client, calling=kafka_producer.send_row_to_kafka, if_condition=lambda row: row.is_over_budget and row.budget_amount > 0, with_args={"topic": "client_over_budget"})
    
    # Invoice Amount Credit 
    # Calculate total invoice amount from items
    Rule.sum(derive=Invoice.invoice_amount, as_sum_of=InvoiceItem.task_amount)
    
    # Invoice Payment Total 
    # Payment total is the sum of Payment amount
    Rule.sum(derive=Invoice.payment_total, as_sum_of=Payment.amount)
    
    # Invoice Balance Formula 
    # Invoice balance is invoice amount less payment total
    Rule.formula(derive=Invoice.invoice_balance, as_expression=lambda row: row.invoice_amount - row.payment_total)
    
    # Invoice Is Paid Formula 
    # Formula: is_paid when invoice balance is than or equal to zero
    Rule.formula(derive=Invoice.is_paid, as_expression=lambda row: row.invoice_balance <= 0)
    
    # Invoice Task Count 
    # Task Count is count of InvoiceItem
    Rule.count(derive=Invoice.task_count, as_count_of=InvoiceItem)
    
    # Invoice Task Completed Count 
    # Task completed count is count of InvoiceItem where is_completed is True
    Rule.count(derive=Invoice.completed_task_count, as_count_of=InvoiceItem, where=lambda row: row.is_completed == True)
    
    # Invoice Is Ready Formula 
    # Formula: is ready when Task Count is equal to Task Completed Count
    Rule.formula(derive=Invoice.is_ready, as_expression=lambda row: row.task_count == row.completed_task_count)
    
    # Invoice Kafka Event 
    # Send invoice to Kafka when is_ready is True
    Rule.after_flush_row_event(on_class=Invoice, calling=kafka_producer.send_row_to_kafka, if_condition=lambda row: row.is_ready, with_args={'topic': 'invoice_ready'})
    
    # InvoiceItem Copy Task Amount 
    # InvoiceItem task amount is copied from Task total task amount billed
    Rule.copy(derive=InvoiceItem.task_amount, from_parent=Task.total_task_amount_billed)
    
    # InvoiceItem Completion Check 
    # Complete status for InvoiceItem when Task is complete
    Rule.copy(derive=InvoiceItem.is_completed, from_parent=Task.is_completed)
    