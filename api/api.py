from flask import Flask, request, jsonify

from tasks.tasks import *

app = Flask(__name__)
storage = InFileStorage('db/db.txt')


def base_response():
    return {'success': False, 'data': {}, 'error': None}


@app.route('/process', methods=['POST'])
def process():
    response = base_response()
    _json = request.get_json()

    if _json and _json.get('url'):
        task = my_background_task.delay(_json.get('url'))
        response['success'] = True
        response['data'] = {'guid': task.task_id}
        return jsonify(response)
    else:
        response['error'] = 'url not found'

    return jsonify(response)


@app.route('/check/<guid>', methods=['GET'])
def check(guid):
    response = base_response()
    task = celery.AsyncResult(guid)

    if task.status == 'SUCCESS':
        response['success'] = True
        response['data'] = {'guid': guid, 'md5': storage.get(guid)}
    elif task.status == 'FAILURE':
        response['error'] = str(task.result)
    elif task.status == 'PENDING':
        response['error'] = 'in process'

    return jsonify(response)
