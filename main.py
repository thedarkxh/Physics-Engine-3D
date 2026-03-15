import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class ProjectileGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("IronVault | Kinematics Engine v3")
        self.root.geometry("1000x700")
        self.root.configure(bg='#0a0a0a')

        # --- Styles ---
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#0a0a0a")
        style.configure("TLabel", background="#0a0a0a", foreground="#ffffff", font=('Consolas', 10))
        style.configure("TButton", font=('Consolas', 10, 'bold'))

        # --- Layout ---
        self.sidebar = ttk.Frame(root, padding="20", style="TFrame")
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        self.plot_area = tk.Frame(root, bg='#0a0a0a')
        self.plot_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # --- Inputs ---
        self.create_input("Initial Velocity (m/s):", "25")
        self.create_input("Elevation Angle (deg):", "45")
        self.create_input("Azimuth Angle (deg):", "0")

        self.calc_btn = ttk.Button(self.sidebar, text="RUN SIMULATION", command=self.update_plot)
        self.calc_btn.pack(pady=20, fill=tk.X)

        # --- Initialize Plot ---
        self.fig = plt.figure(figsize=(8, 6), facecolor='#0a0a0a')
        self.ax = self.fig.add_subplot(111, projection='3d', facecolor='#0a0a0a')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_area)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.update_plot()

    def create_input(self, label_text, default_val):
        ttk.Label(self.sidebar, text=label_text).pack(anchor=tk.W, pady=(10, 0))
        entry = ttk.Entry(self.sidebar)
        entry.insert(0, default_val)
        entry.pack(fill=tk.X, pady=5)
        setattr(self, f"entry_{label_text.split()[0].lower()}", entry)

    def update_plot(self):
        # 1. Get Inputs
        try:
            u = float(self.entry_initial.get())
            theta = np.radians(float(self.entry_elevation.get()))
            phi = np.radians(float(self.entry_azimuth.get()))
            g = 9.81
        except ValueError: return

        # 2. Physics Logic
        t_flight = 2 * (u * np.sin(theta)) / g
        t = np.linspace(0, t_flight, num=200)

        vx = u * np.cos(theta) * np.cos(phi)
        vy = u * np.cos(theta) * np.sin(phi)
        vz = u * np.sin(theta)

        x = vx * t
        y = vy * t
        z = vz * t - 0.5 * g * t**2

        # 3. Render
        self.ax.clear()
        self.ax.set_facecolor('#0a0a0a')
        self.ax.tick_params(colors='white', labelsize=8)
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.zaxis.label.set_color('white')
        
        # Grid/Pane customization for Dark Mode
        self.ax.xaxis.pane.set_facecolor('#1a1a1a')
        self.ax.yaxis.pane.set_facecolor('#1a1a1a')
        self.ax.zaxis.pane.set_facecolor('#1a1a1a')
        
        self.ax.plot(x, y, z, color='#ff0000', lw=2, label="Trajectory")
        self.ax.set_title("3D Kinematics Analysis", color='white', fontfamily='Consolas')
        self.ax.set_xlabel("X (Range)")
        self.ax.set_ylabel("Y (Crossrange)")
        self.ax.set_zlabel("Z (Height)")
        
        # --- ADD THESE LINES TO LOCK THE VIEW ---
        self.ax.set_zlim(0, 50)    # Locks height to 50m
        self.ax.set_xlim(0, 100)   # Locks range to 100m
        self.ax.set_ylim(-50, 50)  # Locks crossrange
        
        self.ax.set_title("3D Kinematics Analysis", color='white', fontfamily='Consolas')
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectileGUI(root)
    root.mainloop()
