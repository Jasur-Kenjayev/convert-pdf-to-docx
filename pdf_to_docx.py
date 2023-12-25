from pdf2docx import Converter
import random
import os

#COLOR
os.system("cls")
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)
banner = f"""

                (((       ,,
                ( *)======/\====
                 )(      /  \ 
      __________/  )    /    \
      
      \___#J4SUR   /   / ""   \ 
        \____    _/   / (**)   \
        
           / \__/    (----------)
          /____|__//_ (  it's   )
               |      ( whxite )
               |       (      )
               |        (____)
              _|__
               \
\n\033[36m┏━━━━━━━━━━━━━##########━━━━━━━━━━━━━━━━━━━━┓\t

   {color1}[\033[31m#\033[0m\033[33m]Developer   : \033[1mJasur Kenjayev\033[0m

   {color1}[\033[31m#\033[0m\033[33m]Phone       : \033[31m+998333009888

   {color1}[\033[31m#\033[0m\033[33m]Telegram    : @Python_Koders

\033[36m┗━━━━━━━━━━━━━##########━━━━━━━━━━━━━━━━━━━━┛\t


\033[34mA Program that Converts a PDF file to a DOCX file!

"""
print(banner)
# Specifying the pdf to docx files
id = random.randint(1,1000000)
pdf_file = input("\033[32mEnter the PDF file: ")
docx_file = f"docx{id}.docx"

try:
    # Converting PDF to Docx
    cv_obj = Converter(pdf_file)
    cv_obj.convert(docx_file)
    cv_obj.close()

except:
    print("\033[31mConversion Filed!")
else:
    print("[\033[31m#\033[0m\033[33m]\033[32mFile Converted Successfully...")

# This program was written by Jasur Kenjayev in the Python programming language...