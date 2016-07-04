from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

tasks = [
	{
		'id': 1,
		'title': 'Buy groceries',
		'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
		'done': False
	},
	{
		'id': 2,
		'title': 'Learn Python',
		'description': 'Need to find a good Python tutorial on the web',
		'done': False
	}
]

url_root = '/todo/api/v1.0/'

@app.route(url_root+'tasks', methods=['GET', 'POST'])
def do_tasks():
	if request.method == 'GET':
		return make_response(jsonify({'tasks': tasks}), 200)

	if request.method == 'POST':
		content = request.get_json(silent=True)
		content["id"] = tasks[-1]['id'] + 1
		tasks.append(content)
		return make_response(jsonify({'id': content["id"]}), 201)

	return make_response(jsonify({'status_code': 500}), 500)

@app.route(url_root+'tasks/<task_id>', methods=['GET', 'PUT', 'DELETE'])
def do_task(task_id):
	task_id = int(task_id)
	if request.method == 'GET':
		task_array = [t for t in tasks if t['id'] == task_id]
		if len(task_array) != 0:
			return make_response(jsonify({'task': task_array[0]}), 200)
		else:
			return make_response(jsonify({'status_code': 404}), 404)

	if request.method == 'PUT':
		content = request.get_json(silent=True)
		task_array = [t for t in tasks if t['id'] == task_id]
		if len(task_array) == 0:
			return make_response(jsonify({'status_code': 404}), 404)
		task = task_array[0]
		task["title"] = content["title"]
		task["description"] = content["description"]
		task["description"] = content["description"]
		return make_response(jsonify({'task': task}), 200)


	if request.method == 'DELETE':
		task_array = [t for t in tasks if t['id'] == task_id]
		if len(task_array) > 0:
			tasks.remove(task_array[0])
			return make_response(jsonify({'status_code': 200}), 200)
		else:
			return make_response(jsonify({'status_code': 404}), 404)

	return make_response(jsonify({'status_code': 500}), 500) 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)