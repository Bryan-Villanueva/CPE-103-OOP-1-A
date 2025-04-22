import tkinter as tk
from PIL import Image, ImageTk

# Create main window
window = tk.Tk()
window.state("zoomed")
window.resizable(False, False)


# Disable minimize
def disable_minimize():
    return


window.iconify = disable_minimize

# Load and resize the background image
image_path = "bg4.png"  # Replace with your image
img = Image.open(image_path)
img = img.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

# Create a canvas
canvas = tk.Canvas(window, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Add background image to canvas
canvas.create_image(0, 0, image=photo, anchor="nw")

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Define text elements
text_elements = [
    # Dashboard (no hover effect)
    {"text": "Dashboard", "x": 0.26, "y": 0.1, "font": ("Open Sans", 35), "tag": "dashboard", "hover": False},

    # Interactive elements (will turn white on hover)
    {"text": "Profile", "x": 0.115, "y": 0.385, "font": ("Poppins", 30, "bold"), "tag": "profile", "hover": True},
    {"text": "Assignment", "x": 0.085, "y": 0.63, "font": ("Poppins", 30, "bold"), "tag": "assignment", "hover": True},
    {"text": "Courses", "x": 0.366, "y": 0.385, "font": ("Poppins", 30, "bold"), "tag": "courses", "hover": True},
    {"text": "Quiz", "x": 0.385, "y": 0.63, "font": ("Poppins", 30, "bold"), "tag": "quiz", "hover": True},
]

# Add text elements to canvas
for element in text_elements:
    x_pos = element["x"] * screen_width
    y_pos = element["y"] * screen_height

    text_id = canvas.create_text(
        x_pos,
        y_pos,
        text=element["text"],
        font=element["font"],
        fill="black",
        anchor="w",
        tags=element["tag"]
    )

    # Only bind hover events if enabled
    if element["hover"]:
        canvas.tag_bind(element["tag"], "<Enter>", lambda e, t=element["tag"]: canvas.itemconfig(t, fill="white"))
        canvas.tag_bind(element["tag"], "<Leave>", lambda e, t=element["tag"]: canvas.itemconfig(t, fill="black"))

# Keep image reference
canvas.image = photo

window.mainloop()