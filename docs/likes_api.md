## Likes

### 1.Get likes on a POST
**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/likes'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve all likes on a post

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/likes'.

#### Why the API endpoint should or should not be used

- Use it to get a all likes on a post
- Don't use if you want to get a single like
- Don't use if you want to get all likes on a comment, use the get likes on comment endpoint instead
- Don't use if you have the post FQID, use the get likes by FQID endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/likes/?page=1&size=1>
Response: A JSON "likes" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/likes",
    "page_number":1,
    "size":1,
    "count": 2,
    "src":[
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        },
    ]
}

```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/likes/>
Response: A JSON "comment" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/likes",
    "page_number":1,
    "size":2,
    "count": 2,
    "src":[
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        },
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        }
    ]
}
```

#### Explantion of JSON Field

type (string): always set to likes becuase it is a likes object.<br />
page (string, URL): the URL of the page where the likes are displayed.<br />
id (string, URL): the unique identifier of the likes.<br />
page_number (int): the current page number of the likes.<br />
size (int): the number of likes per page.<br />
count (int): the total number of likes.<br />
src (list): a list of "like" objects.

#### Interesting Features
Pagination: The likes are paginated, with the page number and size specified in the response.
- To use pagination, the client can use the "page" and "size" query parameters in the request URL.


### 2.Get likes on a POST by FQID
**Endpoint:** 'GET /api/posts/{POST_FQID}/likes'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve all likes on a post

#### How the API endpoint should be used

Send a GET request to '/api/posts/{POST_FQID}/likes'.

#### Why the API endpoint should or should not be used

- Use it to get a all likes on a post
- Don't use if you want to get a single like
- Don't use if you want to get all likes on a comment, use the get likes on comment endpoint instead
- Don't use if you have the author and post serial, use the get likes endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/likes/?page=1&size=1>
Response: A JSON "likes" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/likes",
    "page_number":1,
    "size":1,
    "count": 2,
    "src":[
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        },
    ]
}

```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/likes/>
Response: A JSON "comment" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001/likes",
    "page_number":1,
    "size":2,
    "count": 2,
    "src":[
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        },
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001"
        }
    ]
}
```

#### Explantion of JSON Field

type (string): always set to likes becuase it is a likes object.<br />
page (string, URL): the URL of the page where the likes are displayed.<br />
id (string, URL): the unique identifier of the likes.<br />
page_number (int): the current page number of the likes.<br />
size (int): the number of likes per page.<br />
count (int): the total number of likes.<br />
src (list): a list of "like" objects.

#### Interesting Features
Pagination: The likes are paginated, with the page number and size specified in the response.
- To use pagination, the client can use the "page" and "size" query parameters in the request URL.


### 3.Get likes on a comment
**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/comments/{COMMENT_FQID}/likes'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve all likes on a comment

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/comments/{COMMENT_FQID}/likes'.

#### Why the API endpoint should or should not be used

- Use it to get a all likes on a comment
- Don't use if you want to get a single like
- Don't use if you want to get all likes on a post, use the get likes on post endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/comments/543e4897-e89b-12e3-a456-426685474002/likes/?page=1&size=1>
Response: A JSON "likes" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/comments/543e4897-e89b-12e3-a456-426685474002",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002/likes",
    "page_number":1,
    "size":1,
    "count": 2,
    "src":[
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002"
        },
    ]
}


```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/posts/123e4567-e89b-12d3-a456-426614174001/comments/543e4897-e89b-12e3-a456-426685474002/likes/>
Response: A JSON "comment" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/comments/543e4897-e89b-12e3-a456-426685474002",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002/likes",
    "page_number":1,
    "size":2,
    "count": 2,
    "src":[
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002"
        },
        {
            "type":"like",
            "author":{
                "type":"author",
                "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/123e4567-e89b-12d3-a456-426614174001",
                "host":"http://127.0.0.1:8000/api/",
                "displayName":"John Doe",
                "github": "http://github.com/jdoe",
                "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
            },
            "published":"2025-02-20T13:07:04+00:00",
            "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384",
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/commented/543e4897-e89b-12e3-a456-426685474002"
        }
    ]
}
```

#### Explantion of JSON Field

type (string): always set to likes becuase it is a likes object.<br />
page (string, URL): the URL of the page where the likes are displayed.<br />
id (string, URL): the unique identifier of the likes.<br />
page_number (int): the current page number of the likes.<br />
size (int): the number of likes per page.<br />
count (int): the total number of likes.<br />
src (list): a list of "like" objects.

#### Interesting Features
Pagination: The likes are paginated, with the page number and size specified in the response.
- To use pagination, the client can use the "page" and "size" query parameters in the request URL.