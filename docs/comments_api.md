# Comments

### 1.Get comments on a post by author and post serial

**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/comments/'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve all of the comments on the post in the form of a "comments" object

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/comments/'.

#### Why the API endpoint should or should not be used

- Use it to display all comments on a post
- Don't use if you have the post FQID, use the post FQID endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/comments/>
Response: A JSON "comments" object
``` json
{
    "type":"comments",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/comments/",
    "page_number":1,
    "size":2,
    "count": 2,
    "src":[
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
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002",
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
            },
        }
    ]
}

```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/comments/?page=1&size=1>
Response: A JSON "comments object"
``` json
{
    "type":"comments",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/comments/",
    "page_number":1,
    "size":1,
    "count": 2,
    "src":[
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
            },
        }
    ]
}
```

#### Explantion of JSON Field

type (string): always set to comments becuase it is a comments object.<br />
page (string, URL): the URL of the page where the comments are displayed.<br />
id (string, URL): the unique identifier of the post's comments.<br />
page_number (int): the current page number of the comments.<br />
size (int): the number of comments per page.<br />
count (int): the total number of comments.<br />
src (array): an array of comment objects.

#### Interesting Features
Pagination: The comments are paginated, with the page number and size specified in the response.
- To use pagination, the client can use the "page" and "size" query parameters in the request URL.


### 2.Get comments on a post by post FQID
**Endpoint:** 'GET /api/posts/{POST_FQID}/comments'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve all of the comments on the post in the form of a "comments" object

#### How the API endpoint should be used

Send a GET request to '/api/posts/{POST_FQID}/comments'.

#### Why the API endpoint should or should not be used

- Use it to display all comments on a post
- Don't use if you have the author and post serial, use the author and post serial endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/comments/>
Response: A JSON "comments" object
``` json
{
    "type":"comments",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/comments/",
    "page_number":1,
    "size":2,
    "count": 2,
    "src":[
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
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002",
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
            },
        }
    ]
}

```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/comments/?page=1&size=1>
Response: A JSON "comments object"
``` json
{
    "type":"comments",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/comments/",
    "page_number":1,
    "size":1,
    "count": 2,
    "src":[
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
            },
        }
    ]
}
```

#### Explantion of JSON Field

type (string): always set to comments becuase it is a comments object.<br />
page (string, URL): the URL of the page where the comments are displayed.<br />
id (string, URL): the unique identifier of the post's comments.<br />
page_number (int): the current page number of the comments.<br />
size (int): the number of comments per page.<br />
count (int): the total number of comments.<br />
src (array): an array of comment objects.

#### Interesting Features
Pagination: The comments are paginated, with the page number and size specified in the response.
- To use pagination, the client can use the "page" and "size" query parameters in the request URL.


### 3.Get a specific comment
**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/post/{POST_SERIAL}/comment/{REMOTE_COMMENT_FQID}'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a single comment

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_SERIAL}/post/{POST_SERIAL}/comment/{REMOTE_COMMENT_FQID}'.

#### Why the API endpoint should or should not be used

- Use it to get a single comment
- Don't use if you want multiple comments from a post, use the get comments enpoints instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/comments/543e4897-e89b-12e3-a456-426685474001>
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

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/comments/543e4897-e89b-12e3-a456-426685474002>
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