
import subprocess

# 1. Generate charts
subprocess.run(["python", "reports/charts.py"])
# 2. Build dashboard HTML
subprocess.run(["python", "dashboard/app.py", "--export-html"])
# 3. Convert to PDF
subprocess.run(["python", "- <<EOF

from weasyprint import HTML
HTML('reports/figures/dashboard.html').write_pdf('reports/dashboard.pdf')
EOF"])
# 4. Merge PDFs
from PyPDF2 import PdfMerger
merger = PdfMerger()
merger.append("reports/figures/sales_bar.pdf")
merger.append("reports/dashboard.pdf")
merger.write("reports/full_report.pdf")
merger.close()
print("Complete report generated.")
