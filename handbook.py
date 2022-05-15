"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: We do not expect you to come up with a perfect solution. We are more interested
in how you would approach a problem like this.
"""
import json

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_subset(a, b):
    for item in a:
        if not item in b:
            return False
    return True

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    conditions_list = CONDITIONS[target_course].split()
    
    if conditions_list == []:
        return True

    # handling uoc
    if "units" in conditions_list and "credit" in conditions_list:
        quota = int(conditions_list[conditions_list.index("units") - 1])
        if len(courses_list) >= quota / 6:
            return True
        else:
            return False

    courses = []
    or_cond = True
    and_cond = False
    open_brackets = 0
    index = 0
    courses_index = 0
    while index < len(conditions_list):
        item = conditions_list[index]
        if item.lower() == 'or':
            or_cond = True
        elif item.lower() == 'and':
            and_cond = True
        elif item[0] == '(':
            print(item)
            open_brackets += 1
        elif len(item) == 8:
            if or_cond:
                courses.append([item])
                courses_index += 1
                or_cond = False
            elif and_cond:
                courses[courses_index - 1].append(item)
                and_cond = False
        index += 1

    for condition in courses:
        if is_subset(courses_list, condition):
            return True
    return False