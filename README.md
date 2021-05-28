# Cubic interpolation animation

This project contains a cubic interpolation animation, applied onto a $\sin(x)$ function.

## Cubic Spline interpolation

The interpolation algorithm is documented extensively on the [scipy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html?highlight=cubicspline#scipy.interpolate.CubicSpline).

## Usage

Create a virtual environment using Python's `venv` module.
In case `venv` is not installed, install it using:

```commandline
python -m pip install venv
```

Create the virtual environment:

```commandline
python -m venv venv
```

### Windows

In case you're running Windows (outside the WSL):

```commandline
./venv/Scripts/activate
```

### Unix-like

In Unix-like environments (such as Linux or MacOS):

```commandline
source venv/bin/activate
```
