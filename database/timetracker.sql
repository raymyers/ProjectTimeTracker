-- create database timetracker;
-- \c timetracker
CREATE TABLE client (
	id SERIAL8 NOT NULL, 
	name VARCHAR(100), 
	email VARCHAR(100), 
	phone VARCHAR(100), 
	total_hours DECIMAL(10, 2), 
	total_amount DECIMAL(10, 2), 
	budget_amount DECIMAL(10, 2), 
	is_over_budget BOOLEAN DEFAULT false, 
	PRIMARY KEY (id)
);
-- INSERT INTO client VALUES(5,'Imatia','','',8,400,5000,0);
CREATE TABLE project (
	id SERIAL8 NOT NULL, 
	client_id BIGINT NOT NULL, 
	name VARCHAR(100), 
	total_project_hours DECIMAL(10, 2), 
	total_project_amount DECIMAL(10, 2), 
	project_budget_amount DECIMAL(10, 2), 
	is_over_budget BOOLEAN DEFAULT false, 
	is_active BOOLEAN DEFAULT true, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES client (id)
);
-- INSERT INTO project VALUES(5,5,'WebGenAI',0,0,0,0,0);
-- INSERT INTO project VALUES(6,5,'ALS Training',8,400,1000,0,0);
CREATE TABLE person (
	id SERIAL8 NOT NULL, 
	client_id BIGINT NOT NULL, 
	name VARCHAR(100), 
	email VARCHAR(100), 
	phone VARCHAR(100), 
	billing_rate DECIMAL(10, 2), 
	total_hours_entered DECIMAL(10, 2), 
	total_amount_billed DECIMAL(10, 2), 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES client (id)
);
-- INSERT INTO person VALUES(1,5,'Tyler','tyler@genai-logic.com','4075067094',50,8,400);
CREATE TABLE invoice (
	id SERIAL8 NOT NULL, 
	invoice_date DATE, 
	project_id BIGINT NOT NULL, 
	invoice_amount DECIMAL(10, 2), 
	payment_total DECIMAL(10, 2), 
	invoice_balance DECIMAL(10, 2), 
	is_paid BOOLEAN DEFAULT false, 
	is_ready BOOLEAN DEFAULT false, 
	task_count INTEGER, 
	completed_task_count INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_id) REFERENCES project (id)
);
-- INSERT INTO invoice VALUES(1,'2025-02-18',6,400,0,400,0,0,1,0);
CREATE TABLE task (
	id SERIAL8 NOT NULL, 
	project_id BIGINT NOT NULL, 
	name VARCHAR(100), 
	description TEXT, 
	total_task_hours_worked DECIMAL(10, 2), 
	total_task_amount_billed DECIMAL(10, 2), 
	task_budget_hours DECIMAL(10, 2), 
	is_over_budget BOOLEAN, 
	is_completed BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_id) REFERENCES project (id)
);
-- INSERT INTO task VALUES(1,6,'Create Outline','',0,0,5,0,0);
-- INSERT INTO task VALUES(2,6,'Create Slides','',8,400,8,0,0);
CREATE TABLE invoice_item (
	id SERIAL8 NOT NULL, 
	invoice_id BIGINT NOT NULL, 
	task_id BIGINT NOT NULL, 
	task_amount DECIMAL(10, 2), 
	is_completed BOOLEAN DEFAULT false, 
	PRIMARY KEY (id), 
	FOREIGN KEY(invoice_id) REFERENCES invoice (id), 
	FOREIGN KEY(task_id) REFERENCES task (id)
);
-- INSERT INTO invoice_item VALUES(1,1,2,400,0);
CREATE TABLE timesheet (
	id SERIAL8 NOT NULL, 
	task_id BIGINT NOT NULL, 
	person_id BIGINT NOT NULL, 
	date_worked DATE, 
	hours_worked DECIMAL(10, 2), 
	billing_rate DECIMAL(10, 2), 
	total_amount_billed DECIMAL(10, 2), 
	is_billable BOOLEAN DEFAULT true, 
	PRIMARY KEY (id), 
	FOREIGN KEY(task_id) REFERENCES task (id), 
	FOREIGN KEY(person_id) REFERENCES person (id)
);
-- INSERT INTO timesheet VALUES(1,2,1,NULL,8,50,400,1);
CREATE TABLE payment (
	id SERIAL8 NOT NULL, 
	invoice_id BIGINT NOT NULL, 
	amount DECIMAL(10, 2), 
	payment_date DATE, 
	notes TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(invoice_id) REFERENCES invoice (id)
);
