# Copyright (C) 2015 Accuvant, Inc. (bspengler@accuvant.com)
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os

from lib.cuckoo.common.abstracts import Report
from lib.cuckoo.common.constants import CUCKOO_ROOT
from lib.cuckoo.common.exceptions import CuckooReportError

try:
    from weasyprint import HTML
    HAVE_WEASYPRINT = True
except ImportError:
    HAVE_WEASYPRINT = False


class ReportPDF(Report):
    """Stores report in PDF format."""
    # ensure we run after the HTML report
    order = 10

    def run(self, results):
        if not HAVE_WEASYPRINT:
            raise CuckooReportError("Failed to generate PDF report: "
                                    "Weasyprint Python library is not installed")

        if not os.path.isfile(os.path.join(self.reports_path, "report.html")):
            raise CuckooReportError("Unable to open HTML report to convert to PDF: "
                                    "Ensure reporthtml is enabled in reporting.conf")
        
        HTML(os.path.join(self.reports_path, "report.html")).write_pdf(os.path.join(self.reports_path, "report.pdf"))

        return True