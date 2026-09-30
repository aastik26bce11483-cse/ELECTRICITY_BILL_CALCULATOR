# Project Statement: Electricity Bill Calculator

## Problem Statement
Manually calculating residential electricity bills under tiered or slab-based tariff structures is time-consuming, prone to calculation errors, and lacks immediate transparency for consumers. Small utility administrators, property managers, and individual households need an accessible, automated, and reliable tool to compute progressive energy tariffs, apply standard fixed administrative charges, and track running bill totals within a session.

---

## Scope of the Project

### In-Scope
* **Tiered Energy Calculation:** Progressive pricing based on monthly unit consumption:
  * First 100 units at Rs. 3/unit
  * Next 100 units (101–200) at Rs. 5/unit
  * Next 100 units (201–300) at Rs. 7/unit
  * Units exceeding 300 at Rs. 10/unit
* **Fixed Base Fee:** Mandatory base charge of Rs. 50 automatically included in each computed bill.
* **Input Validation:** Verification of non-empty customer names and non-negative integer values for units consumed.
* **Session Tracking:** In-memory retention of all bills generated during the active terminal session, with running cumulative revenue calculation.
* **Command-Line Interface:** Menu-driven terminal navigation for calculating new bills, viewing history, and exiting cleanly.

### Out-of-Scope
* Persistent data storage (e.g., SQLite, PostgreSQL, CSV, or JSON export across restarts).
* Commercial or industrial multi-tariff configurations.
* Graphical User Interface (GUI) or web deployment.
* Integrated digital payment gateways or automated PDF receipt exporting.

---

## Target Users
* **Property Managers & Landlords:** Individuals managing sub-metered rental properties or shared housing who need to split power costs accurately.
* **Domestic Consumers:** Homeowners and tenants wanting to audit or estimate their utility bills against physical meter readings.
* **Academic Learners & Instructors:** Computer science students examining foundational programming constructs (branching logic, functions, loops, lists, and input validation in Python).

---

## High-Level Features
* **Progressive Slab Computation Engine:** Accurately partitions electricity consumption across predefined marginal price bands.
* **Transparent Cost Breakdown:** Displays an itemized summary for each invoice showing units consumed, energy charges, fixed administrative fees, and total due.
* **Session History & Ledger:** Provides a summary list of all generated bills along with a cumulative total of all amounts collected during runtime.
* **Defensive Input Handling:** Rejects invalid, non-digit inputs and empty identifiers, prompting the user without crashing the runtime environment.
* **Interactive Menu Navigation:** Clear loop-driven CLI enabling repeated calculations and reporting until the user chooses to exit.