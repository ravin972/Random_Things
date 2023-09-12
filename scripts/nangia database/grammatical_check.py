import docx
from docx.shared import RGBColor
from language_tool_python import LanguageTool

# Prompt the user to enter the input Word file name
input_file_name = input("Enter the input Word file name (e.g., input.docx): ")

# Prompt the user to enter the output file name
output_file_name = input("Enter the output file name (e.g., output.docx): ")

# Load the Word document
doc = docx.Document(input_file_name)

# Initialize the LanguageTool
tool = LanguageTool('en-US')

# Define a function to check and highlight errors
def check_and_highlight_errors(text, run):
    matches = tool.check(text)
    for match in reversed(matches):  # Start from the end to avoid offset changes
        start = match.offset
        end = match.offset + match.errorLength
        run.text = run.text[:start] + run.text[start:end].replace('\n', ' ') + run.text[end:]
        for i in range(start, end):
            run[i].font.highlight_color = RGBColor(255, 255, 0)  # Yellow highlight

# Iterate through paragraphs and check for errors
for paragraph in doc.paragraphs:
    for run in paragraph.runs:
        text = run.text
        if text.strip():
            check_and_highlight_errors(text, run)

# Save the modified document with the specified output file name
doc.save(output_file_name)

print(f"Errors highlighted and saved in '{output_file_name}'")
