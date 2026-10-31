# alu-back-end

Back-end projects that gather data from a REST API
(https://jsonplaceholder.typicode.com) and export it.

## api

| File | Description |
|------|-------------|
| `0-gather_data_from_an_API.py` | Prints an employee's TODO list progress |
| `1-export_to_CSV.py` | Exports an employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports an employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' tasks to `todo_all_employees.json` |

## Usage

```
python3 api/0-gather_data_from_an_API.py 2
python3 api/1-export_to_CSV.py 2
python3 api/2-export_to_JSON.py 2
python3 api/3-dictionary_of_list_of_dictionaries.py
```

Requires Python 3 and the `requests` module (`pip3 install requests`).
