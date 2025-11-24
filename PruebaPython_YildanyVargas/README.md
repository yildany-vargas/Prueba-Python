## English

# Inventory & Sales Management System  
Python Project – Performance Test (Module 1)

This project is a **console-based Python system** designed to manage a bookstore inventory, register sales, and generate dynamic reports.  
It fully follows the requirements of the Module 1 performance test and is written in simple, beginner-friendly English.

---

## 📌 System Purpose

As the digital manager of a national bookstore, this system helps you:

- Register, consult, update, and delete products.
- Register sales including client, product, quantity, date, and optional discount.
- Validate stock and update it automatically.
- Generate reports such as:
  - Top 3 best-selling products
  - Sales grouped by author
  - Gross and net income
- Evaluate inventory performance based on sales.

---

## 📁 Project Structure

PruebaPython_YildanyVargas/
│
├── main.py
├── inventory.py
├── sales_reports.py
└── README.md


- **main.py:** interactive menu and option handling  
- **inventory.py:** full inventory management  
- **sales_reports.py:** sales registration and analytical reports  

---

## 📦 1. Inventory Management

Each product contains:

- Title  
- Author  
- Category  
- Price  
- Quantity  

Available actions:

- Add product  
- Search product  
- Update price  
- Update quantity  
- Delete product  
- View inventory  
- Calculate total inventory value  

---

## 💰 2. Sales Registration

A sale includes:

- Client  
- Product  
- Quantity  
- Automatic date  
- Optional discount  

The system:

- Validates available stock  
- Updates the inventory  
- Calculates gross and net income  

---

## 📊 3. Reporting Module

The system generates:

1. **Top 3 best-selling products**  
2. **Sales grouped by author**  
3. **Gross vs net income**  

---

## ✔ Validations Implemented

- Text fields: only letters and spaces  
- Numeric fields: positive values  
- No sales allowed with insufficient stock  
- Exception handling prevents program crashes  

---

## 🧠 Modular Design

- Functions with parameters and return values  
- Nested dictionaries + lists for storage  
- A **lambda function** for inventory value calculation  
- Clean, simple organization into 3 modules  

---

## 🚀 How to Run

python main.py


---

## 🟩 Conclusion

This project **meets 100% of the official requirements**:

- Inventory management  
- Sales and discounts  
- Dynamic reports  
- Validations  
- Exceptions  
- Modular structure  
- Lambda usage  
- 5 pre-loaded products  
- Fully English-based interaction  


**Yildany Mayerly Vargas Zapata**
**1035236502**
**Clan Thompson**