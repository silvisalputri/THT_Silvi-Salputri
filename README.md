# THT QA Automation - Silvi Salputri

This repository contains automated test scripts for both **web** and **mobile** applications of the THT project using **Pytest**, **Selenium**, and **Appium**.

## 📁 Project Structure

THT_QA_Silvi/
│
├── tests/
│ ├── web/ # Web test cases (pytest + selenium)
│ └── mobile/ # Mobile test cases (pytest + appium)
│
├── pages/
│ ├── web/ # Web Page Object files
│ └── mobile/ # Mobile Page Object files
│
├── conftest.py # Fixtures (WebDriver/Appium setup, login helper, etc.)
├── requirements.txt # Python dependencies
└── README.md # Project info

## ✅ Features

- Automated test cases for:
  - Web: Add Company, Verify Company Data, Upload Documents, Login Error Handling, etc.
  - Mobile: Login, Launch App, Error Handling for failed master data, etc.
- Uses Page Object Model (POM)
- Pytest fixtures for reusable setup and teardown
