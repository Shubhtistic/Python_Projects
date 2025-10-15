from pathlib import Path
from pypdf import PdfWriter

merger = PdfWriter()
current_directory = Path('.') ## current dir

for pdf_path in sorted(current_directory.glob("*.pdf")):
    if pdf_path.name != "merged_output.pdf": # Avoid merging the output file itself
        print(f"Appending: {pdf_path.name}")
        merger.append(str(pdf_path))

with open("merged_output.pdf", "wb") as f:
    merger.write(f)

merger.close()
