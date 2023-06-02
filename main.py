import os
import pandas as pd
from PIL import Image
import png


def get_png_data(image_path):
    img = Image.open(image_path)
    reader = png.Reader(filename=image_path)
    png_data = reader.read()
    metadata = png_data[3]

    # Basic data from PIL
    data = {
        'filename': os.path.basename(image_path),
        'format': img.format,
        'size': img.size,  # Output: (width, height)
        'mode': img.mode,
    }

    # Metadata from pypng
    for k, v in metadata.items():
        data[k] = v

    return data


# Specify your directory containing the PNG files
image_dir = 'C:/Users/Dana/PycharmProjects/extract-all-png-data/'

# Get list of PNG files
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

# Extract data from each PNG
all_data = []
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    data = get_png_data(image_path)
    all_data.append(data)

# Convert to a pandas DataFrame and save as CSV
df = pd.DataFrame(all_data)
df.to_csv('png_data.csv', index=False)
