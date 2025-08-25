import os
from PIL import Image, ImageDraw, ImageFont

def make_placeholder(image_path, output_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size

            # Create a gray placeholder background
            placeholder = Image.new("RGB", (width, height), color=(180, 180, 180))

            # Add text with image dimensions
            draw = ImageDraw.Draw(placeholder)
            text = f"{width}x{height}"

            try:
                font = ImageFont.truetype("arial.ttf", size=int(min(width, height) / 6))
            except:
                font = ImageFont.load_default()

            # ✅ Correct method for Pillow >= 10
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_position = ((width - text_width) // 2, (height - text_height) // 2)

            draw.text(text_position, text, fill=(0, 0, 0), font=font)

            # Save placeholder
            placeholder.save(output_path)
            print(f"✅ Created placeholder for {image_path}")
    except Exception as e:
        print(f"❌ Error processing {image_path}: {e}")


def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        # Keep directory structure
        rel_path = os.path.relpath(root, input_dir)
        target_dir = os.path.join(output_dir, rel_path)
        os.makedirs(target_dir, exist_ok=True)

        for file in files:
            input_path = os.path.join(root, file)
            output_path = os.path.join(target_dir, file)

            # Handle image files
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif")):
                make_placeholder(input_path, output_path)
            else:
                # Copy other files unchanged
                if not os.path.exists(output_path):
                    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
                        f_out.write(f_in.read())


if __name__ == "__main__":
    input_directory = "images"                # original images folder
    output_directory = "images_placeholder"   # output placeholders folder

    process_directory(input_directory, output_directory)
    print("✅ Dimension-based placeholder images created successfully!")
