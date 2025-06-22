## 🔧 Selenium Test Automation for "OrangeHRM Website" ##

# 🌐 Project Overview

This repository contains **automated UI and functional test scripts** developed using **Python, Selenium WebDriver**, and the **Page Object Model (POM)** for:

🔗 [OrangeHRM Website](https://www.orangehrm.com/)

> OrangeHRM is a leading HR management platform that offers intuitive and powerful tools for businesses. This test automation project focuses on verifying the functionality, usability, and UI consistency of OrangeHRM's main website using real-world test scenarios.

---

## ✅ What This Project Covers

I created **modular, reusable test scripts for each page and section of the website**. Each script covers:

- Functional testing of forms, buttons, and page content  
- UI validations and navigation behavior  
- Page redirects and links  
- Form validation (positive and negative flows)  
- Visual and functional responsiveness checks  
- Clean architecture following the **Page Object Model (POM)**  

Test scripts are written with maintainability and scalability in mind for professional QA environments.

---

## 📄 Pages and Features Tested

Scripts were created **page-by-page** and fully test the following:

- **Home Page**  
- **Contact Sales Page**  
- **Free Trial Page**  
- **Employee Management Page**  
- **People Management Page**  
- **Header & Footer Components**  
- **Book a Demo Flow**  
- **Language Selector**  
- **Form Submissions and Validations**

Each test scenario is designed to simulate real user interactions and validate business-critical functionality.

---

## 🧾 Test Case Documentation

All **manual test cases** are well-documented and organized in the file below:

📄 [`Test_cases.md`](./Test_cases.md)

This includes:

- UI validations  
- Navigation and link behaviors  
- Responsive element checks  
- Positive/negative form submissions  
- Accessibility and SEO elements  
- Page-specific feature testing

---

## 🧰 Tech Stack Used

| Tool/Library         | Description                             |
|----------------------|-----------------------------------------|
|  Python 3.x          | Core programming language               |
|  Selenium WebDriver  | For web automation                      |
|  PyTest              | Testing framework                       |
|  POM Pattern         | Page-level test architecture            |
|  ChromeDriver        | For browser testing                     |
|  GitHub              | Version control and code hosting        |

---

## 📁 Project Structure
<pre>

OrangeHRM-Automation/
│
├── tests/                            # ✅ Test scripts (named *_test.py)
│   ├── home_test.py
│   ├── contact_sales_test.py
│   ├── free_trial_test.py
│   ├── employee_management_test.py
│   ├── people_management_test.py
│   └── ...
│  
├── pages/                            # 📄 Page Object classes (named *_page.py)
│   ├── home_page.py
│   ├── contact_sales_page.py
│   ├── free_trial_page.py
│   ├── employee_management_page.py
│   ├── people_management_page.py
│   └── ...
│
├── Test_cases.md                     # 📋 Manual test cases in markdown table
├── requirements.txt                  # 📦 Python dependencies
├── conftest.py                       # 🔧 Pytest fixtures (browser setup)
├── README.md                         # 📘 Project overview and instructions
└── .gitignore                        # 🛑 Files to exclude from Git

</pre>

---

## ▶ How to Run the Tests

### 1. Install Dependencies

```bash
pip install -r requirements.txt
