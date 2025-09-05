# 🔐 Password Strength Checker

A simple yet effective **Password Strength Checker** built with **Python + PyQt5**.  
This desktop application helps users create **strong and secure passwords** by analyzing them in real time and giving instant feedback with visual indicators.  

---

## 📖 Project Overview

The **Password Strength Checker** evaluates passwords against multiple security criteria and provides suggestions to improve them.  
It uses regex-based validation to test for **length, uppercase, lowercase, digits, and special characters**.  

* Built with **PyQt5** for a smooth, desktop-friendly UI.  
* Real-time **progress bar** shows password strength.  
* Feedback suggestions guide users towards creating strong passwords.  
* Includes **show/hide password** option for usability.  

---

## ✨ Features

✅ Real-time password strength analysis  
✅ Visual feedback with a **progress bar**  
✅ Strength classification: **Weak, Moderate, Strong**  
✅ Detailed improvement suggestions  
✅ Show/Hide password checkbox  
✅ Lightweight and beginner-friendly  

---

## 🖥️ How It Works

1. Enter your password in the input box.  
2. The app evaluates it against 5 criteria:
   - Length ≥ 8 characters  
   - At least 1 uppercase letter  
   - At least 1 lowercase letter  
   - At least 1 digit  
   - At least 1 special character  
3. Progress bar and feedback update instantly.  

---

## 🚀 Getting Started

1. Clone the repo  

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
````

2. Install dependencies

```bash
pip install pyqt5
```

3. Run the app

```bash
python PassCheck.py
```

---

## 📂 Code Structure

```
password-strength-checker/
│── PassCheck.py         # Main PyQt5 app
│── README.md            # Documentation
```

Key components in `PassCheck.py`:

* `PasswordStrengthChecker(QWidget)` → Main UI class.
* `check_strength()` → Updates progress bar & feedback in real time.
* `evaluate_password(password)` → Core logic to calculate strength score.
* `toggle_password_visibility()` → Show/Hide password option.

---

## 🎯 Use Cases

🔹 Learning password security concepts
🔹 Demonstrating UI development with PyQt5
🔹 Encouraging users to adopt stronger password practices
🔹 Fun project for students & developers

---

## 📸 Demo Screenshot

![image alt](screenshot.png)

---

## 📜 License

This project is open-source under the **MIT License**.
