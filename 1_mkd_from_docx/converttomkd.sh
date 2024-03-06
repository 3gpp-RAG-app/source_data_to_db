#!/bin/bash

input_dir="/home/mufida/Documents/3GPP/38_series/docx"
output_dir="/home/mufida/Documents/3GPP/38_series/markdown"


for docx_file in "$input_dir"/*.docx; do
    base_name=$(basename "$docx_file")
    markdown_file="$output_dir/${base_name%.docx}.md"
    pandoc -f docx -t markdown "$docx_file" -o "$markdown_file"
done
