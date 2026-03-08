```python
from flask import Flask, request, jsonify
from csv_to_json import csv_to_json
import os
import json
from todo_list import TodoList
from weather_api import get_weather_data

app = Flask(__name__)

# Initialize TodoList instance
todo_list = TodoList()

# Define API endpoint for CSV to JSON conversion
@app.route('/csv_to_json', methods=['POST'])
def convert_csv_to_json():
    csv_file = request.files['csv_file']
    json_file_path = 'output.json'
    csv_to_json(csv_file, json_file_path)
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    os.remove(json_file_path)
    return jsonify(data)

# Define API endpoint for Todo List management
@app.route('/todo_list', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_todo_list():
    if request.method == 'GET':
        return jsonify(todo_list.get_all_tasks())
    elif request.method == 'POST':
        task = request.json['task']
        todo_list.add_task(task)
        return jsonify({'message': 'Task added successfully'})
    elif request.method == 'PUT':
        task_id = request.json['task_id']
        task = request.json['task']
        todo_list.update_task(task_id, task)
        return jsonify({'message': 'Task updated successfully'})
    elif request.method == 'DELETE':
        task_id = request.json['task_id']
        todo_list.delete_task(task_id)
        return jsonify({'message': 'Task deleted successfully'})

# Define API endpoint for Weather data fetching
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    data = get_weather_data(city)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```