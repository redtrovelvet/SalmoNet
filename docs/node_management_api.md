## Node Management

### 1. Set Node Info
**Endpoint:** 'POST /api/set_node_info/'

#### When the API endpoint should be used

Use this endpoint when you want to set the info of your local node, can only be used by an admin.

#### How the API endpoint should be used

Send a POST request to '/api/set_node_info/'.

#### Why the API endpoint should or should not be used

- Use it to set the local node info
- Use it if you are an admin
- Don't use it if you are not the admin of a local node (it will fail)

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/set_node_info/>
Body: A JSON object with the following fields:
``` json
{
    "username": "myusername",
    "password": "mypassword"
}
```
Response:
201 Node info created

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/set_node_info/> (not an admin)
Body: A JSON object with the following fields:
``` json
{
    "username": "myusername",
    "password": "mypassword"
}
```
Response:
403 Forbidden

#### Explantion of JSON Field

username (string): Username to set the node info
password (string): Password to set the node info

### 2. Add Remote Node
**Endpoint:** 'POST /api/add_remote_node/'

#### When the API endpoint should be used

Use this endpoint when you want to add an outgoing connection to a remote node to your database

#### How the API endpoint should be used

Send a POST request to '/api/add_remote_node/'.

#### Why the API endpoint should or should not be used

- Use it to set the outgoing connection to a remote node
- Use it if you are an admin
- Don't use it if you are not the admin of a local node (it will fail)

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/add_remote_node/>
Body: A JSON object with the following fields:
``` json
{
    "host": "http://external.com",
    "username": "myusername",
    "password": "mypassword"
}
```
Response:
201 Node added

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/add_remote_node/> (not an admin)
Body: A JSON object with the following fields:
``` json
{
    "username": "myusername",
    "password": "mypassword"
}
```
Response:
403 Forbidden

#### Explantion of JSON Field

host (url): URL of the remote node
username (string): Username to set the remote node info
password (string): Password to set the remote node info

### 3. Connect Node
**Endpoint:** 'POST /api/connect/'

#### When the API endpoint should be used

Use this endpoint when you want to add an incoming connection from a remote node to the database

#### How the API endpoint should be used

Send a POST request to '/api/connect/'.

#### Why the API endpoint should or should not be used

- Use it to set the incoming connection to a remote node
- Use it if you are an external node
- Don't use it if you are on your own node, it will fail

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/connect/>
Body: A JSON object with the following fields:
``` json
{
    "username": "myusername",
    "password": "mypassword"
}
```
Response:
201 Node added

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/connect/> (not the correct username and password)
Body: A JSON object with the following fields:
``` json
{
    "username": "mywrongusername",
    "password": "mywrongpassword"
}
```
Response:
401 Unauthorized

#### Explantion of JSON Field

username (string): Username to authenticate the node
password (string): Password to authenticate the node

### 4. Connect External Node
**Endpoint:** 'POST /api/connect_external/'

#### When the API endpoint should be used

Use this endpoint when you want to fully add a remote

#### How the API endpoint should be used

Send a POST request to '/api/connect_external/'.

#### Why the API endpoint should or should not be used

- Use it to set the incoming and outgoing connections for a remote node
- Use when connecting to other groups
- Use it if you are a local node admin
- Don't use it if you are on an external node or not an admin, it will fail

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/connect_external/>
Body: A JSON object with the following fields:
``` json
{
    "host": "http://external.com",
    "username": "myusername",
    "password": "mypassword"
}
```
Response:
201 Node Info Created

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/connect_external/> (not an admin)
Body: A JSON object with the following fields:
``` json
{
    "host": "http://external.com",
    "username": "mywrongusername",
    "password": "mywrongpassword"
}
```
Response:
401 Unauthorized

#### Explantion of JSON Field

host (url): External host to connect to
username (string): Username to communicate with external node
password (string): Password to communicate with external node

### 5. Remove Connection
**Endpoint:** 'POST /api/remove_connection/'

#### When the API endpoint should be used

Use this endpoint when you want to remove an outgoing connection to a remote node from your database

#### How the API endpoint should be used

Send a POST request to '/api/remove_connection/'.

#### Why the API endpoint should or should not be used

- Use it to renmove the outgoing connection from a remote node
- Use it if you are a local node admin
- Don't use it if you are on an external node or not an admin, it will fail

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/remove_connection/>
Body: A JSON object with the following fields:
``` json
{
    "host": "http://external.com",
}
```
Response:
200 Outgoing connection removed

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/remove_connection/> (not an admin)
Body: A JSON object with the following fields:
``` json
{
    "host": "http://external.com",
}
```
Response:
403 Forbidden

#### Explantion of JSON Field

host (url): External host to remove