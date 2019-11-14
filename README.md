# gtasks_api
[![Build Status](https://travis-ci.com/BlueBlueBlob/gtasks_api.svg?branch=master)](https://travis-ci.com/BlueBlueBlob/gtasks_api)
[![CodeFactor](https://www.codefactor.io/repository/github/blueblueblob/gtasks_api/badge)](https://www.codefactor.io/repository/github/blueblueblob/gtasks_api)
[![PyPI](https://img.shields.io/pypi/v/gtasks-api.svg)](https://pypi.org/project/gtasks-api/)
## Installation

`pip install gtasks-api`

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