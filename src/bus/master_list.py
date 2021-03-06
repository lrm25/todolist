# 
# module that handles coversion from raw data to task objects and display
#

import re
from bus.task import Task, cmp_to_key, compare

tasks = []

#
# convert the lines into tasks, then print the tasks
# TODO move the printing to app layer
# 
# params:
# lines:  full list of lines
#
# returns:  nothing
#
def parse_lines(lines):

    errors = []
    global tasks

    for line in lines:
        
        task_info = re.search('(.*)\sT\((.*)\)$', line[2])
        if task_info is not None:
            description = task_info.group(1)
            # TODO magic number
            fields = task_info.group(2).split(',')
            #task_pu = re.search('([A-F]),\s*(\S+)', task_info.group(2))
            if (2 <= len(fields)) and (len(fields) <= 3):
                priority = fields[0]
                task_dt = re.search('(\d{2}-\d{2}-\d{4})(\|(\d{2}\:\d{2})|)',
                                    fields[1]) 
                if task_dt is not None:
                    difficulty = int(fields[2]) if len(fields) == 3 else None
                    task_date = task_dt.group(1)
                    task_time = task_dt.group(3)
                    task = Task(description, task_date, priority, line[0],
                                line[1], task_time, difficulty)
                    tasks.append(task)
                      


    tasks = sorted(tasks, key=cmp_to_key(compare))
    for task in tasks:
        task.print_()
