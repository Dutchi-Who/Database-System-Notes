---
aliases: 
- Database System
create-date: 2023-03-14
---

# Database System
Database systems are designed to manage large bodies of information, ensure they are safe and avoid possible anomalous result.

## Applications
Database systems are used to manage collections of data that are:
- highly valuable
- relatively large
- accessed by multiple users and applications, often at the same time

Modern database systems exploit commonalities in the structure of data to gain efficiency but also allow for weakly structured data and for data whose format are highly variable.

### Abstraction
Managing complexity is challenging, not only in management of data but in any domain. Abstraction allows a person to use a complex device or system without having to know the details of how that device or system is constructed.

### Two modes
There are two modes in which databases are used.
- Online Transaction Processing
- Data Analytics

> 1. In decision areas, the cost of making wrong decisions can be very high. 
> 2. The field of data mining combines knowledge-discovery techniques and statistical analysts.

## Purpose of Database Systems
Imagine a scenario of school organization. We need a program to do such things:
- Add new students
- Register students for courses
- Assign grades to students

This typical file-processing system is supported by a conventional operating system, which has such disadvantages:
- **Data redundancy and inconsistency**: 
    - the various files are likely to have different structures, and the programs may be written in several programming languages. 
    - In addition, it may lead to data inconsistency. The various copies of the same data may no longer agree.
- **Difficulty in accessing data**.
    - More responsive data-retrieval systems are required for general use.
- **Data isolation**.
- **Integrity problems**.
    - data in the database must satisfy certain types of *consistency constraints*.
- **Atomicity problems**.
    - the data event must be *atomic* - it must happen in its entirety or not at all.
- **Concurrent-access anomalies**.
    - If two bank clerks debit the account balance (by say $500 and $100, respectively) of account A at almost exactly the same time, the result of the concurrent executions may leave the account balance in an incorrect (or inconsistent) state.
    - To guard against this possibility, the system must maintain some form of *supervision*.
- **Security problems**.

> Be aware that **not only programmers** need to access the database. E.g., statists can retrieve data from a database to analysis what regularity does those objects have.

These difficulties, among others, prompted **both the initial development of database systems and the transition of file-based applications to database systems**, back in the 1960s and 1970s.

## View of Data
