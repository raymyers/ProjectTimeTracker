from behave import *
import requests, pdb
import test_utils
import json
from datetime import datetime

dt = datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
client_id = 0
project_id = 0
person_id = 0
task_id = 0
timesheet_id = 0
invoice_id = 0
payment_id = 0

# Implement Behave Tests -- Client -> Project -> Task -> Person -> Timesheet -> invoice

@given('Enter Client Data')
def step_impl(context):
    client_nm = f"client_{dt}"
    context.data = {"name": client_nm}
    assert True

@when('Client Post')
def step_impl(context):
    print(context.data)
    r = test_utils.post("Client", context.data)
    context.response = r
    assert True is not False

@then('Client entered and balances are zero')
def step_impl(context):
    scenario = "New Client"
    test_utils.prt(f'Rules Report', scenario)
    global client_id 
    client_id = int(context.response["data"]["id"])
    client_nm = f"client_{dt}"
    client_nm_resp = context.response["data"]["attributes"]["name"]
    assert client_nm == client_nm_resp, f"Client Name: {client_nm} expected: {client_nm_resp}"
    
    

@given('Enter Project Data')
def step_impl(context):
    project_nm = f"Project_{dt}"
    context.data = {"name": project_nm, "client_id": client_id}
    assert True

@when('Project Post')
def step_impl(context):
    print(context.data)
    r = test_utils.post("Project", context.data)
    context.response = r
    assert True is not False

@then('Project entered and balances are zero')
def step_impl(context):
    scenario = "New Project"
    test_utils.prt(f'Rules Report', scenario)
    global project_id 
    project_id = int(context.response["data"]["id"])
    project_nm = f"Project_{dt}"
    project_nm_resp = context.response["data"]["attributes"]["name"]
    assert project_nm == project_nm_resp, f"Project Name: {project_nm} expected: {project_nm_resp}"
    
@given('Enter Person Data')
def step_impl(context):
    person_nm = f"Person_{dt}"
    context.data = {"name": person_nm, "client_id": client_id, "billing_rate": 100}
    assert True

@when('Person Post')
def step_impl(context):
    print(context.data)
    r = test_utils.post("Person", context.data)
    context.response = r
    assert True is not False

@then('Person entered and balances are zero')
def step_impl(context):
    scenario = "New Person"
    test_utils.prt(f'Rules Report', scenario)
    global person_id 
    person_id = int(context.response["data"]["id"])
    person_nm = f"Person_{dt}"
    person_nm_resp = context.response["data"]["attributes"]["name"]
    assert person_nm == person_nm_resp, f"Person Name: {person_nm} expected: {person_nm_resp}"
    

@given('Enter Task Data')
def step_impl(context):
    task_nm = f"Task_{dt}"
    context.data = {"name": task_nm, "project_id": project_id, "task_budget_hours": 10}
    assert True

@when('Task Post')
def step_impl(context):
    print(context.data)
    r = test_utils.post("Task", context.data)
    context.response = r
    assert True is not False

@then('Task entered and balances are zero')
def step_impl(context):
    scenario = "New Task"
    test_utils.prt(f'Rules Report', scenario)
    global task_id 
    task_id = int(context.response["data"]["id"])
    task_nm = f"Task_{dt}"
    task_nm_resp = context.response["data"]["attributes"]["name"]
    assert task_nm == task_nm_resp, f"Task Name: {task_nm} expected: {task_nm_resp}"
    

@given('Enter Timesheet Data')
def step_impl(context):
    context.data = {"task_id": task_id, "person_id": person_id, "hours_worked": 10, "date_worked": "2025-01-01","is_billable": True}
    assert True is not False

@when('Timesheet Post')
def step_impl(context):
    print(context.data)
    r = test_utils.post("Timesheet", context.data)
    context.response = r
    assert True is not False

@then('Timesheet entered and balances are zero')
def step_impl(context):
    scenario = "New Timesheet"
    test_utils.prt(f'Rules Report', scenario)
    global timesheet_id 
    timesheet_id = int(context.response["data"]["id"])
    r = test_utils.get("Client", client_id)
    total_hrs = r["data"]["attributes"]["total_hours"] ## 10
    assert total_hrs == 10, f"Total Hours: {total_hrs} expected: 10"
    

@given('Enter Invoice Data')
def step_impl(context):
    context.data = {"project_id": project_id,  "client_id": client_id, "invoice_date": "2025-02-01", "description": f"Invoice for Task_{dt}"}
    assert True is not False

@when('Invoice Post')
def step_impl(context):
    print(context.data)
    r = test_utils.post("Invoice", context.data)
    global invoice_id 
    invoice_id = int(r["data"]["id"])
    item = {"invoice_id": invoice_id, "task_id": task_id}
    r = test_utils.post("InvoiceItem", item)
    context.response = r
    assert True is not False

@then('Invoice entered and balances are zero')
def step_impl(context):
    scenario = "New Invoice"
    test_utils.prt(f'Rules Report', scenario)
    r = test_utils.get("Invoice", invoice_id)
    invoice_date = r["data"]["attributes"]["invoice_date"] ## 2025-02-01
    amt = r["data"]["attributes"]["invoice_amount"] ## 1000
    assert invoice_date == '2025-02-01', f"Invoice: {invoice_date} expected: 2025-02-01 "
    assert amt == 1000, f"Total Amount: {amt} expected: 1000"

@given('Update Invoice Data')
def step_impl(context):
    context.data =  test_utils.get("Invoice", invoice_id)
    assert True

@when('Invoice PUT')
def step_impl(context):
    print(context.data)
    context.data["data"]["attributes"]["is_ready"] = True
    r = test_utils.put("Invoice", context.data, invoice_id)
    context.response = r
    assert True is not False

@then('Invoice sent to Kafka')
def step_impl(context):
    scenario = "Invoice Ready"
    test_utils.prt(f'Rules Report', scenario)
    r = test_utils.get("Invoice", invoice_id)
    is_ready = r["data"]["attributes"]["is_ready"] ## true - logs should show Kafka message
    assert is_ready == True, f"Invoice: {is_ready} expected: True "
    
    
@given('Enter Payment Data')
def step_impl(context):
    context.data = {"invoice_id": invoice_id,  "client_id": client_id, "payment_date": "2025-02-23", "notes": f"Payment for Invoice {invoice_id} on 2025-02-23", "amount": 1000}
    assert True is not False

@when('Payment Post')
def step_impl(context):
    print(context.data)
    r = test_utils.post("Payment", context.data)
    global payment_id 
    payment_id = int(r["data"]["id"])
    assert True is not False

@then('Payment entered and balances match on Client')
def step_impl(context):
    scenario = "New Payment"
    test_utils.prt(f'Rules Report', scenario)
    r = test_utils.get("Payment", payment_id)
    invoice_date = r["data"]["attributes"]["payment_date"] ## 2025-02-01
    amt = r["data"]["attributes"]["amount"] ## 1000
    assert invoice_date == '2025-02-23', f"Invoice: {invoice_date} expected: 2025-02-23"
    assert amt == 1000, f"Total Amount: {amt} expected: 1000"
    
    r = test_utils.get("Client", client_id)
    payment_total = r["data"]["attributes"]["payment_total"] ## 1000
    assert payment_total == 1000, f"Payment Total Amount: {payment_total} expected: 1000"
    
