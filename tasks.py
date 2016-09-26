class Tasks:
    def __init__(self):
        '''self.tasks is iterable with task_ids
        '''
        self.tasks = {}
        
    def get_all_tasks(self,):
        tasks = []
        for task_id, task in self.tasks.items():
            tasks.append(task)
        return tasks
        
    def get_task(self, task_id):
        '''return None if task_id is not in tasks; oterwise return the corresponding task
        '''
        return self.tasks.get(task_id, None)
        
        
    def add_task(self, new_task):
        ''' 
        add new_task to tasks 
        new_task is a dict, and the key is id 
        '''
        new_task['id'] =len(self.tasks) + 1
        self.tasks[new_task['id']] = new_task
        return new_task
    
    def delete_task(self, task_id):
        '''return None if task_id is not in tasks; otherwise return the corresponding task, and delete it from tasks
        '''
        return self.tasks.pop(task_id, None)
    
    