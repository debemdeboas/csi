import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from typing import Any
from scipy.interpolate import CubicSpline


def gen_function():
    """Function position generator

    Calculates the x and y positions for a given x.
    Calculates the cubic spline for the given x value in `x_points`.

    Iterates to and fro the list, creating a nicer animation.

    Yields:
        Tuple: Tuple of (x, y) coordinates
    """    
    x_list = list(x_points)
    while True:
        for x in x_list:
            yield x, cs(x)
        for x in reversed(x_list):
            yield x, cs(x)


def update(frame, *fargs) -> Any:
    """Update the point's position

    Args:
        frame: tuple returned by the `frames` generator

    Returns:
        Any: the updated point
    """
    point.set_data(frame[0], frame[1])
    return point

# Get figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
# Create the point object for the animation
point, = ax.plot([], [], marker='o', color='crimson', ms=15)

# Generate a sample from 0 to 10 with 1 increment between values
x = np.arange(10)
# Reference to the sine function
y = np.sin
# Create the Cubic Spline object with the x points and y(x)
cs = CubicSpline(x, y(x))

# Generate a sample from -0.5 to 9.6 with 0.1 increment between values
x_points = np.arange(-0.5, 9.6, 0.1)
# Generate a smaller sample, from -0.5 to 9.6 with 1 increment between values
x_points_less_samples = np.arange(-0.5, 9.6, 1)

# Plot y=sin(x)
ax.plot(x_points, y(x_points), label='sin(x)')
# Plot y=Cubic_Interpolation(sin(x))
ax.plot(x_points, cs(x_points), label='B-Spline(sin(x))')
# Plot the cubic interpolation function but with a smaller sample size
ax.plot(x_points_less_samples, cs(x_points_less_samples), '-o', label='control points')

# Legend position
ax.legend(loc='lower left')

# Set the minimum and maximum `x` values
ax.set_xlim(-0.5, 9.5)

# Animation object
ani = animation.FuncAnimation(
    fig, update, interval=25, repeat=True, frames=gen_function)

# Show the figure
plt.show()
