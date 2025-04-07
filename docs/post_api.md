# Posts

### 1. **Get a Specific Post**

#### **Endpoint**: `GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/`

#### **When to Use**

- Use this endpoint to retrieve the details of a specific post by its ID.
- Useful for displaying a single post on a user's profile or feed.

#### **How to Use**

- Send a `GET` request to the endpoint with the `AUTHOR_ID` and `POST_ID` in the URL.
- If the post is friends-only, the user must be authenticated.

#### **Why to Use**

- To fetch a single post for display or editing.
- To verify the existence of a post.

#### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the author (e.g., `123e4567-e89b-12d3-a456-426614174000`).
  - `POST_ID`: UUID of the post (e.g., `123e4567-e89b-12d3-a456-426614174001`).

#### **Response**

- **Status Code**: `200 OK` (success), `403 Forbidden` (friends-only post without authentication), `404 Not Found` (post not found).
- **Body**:

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"PUBLIC"
  }
```

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post for Friends!",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"FRIENDS"
  }
```

#### **Examples**

- **Public Post**:

```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/
```
Response:

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"PUBLIC"
  }

- **Friends-Only Post (Unauthenticated)**:

```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002/
```

  - If user is not logged in:
  Response:

```json
  {
    "detail": "Authentication required."
  }
```

  - If user is not a friend:
  Response:

```json
  {
    "detail": "You are not friends with the author."
  }
```

  - If user is a friend:
  Response:

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"PUBLIC"
  }
```

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post for Friends!",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"FRIENDS"
  }
```

---

### 2. **Delete a Post**

#### **Endpoint**: `DELETE /api/authors/{AUTHOR_ID}/posts/{POST_ID}/`

#### **When to Use**

- Use this endpoint to delete a post created by the authenticated author.
- Useful for removing outdated or incorrect posts.

#### **How to Use**

- Send a `DELETE` request to the endpoint with the `AUTHOR_ID` and `POST_ID` in the URL.
- The user must be authenticated as the author of the post.

#### **Why to Use**

- This endpoint soft-deletes the post by setting its visibility to "DELETED". The post is no longer visible but remains in the database.

#### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the author (e.g., `123e4567-e89b-12d3-a456-426614174000`).
  - `POST_ID`: UUID of the post (e.g., `123e4567-e89b-12d3-a456-426614174001`).

#### **Response**

- **Status Code**: `204 No Content` (success), `403 Forbidden` (unauthorized user), `404 Not Found` (post not found).

#### **Examples**

- **Successful Deletion**:

```bash
  curl -X DELETE http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/ -H "Authorization: Token <auth_token>"
```

 Response:

```json
  {
    "detail": "Post Deleted."
  }
```

- **Unauthorized User**:

```bash
  curl -X DELETE http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/
```

  Response:

```json
  {
    "detail": "Authentication credentials were not provided."
  }
```

---

### 3. **Update a Post**

#### **Endpoint**: `PUT /api/authors/{AUTHOR_ID}/posts/{POST_ID}/`

#### **When to Use**

- Use this endpoint to update the content of a post.
- Useful for correcting typos or updating information.

#### **How to Use**

- Send a `PUT` request to the endpoint with the `AUTHOR_ID` and `POST_ID` in the URL.
- Include the updated post data in the request body.
- The user must be authenticated as the author of the post.

#### **Why to Use**

- To modify an existing post without deleting and recreating it.

#### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the author (e.g., `123e4567-e89b-12d3-a456-426614174000`).
  - `POST_ID`: UUID of the post (e.g., `123e4567-e89b-12d3-a456-426614174001`).
- **Body**:

```json
  {
    "content": "Updated Post",
  }
```

#### **Response**

- **Status Code**: `200 OK` (success), `400 Bad Request` (invalid data), `403 Forbidden` (unauthorized user), `404 Not Found` (post not found).
- **Body**:

```json
  {
    "id": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "content": "Updated Post",
  }
```

#### **Examples**

- **Successful Update**:

```bash
  curl -X PUT http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/ -H "Authorization: Token <auth_token>" -H "contentType: text/plain" -d '{"text": "Updated Post"}'
```

- **Invalid Data**:

```bash
  curl -X PUT http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/ -H "Authorization: Token <auth_token>" -H "Content-Type: application/json" -d '{"text": ""}'
```

  Response:

```json
  {
    "text": ["This field may not be blank."]
  }
```

---

### 4. **Get Posts by Author**

#### **Endpoint**: `GET /api/authors/{AUTHOR_ID}/posts/`

#### **When to Use**

- Use this endpoint to retrieve all posts by a specific author.
- Useful for displaying a user's profile or feed.

#### **How to Use**

- Send a `GET` request to the endpoint with the `AUTHOR_ID` in the URL.
- Pagination is supported using query parameters (`page` and `size`).

#### **Why to Use**

- To fetch a list of posts for display or analysis.

#### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the author (e.g., `123e4567-e89b-12d3-a456-426614174000`).
- **Query Parameters**:
  - `page`: Page number (default: `1`).
  - `size`: Number of posts per page (default: `10`).

#### **Response**

- **Status Code**: `200 OK` (success), `404 Not Found` (author not found).
- **Body**:

```json
  {
    "type":"posts",
    "page_number":1,
    "size":10,
    "count": 9001,
    "src":[
        
        {
          "type":"post",
          "title":"plain text post",
          "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
          "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
          "description":"plain text post",
          "contentType":"text/plain",
          "content":"Test Post",
          "author":{
              "type":"author",
              "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
              "host":"http://127.0.0.1:8000/api/",
              "displayName":"Test User",
              "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
              "github": "https://github.com/testuser",
              "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
          },
          "published":"2015-03-09T13:07:04+00:00",
          "visibility":"PUBLIC"
        },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
        { "type":"post", /* ... the rest of the post object */ },
    ]

  }
```

#### **Examples**

- **Fetch First Page**:

```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/?page=1&size=10
```

- **Fetch Second Page**:

```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/?page=2&size=10
```

---

### 5. **Create a Post**

#### **Endpoint**: `POST /api/authors/{AUTHOR_ID}/posts/`

#### **When to Use**

- Use this endpoint to create a new post.
- Useful for authors to share content.

#### **How to Use**

- Send a `POST` request to the endpoint with the `AUTHOR_ID` in the URL.
- Include the post data in the request body.
- The user must be authenticated as the author.

#### **Why to Use**

- To add new content to the platform.

#### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the author (e.g., `123e4567-e89b-12d3-a456-426614174000`).
- **Body**:

```json
  {
    "text": "New Post",
    "visibility": "PUBLIC",
    "contentType": "text/plain"
  }
```

#### **Response**

- **Status Code**: `201 Created` (success), `400 Bad Request` (invalid data), `403 Forbidden` (unauthorized user).
- **Body**:

```json
  {
  "type":"post",
  "title":"plain text post",
  "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174011",
  "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174011",
  "description":"plain text post",
  "contentType":"text/plain",
  "content":"New Post",
  "author":{
      "type":"author",
      "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
      "host":"http://127.0.0.1:8000/api/",
      "displayName":"Test User",
      "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
      "github": "https://github.com/testuser",
      "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
  "published":"2015-03-09T13:07:04+00:00",
  "visibility":"PUBLIC"
  }
```

#### **Examples**

- **Successful Creation**:

```bash
  curl -X POST http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/ -H "Authorization: Token <auth_token>" -H "Content-Type: application/json" -d '{"text": "New Post", "visibility": "PUBLIC"}'
```

---

### 6. **Get a Specific Post by FQID**

#### **Endpoint**: `GET /api/posts/{POST_FQID}/`

#### **When to Use**

- Use this endpoint to retrieve the details of a specific post by its FQID.

#### **How to Use**

- Send a `GET` request to the endpoint with the `POST_FQID` in the URL.
- If the post is friends-only, the user must be authenticated.

#### **Why to Use**

- To fetch a single post for display or editing.
- To verify the existence of a post.
- To display the post without needing to separately supply the author's identifier.

#### **Request**

- **URL Parameters**:
  - `POST_FQID`: Fully Qualified ID (FQID) of the post (e.g., `http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001`).

#### **Response**

- **Status Code**: `200 OK` (success), `403 Forbidden` (Authentication required.), `404 Not Found` (post not found).
- **Body**:

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"PUBLIC"
  }
```

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post for Friends!",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"FRIENDS"
  }
```

#### **Examples**

- **Public Post**:

