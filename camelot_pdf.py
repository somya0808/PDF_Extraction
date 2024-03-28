import camelot
import pandas as pd

# Specify the path to your PDF file
pdf_file = 'D:\Image_to_text_ocr\PDF_Extraction\china.pdf_safe.pdf'

# Correct usage of Camelot's read_pdf function
tables = camelot.read_pdf(pdf_file, flavor='stream')

# Loop through the extracted tables and save them into CSV files
for i, table in enumerate(tables):
    # Save each table to a CSV file
    csv_file = f'table_{i+1}.csv'
    table.to_csv(csv_file)  # Save table to CSV file

    print(f"Table {i+1} saved as {csv_file}")

print("Tables extracted from the PDF have been saved as CSV files")

