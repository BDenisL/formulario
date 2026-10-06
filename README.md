# Commercial Operations & Transactional Data System (Python & SQL)

This repository features a desktop management system engineered to centralize commercial operations, inventory control, payroll, and billing workflows. The project focuses heavily on **Relational Database Design, Operational Data Integrity, and Backend Business Logic Application**.

---

## 📌 Project Overview & Architecture
In business environments, transactional systems (OLTP) must process operations seamlessly while ensuring zero data loss and maintaining perfect relational consistency. This system bridges a desktop interface with a persistent database layer to execute business metrics in real-time.

* **Inventory & Vendor Operations:** Dynamic tracking of stock levels and automated vendor logs.
* **Human Resources & Payroll:** Built-in calculation modules for corporate salaries, net pay structures, and deductions.
* **Billing & Tax Processing:** High-volume transaction simulation with dynamic tax brackets and discount rules.

---

## ⚙️ Core Technical Features

### 1. Relational Database Architecture (MySQL)
The backbone of this system is a normalized relational schema designed from scratch. It models entities using strict relational constraints:
* **Referential Integrity:** Implemented Primary Keys (PK) and Foreign Keys (FK) across schemas to maintain absolute consistency between payroll data, employee details, and transactional history.
* **Data Redundancy Mitigation:** Applied normalization rules to isolate specific operational attributes, optimizing query execution times and preventing data anomalies.

### 2. Secure Data Persistency (Full CRUD Pipeline)
The system leverages a secure database connector to perform safe data execution blocks:
* **Write Operations:** Formatted queries to ingest text strings and numerical transaction parameters smoothly.
* **Safe Modifications & Deletions:** Managed system entities via parametrized data execution to handle relational cascade rules without compromising historic financial records.

### 3. Automated Business Logic Implementation (Python)
Instead of relying on basic calculations, all computational variables are driven by structured Python code mapping corporate business requirements:
* **Dynamic Tax Computations:** Engineered backend formulas to parse individual transactions and automatically calculate taxes and commercial deductions based on progressive brackets.
* **Payroll Automation:** Created functions that map dynamic work variables to calculate automated salary structures, employee benefits, and payroll logs.

---


## 📊 Sample Database Views & Verification

The database includes structured analytical layers to verify system operations:

1. **Active Inventory Balance:** Real-time logging comparing product stock, unit cost parameters, and incoming vendor deliveries.
2. **Consolidated Payroll Records:** Aggregated summary views detailing historical salary calculations, taxes withheld, and corporate payouts per department.

---
*Developed as a foundational portfolio project demonstrating robust software design, database normalization, and relational integrity mapping.*
