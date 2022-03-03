import fitz
from glob import glob

result = fitz.open()
for item in glob("*.pdf"):
	with fitz.open(item) as mfile:
		#result.insertPDF(mfile)
		result.insert_pdf(mfile)

result.save("FINAL.pdf")