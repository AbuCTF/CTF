from PIL import Image, ImageDraw

# Open the original image
image = Image.open("confidential.jpg")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the color for the markers (e.g., red)
marker_color = "red"

# Define the size of the marker (in pixels)
marker_size = 5

# Read coordinates from the file
with open("5ecret_c0de.txt", "r") as file:
    # Read each line containing coordinates
    for line in file:
        # Remove parentheses and split the line into x and y coordinates
        x, y = map(int, line.strip()[1:-1].split(","))
        # Draw a marker at the coordinate
        draw.rectangle((x - marker_size, y - marker_size, 
                        x + marker_size, y + marker_size), 
                       fill=marker_color)

# Save the modified image with markers
image.save("marked_image.jpg")

# Close the image
image.close()
