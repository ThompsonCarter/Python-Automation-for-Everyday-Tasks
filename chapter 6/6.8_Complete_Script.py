# Complete Script for Report Generation
import pandas as pd
from pathlib import Path
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from docx import Document
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

def generate_report():
    summary = pd.read_csv("data/sales_2025-05.csv")

    # Generate Excel
    generate_excel_report(summary)

    # Generate Word Document
    assemble_word_report(summary)

    # Convert to PDF
    convert_docx_to_pdf()

    # Email the report
    send_email_with_report()

    print("Report generation pipeline complete.")

if __name__ == "__main__":
    generate_report()
