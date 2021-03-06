# coding=utf-8
import win32com.client
import os
from scenario_classes import ScenarioClass


class ExcelInput(object):
    def __init__(self, description):
        self.description_of_scenario = description

    def excel_write(self):
        # open excel file
        excel_app = win32com.client.Dispatch("Excel.Application")
        is_debug = True
        if is_debug:
            excel_app.Visible = 0  # excel窗口不可见：0；excel窗口可见：1
        excel_app.DisplayAlerts = 0  # 禁止弹出确认框
        file_path = os.path.abspath(r".\scenario_output\basic_scenario.xlsx")
        workbook = excel_app.Workbooks.Open(file_path)
        # review excel content and write new item
        sheet = workbook.Worksheets(self.description_of_scenario[0])
        excel_row = 4  # 第一个场景所在的行号
        excel_col = 2  # 第一个场景的列号
        while True:
            content = sheet.Cells(excel_row, excel_col).Value
            if content is not None:
                excel_row = excel_row+1
            else:
                self.description_of_scenario.insert(0, excel_row-3)
                for index_des in [3, 5, 7, 8, 11]:
                    self.description_of_scenario.insert(index_des, " ")
                self.description_of_scenario[5] = "%s-%d" % (self.description_of_scenario[14], excel_row-3)
                columns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                for column in columns:
                    sheet.Cells(excel_row, column).Value = self.description_of_scenario[column - 2]
                    sheet.Cells(excel_row, column).BorderAround(1)
                    sheet.Cells(excel_row, column).VerticalAlignment = -4160
                    sheet.Cells(excel_row, column).HorizontalAlignment = -4131
                print(self.description_of_scenario[15])
                sheet.Shapes.AddPicture(self.description_of_scenario[15], 1, 1, 850, 100+160*(excel_row-4), 200, 100)
                sheet.Cells(excel_row, 16).BorderAround(1)  # border of Level6
                break
        # save and quit
        workbook.Save()
        workbook.Close(SaveChanges=0)
        excel_app.Quit()


# scenario1 = ScenarioClass(2, [3, 2], [4, 2])
# description = scenario1.catalog()
# excel_write(description)
