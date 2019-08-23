from tool.opera_excel import OperaExcel
from base.runmethod import RunMethod
import time


class Runtest:
    def __init__(self, user_file_name, case_file_name):
        self.user_file_name = user_file_name
        self.case_file_name = case_file_name
        self.user_file = OperaExcel(self.user_file_name)
        self.case_file = OperaExcel(self.case_file_name)
        self.run_method = RunMethod()

    def go_on_run(self):
        user_max_row = self.user_file.getRowsNum()
        for row in range(2, user_max_row + 1):
            request_file = self.case_file.getCellValue(row=row, column=10)
            request_name = request_file.split(",")
            parameter_value = self.user_file.getRowValues(row=row)
            request_data = dict(zip(request_name, parameter_value))
            request_method = self.case_file.getCellValue(row=row, column=5)
            request_url = self.case_file.getCellValue(row=row, column=3)
            responses = self.run_method.runMain(method=request_method, url=request_url, data=request_data)
        return responses


if __name__ == '__main__':
    run = Runtest("D:\\PycharmProjects\\FenmiApiTets\\dataconfig\\user.xlsx",
                  "D:\\PycharmProjects\\FenmiApiTets\\dataconfig\\case.xlsx")
    run.go_on_run()
