import tkinter as tk

class SensorDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensor Display")
        
        self.sensor_value = tk.DoubleVar(value=25.0)
        self.sensor_unit = "°C"
        self.low_value = 0.0
        self.high_value = 50.0

        self.label = tk.Label(root, text="Sensor Value: ", font=("Arial", 12))
        self.label.pack()

        self.canvas = tk.Canvas(root, width=300, height=100, bg="white")
        self.canvas.pack()
        self.update_display()

        self.entry = tk.Entry(root, textvariable=self.sensor_value, font=("Arial", 12))
        self.entry.pack()

        self.update_button = tk.Button(root, text="Update", command=self.update_display)
        self.update_button.pack()

    def update_display(self):
        try:
            new_value = self.sensor_value.get()
            if new_value < self.low_value or new_value > self.high_value:
                raise ValueError("Value out of range")

            self.canvas.delete("all")

            percentage = (new_value - self.low_value) / (self.high_value - self.low_value)
            bar_width = int(percentage * 300)
            self.canvas.create_rectangle(10, 10, 10 + bar_width, 90, fill="blue")

            display_text = f"{new_value:.1f} {self.sensor_unit}"
            self.label.config(text="Sensor Value: " + display_text)

        except ValueError as e:
            self.label.config(text="Sensor Value: Invalid input")
        except Exception as e:
            self.label.config(text="Sensor Value: Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = SensorDisplayApp(root)
    root.mainloop()
