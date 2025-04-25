import sys
import numpy as np
from scipy.integrate import quad
import sympy
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QComboBox, QSizePolicy)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class FunctionVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Function Visualizer")

        # Input Widgets
        self.function_label = QLabel("Enter function (Python syntax):")
        self.function_entry = QLineEdit()
        self.x_min_label = QLabel("X-min:")
        self.x_min_entry = QLineEdit("-5")
        self.x_max_label = QLabel("X-max:")
        self.x_max_entry = QLineEdit("5")
        self.calculate_button = QPushButton("Calculate and Plot")
        self.operation_label = QLabel("Operation:")
        self.operation_combo = QComboBox()
        self.operation_combo.addItem("Original Function")
        self.operation_combo.addItem("First Derivative")
        self.operation_combo.addItem("Second Derivative")
        self.operation_combo.addItem("Integral")

        # Matplotlib Canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot_axes = self.figure.add_subplot(111)

        # Output Label
        self.output_label = QLabel("")
        self.output_label.setAlignment(Qt.AlignCenter)

        # Layout
        input_layout = QGridLayout()
        input_layout.addWidget(self.function_label, 0, 0)
        input_layout.addWidget(self.function_entry, 0, 1, 1, 2)
        input_layout.addWidget(self.x_min_label, 1, 0)
        input_layout.addWidget(self.x_min_entry, 1, 1)
        input_layout.addWidget(self.x_max_label, 1, 2)
        input_layout.addWidget(self.x_max_entry, 1, 3)
        input_layout.addWidget(self.operation_label, 2, 0)
        input_layout.addWidget(self.operation_combo, 2, 1, 1, 3)
        input_layout.addWidget(self.calculate_button, 3, 0, 1, 4)

        plot_layout = QVBoxLayout()
        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(plot_layout)
        main_layout.addWidget(self.output_label)

        self.setLayout(main_layout)

        # Connect button to calculation and plotting function
        self.calculate_button.clicked.connect(self.plot_function)

    def get_function_from_input(self):
        function_str = self.function_entry.text().strip()
        try:
            x = sympy.Symbol('x')
            from sympy.parsing.sympy_parser import parse_expr
            function = parse_expr(function_str)
            return sympy.lambdify(x, function)
        except (SyntaxError, TypeError):
            self.plot_axes.clear()
            self.plot_axes.text(0.5, 0.5, "Invalid function input.", ha='center', va='center', fontsize=12, color='red')
            self.canvas.draw()
            self.output_label.setText("Invalid function input.")
            return None

    def plot_function(self):
        function_str = self.function_entry.text().strip()
        try:
            x_sym = sympy.Symbol('x')
            from sympy.parsing.sympy_parser import parse_expr
            original_function_sym = parse_expr(function_str)
            func = sympy.lambdify(x_sym, original_function_sym)
        except (SyntaxError, TypeError):
            self.plot_axes.clear()
            self.plot_axes.text(0.5, 0.5, "Invalid function input.", ha='center', va='center', fontsize=12, color='red')
            self.canvas.draw()
            self.output_label.setText("Invalid function input.")
            return

        try:
            x_min = float(self.x_min_entry.text())
            x_max = float(self.x_max_entry.text())
            x_num = np.linspace(x_min, x_max, 400).round(3) # Round x-values as well
        except ValueError:
            self.plot_axes.clear()
            self.plot_axes.text(0.5, 0.5, "Invalid x-range input.", ha='center', va='center', fontsize=12, color='red')
            self.canvas.draw()
            self.output_label.setText("Invalid x-range input.")
            return

        self.plot_axes.clear()
        operation = self.operation_combo.currentText()

        if operation == "Original Function":
            y = [round(func(val), 3) for val in x_num]
            self.plot_axes.plot(x_num, np.array(y).round(3), label="f(x)") # Round again for good measure
            self.plot_axes.set_ylabel("f(x)")
            self.plot_axes.set_title("Original Function")
            self.output_label.setText("")
        elif operation == "First Derivative":
            try:
                first_derivative_sym = sympy.diff(original_function_sym, x_sym)
                simplified_derivative = sympy.simplify(first_derivative_sym)
                first_derivative_func = sympy.lambdify(x_sym, simplified_derivative)
                dy = [round(first_derivative_func(val), 3) for val in x_num]
                self.plot_axes.plot(x_num, np.array(dy).round(3), label="f'(x)") # Round again
                self.plot_axes.set_ylabel("f'(x)")
                self.plot_axes.set_title("First Derivative")
                self.output_label.setText(f"First Derivative: {simplified_derivative}")
            except Exception as e:
                self.plot_axes.text(0.5, 0.5, f"Error computing derivative: {e}", ha='center', va='center', fontsize=10, color='red')
                self.output_label.setText(f"Error computing derivative: {e}")
        elif operation == "Second Derivative":
            try:
                first_derivative_sym = sympy.diff(original_function_sym, x_sym)
                second_derivative_sym = sympy.diff(first_derivative_sym, x_sym)
                simplified_second_derivative = sympy.simplify(second_derivative_sym)
                second_derivative_func = sympy.lambdify(x_sym, simplified_second_derivative)
                dy2 = [round(second_derivative_func(val), 3) for val in x_num]
                self.plot_axes.plot(x_num, np.array(dy2).round(3), label="f''(x)") # Round again
                self.plot_axes.set_ylabel("f''(x)")
                self.plot_axes.set_title("Second Derivative")
                self.output_label.setText(f"Second Derivative: {simplified_second_derivative}")
            except Exception as e:
                self.plot_axes.text(0.5, 0.5, f"Error computing second derivative: {e}", ha='center', va='center', fontsize=10, color='red')
                self.output_label.setText(f"Error computing second derivative: {e}")
        elif operation == "Integral":
            try:
                integral_values_full = []
                for val in x_num:
                    result, _ = quad(func, x_min, val)
                    integral_values_full.append(result)
                integral_values = [round(val, 3) for val in integral_values_full]
                self.plot_axes.plot(x_num, np.array(integral_values).round(3), label="∫f(t)dt") # Round again
                self.plot_axes.set_ylabel("∫f(t)dt")
                self.plot_axes.set_title("Integral")
                integral_sym = sympy.integrate(original_function_sym, x_sym)
                simplified_integral = sympy.simplify(integral_sym)
                self.output_label.setText(f"Integral: {simplified_integral} + C (plotted numerically)")
            except Exception as e:
                self.plot_axes.text(0.5, 0.5, f"Error computing integral: {e}", ha='center', va='center', fontsize=10, color='red')
                self.output_label.setText(f"Error computing integral: {e}")

        self.plot_axes.axhline(0, color='black', linewidth=0.5)
        self.plot_axes.axvline(0, color='black', linewidth=0.5)
        self.plot_axes.grid(True)
        self.plot_axes.legend()
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionVisualizer()
    window.show()
    sys.exit(app.exec_())