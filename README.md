# gapi-tasks

## Installation

`pip install gapi-tasks`

## Usage
Import the package: 
```python
from gapitasks import Gtasks
```

Obtain a Gtasks instance:
```python
gtasks = Gtasks('credentials.json', 'token.pickle')
if gtasks.auth_url:
    gtasks.finish_login(auth_code)

```

Get all task lists:
```python
gtasks.service.tasklists().list().execute()
```

API Documentation : https://developers.google.com/resources/api-libraries/documentation/tasks/v1/python/latest/