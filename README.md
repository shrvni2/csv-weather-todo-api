# 📚 csv-weather-todo-api
csv-weather-todo-api is a Python CLI tool and Flask API for CSV to JSON conversion, todo list management, and weather data fetching.

## 📝 Description
This project provides a command-line interface for converting CSV files to JSON, managing todo lists, and fetching weather data. It utilizes Flask to create a RESTful API for these services.

## 🎯 Features
* CSV to JSON conversion
* Todo list management
* Weather data fetching
* RESTful API using Flask

## 🛠️ Tech Stack
* Python
* Flask
* CSV
* JSON

## 📦 Installation
To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

## 📊 Usage
To use the CSV to JSON converter, run the following command:
```bash
python csv_to_json.py -c <csv_file_path> -j <json_file_path>
```
Replace `<csv_file_path>` and `<json_file_path>` with the actual file paths.

## 🗂️ Project Structure
* `csv_to_json.py`: CSV to JSON conversion script
* `app.py`: Flask API application
* `weather_fetcher.py`: Weather data fetching script
* `requirements.txt`: Dependencies required by the project
* `todo_api/routes.py`: Todo list management API routes
* `.gitignore`: Files and directories to ignore in the Git repository
* `config.py`: Configuration file for the project
* `tests/test_main.py`: Unit tests for the project

## 📄 License
This project is licensed under the MIT License. See the [GitHub repository](https://github.com/shrvni2/csv-weather-todo-api) for more information.