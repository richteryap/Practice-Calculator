import sys
import numpy as np
from scipy.optimize import approx_fprime
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
        self.operation_combo.addItem("Integral")

        # Matplotlib Canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot_axes = self.figure.add_subplot(111)

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
            return None

    def plot_function(self):
        func = self.get_function_from_input()
        if func is None:
            return

        try:
            x_min = float(self.x_min_entry.text())
            x_max = float(self.x_max_entry.text())
            x = np.linspace(x_min, x_max, 400) # More points for smoother curves
        except ValueError:
            self.plot_axes.clear()
            self.plot_axes.text(0.5, 0.5, "Invalid x-range input.", ha='center', va='center', fontsize=12, color='red')
            self.canvas.draw()
            return

        self.plot_axes.clear()
        operation = self.operation_combo.currentText()

        if operation == "Original Function":
            y = [func(val) for val in x]
            self.plot_axes.plot(x, y, label="f(x)")
            self.plot_axes.set_ylabel("f(x)")
            self.plot_axes.set_title("Original Function")
        elif operation == "First Derivative":
            try:
                def f(t):
                    return func(t)
                h = 1e-6  # Small step size for numerical differentiation
                dy = [(f(val + h) - f(val)) / h for val in x]
                self.plot_axes.plot(x, dy, label="f'(x)")
                self.plot_axes.set_ylabel("f'(x)")
                self.plot_axes.set_title("First Derivative")
            except Exception as e:
                self.plot_axes.text(0.5, 0.5, f"Error computing derivative: {e}", ha='center', va='center', fontsize=10, color='red')
        elif operation == "Integral":
            integral_values = []
            cumulative_integral = 0
            try:
                for val in x:
                    result, _ = quad(func, x_min, val)
                    integral_values.append(result)
                self.plot_axes.plot(x, integral_values, label="∫f(t)dt")
                self.plot_axes.set_ylabel("∫f(t)dt")
                self.plot_axes.set_title("Integral")
            except Exception as e:
                self.plot_axes.text(0.5, 0.5, f"Error computing integral: {e}", ha='center', va='center', fontsize=10, color='red')

        self.plot_axes.axhline(0, color='black', linewidth=0.5)
        self.plot_axes.axvline(0, color='black', linewidth=0.5)
        self.plot_axes.grid(True)
        self.plot_axes.legend()
        self.canvas.draw()

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