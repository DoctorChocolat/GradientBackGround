import tkinter as tk
from tkinter import colorchooser

def create_gradient(canvas, width, height, start_color, end_color):
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    r_step = (end_rgb[0] - start_rgb[0]) / height
    g_step = (end_rgb[1] - start_rgb[1]) / height
    b_step = (end_rgb[2] - start_rgb[2]) / height

    for i in range(height):
        r = int(start_rgb[0] + (r_step * i))
        g = int(start_rgb[1] + (g_step * i))
        b = int(start_rgb[2] + (b_step * i))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color, width=1)

def choose_colors():
    start_color = colorchooser.askcolor(title="Choose Start Color")[1]
    end_color = colorchooser.askcolor(title="Choose End Color")[1]
    if start_color and end_color:
        create_gradient(canvas, width, height, start_color, end_color)

def main():
    global canvas, width, height
    root = tk.Tk()
    root.title("Gradient Background")

    width, height = 800, 800
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # Add a button to choose colors
    button = tk.Button(root, text="Choose Colors", command=choose_colors)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
