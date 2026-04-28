## Heat Equation
A partial differential equation that describes how the temperature of a physical system changes over time.
It is typically written as:

```math
    \frac{\delta(u)} {\delta(t)} = k \frac{\delta(u^2)} {\delta(x^2)} 
```

We can use finite difference, such as the central difference method to approximate the derivative of a function by calculating the slope between two nearby points:

```math
f'(x) \approx \frac{f(x-h) - f(x - h)}{2h}

```

Where
```math
f'(x)
```

is the derivative at point x, h is a small interval, and 
```math
f(x)
```

is the function value at x

---
### Numerical derivation schemes
Numerical derivation schemes are techniques to approximate derivates of functions using discrete data points. Common schemes include:

- First-Order Derivative Schemes:
    - Forward Difference
    ```math
    f'(x) \approx \frac{f(x+h) - f(x)}{h} 
    ```

    - Backward Difference
    ```math
    f'(x) \approx \frac{f(x) - f(x-h)}{h} 
    ```

    - Central Difference
    ```math
    f'(x) \approx \frac{f(x+h) - f(x-h)}{2h} 
    ```
- Second-Order Derivative Schemes:
    - Three-Point Central Difference
    ```math
    f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} 
    ```

    - Five-Point Stencil
    ```math
    f''(x) \approx \frac{f(x + 2h) - 4f(x+h) + 6f(x) - 4f(x-h) + f(x - 2h)}{h^2} 
    ```
---
### Equation Discretazion
The process of convertging a continuous mathematical function to a discrete form, considering:

```math
    \frac{\delta(u)} {\delta(t)} = k \frac{\delta(u^2)} {\delta(x^2)} ,
```

and the first and second derivative equivalents:

```math
    f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} ,
```

```math
    f'(x) \approx \frac{f(x+h) - f(x)}{h} 
```

then the discretization is:

```math
    \frac{u(t + dt, x) - u(t,x)}{dt} = k \frac{u(t, x + dx) - 2u(t,x) + u(t, x - dx)}{dx^2}
```
