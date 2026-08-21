# ArtyCalc

A high-fidelity Python-based physics simulation that calculates the 2D trajectory of artillery shells. The engine uses a numerical integration method (Euler-Maruyama method) to compute instantaneous velocities and positions, accounting for gravity and variable atmospheric aerodynamic drag using the International Standard Atmosphere (ISA) model.

## 🚀 Features
* **Two-Layer Atmosphere Model:** Calculates realistic aerodynamic drag profiles by dynamically shifting between the troposphere (under 11,000m) and the stratosphere (above 11,000m) density equations.
* **Sub-timestep Linear Interpolation:** Employs precise boundary landing approximations to capture exact impact coordinate offsets even when the final step falls below the horizon grid line (`y < 0`).

## ⚙️ Setup and Running
1. Clone this repository to your local system.
2. Ensure both `main.py` and `shells.py` are located in the exact same directory.
3. Run the script in bash:
   ```bash
   python main.py
   ```

## 📈 Roadmap
* [ ] Integrate `matplotlib` to export high-definition trajectory plots showing X vs Y positions.
* [ ] Implement an automated metric-to-imperial converter for flexible user inputs.
* [ ] Expand `shells.py` with an exhaustive list of standard NATO and Eastern Bloc calibres (e.g., 105mm, 122mm, 203mm).
* [ ] Introduce 3D vector calculations to account for crosswinds and the Coriolis effect.

## 🤖 AI Disclosure
*The use of Artificial Intelligence was limited in this project and will be. (Mainly used for research purposes.)*

