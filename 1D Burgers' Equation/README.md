## 1D Burgers' Equation

The one-dimensional Burgers' equation is a classical nonlinear partial differential equation widely used as a simplified model for fluid flow, traffic dynamics, and wave propagation. It captures the balance between nonlinear convection and diffusion, making it an excellent benchmark problem for studying shock formation and numerical methods for conservation laws.

- **Viscous Burgers' Equation:**

```math
\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x}
= \nu \frac{\partial^2 u}{\partial x^2}
```

where:

- \(u(x,t)\) is the dependent variable (e.g., velocity),
- \(x\) is the spatial coordinate,
- \(t\) is time,
- \(\nu\) is the viscosity coefficient.

The nonlinear convective term may lead to the development of steep gradients or shock-like structures, while the diffusion term acts to smooth the solution.

## Numerical Approach

The equation will be solved using a **Total Variation Diminishing (TVD)** method. TVD schemes are designed to accurately capture sharp gradients and discontinuities while preventing spurious numerical oscillations. By incorporating flux limiters, these methods achieve high resolution in smooth regions and maintain stability near shocks.

The objective of this study is to analyze the temporal evolution of the Burgers' equation solution and evaluate the capability of the TVD scheme to resolve nonlinear wave propagation and shock formation.
```