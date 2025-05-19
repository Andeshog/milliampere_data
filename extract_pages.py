import sys
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, page_numbers):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    num_pages = len(reader.pages)
    
    for page_num in page_numbers:
        # Pages in PyPDF2 are zero-indexed
        if 1 <= page_num <= num_pages:
            writer.add_page(reader.pages[page_num - 1])
        else:
            print(f"Page number {page_num} is out of range (1-{num_pages})")

    with open(output_pdf, 'wb') as f_out:
        writer.write(f_out)
    print(f"Extracted pages {page_numbers} to {output_pdf}")

if __name__ == "__main__":
    # Example usage:
    # python extract_pages.py input.pdf output.pdf 3 7
    if len(sys.argv) < 4:
        print("Usage: python extract_pages.py input.pdf output.pdf page1 page2 ...")
        sys.exit(1)
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    pages = [int(x) for x in sys.argv[3:]]
    extract_pages(input_pdf, output_pdf, pages)
