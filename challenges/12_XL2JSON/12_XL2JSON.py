
import xlrd
import json

# declare variables 
member_dict = {}
member_list = []
group_dict = {}                            
group_list = []
groups_struc = {} # envelop groups_struc in a dict
groups_struc['groups'] = [] # envelop group_struc['groups'] in a dict

def find_all_persons_and_groups(xlf):
    # read excel file and return number of rows
    wb = xlrd.open_workbook(xlf)
    sheet = wb.sheet_by_index(0)
    number_rows = sheet.nrows
    all_members = []
    for row in range(number_rows):
        if row > 0: # first row contains columns names
            # 3 columns in the excel sheet, we read the values for every row and store them in the variable 
            COL_A =  sheet.cell_value(row, 0)  # column A
            COL_B =  sheet.cell_value(row, 1)  # column B
            COL_C =  sheet.cell_value(row, 2)  # column C
            # we pair those values with keys
            member_dict["group"] = COL_A
            member_dict["person_name"]  = COL_B 
            member_dict["email"] = COL_C
            all_members.append(member_dict.copy()) # and append the key value pairs to the all_members list so we get key value pair dicts in a list
    return all_members
# check if the above function works as intended
# member_list = find_all_persons_and_groups("webex_groups.xlsx")
# print(type(member_list))
# print(member_list)

def make_list_of_groups(membr_list):    
    all_groups = []
    member = None
    # for every record in the member_list extract the value for record["group"]
    for record in membr_list:
        group = record["group"]
        if member != group: # if member is not equal to group
            all_groups.append(group) # append it to all gorups
        member =  group # set member equal to group for the next loop (this way we can filter out double group entries with thesame name)
    return all_groups

# check if hte above function works as intended
# group_list = make_list_of_groups(member_list)
# print(type(group_list))
# print(group_list)

def attach_members_to_groups(group_name, membr_list):
    membr_dict = {}
    all_group_members = [membr_dict] # envelop mebr_dict into the list all_group_members
    for membr in membr_list: # for every member in the member_list 
        if membr["group"] == group_name: # if the value for member["group"] equals group name
            if membr["person_name"] != None:
                membr_dict["person_name"]  = membr["person_name"] # extract the value for membr["person_name"] and add it to the member_dict
                membr_dict["email"] = membr["email"] # do thesame for the email
                all_group_members.append(membr_dict.copy()) # append a copy of the created dict to all_group_members
    return all_group_members

# check if hte above function works as intended
for group_record in group_list:
    all_members = attach_members_to_groups(group_record, member_list)
    print(type(all_members))
    print(all_members)

# define main function
def main():
    member_list = find_all_persons_and_groups("webex_groups.xlsx") # reads in the file and extracts 
    group_list  = make_list_of_groups(member_list)  
    all_members = []
    for group_rec in group_list:
        all_members = attach_members_to_groups(group_rec, member_list)
        del all_members[0] #### delete the first element, which is a copy of the last element
        group_dict["group"] = { "group": {"group_name": group_rec , "members": all_members }} 
        groups_struc['groups'].append(group_dict["group"])
    js_groups = json.dumps(groups_struc, indent=4)
    print(js_groups)

# execute main 
if __name__ == '__main__':
    main()
