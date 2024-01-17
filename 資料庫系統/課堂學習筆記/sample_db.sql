---- 修改日期格式
alter session set nls_date_language='american';
alter session set nls_date_format='DD-MON-RR';

rem =====================================
rem script to build example ORACLE tables
rem =====================================
rem
rem Version 1.00
rem Dave Taylor
rem 10-NOV-2003
rem
rem Please report any errors to Dave Taylor
rem so I can correct the script
rem =====================================

set echo on

drop table countries
/
drop table departments
/
drop table employees
/
drop table jobs
/
drop table job_grades
/
drop table job_history
/
drop table locations
/
drop table regions
/

rem -----------------------------

create table countries
(
	country_ID	char(2),
	country_name	varchar2(40),
	regionID	number,
	primary key	(country_ID)
)
/

insert into countries values
('CA','Canada',2)
/
insert into countries values
('DE','Germany',1)
/
insert into countries values
('UK','United Kingdom',1)
/
insert into countries values
('US','United States of America',2)
/

rem -----------------------------

create table departments
(
	department_ID	number(4),
	department_name	varchar2(30)	not null,
	manager_ID	number(6),
	location_ID	number(4),
	primary key	(department_ID)
)
/

insert into departments values (10,'Administration',200,1700)
/
insert into departments values (20,'Marketing',201,1800)
/
insert into departments values (50,'Shipping',124,1500)
/
insert into departments values (60,'IT',103,1400)
/
insert into departments values (80,'Sales',149,2500)
/
insert into departments values (90,'Executive',100,1700)
/
insert into departments values (110,'Accounting',205,1700)
/
rem an example of insert statement avoiding NULLS
insert into departments 
(department_ID,department_name,location_ID) values (190,'Contracting',1700)
/

rem -----------------------------

create table employees
(
	employee_ID	number(6),
	first_name	varchar2(20),
	last_name	varchar2(25)	not null,
	email		varchar2(25)	not null,
	phone_number	varchar2(20),
	hire_date	date		not null,
	job_ID		varchar2(10)	not null,
	salary		number(8,2),
	commission_pct	number(2,2),
	manager_ID	number(6),
	department_ID	number(4),
	primary key	(employee_ID)
)
/

insert into employees values
(100,'Steven','King','SKING','515.123.4567','17-JUN-87','AD_PRES',24000,NULL,NULL,90)
/
insert into employees values
(101,'Neena','Kochhar','NKOCHHAR','515.123.4568','21-SEP-89','AD_VP',17000,NULL,100,90)
/
insert into employees values
(102,'Lex','De Haan','LDEHANN','515.123.4569','13-JAN-93','AD_VP',17000,NULL,100,90)
/
insert into employees values
(103,'Alexander','Hunold','AHUNOLD','590.423.4567','03-JAN-90','IT_PROG',9000,NULL,102,60)
/
insert into employees values
(104,'Bruce','Ernst','BERNST','590.423.4568','21-MAY-91','IT_PROG',6000,NULL,103,60)
/
insert into employees values
(107,'Diana','Lorentz','DLORENTZ','590.423.5567','07-FEB-99','IT_PROG',4200,NULL,103,60)
/
insert into employees values
(124,'Kevin','Mourgos','KMOURGOS','650.123.5234','16-NOV,99','ST_MAN',5800,NULL,100,50)
/
insert into employees values
(141,'Trenna','Rajs','TRAJS','650.121.8009','17-OCT-95','ST_CLERK',3500,NULL,124,50)
/
insert into employees values
(142,'Curtis','Davies','CDAVIES','650.121.2994','29-JAN-97','ST_CLERK',3100,NULL,124,50)
/
insert into employees values
(143,'Randall','Matos','RMATOS','650.121.2874','15-MAR-98','ST_CLERK',2600,NULL,124,50)
/
insert into employees values
(144,'Peter','Vargas','PVARGAS','650.121.2004','09-JUL-98','ST_CLERK',2500,NULL,124,50)
/
insert into employees values
(149,'Eleni','Zlotkey','EZLOTKEY','011.44.1344.429018','29-JAN-00','SA_MAN',10500,.2,100,80)
/
insert into employees values
(174,'Ellen','Abel','EABEL','011.44.1644.429267','11-MAY-96','SA_REP',11000,.3,149,80)
/
insert into employees values
(176,'Jonathon','Taylor','JTAYLOR','011.44.1644.429265','24-MAR-98','SA_REP',8600,.2,149,80)
/
insert into employees values
(178,'Kimberley','Grant','KGRANT','011.44.1644.429263','24-MAY-99','SA_REP',7000,.15,149,NULL)
/
insert into employees values
(200,'Jennefer','Whalen','JWHALEN','515.123.4444','17-SEP-87','AD_ASST',4400,NULL,101,10)
/
insert into employees values
(201,'Michael','Hartstein','MHARTSTE','515.123.5555','17-FEB-96','MK_MAN',13000,NULL,100,20)
/
insert into employees values
(202,'Pat','Fay','PFAY','603.123.6666','17-AUG-97','MK_REP',6000,NULL,201,20)
/
insert into employees values
(205,'Shelley','Higgins','SHIGGINS','515.123.8080','07-JUN-94','AC_MGR',12000,NULL,101,110)
/
insert into employees values
(206,'William','Gietz','WGIETZ','515.123.8181','07-JUN-94','AC_ACCOUNT',8300,NULL,205,110)
/

