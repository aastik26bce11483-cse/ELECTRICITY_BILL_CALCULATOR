# Electricity Bill Calculator

A command-line application that calculates electricity bills using tiered
(slab) billing rates, validates user input, and keeps a session record of
every bill generated. Built as the Evaluated Course Project for CSE1021
(Problem Solving through Python).

## Overview
The program asks for a customer's name and units of electricity consumed,
then calculates the bill using slab-based rates plus a fixed charge. All
bills generated in a session can be viewed together with the total amount
collected.

## Features
- Calculate a new bill using 4-tier slab rates
- Automatic fixed charge added to every bill
- Input validation (empty names and invalid unit values are rejected)
- View all bills generated in the current session, with a grand total
- Simple, menu-driven command-line interface

## Technologies / Tools Used
- **Language:** Python 3
- **Libraries:** None — built entirely using Python's standard features
  (no external dependencies to install)
- **Version Control:** Git / GitHub

## Project Structure
```
electricity-bill-calculator/
├── main.py           # Entry point: menu and program flow
├── billing.py         # Slab rate calculation logic
├── validation.py       # Input validation logic
├── records.py          # Stores and retrieves session bill records
├── test_project.py     # Simple tests for billing and validation logic
├── README.md
└── statement.md         # Problem statement, scope, users, features
```

## Requirements
- Python 3.7 or higher
- No external libraries required

## Steps to Install & Run
1. **Install Python** (if not already installed):
   Download from [python.org/downloads](https://www.python.org/downloads/)
   and check "Add Python to PATH" during installation.

2. **Clone this repository:**
   ```
   git clone https://github.com/<your-username>/electricity-bill-calculator.git
   cd electricity-bill-calculator
   ```

3. **Run the program:**
   ```
   python main.py
   ```
   (Use `python3 main.py` if `python` is not recognized on your system.)

## Usage
After running, you'll see a menu:
```
===== ELECTRICITY BILL CALCULATOR =====
1. Calculate a new bill
2. View all bills
3. Exit
```
Enter the number for the action you want and follow the prompts.

## Instructions for Testing
A simple test file is included to verify the calculation and validation
logic. To run it:
```
python test_project.py
```
If everything works correctly, you'll see `ALL TESTS PASSED`.

## Slab Rate Reference
| Units          | Rate per unit |
|----------------|---------------|
| First 100      | Rs 3          |
| Next 100 (101-200) | Rs 5      |
| Next 100 (201-300) | Rs 7      |
| Above 300      | Rs 10         |

A fixed charge of Rs 50 is added to every bill.
