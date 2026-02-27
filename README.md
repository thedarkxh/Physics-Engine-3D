# 🚀 3D Ballistic Trajectory & Kinematics Simulator

An interactive 3D physics engine built to visualize projectile motion in a Cartesian coordinate system. This project was developed as a bridge between **JEE Advanced Physics** concepts and **Computational Engineering**.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Z9dcVIRoKI9NHQIv0hZ8Cznzka-XsSeu?usp=sharing)
> **Note:** GitHub may show an "Invalid Notebook" error because of the interactive sliders. Please click the button above to run the full simulation in Google Colab.

## 🔬 Core Physics Analysis
The simulator resolves initial velocity $u$ into three-dimensional components:
- $V_x = u \cos(\theta) \cos(\phi)$
- $V_y = u \cos(\theta) \sin(\phi)$
- $V_z = u \sin(\theta)$

### Displacement vs. Distance
One of the key features of this engine is the distinction between:
1. **Net Displacement:** The straight-line vector from origin to landing point $|\vec{s}| = \sqrt{x^2 + y^2 + z^2}$.
2. **Total Path Distance:** Calculated via numerical integration (Arc Length) of the trajectory:
   $$d = \int_{0}^{t} \sqrt{v_x^2 + v_y^2 + v_z^2} \, dt$$

## 🛠️ Features
- **3D Interactive UI:** Real-time sliders for Velocity, Elevation ($\theta$), and Azimuth ($\phi$).
- **Dynamic Scaling:** Axes automatically adjust to prevent "clipping" at high angles (e.g., $85^\circ$).
- **Ground Projection:** Dashed tracing to visualize the horizontal range relative to altitude.

## 🇯🇵 Aiming for Japan (MEXT)
This project serves as a technical demonstration of my readiness for undergraduate engineering studies in Japan, focusing on **Applied Physics** and **Scientific Computing**.
