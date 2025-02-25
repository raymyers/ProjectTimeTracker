Feature: TimeTracker

  Scenario: New Client
    Given Enter Client Data
      When Client Post
      Then Client entered and balances are zero

  Scenario: New Project
    Given Enter Project Data
      When Project Post
      Then Project entered and balances are zero

  Scenario: New Person
    Given Enter Person Data
      When Person Post
      Then Person entered and balances are zero

  Scenario: New Task
    Given Enter Task Data
      When Task Post
      Then Task entered and balances are zero

  Scenario: New Timesheet
    Given Enter Timesheet Data
      When Timesheet Post
      Then Timesheet entered and balances are zero
  
    Scenario: New Invoice
    Given Enter Invoice Data
      When Invoice Post
      Then Invoice entered and balances are zero

    Scenario: Invoice Ready
    Given Update Invoice Data
      When Invoice PUT
      Then Invoice sent to Kafka

  Scenario: New Payment
    Given Enter Payment Data
      When Payment Post
      Then Payment entered and balances match on Client