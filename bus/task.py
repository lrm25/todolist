from datetime import datetime

priority_dict = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 3, 'F': 4 }

class Task:

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
        

    def get_date(self):
        return self._converted_date

    def get_time(self):
        return self._time

    def print_(self):
        print("%s %s %s %s" % (self._description, self._priority_str,
              self._list_name, self._line))
        #print("Time delta:  %s" % (datetime.now() - self._converted_date))

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

# From docs.python.org
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
