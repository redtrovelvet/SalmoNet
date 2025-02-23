# API documentation requirements for SocialDistribution

## Identity

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

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/>
Response: A JSON array of author objects is returned
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

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
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
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c>",
    "username": "example",
    "display_name": "Example",
    "github": "<https://www.google.com/>",
    "profile_image": "images/pexels-pixabay-158063_8FOC3DL.jpg",
    "host": "<http://127.0.0.1:8000>"
}

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a/>
Response: A JSON object representing the author's details:
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a>",
    "username": "anotherexample",
    "display_name": "Another Example",
    "github": "<http://www.github.com>",
    "profile_image": "images/pexels-pixabay-158063.jpg",
    "host": "<http://127.0.0.1:8000>"
}

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
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
{
    "username": "new_user",
    "host": "<http://127.0.0.1:8000>"
}
Response: A JSON object representing the created author's details:
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0>",
    "username": "new_user",
    "display_name": "Display Name",
    "github": null,
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}

#### 2nd Example

Request: POST <http://127.0.0.1:8000/api/authors/create/>
{
    "username": "another_new_user",
    "host": "<http://127.0.0.1:8000>"
}
Response: A JSON object representing the created author's details:
{
    "type": "author",
    "id": "<http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7>",
    "username": "another_new_user",
    "display_name": "Display Name",
    "github": null,
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
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
{
    "display_name": "Updated User"
}
Response:  A JSON object representing the updated author's details:
{
    "id": "<http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0>",
    "username": "new_user",
    "display_name": "Updated User",
    "github": null,
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}

#### 2nd Example

Request: POST <http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7/update/>
{
    "github": "<http://www.github.com/updated_user/>",
}
Response:  A JSON object representing the updated author's details:
{
    "id": "<http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7>",
    "username": "another_new_user",
    "display_name": "Display Name",
    "github": "<http://www.github.com/updated_user/>",
    "profile_image": "",
    "host": "<http://127.0.0.1:8000>"
}

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
host (string, URL): url of the node where the author is.

Below is the comprehensive documentation for your API endpoints. Each endpoint is documented with its purpose, usage, request/response structure, and examples. Additionally, I've included explanations for any interesting aspects of the endpoints, such as pagination.

---

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
    "id": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "type": "post",
    "author": {
      "id": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000",
      "displayName": "Test User",
      "github": "https://github.com/testuser"
    },
    "text": "Test Post",
    "visibility": "PUBLIC",
    "contentType": "text/plain",
    "created_at": "2023-10-01T12:00:00Z"
  }
  ```

#### **Examples**

- **Public Post**:

  ```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/
  ```

- **Friends-Only Post (Unauthenticated)**:

  ```bash
  curl -X GET http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002/
  ```

  Response:

  ```json
  {
    "detail": "Authentication credentials were not provided."
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

- To remove a post permanently from the system.

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
    "text": "Updated Post",
    "visibility": "PUBLIC"
  }
  ```

#### **Response**

- **Status Code**: `200 OK` (success), `400 Bad Request` (invalid data), `403 Forbidden` (unauthorized user), `404 Not Found` (post not found).
- **Body**:

  ```json
  {
    "id": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
    "text": "Updated Post",
    "visibility": "PUBLIC"
  }
  ```

#### **Examples**

- **Successful Update**:

  ```bash
  curl -X PUT http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001/ -H "Authorization: Token <auth_token>" -H "Content-Type: application/json" -d '{"text": "Updated Post"}'
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
    "type": "posts",
    "items": [
      {
        "id": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174001",
        "text": "Test Post",
        "visibility": "PUBLIC",
        "created_at": "2023-10-01T12:00:00Z"
      }
    ],
    "page": 1,
    "size": 10,
    "count": 1
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
    "id": "http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/123e4567-e89b-12d3-a456-426614174002",
    "text": "New Post",
    "visibility": "PUBLIC",
    "created_at": "2023-10-01T12:00:00Z"
  }
  ```

#### **Examples**

- **Successful Creation**:

  ```bash
  curl -X POST http://127.0.0.1:8000/api/authors/123e4567-e89b-12d3-a456-426614174000/posts/ -H "Authorization: Token <auth_token>" -H "Content-Type: application/json" -d '{"text": "New Post", "visibility": "PUBLIC"}'
  ```
