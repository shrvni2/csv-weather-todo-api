```python
import os

class Config:
    def __init__(self):
        self.OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
        self.TODOIST_API_KEY = os.environ.get('TODOIST_API_KEY')
        self.CSV_OUTPUT_FILE = 'output.json'
        self.WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/'
        self.TODO_LIST_FILE = 'todo.json'

config = Config()
```