
from typing import Dict
import xlrd # library to manage excel spreadsheets
import json # library to manage json functions

# open the spreadsheet/workbook and select the sheet/tab at index 0
def find_all_persons_and_groups(xlf):
    wb = xlrd.open_workbook("webex_groups.xlsx")
    sheet = wb.sheet_by_index(0)


    number_rows = sheet.nrows # define the number of rows in the sheet
    members = [] # stores the build up json structure
    member_dict = {} # stores key value pairs for each inividual row
    for i in range(number_rows -1 ):
        if i > 0:  # first row contains the column names
            # loop trough the rows and get the cell value out store them in a variable
            COL_A = sheet.cell_value(i, 0) # column A
            COL_B = sheet.cell_value(i, 1) # column B
            COL_C = sheet.cell_value(i, 2) # column C
            # loop trough the rows and add the cell values to the membe_dict keys
            member_dict["group"] = COL_A
            member_dict["name"] = COL_B
            member_dict["email"] = COL_C
            members.append(member_dict.copy()) # append a copy from the member_dict to the members list since the dict will get overwritten every loop
    return members

# extract the groups from the member list retrieved in the previous function
def make_list_of_groups(membr_list):
    all_groups = [] # storage for the groups
    member = None

    # for every item in the list, if the next records group value differs from the previous record, append the group to the all_groups
    for record in membr_list:
        group = record["group"]
        if member != group:
            all_groups.append(group)
        member = group
    return all_groups

# combine the output from both functions to create the required json tree structure
def atach_members_to_group(group_name, membr_list):
    membr_dict = {}
    all_group_members = [membr_dict]
    for membr in membr_list:
        if membr["group"] == group_name:
            if membr["name"] != None:
                membr_dict["person_name"] = membr["name"]
                membr_dict["email"] = membr["email"]
                all_group_members.append(membr_dict.copy())
    return all_group_members

def main():
    member_list = find_all_persons_and_groups("webex_groups.xlsx")
    group_list = make_list_of_groups(member_list)
    all_members = []
    groups_struc = []
    for group_rec in group_list:
        all_members = atach_members_to_group(group_rec, member_list)
        del all_members[0]
        group_dict = {"group": {"group_name": group_rec, "members": all_members}}
        groups_struc.append(group_dict)
    js_groups = json.dumps(groups_struc, indent=4)
    print(js_groups)

if __name__ =='__main__':
    main()