import sys
import math
from pypdf import PdfReader, PdfWriter

def split_pdf(input_file, pages_per_chunk=20):
    try:
        reader = PdfReader(input_file)
        total_pages = len(reader.pages)
        
        # Calculate how many parts will be generated
        total_chunks = math.ceil(total_pages / pages_per_chunk)
        print(f"Total pages: {total_pages}. Splitting into {total_chunks} files...")

        for i in range(total_chunks):
            writer = PdfWriter()
            start_page = i * pages_per_chunk
            # Ensure we don't go past the last page
            end_page = min(start_page + pages_per_chunk, total_pages) 
            
            # Add the range of pages to the writer
            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])
            
            # Generate output filename (e.g., document_part_1.pdf)
            output_filename = f"{input_file.rsplit('.', 1)[0]}_part_{i + 1}.pdf"
            
            with open(output_filename, "wb") as output_file:
                writer.write(output_file)
                
            print(f"Created: {output_filename} (Pages {start_page + 1}-{end_page})")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_pdf.py <filename.pdf>")
    else:
        split_pdf(sys.argv[1])
