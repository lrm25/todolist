from datetime import datetime

# 
# Priorities:
# A:  has to be done
# B:  should be done, or negative consequences can happen
# C:  positive consequences
# D:  delegate (right now, I don't use this)
# E:  leisure
# F:  don't do, should be deleted
#
priority_dict = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 3, 'F': 4 }

#
# class representing converted task object from text line
#
class Task:

    #
    # __init__
    # 
    # params:
    # description:  task description
    # date:  task due date
    # priority:  task priority, A-F
    # list_name:  name of .txt file task was pulled from
    # line:  line number of task in .txt file
    # time:  task time, currently in military time
    # difficulty:  task difficulty on scale of 1-10
    #
    def __init__(self, description, date, priority, list_name, line, time=None,
                 difficulty=None):
        self._description = description
        self._converted_date = datetime.strptime(date, '%m-%d-%Y')
        self._priority = priority
        self._list_name = list_name
        self._line = line
        self._time = time
        self._difficulty = difficulty
        time_delta = (datetime.now() - self._converted_date).days
        #print("time delta:  %d" % time_delta)
        if time is None:
            # If no time, adjust position in todolist based on priority
            priority_add = priority_dict[priority]
            orig_time_delta = time_delta
            time_delta -= priority_add
            self._sec = 0
            self._priority_str = priority+","+str(orig_time_delta * -1)
            if difficulty is not None:
                self._priority_str += ","+str(difficulty)
        else:
            time_strs = time.split(':')
            self._sec = (int(time_strs[0]) * 3600) + int(time_strs[1])
            self._priority_str = priority+","+date+","+time
        self._time_delta = time_delta
        #print("Priority str:  %s" % self._priority_str)
        

    #
    # return:  task due date
    #
    def get_date(self):
        return self._converted_date

    #
    # return:  task time, in military time (for tasks with specific times)
    # 
    def get_time(self):
        return self._time

    #
    # TODO:  override "__" print function
    # print user-readable description of task
    # 
    def print_(self):
        print("%s %s %s %s" % (self._description, self._priority_str,
              self._list_name, self._line))
        #print("Time delta:  %s" % (datetime.now() - self._converted_date))

#
# compare tasks in the following fashion:
# 
# specific time is provided:  sort strictly by time
# only date:  if priority is lower, subtract value provided in priority dict, 
# then sort by reverse priority, then by difficulty, hardest to lowest
# e.g.
# A0 B0 A1 C0 B1 A2 D0 C1 B2 A3 etc ...
#
# params:
# task_one, task_two:  tasks being sorted
#
# returns:
# 1 if task_two comes first in list
# -1 if task_one comes first
# 0 if don't care
#
def compare(task_one, task_two):
    if (task_one._time_delta < task_two._time_delta):
        return 1
    elif (task_two._time_delta < task_one._time_delta):
        return -1
    else:
        if (task_one._time is None) and (task_two._time is not None):
            return 1
        elif (task_two._time is None) and (task_one._time is not None):
            return -1
        elif (task_two._time is not None) and (task_one._time is not None):
            if (task_two._sec < task_one._sec):
                return 1
            elif (task_one._sec < task_two._sec):
                return -1
            elif (task_one._priority < task_two._priority):
                return -1
            elif (task_two._priority < task_one._priority):
                return 1
            return 0
        else:
            if (task_one._priority < task_two._priority):
                return 1
            elif (task_two._priority < task_one._priority):
                return -1
            elif ((task_one._difficulty is None) and 
                  (task_two._difficulty is not None)):
                return 1
            elif ((task_two._difficulty is None) and
                  (task_one._difficulty is not None)):
                return -1
            elif ((task_two._difficulty is not None) and
                  (task_one._difficulty is not None)):
                if (task_one._difficulty < task_two._difficulty):
                    return 1
                elif (task_two._difficulty < task_one._difficulty):
                    return -1
                else:
                    return 0
            else:
                return 0

#
# From docs.python.org
#
# convert comparison function to key function required for python 3
#
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
