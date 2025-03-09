# Author

### 1.Get all Authors

**Endpoint:** 'GET /api/authors/'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a list of all authors in the local node.

#### How the API endpoint should be used

Send a GET request to '/api/authors/'.

#### Why the API endpoint should or should not be used

- use it to display all available authors
- Maybe don't use if database is really large because API might time-out, use pagnation instead, but not implemented yet.

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/>
Response: A JSON array of author objects is returned
``` json
[
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c",
        "username": "example",
        "display_name": "Example",
        "github": "https://www.google.com/",
        "profile_image": "images/pexels-pixabay-158063_8FOC3DL.jpg",
        "host": "http://127.0.0.1:8000"
    },
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a",
        "username": "anotherexample",
        "display_name": "Another Example",
        "github": "http://www.github.com",
        "profile_image": "images/pexels-pixabay-158063.jpg",
        "host": "http://127.0.0.1:8000"
    }
]
```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/>
Response: A JSON array of author objects is returned
``` json
[
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c",
        "username": "example",
        "display_name": "Example",
        "github": "https://www.google.com/",
        "profile_image": "images/pexels-pixabay-158063_8FOC3DL.jpg",
        "host": "http://127.0.0.1:8000"
    },
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a",
        "username": "anotherexample",
        "display_name": "Another Example",
        "github": "http://www.github.com",
        "profile_image": "images/pexels-pixabay-158063.jpg",
        "host": "http://127.0.0.1:8000"
    },
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/72a7003a-b440-457d-99ac-17469b9f3076",
        "username": "examplethree",
        "display_name": "Example Three",
        "github": "http://www.github.com/example_three",
        "profile_image": "",
        "host": "http://127.0.0.1:8000"
    }
]
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
username (string): the author's unique username.<br />
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
host (string, URL): url of the node where the author is.

### 2.Get Specific Author

**Endpoint:** 'GET /api/authors/{author_id}/'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve details about a specific author using their unique identifier.

#### How the API endpoint should be used

Send a GET request to '/api/authors/{author_id}'.
Replace {author_id} with the actual UUID of the author.

#### Why the API endpoint should or should not be used

- use it to display author details for a specific author.
- Don't use if you don't know the author id.

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/>
Response: A JSON object representing the author's details:
``` json
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c>",
    "username": "example",
    "display_name": "Example",
    "github": "<https://www.google.com/>",
    "profile_image": "images/pexels-pixabay-158063_8FOC3DL.jpg",
    "host": "<http://127.0.0.1:8000>"
}
```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a/>
Response: A JSON object representing the author's details:
``` json
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a>",
    "username": "anotherexample",
    "display_name": "Another Example",
    "github": "<http://www.github.com>",
    "profile_image": "images/pexels-pixabay-158063.jpg",
    "host": "<http://127.0.0.1:8000>"
}
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
username (string): the author's unique username.<br />
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
host (string, URL): url of the node where the author is.

### 3.Create Author

**Endpoint:** 'POST /api/authors/create/'

#### When the API endpoint should be used

Use this endpoint when you want to create a new author.

#### How the API endpoint should be used

Send a POST request to '/api/authors/create' with the required fields.

#### Why the API endpoint should or should not be used

- use it to create a new author.
- Don't use if you want to update existing author.

#### 1st Example

Request: POST <http://127.0.0.1:8000/api/authors/create/>
``` json
{
    "username": "new_user",
    "host": "<http://127.0.0.1:8000>"
}
```
Response: A JSON object representing the created author's details:
``` json
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0>",
    "username": "new_user",
    "display_name": "Display Name",
    "github": null,
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}
```

#### 2nd Example

Request: POST <http://127.0.0.1:8000/api/authors/create/>
``` json
{
    "username": "another_new_user",
    "host": "<http://127.0.0.1:8000>"
}
```
Response: A JSON object representing the created author's details:
``` json
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7>",
    "username": "another_new_user",
    "display_name": "Display Name",
    "github": null,
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
username (string): the author's unique username.<br />
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
host (string, URL): url of the node where the author is.

### 4.Update a Specific Author

**Endpoint:** 'POST /api/authors/{author_id}/update/'

#### When the API endpoint should be used

Use this endpoint when you want to update an author's profile.

#### How the API endpoint should be used

Send a POST request to '/api/authors/{author_id}/update/'.
Replace {author_id} with the actual UUID of the author.

#### Why the API endpoint should or should not be used

- use it to change an exisitng author's details.
- Don't use if you don't know the author id or author does not exist.

#### 1st Example

Request: POST <http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0/update/>
``` json
{
    "display_name": "Updated User"
}
```
Response:  A JSON object representing the updated author's details:
``` json
{
    "id": "<http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0>",
    "username": "new_user",
    "display_name": "Updated User",
    "github": null,
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}
```

#### 2nd Example

Request: POST <http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7/update/>
``` json
{
    "github": "<http://www.github.com/updated_user/>",
}
```
Response:  A JSON object representing the updated author's details:
``` json
{
    "id": "<http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7>",
    "username": "another_new_user",
    "display_name": "Display Name",
    "github": "<http://www.github.com/updated_user/>",
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
username (string): the author's unique username.<br />
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
host (string, URL): url of the node where the author is.