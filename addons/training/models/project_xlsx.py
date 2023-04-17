from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class PartnerXlsx(models.AbstractModel):
    _name = 'report.project.one'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        _logger.error('partners.name')
        _logger.error(partners.name)
        date_format = workbook.add_format({'num_format': 'mm/dd/yy'})
        report_name = partners.name
        # One sheet by partner
        sheet = workbook.add_worksheet(report_name[:2])
        bold = workbook.add_format({'bold': True})

        sheet.set_column('A:D', 25)
        # sheet.set_column(0, 0, 25)
        # sheet.set_column(0, 1, 25)
        # sheet.set_column(0, 2, 25)
        # sheet.set_column(0, 3, 25)

        sheet.write(0, 0, 'Name : ', bold)
        sheet.write(0, 1, partners.name)

        sheet.write(1, 0, 'Customer :', bold)
        sheet.write(1, 1, partners.customer.name)

        sheet.write(2, 0, 'Penanggung Jawab :', bold)
        sheet.write(2, 1, partners.penanggung_jawab.name)
        sheet.write(3, 0, 'Start Date :', bold)
        sheet.write(3, 1, partners.start_date, date_format)

        sheet.write(4, 0, 'End Date :', bold)
        sheet.write(4, 1, partners.end_date, date_format)
        x = 7
        sheet.write(6, 0, 'Name', bold)
        sheet.write(6, 1, 'Start Date', bold)
        sheet.write(6, 2, 'End Date', bold)
        sheet.write(6, 3, 'Budget', bold)
        sheet.freeze_panes('A8')
        if partners.sub_project_ids:
          for sub_obj in partners.sub_project_ids:
              sheet.write(x, 0, sub_obj.name)
              sheet.write(x, 1, sub_obj.start_date, date_format)
              sheet.write(x, 2, sub_obj.end_date, date_format)
              sheet.write(x, 3, sub_obj.budget)
              x = x+1
          sheet.write(x, 0, 'TOTAL :', bold)
          sheet.write(x, 3, partners.budget)
        else:
          sheet.merge_range('A8:D8', 'KOSONG', bold)
          
