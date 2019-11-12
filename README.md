# gapi-tasks
[![Build Status](https://travis-ci.com/BlueBlueBlob/gapi-tasks.svg?branch=master)](https://travis-ci.com/BlueBlueBlob/gapi-tasks)

## Installation

`pip install gapi-tasks`

## Usage
Import the package: 
```python
from gtasks_api import GtasksAPI
```

Obtain a Gtasks instance:
```python
gtasks = GtasksAPI('credentials.json', 'token.pickle')
if gtasks.auth_url:
    gtasks.finish_login(auth_code)

```

Get all task lists:
```python
gtasks.service.tasklists().list().execute()
```

API Documentation : https://developers.google.com/resources/api-libraries/documentation/tasks/v1/python/latest/