import requests
from flask import request
from task_app import app

def test_task_app():
    #domain = 'http://luc14.pythonanywhere.com'
    domain = 'http://localhost:5000'
    url = domain + '/todo/api/v1.0/tasks'
    r = requests.delete(url)
    assert r.json()['result'] == True
    assert r.status_code == 200
    test_tasks = [
        {'description': 'haha', 'id': 1, 'title': 'Lu'},
        {'description': 'latte', 'id': 2, 'title': 'Coffee'}   
    ]
    task_num = len(test_tasks)
    for task in test_tasks:
        requests.post(url, json=task)
    assert len(requests.get(url).json()['tasks']) == task_num
    for idx, task in enumerate(test_tasks):
        task_url = url+'/'+str(idx+1)
        assert requests.get(task_url).json()['task'] == task
        assert requests.delete(task_url).json()['result']==True
        task_num-= 1
        assert requests.get(task_url).json()['error'] == 'Not Found'    
        assert requests.delete(task_url).json()['error'] == 'Not Found'   
        assert len(requests.get(url).json()['tasks']) == task_num
    
    #func = request.environ.get('werkzeug.server.shutdown')
    #if func is not None:
        #func()
        
#if __name__ == '__main__':
    #test_task_app()
