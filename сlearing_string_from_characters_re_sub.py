import re


# https://www.w3schools.com/jsref/jsref_obj_regexp.asp
# Brackets are used to find a range of characters:
# [abc]	Find any character between the brackets

my_string = '+7-(999)-11-22'
cleared_string = re.sub("[\+ \- \( \)]", "", my_string)
print(cleared_string)
# 79991122