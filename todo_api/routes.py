```python
from flask import Blueprint, request, jsonify
from todo_list import TodoList

todo_api = Blueprint('todo_api', __name__)

# Initialize TodoList instance
todo_list = TodoList()

# Define API endpoint for creating a new todo item
@todo_api.route('/todo', methods=['POST'])
def create_todo():
    data = request.get_json()
    if 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    todo_item = todo_list.create_todo(data['title'], data['description'])
    return jsonify(todo_item), 201

# Define API endpoint for retrieving all todo items
@todo_api.route('/todo', methods=['GET'])
def get_all_todos():
    todos = todo_list.get_all_todos()
    return jsonify(todos), 200

# Define API endpoint for retrieving a single todo item by ID
@todo_api.route('/todo/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo_item = todo_list.get_todo(todo_id)
    if todo_item is None:
        return jsonify({'error': 'Todo item not found'}), 404
    return jsonify(todo_item), 200

# Define API endpoint for updating a todo item
@todo_api.route('/todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    if 'title' not in data and 'description' not in data:
        return jsonify({'error': 'No updates provided'}), 400
    todo_item = todo_list.update_todo(todo_id, data.get('title'), data.get('description'))
    if todo_item is None:
        return jsonify({'error': 'Todo item not found'}), 404
    return jsonify(todo_item), 200

# Define API endpoint for deleting a todo item
@todo_api.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if not todo_list.delete_todo(todo_id):
        return jsonify({'error': 'Todo item not found'}), 404
    return jsonify({'message': 'Todo item deleted successfully'}), 200
```