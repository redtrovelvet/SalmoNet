## Commented

### 1.GET and POST comments for an author
**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/commented'
**Endpoint:** 'POST /api/authors/{AUTHOR_SERIAL}/commented'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a a list of comments made by an author or when you want to create a new comment.

#### How the API endpoint should be used

Send a GET or POST request to '/api/authors/{AUTHOR_SERIAL}/commented'.

#### Why the API endpoint should or should not be used

- Use it to get all comments made by an author
- Use it to create a new comment
- Don't use if you want to get a specific comment, use the get comment endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/commented>
Response: A JSON list of "comment" objects
``` json
[
    {
        "type":"comment",
        "author":{
            "type":"author",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "host":"http://127.0.0.1:8000/api/",
            "displayName":"John Doe",
            "github": "http://github.com/jdoe",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        },
        "comment":"Hello World",
        "contentType":"text/markdown",
        "published":"2025-02-20T13:07:04+00:00",
        "id":"http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001",
        "post": "http://nodebbbb/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page": "http://nodebbbb/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        "likes": {
            "type": "likes",
            "id": "http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
            "page": "http://nodeaaaa/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
            "page_number": 1,
            "size": 50,
            "count": 0,
            "src": [],
        },
    },
    {
        "type":"comment",
        "author":{
            "type":"author",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "host":"http://127.0.0.1:8000/api/",
            "displayName":"John Doe",
            "github": "http://github.com/jdoe",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        },
        "comment":"Hello World2",
        "contentType":"text/markdown",
        "published":"2025-02-20T13:07:04+00:00",
        "id":"http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002",
        "post": "http://nodebbbb/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page": "http://nodebbbb/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        "likes": {
            "type": "likes",
            "id": "http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
            "page": "http://nodeaaaa/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
            "page_number": 1,
            "size": 50,
            "count": 0,
            "src": [],
        },
    }
]

```

#### 2nd Example

Request: POST <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/comments/543e4897-e89b-12e3-a456-426685474001>
Body: A JSON "comment" object
``` json
{
    "type":"comment",
    "comment":"Hello World",
    "contentType":"text/markdown",
    "post": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
}
```
Response: HTTP 302 Found

#### Explantion of JSON Field

type (string): always set to comment becuase it is a comment object.<br />
author (object): the author of the comment in the form of an author object.<br />
comment (string): the text content of the comment.<br />
contentType (string): the type of content in the comment.<br />
published (string): the date and time the comment was published.<br />
id (string, URL): the unique identifier of the comment.<br />
post (string, URL): the URL of the post the comment is on.<br />
page (string, URL): the URL of the page where the comment is displayed.<br />
likes (object): the likes object of the comment listing all likes.


### 2.GET comments for an author locally
**Endpoint:** 'GET /api/authors/{AUTHOR_FQID}/commented'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a a list of comments made by an author locally.

#### How the API endpoint should be used

Send a GET or POST request to '/api/authors/{AUTHOR_FQID}/commented'.

#### Why the API endpoint should or should not be used

- Use it to get all comments made by an author
- Don't use it to create a comment
- Don't use it if you want to get the comments of an author on a remote server
- Don't use if you want to get a specific comment, use the get comment endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/commented>
Response: A JSON list of "comment" objects
``` json
[
    {
        "type":"comment",
        "author":{
            "type":"author",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "host":"http://127.0.0.1:8000/api/",
            "displayName":"John Doe",
            "github": "http://github.com/jdoe",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        },
        "comment":"Hello World",
        "contentType":"text/markdown",
        "published":"2025-02-20T13:07:04+00:00",
        "id":"http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001",
        "post": "http://nodebbbb/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page": "http://nodebbbb/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        "likes": {
            "type": "likes",
            "id": "http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
            "page": "http://nodeaaaa/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
            "page_number": 1,
            "size": 50,
            "count": 0,
            "src": [],
        },
    },
    {
        "type":"comment",
        "author":{
            "type":"author",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "host":"http://127.0.0.1:8000/api/",
            "displayName":"John Doe",
            "github": "http://github.com/jdoe",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        },
        "comment":"Hello World2",
        "contentType":"text/markdown",
        "published":"2025-02-20T13:07:04+00:00",
        "id":"http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002",
        "post": "http://nodebbbb/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page": "http://nodebbbb/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        "likes": {
            "type": "likes",
            "id": "http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
            "page": "http://nodeaaaa/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
            "page_number": 1,
            "size": 50,
            "count": 0,
            "src": [],
        },
    }
]

```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/commented>
Response: A JSON list of "comment" objects
``` json
[
    {
        "type":"comment",
        "author":{
            "type":"author",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
            "host":"http://127.0.0.1:8000/api/",
            "displayName":"John Doe",
            "github": "http://github.com/jdoe",
            "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
        },
        "comment":"Hello World",
        "contentType":"text/markdown",
        "published":"2025-02-20T13:07:04+00:00",
        "id":"http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001",
        "post": "http://nodebbbb/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page": "http://nodebbbb/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        "likes": {
            "type": "likes",
            "id": "http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
            "page": "http://nodeaaaa/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
            "page_number": 1,
            "size": 50,
            "count": 0,
            "src": [],
        },
    }
]
```

