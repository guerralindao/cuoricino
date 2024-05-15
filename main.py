
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import time


def f(x):
  """Defines the mathematical formula."""
  return np.sqrt(np.cos(x)) * np.cos(100 * x) + np.sqrt(np.abs(x)) - 0.7


# Define x-axis values
x = np.linspace(-2, 2, 400)  # Adjust range and number of points as needed

# Define animation parameters
delay = 0.001  # Adjust delay for animation speed (seconds)
num_steps = 100  # Number of steps to simulate "compiling"

#plt.figure(figsize=(8, 6))  # Adjust figure size
plt.figure(figsize=(4, 3))  # Adjust figure size

# Initialize an empty line object
line, = plt.plot([], [])  # Initial empty plot

# Set plot limits (assuming you know the function's range)
plt.xlim(-1.5, 1.5)  # Adjust x-axis limits based on function range
plt.ylim(-1.5, 1.0)  # Adjust y-axis limits based on function range

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Il mio cuoricino sta compilando...')
plt.grid(True)
plt.legend()

# Simulate "compiling" by gradually adding data points
for i in range(num_steps):
  # Calculate a portion of the data points
  y_points = f(x[:i * len(x) // num_steps])

  # Update the line data with the calculated points
  line.set_data(x[:i * len(x) // num_steps], y_points)

  # Update the plot and introduce a delay
  plt.pause(delay)

# Plot the complete function after the simulation
plt.plot(x, f(x))
plt.legend()

plt.show()
