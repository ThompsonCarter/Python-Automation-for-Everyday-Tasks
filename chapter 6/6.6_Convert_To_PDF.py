# Step 4: Convert DOCX to PDF with PyPDF2
import subprocess

def convert_docx_to_pdf():
    subprocess.call(["libreoffice", "--headless", "--convert-to", "pdf", "output/report_2025-05.docx", "--outdir", "output"])
    print("PDF generated.")