#### Explantion of JSON Field

type (string): always set to comment becuase it is a comment object.<br />
author (object): the author of the comment in the form of an author object.<br />
comment (string): the text content of the comment.<br />
contentType (string): the type of content in the comment.<br />
published (string): the date and time the comment was published.<br />
id (string, URL): the unique identifier of the comment.<br />
post (string, URL): the URL of the post the comment is on.<br />
page (string, URL): the URL of the page where the comment is displayed.<br />
likes (object): the likes object of the comment listing all likes.


### 3.Get a specific comment
**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/commented/{COMMENT_SERIAL}'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a single comment locally or remotely

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_SERIAL}/commented/{COMMENT_SERIAL}'.

#### Why the API endpoint should or should not be used

- Use it to get a single comment
- Don't use if you want multiple comments from a post, use the get comments enpoints instead
- Don't use it if you have the comment FQID, use the get comment by FQID endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001>
Response: A JSON "comment" object
``` json
{
    "type":"comment",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"John Doe",
        "github": "http://github.com/jdoe",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "comment":"Hello World",
    "contentType":"text/markdown",
    "published":"2025-02-20T13:07:04+00:00",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001",
    "post": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
    "likes": {
        "type": "likes",
        "id": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
        "page": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
        "page_number": 1,
        "size": 50,
        "count": 0,
        "src": [],
    }
}

```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002>
Response: A JSON "comment" object
``` json
{
    "type":"comment",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"John Doe",
        "github": "http://github.com/jdoe",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "comment":"Hello World2",
    "contentType":"text/markdown",
    "published":"2025-02-20T13:07:04+00:00",
    "id":"http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002",
    "post": "http://nodebbbb/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://nodebbbb/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
    "likes": {
        "type": "likes",
        "id": "http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
        "page": "http://nodeaaaa/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
        "page_number": 1,
        "size": 50,
        "count": 0,
        "src": [],
    }
}
```

#### Explantion of JSON Field

type (string): always set to comment becuase it is a comment object.<br />
author (object): the author of the comment in the form of an author object.<br />
comment (string): the text content of the comment.<br />
contentType (string): the type of content in the comment.<br />
published (string): the date and time the comment was published.<br />
id (string, URL): the unique identifier of the comment.<br />
post (string, URL): the URL of the post the comment is on.<br />
page (string, URL): the URL of the page where the comment is displayed.<br />
likes (object): the likes object of the comment listing all likes.


### 4.Get a specific comment by FQID
**Endpoint:** 'GET /api/commented/{COMMENT_FQID}'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a single comment locally or remotely

#### How the API endpoint should be used

Send a GET request to '/api/commented/{COMMENT_FQID}'.

#### Why the API endpoint should or should not be used

- Use it to get a single comment
- Don't use if you want multiple comments from a post, use the get comments enpoints instead
- Don't use it if you have the author and comment serial, use the get comment endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/commented/543e4897-e89b-12e3-a456-426685474001>
Response: A JSON "comment" object
``` json
{
    "type":"comment",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"John Doe",
        "github": "http://github.com/jdoe",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "comment":"Hello World",
    "contentType":"text/markdown",
    "published":"2025-02-20T13:07:04+00:00",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001",
    "post": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
    "likes": {
        "type": "likes",
        "id": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
        "page": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
        "page_number": 1,
        "size": 50,
        "count": 0,
        "src": [],
    }
}

```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/commented/543e4897-e89b-12e3-a456-426685474002>
Response: A JSON "comment" object
``` json
{
    "type":"comment",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"John Doe",
        "github": "http://github.com/jdoe",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "comment":"Hello World2",
    "contentType":"text/markdown",
    "published":"2025-02-20T13:07:04+00:00",
    "id":"http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002",
    "post": "http://nodebbbb/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://nodebbbb/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
    "likes": {
        "type": "likes",
        "id": "http://nodeaaaa/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes",
        "page": "http://nodeaaaa/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474001/likes"
        "page_number": 1,
        "size": 50,
        "count": 0,
        "src": [],
    }
}
```

#### Explantion of JSON Field

type (string): always set to comment becuase it is a comment object.<br />
author (object): the author of the comment in the form of an author object.<br />
comment (string): the text content of the comment.<br />
contentType (string): the type of content in the comment.<br />
published (string): the date and time the comment was published.<br />
id (string, URL): the unique identifier of the comment.<br />
post (string, URL): the URL of the post the comment is on.<br />
page (string, URL): the URL of the page where the comment is displayed.<br />
likes (object): the likes object of the comment listing all likes.