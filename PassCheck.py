import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QCheckBox, QProgressBar
)
from PyQt5.QtCore import Qt


class PasswordStrengthChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔐 Password Strength Checker")
        self.setGeometry(500, 200, 400, 200)

        layout = QVBoxLayout()

        # Instruction label
        self.label = QLabel("Enter your password:")
        layout.addWidget(self.label)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.textChanged.connect(self.check_strength)
        layout.addWidget(self.password_input)

        # Show/Hide password checkbox
        self.show_password_checkbox = QCheckBox("Show Password")
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        layout.addWidget(self.show_password_checkbox)

        # Strength label
        self.strength_label = QLabel("Strength: ")
        layout.addWidget(self.strength_label)

        # Progress bar for strength level
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        layout.addWidget(self.progress)

        # Feedback label
        self.feedback_label = QLabel("")
        layout.addWidget(self.feedback_label)

        self.setLayout(layout)

    def toggle_password_visibility(self, state):
        if state == Qt.Checked:
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

    def check_strength(self):
        password = self.password_input.text()
        score, feedback = self.evaluate_password(password)

        # Update progress bar
        self.progress.setValue(score)

        # Update strength label
        if score < 40:
            strength = "Weak"
        elif score < 70:
            strength = "Moderate"
        else:
            strength = "Strong"

        self.strength_label.setText(f"Strength: {strength}")
        self.feedback_label.setText(feedback)

    def evaluate_password(self, password):
        score = 0
        feedback = []

        # Criteria checks
        if len(password) >= 8:
            score += 20
        else:
            feedback.append("❌ Use at least 8 characters")

        if re.search(r"[A-Z]", password):
            score += 20
        else:
            feedback.append("❌ Add an uppercase letter")

        if re.search(r"[a-z]", password):
            score += 20
        else:
            feedback.append("❌ Add a lowercase letter")

        if re.search(r"\d", password):
            score += 20
        else:
            feedback.append("❌ Include a number")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 20
        else:
            feedback.append("❌ Add a special character")

        if score == 100:
            feedback = ["✅ Strong password!"]

        return score, "\n".join(feedback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordStrengthChecker()
    window.show()
    sys.exit(app.exec_())
