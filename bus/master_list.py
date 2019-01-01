import re

from bus.task import Task, cmp_to_key, compare

tasks = []

def sort_list(task_one, task_two):

    date_one = task_one.get_date()
    date_two = task_two.get_date()

    if (date_one < date_two):
        return -1
    elif (date_one == date_two):
        return 0
    return 1

def parse_lines(lines):

    errors = []
    global tasks

    for line in lines:
        
        task_info = re.search('(.*)\sT\((.*)\)$', line[2])
        if task_info is not None:
            description = task_info.group(1)
            task_pu = re.search('([A-F]),\s*(\S+)', task_info.group(2))
            if task_pu is not None:
                priority = task_pu.group(1)
                task_dt = re.search('(\d{2}-\d{2}-\d{4})(\|(\d{2}\:\d{2})|)',
                                  task_info.group(0)) 
                if task_dt is not None:
                    task_date = task_dt.group(1)
                    task_time = task_dt.group(3)
                    task = Task(description, task_date, priority, line[0],
                                line[1], task_time)
                    tasks.append(task)


    tasks = sorted(tasks, key=cmp_to_key(compare))
    for task in tasks:
        task.print_()