rem -----------------------------

create table jobs
(
	job_ID		varchar2(10),
	job_title	varchar2(35)	not null,
	min_salary	number(6),
	max_salary	number(6),
	primary key	(job_ID)
)
/

insert into jobs values ('AD_PRES','President',20000,40000)
/
insert into jobs values ('AD_VP','Administration Vice President',15000,30000)
/
insert into jobs values ('AD_ASST','Administration Assistant',3000,6000)
/
insert into jobs values ('AC_MGR','Accounting Manager',8200,16000)
/
insert into jobs values ('AC_ACCOUNT','Public Accountant',4200,9000)
/
insert into jobs values ('SA_MAN','Sales Manager',10000,20000)
/
insert into jobs values ('SA_REP','Sales Representative',6000,12000)
/
insert into jobs values ('ST_MAN','Stock Manager',5500,8500)
/
insert into jobs values ('ST_CLERK','Stock Clerk',2000,5000)
/
insert into jobs values ('IT_PROG','Programmer',4000,10000)
/
insert into jobs values ('MK_MAN','Marketing Manager',9000,15000)
/
insert into jobs values ('MK_REP','Marketing Representative',4000,9000)
/


rem -----------------------------

create table job_grades
(
	grade_level	varchar2(3),
	lowest_sal	number,
	highest_sal	number,
	primary key	(grade_level)
)
/

insert into job_grades values ('A',1000,2999)
/
insert into job_grades values ('B',3000,5999)
/
insert into job_grades values ('C',6000,9999)
/
insert into job_grades values ('D',10000,14999)
/
insert into job_grades values ('E',15000,24999)
/
insert into job_grades values ('F',20000,40000)
/

rem -----------------------------

create table job_history
(
	employee_ID	number(6),
	start_date	date		not null,
	end_date	date		not null,
	job_ID		varchar2(10)	not null,
	department_ID	number(4),
	primary key	(employee_ID,start_date)
)
/

insert into job_history values (102,'13-JAN-93','24-JUL-98','IT_PROG',60)
/
insert into job_history values (101,'21-SEP-89','27-OCT-93','AC-ACCOUNT',110)
/
insert into job_history values (101,'28-OCT-93','15-MAR-97','AC_MGR',110)
/
insert into job_history values (201,'17-FEB-96','19-DEC-99','MK_REP',20)
/
insert into job_history values (114,'24-MAR-98','31-DEC-99','ST_CLERK',50)
/
insert into job_history values (122,'01-JAN-99','31-DEC-99','ST_CLERK',50)
/
insert into job_history values (200,'17-SEP-87','17-JUN-93','AD_ASST',90)
/
insert into job_history values (176,'24-MAR-98','31-DEC-98','SA_REP',80)
/
insert into job_history values (176,'01-JAN-99','31-DEC-99','SA_MAN',80)
/
insert into job_history values (200,'01-JUL-94','31-DEC-98','AC_ACCOUNT',90)
/

rem -----------------------------

create table locations
(
	location_ID	number(4),
	street_address	varchar2(40),
	postal_code	varchar2(12),
	city		varchar2(30)	not null,
	state_province	varchar2(25),
	country_ID	char(2),
	primary key	(location_ID)
)
/

insert into locations values (1400,'2014 Jabberwocky Rd','26192','Southlake','Texas','US')
/
insert into locations values (1500,'2011 Interiors Blvd','99236','South San Fransisco','California','US')
/
insert into locations values (1700,'2004 Charade Rd','98199','Seattle','Washington','US')
/
insert into locations values (1800,'460 Bloor St. W.','ON M5S 1XB','Toronto','Ontario','CA')
/
insert into locations values (2500,'Magdalen Centre, The Oxford Science Park','OX9 9ZB','Oxford','Oxford','UK')
/


rem -----------------------------

create table regions
(
	region_ID	number,
	region_name	varchar2(25),
	primary key	(region_ID)
)
/

insert into regions values (1,'Europe')
/
insert into regions values (2,'Americas')
/
insert into regions values (3,'Asia')
/
insert into regions values (4,'Middle East and Africa')
/

commit
/

ALTER TABLE EMPLOYEES
 ADD CONSTRAINT EMPLOYEE_DEPARTMENT_FK
 FOREIGN KEY (department_ID)
 REFERENCES DEPARTMENTS (department_ID) ENABLE;

ALTER TABLE EMPLOYEES
 ADD CONSTRAINT EMP_JOB
 FOREIGN KEY (job_ID)
 REFERENCES JOBS (job_ID) ENABLE;
 
ALTER TABLE DEPARTMENTS
 ADD CONSTRAINT DEPARTMENT_EMPLOYEE_FK
 FOREIGN KEY (manager_ID)
 REFERENCES EMPLOYEE (employee_ID) ENABLE;
 
ALTER TABLE  DEPARTMENTS
 ADD CONSTRAINT DEPARTMENT_LOCATION_FK
 FOREIGN KEY (location_ID)
 REFERENCES  locations (location_ID) ENABLE;

ALTER TABLE EMPLOYEES
 ADD CONSTRAINT EMPLOYEE_MANAGER_FK
 FOREIGN KEY (manager_ID)
 REFERENCES EMPLOYEE (employee_ID) ENABLE;
