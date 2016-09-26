from flask import Flask, jsonify, abort, request, make_response
import json
import time
import requests
import tasks
        
t = tasks.Tasks()
app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify({'tasks': t.get_all_tasks()})

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
    new_task = t.add_task(request.json)
    return jsonify({'task': new_task}), 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = t.delete_task(task_id)
    if task is None:
        abort(404)
    return jsonify({'result': True})

@app.route('/todo/api/v1.0/tasks', methods=['DELETE'])
def clear_tasks():
    for task_id in t.tasks:
        t.delete_task(task_id)
    task_num = len(t.get_all_tasks())
    return jsonify({'result': task_num == 0})

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host= '0.0.0.0') 
