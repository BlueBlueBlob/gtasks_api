# gtasks_api
[![Build Status](https://travis-ci.com/BlueBlueBlob/gapi-tasks.svg?branch=master)](https://travis-ci.com/BlueBlueBlob/gapi-tasks)
[![CodeFactor](https://www.codefactor.io/repository/github/blueblueblob/gtasks_api/badge)](https://www.codefactor.io/repository/github/blueblueblob/gtasks_api)

## Installation

`pip install gtasks_api`

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