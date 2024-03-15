from PIL import Image, ImageSequence

def make_gif_more_opaque(input_path, output_path, opacity=0.5):
    with Image.open(input_path) as img:
        frames = []
        for frame in ImageSequence.Iterator(img):
            # Convert the frame to RGBA mode if it's not already
            frame = frame.convert("RGBA")

            # Get the alpha channel and apply opacity
            alpha = frame.getchannel("A")
            alpha = alpha.point(lambda p: int(p * opacity))
            frame.putalpha(alpha)

            frames.append(frame)

        # Save the modified frames as a new GIF
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0, duration=img.info['duration'])

# Example usage
input_gif_path = "./images/regionRed.png"
output_gif_path = "./images/regionRed2.png"
make_gif_more_opaque(input_gif_path, output_gif_path, opacity=0.7)
