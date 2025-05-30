CREATE DATABASE COMPANY; 
USE COMPANY;

CREATE TABLE DEPARTMENT
(DNO VARCHAR(20) PRIMARY KEY,
DNAME VARCHAR(20),
MGR_SSN VARCHAR(20),
MGR_START_DATE DATE);

DESC DEPARTMENT;

CREATE TABLE EMPLOYEE
(SSN VARCHAR(20) PRIMARY KEY,
NAME VARCHAR(20), 
ADDRESS VARCHAR(20),
SEX CHAR(1),
SALARY INT,
SUPERSSN VARCHAR(20),
DNO VARCHAR(20),
FOREIGN KEY (SUPERSSN) REFERENCES EMPLOYEE (SSN),
FOREIGN KEY (DNO) REFERENCES DEPARTMENT (DNO));
DESC EMPLOYEE;


ALTER TABLE DEPARTMENT
ADD FOREIGN KEY (MGR_SSN) REFERENCES EMPLOYEE(SSN);


CREATE TABLE DLOCATION (DLOC VARCHAR(20),
DNO VARCHAR(20),
FOREIGN KEY (DNO) REFERENCES DEPARTMENT(DNO),
 PRIMARY KEY (DNO, DLOC));

DESC DLOCATION;


CREATE TABLE PROJECT
 (PNO INT PRIMARY KEY,
PNAME VARCHAR(20),
PLOCATION VARCHAR(20),


	
