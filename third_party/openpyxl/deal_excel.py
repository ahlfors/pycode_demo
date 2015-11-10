# -*- coding: utf-8 -*-
__author__ = "minghao.mamh@alibaba-inc.com"

import openpyxl


def demo1(source_excel):
    book = openpyxl.load_workbook(source_excel)
    # ��ӡ������sheet��name
    print(book.get_sheet_names())
    sheet = book[book.get_sheet_names()[0]]
    # ��ʾ������
    row_count = sheet.max_row
    print("row count:{0}".format(row_count))
    # �������еĵ�һ������Ϊ���
    for i in range(2, row_count+1):
        cell = sheet.cell(row=i, column=1)
        cell.value = str(i - 1)
    # ���޸ı���Ϊһ���µ��ļ�
    print("output file: output.xlxs")
    book.save("output.xlsx")


if __name__ == "__main__":
    demo1("input.xlsx")