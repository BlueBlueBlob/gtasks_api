# gapi-tasks

## Installation

`pip install gapi-tasks`

## Usage
Import the package: 
```python
from gapi-tasks import Gtasks
```

Obtain a Gtasks instance:
```python
gtasks = Gtasks('credentials.json', 'token.pickle')
if gtasks.auth_url:
    gtasks.finish_login(auth_code)

```

