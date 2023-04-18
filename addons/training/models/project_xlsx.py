from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class PartnerXlsx(models.AbstractModel):
    _name = 'report.project.one'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
      for obj in partners:
        report_name = obj.name
        
        # One sheet by Project
        sheet = workbook.add_worksheet(report_name[:31])
        
        bold = workbook.add_format({'bold': True})
        formatHeader = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'left', 'bold': False, 'text_wrap': True})
        formatHeaderLeft = workbook.add_format({'font_size': 14, 'valign':'vcenter', 'align': 'left', 'bold': True, 'text_wrap': True})
        formatHeaderCenter = workbook.add_format({'font_size': 14, 'valign':'vcenter', 'align': 'center', 'bold': True, 'text_wrap': True})
        formatHeaderTable = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'centre', 'bold': True, 'bg_color':'#4ead2f', 'color':'black', 'text_wrap': True})
        formatHeaderTitle = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'left', 'bold': True, 'bg_color':'#4ead2f', 'color':'black', 'text_wrap': True})
        formatHeaderTableRight = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'right', 'bold': True, 'bg_color':'#3eaec2', 'text_wrap': True, 'num_format': '#,##0'})
        formatHeaderTableCenterWhite = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'center', 'bold': True, 'text_wrap': True, 'num_format': '#,##0'})
        formatHeaderDetailCenter = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'centre', 'text_wrap': True})
        formatHeaderDetailCenterNumber = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'centre', 'text_wrap': True, 'num_format': '#,##0'})
        formatHeaderDetailCenterNumberFour = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'centre', 'text_wrap': True, 'num_format': '#,##4'})
        formatHeaderDetailLeft = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'left'})
        formatHeaderDetailRight = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'right', 'num_format': '#,##0'})
        formatHeaderDetailRightFour = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'right', 'num_format': '#,##0.0000'})
        
        formatHeaderLeft.set_border(1)
        formatHeader.set_border(1)
        formatHeaderCenter.set_border(1)
        formatHeaderTitle.set_border(1)
        formatHeaderTable.set_border(1)
        formatHeaderTableRight.set_border(1)
        formatHeaderTableCenterWhite.set_border(1)
        formatHeaderDetailCenter.set_border(1)
        formatHeaderDetailLeft.set_border(1)
        formatHeaderDetailCenterNumber.set_border(1)
        formatHeaderDetailCenterNumberFour.set_border(1)
        formatHeaderDetailRight.set_border(1)
        formatHeaderDetailRightFour.set_border(1)
        formatHeaderDetailLeft.set_border(1)

        formatHeaderTable.set_text_wrap()
        formatHeaderTableRight.set_text_wrap()
        formatHeaderDetailCenter.set_text_wrap()
        formatHeaderDetailRight.set_text_wrap()
        formatHeaderDetailLeft.set_text_wrap()

        formatTotal = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'right', 'num_format': '#,##0', 'bold': True, 'bg_color':'#4ead2f', 'color':'black', })
        formatTotalFour = workbook.add_format({'font_size': 10, 'valign':'vcenter', 'align': 'right', 'num_format': '#,##0.0000', 'bold': True, 'bg_color':'#4ead2f', 'color':'black', })
        formatTotal.set_border(1)
        formatTotalFour.set_border(1)      

        # sheet.write(0, 0, obj.name, bold)
        sheet.set_column(0, 0, 5)
        sheet.set_column(1, 1, 15)
        sheet.set_column(2, 2, 15)
        sheet.set_column(3, 3, 15)
        sheet.set_column(4, 4, 15)
        sheet.set_column(5, 5, 20)

        sheet.merge_range(1, 1, 1, 2, 'PROJECT REPORT', bold)
        sheet.write(2, 1, 'NOMOR', bold)
        sheet.write(3, 1, 'CUSTOMER', bold)
        sheet.write(4, 1, 'BUDGET', bold)
        sheet.write(5, 1, 'TOTAL', bold)

        sheet.write(2, 2, obj.id, formatHeader)
        sheet.write(3, 2, obj.customer.name, formatHeader)
        sheet.write(4, 2, obj.budget, formatHeader)
        sheet.write(5, 2, obj.total, formatHeader)

        row = 8
        sheet.write(row, 0, 'NO', formatHeaderTable)
        sheet.write(row, 1, 'ID', formatHeaderTable)
        sheet.write(row, 2, 'NAME', formatHeaderTable)
        sheet.write(row, 3, 'START DATE', formatHeaderTable)
        sheet.write(row, 4, 'END DATE', formatHeaderTable)
        sheet.write(row, 5, 'BUDGET', formatHeaderTable)

        row = total_line = 9
        number = 1
        if obj.sub_project_ids:
          for i in obj.sub_project_ids:         
            sheet.write(row, 0, number, formatHeaderDetailCenter)
            sheet.write(row, 1, i['id'], formatHeaderDetailLeft)            
            sheet.write(row, 2, i['name'], formatHeaderDetailLeft)
            sheet.write(row, 3, i['start_date'], formatHeaderDetailLeft)            
            sheet.write(row, 4, i['end_date'], formatHeaderDetailLeft)
            sheet.write(row, 5, i['budget'], formatHeaderDetailRight)            
            row += 1
            number += 1
          sheet.merge_range(row, 0, row, 4, 'TOTAL', formatHeaderTable)
          sheet.write_formula(row, 5, '=SUM(F'+str(total_line+1)+':F'+str(row)+')', formatTotal)
        else:
          sheet.merge_range('A10:F10', 'KOSONG', formatHeaderDetailCenter)


        # sheet.merge_range(row, 0, row, 4, 'TOTAL', formatHeaderTable)
        # sheet.write_formula(row, 5, '=SUM(F'+str(total_line+1)+':F'+str(row)+')', formatTotal)
        # _logger.error('partners.name')
        # _logger.error(partners.name)
        # date_format = workbook.add_format({'num_format': 'mm/dd/yy'})
        # report_name = partners.name
        # # One sheet by partner
        # sheet = workbook.add_worksheet(report_name[:2])
        # bold = workbook.add_format({'bold': True})

        # sheet.set_column('A:D', 25)
        # # sheet.set_column(0, 0, 25)
        # # sheet.set_column(0, 1, 25)
        # # sheet.set_column(0, 2, 25)
        # # sheet.set_column(0, 3, 25)

        # sheet.write(0, 0, 'Name : ', bold)
        # sheet.write(0, 1, partners.name)

        # sheet.write(1, 0, 'Customer :', bold)
        # sheet.write(1, 1, partners.customer.name)

        # sheet.write(2, 0, 'Penanggung Jawab :', bold)
        # sheet.write(2, 1, partners.penanggung_jawab.name)
        # sheet.write(3, 0, 'Start Date :', bold)
        # sheet.write(3, 1, partners.start_date, date_format)

        # sheet.write(4, 0, 'End Date :', bold)
        # sheet.write(4, 1, partners.end_date, date_format)
        # x = 7
        # sheet.write(6, 0, 'Name', bold)
        # sheet.write(6, 1, 'Start Date', bold)
        # sheet.write(6, 2, 'End Date', bold)
        # sheet.write(6, 3, 'Budget', bold)
        # sheet.freeze_panes('A8')
        # if partners.sub_project_ids:
        #   for sub_obj in partners.sub_project_ids:
        #       sheet.write(x, 0, sub_obj.name)
        #       sheet.write(x, 1, sub_obj.start_date, date_format)
        #       sheet.write(x, 2, sub_obj.end_date, date_format)
        #       sheet.write(x, 3, sub_obj.budget)
        #       x = x+1
        #   sheet.write(x, 0, 'TOTAL :', bold)
        #   sheet.write(x, 3, partners.budget)
        # else:
        #   sheet.merge_range('A8:D8', 'KOSONG', bold)
          
