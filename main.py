import pandas
import openpyxl

files = [
    "excel/test1.xlsx",
    "excel/test2.xlsx"
]

def write_value(file, instruction, cell_position,sheet='Feuil1'):
    """This function allow to write a value or an instruction in a gave cell_position, on a file for wich path is required"""
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]
    sheet[cell_position] = instruction
    workbook.save(file)



#sheet['F9'].style='Currency' permet de modifier le style d'une cellule

def get_value(file, cell_position,sheet='Feuil1'):
    """This function is getting and returning the value of the gave cell, in a sheet of a file gave too"""
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]
    value = sheet[cell_position].value
    return value


def combining_files(files):
    """
    This function allow to combine files, giving the list files path.
    For this, it's necessary to import pandas.
    """

    combined_files = pandas.DataFrame()

    for file in files:
        df = pandas.read_excel(file)
        combined_files = combined_files.append(df, ignore_index =True)

    combined_files.to_excel('combined_file.test.xlsx')