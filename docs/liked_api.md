## Liked

### 1.Get author's likes
**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/liked'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve all likes by an author

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_SERIAL}/liked'.

#### Why the API endpoint should or should not be used

- Use it to get a all likes by an author
- Don't use if you want to get a single like
- Don't use if you want to get all likes on a post or comment, use the get likes on post or comment endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/?page=1&size=1>
Response: A JSON "likes" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/likes",
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

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/>
Response: A JSON "comment" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/likes",
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
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/543e4897-e89b-12e3-a456-426685474002"
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


### 2.Get a single like
**Endpoint:** 'GET /api/authors/{AUTHOR_SERIAL}/liked/{LIKE_SERIAL}'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a single like by an author

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_SERIAL}/liked/{LIKE_SERIAL}'.

#### Why the API endpoint should or should not be used

- Use it to get a single like by an author
- Don't use if you want to get multiple likes, use the get likes endpoint instead
- Don't use if you have the like FQID, use the get like by FQID endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7384>
Response: A JSON "like" object
``` json
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


```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7385>
Response: A JSON "comment" object
``` json
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
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7385",
    "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/543e4897-e89b-12e3-a456-426685474002"
}
```

#### Explantion of JSON Field

type (string): always set to like becuase it is a like object.<br />
author (object): the author who liked the object in the form of an author object.<br />
published (string): the date and time the like was published.<br />
id (string, URL): the unique identifier of the like.<br />
object (string, URL): the URL of the object that was liked (either a post or a comment).


### 3.Get author's likes by FQID
**Endpoint:** 'GET /api/authors/{AUTHOR_FQID}/liked'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve all likes by an author

#### How the API endpoint should be used

Send a GET request to '/api/authors/{AUTHOR_FQID}/liked'.

#### Why the API endpoint should or should not be used

- Use it to get a all likes by an author
- Don't use if you want to get a single like
- Don't use if you want to get all likes on a post or comment, use the get likes on post or comment endpoint instead
- Don't use for remote authors

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/?page=1&size=1>
Response: A JSON "likes" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/likes",
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

Request: GET <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/>
Response: A JSON "comment" object
``` json
{
    "type":"likes",
    "page":"http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c",
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/likes",
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
            "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/543e4897-e89b-12e3-a456-426685474002"
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


### 4.Get a single like by FQID
**Endpoint:** 'GET /api/liked/{LIKE_FQID}'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a single like

#### How the API endpoint should be used

Send a GET request to '/api/liked/{LIKE_FQID}'.

#### Why the API endpoint should or should not be used

- Use it to get a single like 
- Don't use if you want to get multiple likes, use the get likes endpoint instead
- Don't use if you have the like author and like serial, use the get like endpoint instead

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/liked/12123457-e89b-12d3-a456-42661ead7384>
Response: A JSON "like" object
``` json
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


```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/liked/12123457-e89b-12d3-a456-42661ead7385>
Response: A JSON "comment" object
``` json
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
    "id":"http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/liked/12123457-e89b-12d3-a456-42661ead7385",
    "object": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/543e4897-e89b-12e3-a456-426685474002"
}
```

#### Explantion of JSON Field

type (string): always set to like becuase it is a like object.<br />
author (object): the author who liked the object in the form of an author object.<br />
published (string): the date and time the like was published.<br />
id (string, URL): the unique identifier of the like.<br />
object (string, URL): the URL of the object that was liked (either a post or a comment).


### 5.Like a post
**Endpoint:** 'POST /api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/liked'

#### When the API endpoint should be used

Use this endpoint when you want to like a post

#### How the API endpoint should be used

Send a POST request to '/api/authors/{AUTHOR_SERIAL}/posts/{POST_SERIAL}/liked'.
AUTHOR_SERIAL is the serial of the author who liked the post.
POST_SERIAL is the serial of the post that was liked.

#### Why the API endpoint should or should not be used

- Use it to like a post
- Don't use it to like a comment, use the like comment endpoint instead

#### 1st Example

Request: POST <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/543e4897-e89b-12e3-a456-426685474002/liked>
BODY:
``` json
{
    "type":"like"
}
```
Response: HTTP 302 Found

#### 2nd Example

Request: POST <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/posts/543e4897-e89b-12e3-a456-426685474002/liked>
BODY:
``` json
{
    "type":"comment"
}
```
Response: HTTP 405 Method Not Allowed

#### Explantion of JSON Field

type (string): always set to like becuase it is a like object.


### 6.Like a comment
**Endpoint:** 'POST /api/authors/{AUTHOR_SERIAL}/comments/{COMMENT_SERIAL}/liked'

#### When the API endpoint should be used

Use this endpoint when you want to like a comment

#### How the API endpoint should be used

Send a POST request to '/api/authors/{AUTHOR_SERIAL}/comments/{comment_SERIAL}/liked'.
AUTHOR_SERIAL is the serial of the author who liked the comment.
POST_SERIAL is the serial of the comment that was liked.

#### Why the API endpoint should or should not be used

- Use it to like a comment
- Don't use it to like a post, use the like post endpoint instead

#### 1st Example

Request: POST <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/comments/543e4897-e89b-12e3-a456-426685474002/liked>
BODY:
``` json
{
    "type":"like"
}
```
Response: HTTP 302 Found

#### 2nd Example

Request: POST <http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/comments/543e4897-e89b-12e3-a456-426685474002/liked>
BODY:
``` json
{
    "type":"comment"
}
```
Response: HTTP 405 Method Not Allowed

#### Explantion of JSON Field

type (string): always set to like becuase it is a like object.