import os
import re


def split_markdown_file(input_file, headers_to_split_on):
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    for header, prefix in headers_to_split_on:
        pattern = f"{re.escape(header)}(.+?)(?={re.escape(header)}|$)"
        matches = re.finditer(pattern, markdown_content, re.DOTALL)

        for index, match in enumerate(matches, start=1):
            section_content = match.group(1).strip()
            print(section_content)

            # Replace section content with an empty string
            markdown_content = markdown_content.replace(match.group(1), "")

            # Specify output file location (modify as needed)
            output_file = os.path.join(
                os.path.dirname(input_file), f"{prefix}_{index}.md"
            )
            with open(output_file, "w", encoding="utf-8") as output:
                output.write(section_content)

    # Save the modified markdown content to the original file
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)


def process_markdown_files_in_directory(directory, headers_to_split_on):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                input_file_path = os.path.join(root, file)
                split_markdown_file(input_file_path, headers_to_split_on)


if __name__ == "__main__":
    input_directory = "/home/mufida/Documents/3GPP/38_series/markdown/"
    headers_to_split_on = [
        ("########", "Annex"),
        # Add more headers as needed
    ]

    process_markdown_files_in_directory(input_directory, headers_to_split_on)
