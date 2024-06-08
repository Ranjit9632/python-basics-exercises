# the below code will work for python > 3.5
from pathlib import Path
# the imported objects are as per the latest PyPDF2
from PyPDF2 import PdfReader, PdfWriter


class PdfFileSplitter:
    # class instantiated with path string
    # pdf reader class cannot be used from inside the class as it is not defined only in init
    def __init__(self,pdf_path):
        self.pdf_path = pdf_path 

    def split(self, superpoint, breakpoint):
         # instantiate the writerobject
        self.writer1 = PdfWriter()
        self.writer2 = PdfWriter()    

        # break the pages till breakpoint
        for page in range(breakpoint):
            pages1 = self.pdf_path.pages[page]
            self.writer1.add_page(pages1)
        # get the last page as input and remember order is positional argument and then key argument   
        for page in range(breakpoint, superpoint):
            pages1 = self.pdf_path.pages[page]
            self.writer2.add_page(pages1)

    def write(self):
        # save the files with 1 and 2 names then check it with print statement
        with Path("1.pdf").open(mode = "wb") as file:
            self.writer1.write(file)
            print(f"File 1.pdf created successfully.")

        with Path("2.pdf").open(mode = "wb") as file:
            self.writer2.write(file)

pdf_og = Path.home()/"Python_Complete_Guide.pdf"
print(pdf_og)
# pdf reader instance
input_pdf = PdfReader(str(pdf_og))
endpage = len(input_pdf.pages)
print(endpage)

# class is called with the instance created
pf_splitter = PdfFileSplitter(input_pdf)
pf_splitter.split(endpage,breakpoint = 150)
pf_splitter.write()
