# Importing convert from the docx2pdf module after installing docx2pdf module through pip
from docx2pdf import convert

# Get user input with the lower method
question = input("Do you want to convert doc/word file to pdf:? ").lower()

# if statement to get user decision
if question == 'y':

    # get the path to the input file for the Word document i.e docx
    doc_file = input(r"Paste the doc file here: ")

    # the path where the out file will be converted to
    pdf_file = input(r"Paste where you want to save the csv file: ")

    # convert the source file to destination file (from docx to pdf)
    convert(doc_file, pdf_file)