```bash
  curl -X GET http://127.0.0.1:8000/api/posts/http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/
```
Response:

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"PUBLIC"
  }
```


- **Friends-Only Post (Unauthenticated)**:

```bash
  curl -X GET http://127.0.0.1:8000/api/posts/http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002/
```

  - If user is not logged in:
  Response:

```json
  {
    "detail": "Authentication required."
  }
```

  - If user is not a friend:
  Response:

```json
  {
    "detail": "You are not friends with the author."
  }
```

  - If user is a friend:
  Response:

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"PUBLIC"
  }
```

```json
    {
    "type":"post",
    "title":"plain text post",
    "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "page": "http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "description":"plain text post",
    "contentType":"text/plain",
    "content":"Test Post for Friends!",
    "author":{
        "type":"author",
        "id":"http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
        "host":"http://127.0.0.1:8000/api/",
        "displayName":"Test User",
        "page":"http://127.0.0.1:8000/authors/123e4567-e89b-12d3-a456-426614174000",
        "github": "https://github.com/testuser",
        "profileImage": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174010/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"FRIENDS"
  }
```

---


### 7. **Get Image Post**

#### **Endpoint**: `GET /api/authors/{AUTHOR_ID}/posts/{POST_ID}/image`

#### **When to Use**

- Use this endpoint to retrieve an image post converted to binary format.
- It supports both local and remote requests.
- Returns a 404 Not Found if the specified post is not an image.

#### **How to Use**

- Send a `GET` request to the endpoint with the `AUTHOR_ID` and `POST_ID` in the URL.
- The returned binary data is suitable for rendering in image tags, or for proxying/caching purposes.

#### **Why to Use**

- To fetch the actual image data of a post when the post represents an image.
- Useful for displaying images embedded in Markdown or in client applications.

#### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the author (e.g., `123e4567-e89b-12d3-a456-426614174000`).
  - `POST_ID`: UUID of the image post (e.g., `123e4567-e89b-12d3-a456-426614174004`).

#### **Response**

- **Status Code**: `200 OK` (success), `403 Forbidden` (friends-only post without authentication), `404 Not Found` (post not found).

#### **Examples**

- **Public Post**:

```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174004/image/
```
Response:
An HTTP response displaying the image from the image post with uuid = 123e4567-e89b-12d3-a456-426614174004

- **Friends-Only Post (Unauthenticated)**:

```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174005/image/
```

  - If user is not logged in:
  Response:

```json
  {
    "detail": "Authentication required."
  }
```

  - If user is not a friend:
  Response:

```json
  {
    "detail": "You are not friends with the author."
  }
```

  - If user is a friend:
  Response:

An HTTP response displaying the image from the image post with uuid = 123e4567-e89b-12d3-a456-426614174005

---

### 8. **Get Image Post By FQID**

#### **Endpoint**: `GET /api/posts/{POST_FQID}/image`

#### **When to Use**

- Use this endpoint to retrieve an image post converted to binary format.
- It supports both local and remote requests.
- Returns a 404 Not Found if the specified post is not an image.

#### **How to Use**

- Send a `GET` request to the endpoint with the `POST_FQID` in the URL.
- The returned binary data is suitable for rendering in image tags, or for proxying/caching purposes.

#### **Why to Use**

- To fetch the actual image data of a post when the post represents an image.
- Useful for displaying images embedded in Markdown or in client applications.

#### **Request**

- **URL Parameters**:
  - `POST_FQID`: Fully qualified ID (FQID) of the image post (e.g., `http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174004`).

#### **Response**

- **Status Code**: `200 OK` (success), `403 Forbidden` (friends-only post without authentication), `404 Not Found` (post not found).

#### **Examples**

- **Public Post**:

```bash
  curl -X GET http://127.0.0.1:8000/api/posts/http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174004/image/
```
Response:
An HTTP response displaying the image from the image post with FQID = http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174004 

- **Friends-Only Post (Unauthenticated)**:

```bash
  curl -X GET http://127.0.0.1:8000/api/posts/http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174005/image/
```

  - If user is not logged in:
  Response:

```json
  {
    "detail": "Authentication required."
  }
```

  - If user is not a friend:
  Response:

```json
  {
    "detail": "You are not friends with the author."
  }
```

  - If user is a friend:
  Response:

An HTTP response displaying the image from the image post with FQID = http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174005


---
