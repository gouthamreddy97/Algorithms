import re

def reformat_tags(string_, max_width):

    lines = string_.split("\n")
    new_string = ""
    for line in lines:
        str_ = ""
        indent = ""
        m = re.search(r'(.*?\s+)[a-z].*', line, re.I)
        if m:
            indent = " " * len(m.group(1))
        if len(line) > max_width:
            words = line.split(" ")
            for word in words:
                if len(str_) + len(word) <= max_width:
                    str_ = str_ + str(word) + " "
                else:
                    str_ = "{}\n".format(str_.rstrip(" "))
						
                    new_string = new_string + str_.rstrip(" ")
                    str_ = indent + str(word) + " "
        else:
            new_string = new_string + line
        new_string += str_ + "\n"
    return new_string





if __name__ == '__main__':
	string_ = 'taskCreateWithGuard shall perform the following:\n    1. if [name] is equal to [NULL]:\n        1.1. set namelessPrefixLen to size in bytes of namelessPrefix\n        1.2. invoke [strncpy] with parameters newName, [namelessPrefix] and namelessPrefixLen, typecast the return value to void\n        1.6. perform the following in the loop at least once:\n            1.6.1. set newName at index [nBytes incremented by one] to digits at index [value modulus by [TASK_TEN_VALUE]]\n            1.6.2. set value to the result of (value divided by [TASK_TEN_VALUE])'
	max_width = 65
	new_string = reformat_tags(string_, max_width)
	print(new_string)