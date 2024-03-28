from tabula import read_pdf
import pandas as pd

file = 'D:\Image_to_text_ocr\china.pdf_safe.pdf'

# Read the PDF and store the tables in a list
df_temp = read_pdf(file, pages='1', stream=True) 

# Create an empty DataFrame to store the concatenated tables
result_df = pd.DataFrame()

# Concatenate the tables and store them in the result DataFrame
for df in df_temp:
    result_df = pd.concat([result_df, df])

# Write the DataFrame to a CSV file
result_df.to_csv('output4_table.csv', index=False)

print("Tables extracted from the PDF have been saved to 'output4_table.csv'")
