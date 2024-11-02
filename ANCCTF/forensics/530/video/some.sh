#!/bin/bash

# Loop through each PNG file
for file in output_frame_*.png; do
    # Extract the base filename without extension
    base=$(basename "$file" .png)
    
    # Run Tesseract OCR on the frame
    tesseract "$file" "${base}_text" -l eng
done
