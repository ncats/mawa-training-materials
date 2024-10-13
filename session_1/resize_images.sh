#!/bin/bash

resize_perc=50

# Create the reduced directory if it doesn't exist
mkdir -p reduced

# Loop through all files in the full directory
for file in full/*; do
  # Get the filename without the directory
  filename=$(basename "$file")
  # Get the filename without the extension
  name="${filename%.*}"
  # Get the file extension
  extension="${filename##*.}"
  # Convert the image to 50% of its size and save it with -reduced appended to the filename
  # all of these work, with Lanczos and scale seeming to be the best. Choosing the former as in theory it's generally better
  convert "$file" -filter Lanczos -resize ${resize_perc}% "reduced/${name}.${extension}"
  # convert "$file" -filter Mitchell -resize 50% "reduced/${name}-mitchell.${extension}"
  # convert "$file" -filter Catrom -resize 50% "reduced/${name}-catrom.${extension}"
  # convert "$file" -filter Cubic -resize 50% "reduced/${name}-cubic.${extension}"
  # convert "$file" -adaptive-resize 50% "reduced/${name}-adaptive.${extension}"
  # convert "$file" -scale 50% "reduced/${name}-scale.${extension}"
  # convert "$file" -sample 50% "reduced/${name}-sample.${extension}"
  # convert "$file" -thumbnail 50% "reduced/${name}-thumbnail.${extension}"
done
