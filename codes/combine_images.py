import img2pdf
import os
import sys

def combine_images_to_pdf(image_paths, output_pdf_path):
    """Combines multiple images into a single PDF file."""

    with open(output_pdf_path, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(image_paths))

if __name__ == "__main__":
    image_folder = sys.argv[1]
    print('using folder', image_folder)

    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith((".jpg", ".png", ".jpeg"))]
    output_pdf_path = "output.pdf"

    combine_images_to_pdf(image_paths, output_pdf_path)
