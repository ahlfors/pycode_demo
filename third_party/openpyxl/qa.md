����ͽ������
======
����1����װʱ����encoding����
ʹ��pip install openpyxl����encoding������
��ȥpypi����openpyxl��װ����Ȼ������������
���ص�ַhttps://pypi.python.org/pypi/openpyxl/2.3.0
�����
��setup.py��import sys��������
reload(sys)
sys.setdefaultencoding('Cp1252')
======
����2��importʱ����encoding����
��import openpyxlʱ����encoding����
�����
��mimetypes.py����������ͬ���Ĵ���
======
����3��openpyxl.load_workbook�����쳣
����ʹ��openpyxl.load_workbookָ����һ�������и�ʽ��xlsx�ļ������쳣
����stackoverflow��������£����ֿ�����openpyxl��֧����ʽ��һ��bug
��xlsx�ļ����е���ʽȥ������ok��