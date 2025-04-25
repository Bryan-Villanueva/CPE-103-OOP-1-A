import tkinter as tk
from PIL import Image, ImageTk

# Create main window
window = tk.Tk()
window.state("zoomed")
window.resizable(False, True)

# Disable minimize
def disable_minimize():
    return

window.iconify = disable_minimize

# Load and resize the background image
image_path = "bg5.png"  # Replace with your image path
img = Image.open(image_path)

# Base monitor dimensions for scaling (reference monitor)
BASE_WIDTH = 1920
BASE_HEIGHT = 1080

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Scaling factors
scale_x = screen_width / BASE_WIDTH
scale_y = screen_height / BASE_HEIGHT

# Resize the background image to match the screen dimensions
img = img.resize((screen_width, screen_height), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

# Create a canvas
canvas = tk.Canvas(window, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Add background image to canvas
canvas.create_image(0, 0, image=photo, anchor="nw")

# Define text elements
text_elements = [
    {"text": "Dashboard", "x": 0.26, "y": 0.095, "font": ("Open Sans", 35), "tag": "dashboard", "hover": False},
    {"text": "Home", "x": 0.138, "y": 0.326, "font": ("Poppins", 30, "bold"), "tag": "home", "hover": True},
    {"text": "Assignment", "x": 0.11, "y": 0.6, "font": ("Poppins", 30, "bold"), "tag": "assignment", "hover": True},
    {"text": "Courses", "x": 0.125, "y": 0.465, "font": ("Poppins", 30, "bold"), "tag": "courses", "hover": True},
    {"text": "Quiz", "x": 0.145, "y": 0.74, "font": ("Poppins", 30, "bold"), "tag": "quiz", "hover": True},
]

# Add text elements to canvas
for element in text_elements:
    x_pos = element["x"] * scale_x * BASE_WIDTH
    y_pos = element["y"] * scale_y * BASE_HEIGHT

    text_id = canvas.create_text(
        x_pos,
        y_pos,
        text=element["text"],
        font=(element["font"][0], int(element["font"][1] * scale_y)),  # Scale font size dynamically
        fill="black",
        anchor="w",
        tags=element["tag"]
    )

    if element["hover"]:
        canvas.tag_bind(element["tag"], "<Enter>", lambda e, t=element["tag"]: canvas.itemconfig(t, fill="white"))
        canvas.tag_bind(element["tag"], "<Leave>", lambda e, t=element["tag"]: canvas.itemconfig(t, fill="black"))

# Function to reset to the home screen
def reset_home_screen():
    # Remove all dynamically created widgets
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

# Function to display "Lessons" UI for a specific course
def show_lessons(event, name):
    # Remove all dynamically created UI elements
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

    # Create a "Lessons" UI positioned to the right
    lessons_frame = tk.Frame(window, bg="#f0f0f0", width=int(screen_width * 0.4), height=screen_height)
    lessons_frame.place(x=int(screen_width * 0.6), y=0)  # Positioned to the right

    # Add title
    tk.Label(
        lessons_frame, text=f"Lessons for {name}",
        font=("Arial", int(35 * scale_y), "bold"), bg="#f0f0f0"
    ).pack(pady=int(20 * scale_y))

# Example function for dynamic UI (Courses section)
def show_courses_section():
    # Remove all dynamically created UI elements
    reset_home_screen()

    # Create a frame for "Courses"
    courses_frame = tk.Frame(window, bg="#f0f0f0", width=int(screen_width * 0.4), height=screen_height)
    courses_frame.place(x=int(screen_width * 0.6), y=0)  # Positioned to the right

    # Add title
    tk.Label(
        courses_frame, text="Courses",
        font=("Arial", int(35 * scale_y), "bold"), bg="#f0f0f0"
    ).pack(pady=int(20 * scale_y))

    # Add placeholder courses
    tk.Label(
        courses_frame, text="Math 101", font=("Arial", int(15 * scale_y)), bg="#f0f0f0"
    ).pack(anchor="w", padx=int(20 * scale_x), pady=int(10 * scale_y))
    tk.Label(
        courses_frame, text="Physics 101", font=("Arial", int(15 * scale_y)), bg="#f0f0f0"
    ).pack(anchor="w", padx=int(20 * scale_x), pady=int(10 * scale_y))
    tk.Label(
        courses_frame, text="Programming 101", font=("Arial", int(15 * scale_y)), bg="#f0f0f0"
    ).pack(anchor="w", padx=int(20 * scale_x), pady=int(10 * scale_y))

# Bind click events to "Home" and "Courses"
canvas.tag_bind("home", "<Button-1>", lambda e: reset_home_screen())
canvas.tag_bind("courses", "<Button-1>", lambda e: show_courses_section())

# Keep a reference to the background image
canvas.image = photo

# Start the Tkinter event loop
window.mainloop()
