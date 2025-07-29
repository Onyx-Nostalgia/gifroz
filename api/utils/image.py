import io
import logging

from PIL import Image, ImageSequence


def add_watermark_to_image_sequence(image_bytes_data: bytes, logo_path: str, padding: int = 0, fixed_logo_width: int = 100, opacity: float = 0.8) -> bytes | None:
    """
    Adds a watermark logo to the bottom-right corner of each frame of an image sequence (GIF or WebP).

    Args:
        image_bytes_data (bytes): The raw bytes data of the input GIF or WebP file.
        logo_path (str): Path to the logo image file (preferably with transparency).
        padding (int): Padding from the bottom and right edges in pixels. Defaults to 0.
        fixed_logo_width (int): Desired fixed width for the logo in pixels.
        opacity (float): Opacity of the watermark (0.0 to 1.0).
    
    Returns:
        bytes: The raw bytes data of the watermarked image sequence file (same format as input).
    """
    try:
        logo = Image.open(logo_path).convert("RGBA")
        
        image_sequence = Image.open(io.BytesIO(image_bytes_data))
        original_format = image_sequence.format # Get original format (e.g., 'GIF', 'WEBP')

        frames = []
        
        original_disposal = image_sequence.info.get("disposal", 0) 

        logo_width, logo_height = logo.size
        target_logo_height = int(fixed_logo_width * (logo_height / logo_width))
        resized_logo = logo.resize((fixed_logo_width, target_logo_height), Image.Resampling.LANCZOS)

        if opacity < 1.0:
            alpha = resized_logo.split()[-1]
            alpha = Image.eval(alpha, lambda x: int(x * opacity))
            resized_logo.putalpha(alpha)

        for frame in ImageSequence.Iterator(image_sequence):
            current_frame = frame.convert("RGBA")

            position_x = current_frame.width - resized_logo.width - padding
            position_y = current_frame.height - resized_logo.height - padding

            watermarked_frame = current_frame.copy()
            watermarked_frame.paste(resized_logo, (position_x, position_y), resized_logo)
            
            # Convert to RGB before quantization for better GIF compatibility and to avoid transparency issues.
            # Quantize to P mode (palette mode) for GIF.
            quantized_frame = watermarked_frame.convert("RGB").quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
            
            frames.append(quantized_frame)
            
        save_args = {
            "save_all": True,
            "append_images": frames[1:],
            "duration": image_sequence.info.get("duration", 100),
            "loop": image_sequence.info.get("loop", 0),
            "disposal": original_disposal
        }

        # Save the modified frames to a BytesIO object instead of a file
        output_buffer = io.BytesIO()
        frames[0].save(output_buffer, format=original_format, **save_args)
        output_buffer.seek(0) # Rewind the buffer to the beginning

        logging.info("Watermark added successfully in-memory.")
        return output_buffer.getvalue()

    except FileNotFoundError:
        logging.error("Error: Logo file not found. Please check path.")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None