import cairo
import cairocffi

def write_text_on_image(image_path, text, output_path="modified_image.png"):
    """Writes text on an existing image using Cairo."""

    try:
        # Load image
        surface = cairocffi.ImageSurface.create_from_png(image_path)
        ctx = cairo.Context(surface) #surface is compatible with cairo.Surface

        # Set font
        ctx.select_font_face("arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(40)

        # Set text color
        ctx.set_source_rgb(0, 0, 0)

        # Draw the text
        ctx.move_to(100, 100)
        ctx.show_text(text)

        # Save the modified image
        surface.write_to_png(output_path)
        print(f"Text written on image and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    user_phrase = input("What shall we illuminate today?\n")
    image_path = "assets/half-colorful.png"
    write_text_on_image(image_path, user_phrase)


if __name__ == "__main__":
    main()