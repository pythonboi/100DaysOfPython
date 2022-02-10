from docx2pdf import convert

question = input("Do you want to convert txt file to csv:? ").lower()

if question == 'y':

    txt_file = input(r"Paste the txt file here: ")
    # my_Index = index = None
    pdf_file = input(r"Paste where you want to save the csv file: ")
    convert(txt_file, pdf_file)

