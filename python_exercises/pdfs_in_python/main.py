from pypdf import PdfReader,PdfWriter

## lets read in pdf file in our memory
read=PdfReader("sample2.pdf")

## lets get meta data
data=read.metadata
print(f"Author {data.author}")

## lets try to find total pages in pdf file
num_pages=len(read.pages)
print(f"Pages: {num_pages}")

# Get a specific page
first_page = read.pages[0]

# Extract text from the page
text = first_page.extract_text()
print(f"Text from page 1: {text[:100]}...")
## prints first 100 chars from the page

# lets write to an pdf file
writer = PdfWriter()

# lets add an blank page to the opned file
writer.add_blank_page(width=612, height=792) # standard lettr size

# lets also use an existing file
writer.add_page(first_page)

# write to the file
# file is opened in 'wb' (write binary) mode
with open("new_sample1.pdf", "wb") as f:
    writer.write(f)
