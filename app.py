from flask import Flask, jsonify, abort, request, make_response
import json
import time
import requests

class Tasks:
    def __init__(self):
        '''
        '''
        self.tasks = {}

    def get_task(self, task_id):
        '''return None if task_id is not in tasks; oterwise return the corresponding task
        '''
        return self.tasks.get(task_id, None)
        
        
    def add_task(self, new_task):
        ''' add new_task to tasks 
        new_task is a dict, and the key is id 
        '''
        if new_task['id'] not in self.tasks:
            self.tasks[new_task['id']] = new_task
        
    
    def delete_task(self, task_id):
        '''return None if task_id is not in tasks; otherwise return the corresponding task, and delete it from tasks
        '''
        return self.tasks.pop(task_id, None)
        
t = Tasks()
app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify({'tasks': t.tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = t.get_task(task_id)
    if task is None:
        abort(404)
    return jsonify({'task': task})
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json: 
        return request.json    
    if len(t.tasks) > 0:
        new_id = max(t.tasks.keys()) + 1
    else:
        new_id = 1
    new_task = {
        'id': new_id,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
    }
    t.add_task(new_task)
    return jsonify({'task': new_task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = t.delete_task(task_id)
    if task is None:
        abort(404)
    return jsonify({'result': True})
   

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host= '0.0.0.0') 
