# 
# Exception helper function
# 
# params:
# val:  input value to list file init function
# exception:  expected exception text
# 
# return:  true if exception matches text (and is thrown), false if not
# 
def init(val, exception, exception_type, class_name):

    pass_test = False
    try:
        obj = class_name(val)
    except exception_type as err:
        pass_test = True if str(err) == exception else False
    return pass_test
