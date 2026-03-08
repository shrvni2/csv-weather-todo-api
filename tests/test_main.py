```python
import pytest
import csv
import json
import os
import tempfile
import requests
from csv_to_json import csv_to_json, main
from app import app, todo_list

def test_csv_to_json_normal_case():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        json_file_path = os.path.join(temp_dir, 'output.json')
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Age'])
            csv_writer.writerow(['John', 30])
            csv_writer.writerow(['Alice', 25])
        csv_to_json(csv_file_path, json_file_path)
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        assert len(data) == 2
        assert data[0]['Name'] == 'John'
        assert data[0]['Age'] == '30'
        assert data[1]['Name'] == 'Alice'
        assert data[1]['Age'] == '25'

def test_csv_to_json_edge_case_empty_csv():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        json_file_path = os.path.join(temp_dir, 'output.json')
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
        csv_to_json(csv_file_path, json_file_path)
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        assert len(data) == 0

def test_csv_to_json_error_case_invalid_csv():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        json_file_path = os.path.join(temp_dir, 'output.json')
        with open(csv_file_path, 'w') as csv_file:
            csv_file.write('Invalid CSV data')
        with pytest.raises(csv.Error):
            csv_to_json(csv_file_path, json_file_path)

def test_main_normal_case():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        json_file_path = os.path.join(temp_dir, 'output.json')
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Age'])
            csv_writer.writerow(['John', 30])
            csv_writer.writerow(['Alice', 25])
        main_args = ['-c', csv_file_path, '-j', json_file_path]
        with pytest.raises(SystemExit) as exit_info:
            main()
        assert exit_info.value.code == 0

def test_main_edge_case_csv_file_not_found():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'non_existent_csv.csv')
        json_file_path = os.path.join(temp_dir, 'output.json')
        main_args = ['-c', csv_file_path, '-j', json_file_path]
        with pytest.raises(SystemExit) as exit_info:
            main()
        assert exit_info.value.code == 0

def test_main_error_case_invalid_args():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        json_file_path = os.path.join(temp_dir, 'output.json')
        main_args = ['-c', csv_file_path]
        with pytest.raises(SystemExit) as exit_info:
            main()
        assert exit_info.value.code == 2

def test_convert_csv_to_json_normal_case():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Age'])
            csv_writer.writerow(['John', 30])
            csv_writer.writerow(['Alice', 25])
        with open(csv_file_path, 'rb') as csv_file:
            response = app.test_client().post('/csv_to_json', data={'csv_file': csv_file})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 2
        assert data[0]['Name'] == 'John'
        assert data[0]['Age'] == '30'
        assert data[1]['Name'] == 'Alice'
        assert data[1]['Age'] == '25'

def test_convert_csv_to_json_edge_case_empty_csv():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
        with open(csv_file_path, 'rb') as csv_file:
            response = app.test_client().post('/csv_to_json', data={'csv_file': csv_file})
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 0

def test_convert_csv_to_json_error_case_invalid_csv():
    with tempfile.TemporaryDirectory() as temp_dir:
        csv_file_path = os.path.join(temp_dir, 'input.csv')
        with open(csv_file_path, 'w') as csv_file:
            csv_file.write('Invalid CSV data')
        with open(csv_file_path, 'rb') as csv_file:
            response = app.test_client().post('/csv_to_json', data={'csv_file': csv_file})
        assert response.status_code == 500

def test_manage_todo_list_normal_case():
    response = app.test_client().get('/todo_list')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 0
    response = app.test_client().post('/todo_list', json={'task': 'Buy milk'})
    assert response.status_code == 200
    response = app.test_client().get('/todo_list')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['task'] == 'Buy milk'
    response = app.test_client().put('/todo_list', json={'task_id': 0, 'task': 'Buy eggs'})
    assert response.status_code == 200
    response = app.test_client().get('/todo_list')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['task'] == 'Buy eggs'
    response = app.test_client().delete('/todo_list', json={'task_id': 0})
    assert response.status_code == 200
    response = app.test_client().get('/todo_list')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 0

def test_get_weather_normal_case():
    response = app.test_client().get('/weather')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'weather' in data
```