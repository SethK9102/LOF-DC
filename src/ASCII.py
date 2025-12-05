from PIL import Image

def image_to_ascii(image_path, output_width=100):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "Error: Image not found at the specified path."

    # Calculate aspect ratio and new height
    width, height = img.size
    aspect_ratio = height / width
    output_height = int(output_width * aspect_ratio * 0.55) # Adjust for character aspect ratio

    # Resize and convert to grayscale
    img = img.resize((output_width, output_height)).convert('L')

    # ASCII characters ordered by intensity
    ascii_chars = " .:-=+*#%@cvnxriltfjyzuaeos"
    # You can customize this string for different visual effects

    ascii_art = ""
    pixels = img.getdata()

    for pixel_value in pixels:
        # Map pixel intensity (0-255) to an ASCII character
        index = int((pixel_value / 255) * (len(ascii_chars) - 1))
        ascii_art += ascii_chars[index]

    # Format into lines
    formatted_art = ""
    for i in range(0, len(ascii_art), output_width):
        formatted_art += ascii_art[i:i+output_width] + "\n"

    return formatted_art

