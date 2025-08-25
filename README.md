# 🖼️ Image Placeholder Generator

A simple Python tool to generate placeholder images from your existing image folders.  
It preserves the original folder structure and replaces each image with a gray placeholder showing its dimensions (e.g., 1920x1080).

## 🚀 Features

- Generates placeholder images with the same dimensions as originals  
- Displays image size (e.g., 800x600) centered on the placeholder  
- Supports multiple formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.gif`  
- Preserves original folder structure  
- Option to build a stand-alone `.exe` (no Python needed)  

## 📂 Project Structure

your-project/
│
├── images/ # Original images (input)
│ ├── subfolder1/
│ │ ├── img1.jpg
│ │ └── img2.png
│ └── subfolder2/
│ └── img3.jpg
│
├── images_placeholder/ # Output folder with placeholders
│ ├── subfolder1/
│ │ ├── img1.jpg → (placeholder)
│ │ └── img2.png → (placeholder)
│ └── subfolder2/
│ └── img3.jpg → (placeholder)
│
└── placeholder.py # Main script
