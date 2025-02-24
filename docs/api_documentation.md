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

type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
host (string, URL): url of the node where the author is.


## Following/Friends:

### 1.Send Follow Request:

**Endpoint:** 'POST /authors/<uuid:author_id>/follow/'

#### When to use this endpoint:
Use this endpoint when an authenticated author wants to follow another author. This sends a follow request from the current user to the target author.

#### How the API endpoint should be used:
Send a POST request to /authors/<uuid:author_id>/follow/, replacing <uuid:author_id> with the UUID of the target author.

### Response:
On success, the endpoint redirects (HTTP 302) to the target author’s profile page, indicating that the follow request was sent.

#### 1st Example:
Request: POST http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/follow/

Response: HTTP 302 redirect to the profile page with a success message.

### 2. Approve Follow Request:

**Endpoint:** 'POST /follow_requests/<int:request_id>/approve/'

#### When to use this endpoint:
Use this endpoint when an authenticated author (the receiver) wants to approve a follow request.

#### How the API endpoint should be used:
Send a POST request to /follow_requests/<int:request_id>/approve/ replacing <int:request_id> with the follow request's numeric ID.

### Response:
On success, the follow request's status is updated to "ACCEPTED", the sender is added as a follower, and the endpoint redirects (HTTP 302) with a confirmation message.

#### Example:
Request: POST http://127.0.0.1:8000/follow_requests/10/approve/

Response: HTTP 302 redirect with a message that the follow request was approved.

### 3. Deny Follow Request:

**Endpoint:** 'POST /follow_requests/<int:request_id>/deny/'

#### When to use this endpoint:
Use this endpoint when an authenticated author (the receiver) wants to deny a follow request.

#### How the API endpoint should be used:
Send a POST request to /follow_requests/<int:request_id>/deny/, replacing <int:request_id> with the numeric identifier of the follow request.

### Response:
On success, the follow request's status is updated to "DENIED", and the endpoint redirects (HTTP 302) with a message indicating the request was denied.

#### Example:
Request: POST http://127.0.0.1:8000/follow_requests/10/deny/

Response: HTTP 302 redirect with a message that the follow request was denied.

### 4. Unfollow an Author:

**Endpoint:** 'GET /authors/<uuid:author_id>/unfollow/'

#### When to use this endpoint:
Use this endpoint when an authenticated author wants to unfollow another author.

#### How the API endpoint should be used:
Send a GET request to /authors/<uuid:author_id>/unfollow/, where <uuid:author_id> is the UUID of the author to unfollow.

### Response:
On success, the specified author is removed from the current user's following list (and posts from that author are blocked from the feed). The endpoint then redirects (HTTP 302) to the unfollowed author's profile page..

#### Example:
Request: GET http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/unfollow/


Response: HTTP 302 redirect with a message confirming the unfollow action.

### 5. View Followers, Following, and Friends:

**Endpoint:**
- View Followers: GET /profile/followers/
- View Following: GET /profile/following/
- View Friends: GET /profile/friends/

#### When to use this endpoint:
Use these endpoints to view the lists of:
    - Authors following the current user (followers),
    - Authors the current user is following (following),
    - Authors who are mutual followers (friends).

#### How the API endpoint should be used:
Send a GET request to each endpoint. These endpoints render HTML pages listing the respective authors.


#### Example:
Request: GET http://127.0.0.1:8000/profile/followers/

Response: An HTML page is returned listing all followers of the current user.

### 6. Get Followers List:

**Endpoint:** 'GET /api/authors/<uuid:author_id>/followers/'

#### When to use this endpoint:
Retrieve a JSON list of all authors who follow the specified author.

#### How the API endpoint should be used:
Send a GET request to /api/authors/<uuid:author_id>/followers/, replacing <uuid:author_id> with the target author's UUID.


#### Example:
Request: GET http://127.0.0.1:8000/api/authors/27540e3a-fe47-4da1-8d75-c7a9a33cd324/followers/


#### **Response**
 ```json
{
    "type": "followers",
    "followers": [
        {
            "type": "author",
            "id": "http://127.0.0.1:8000/api/authors/a4e29eba-f840-425c-99ef-b1f6ae44ccd8",
            "host": "http://127.0.0.1:8000/api/",
            "displayName": "Bruce Wayne",
            "page": "http://127.0.0.1:8000/authors/a4e29eba-f840-425c-99ef-b1f6ae44ccd8",
            "github": "https://github.com/brucewayne",
            "profileImage": "path/to/bruce_profile.jpg"
        }
        // ... additional follower objects
    ]
}
 ```


### 7. Check a Specific Follower:

**Endpoint:** 'GET /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/'

#### When to use this endpoint:
Check if a specific foreign author (provided as a percent‐encoded URL) is a follower of the given author.

#### How the API endpoint should be used:
Send a GET request to /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/, replacing <path:foreign_author_fqid> with the percent-encoded URL of the foreign author.

#### **Response**
If the foreign author is a follower, returns their author object as JSON.
Otherwise, returns a 404 error.


#### Example:
Request: GET http://127.0.0.1:8000/api/authors/27540e3a-fe47-4da1-8d75-c7a9a33cd324/followers/http%3A%2F%2F127.0.0.1%3A8000%2Fapi%2Fauthors%2Fa4e29eba-f840-425c-99ef-b1f6ae44ccd8


#### **Response** (if follower exists)
 ```json
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/a4e29eba-f840-425c-99ef-b1f6ae44ccd8",
    "host": "http://127.0.0.1:8000/api/",
    "displayName": "Bruce Wayne",
    "page": "http://127.0.0.1:8000/authors/a4e29eba-f840-425c-99ef-b1f6ae44ccd8",
    "github": "https://github.com/brucewayne",
    "profileImage": "path/to/bruce_profile.jpg"
}
 ```
### 8. Add a Follower:

**Endpoint:** 'PUT /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/'

#### When to use this endpoint:
Manually add a foreign author as a follower.

#### How the API endpoint should be used:
Send a PUT request to /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/.

#### **Response**
On success, returns the added follower’s author object as JSON with a 200 status code.

### 9. Remove a Follower:

**Endpoint:** 'DELETE /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/'

#### When to use this endpoint:
Remove a foreign author from the followers list of the specified author.

#### How the API endpoint should be used:
Send a DELETE request to /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/.

#### **Response**
On success, returns a 204 No Content status code.

### 10. Send Follow Request:

**Endpoint:** 'POST /api/authors/<uuid:author_id>/inbox/'

#### When to use this endpoint:
Use this endpoint when an author (actor) wants to send a follow request to another author (object) via their inbox. This is typically used for node-to-node communication.

#### How the API endpoint should be used:
Send a POST request to /api/authors/<uuid:author_id>/inbox/, replacing <uuid:author_id> with the UUID of the target author. The request body should be a JSON object representing the follow request.

#### Example:
Request: POST http://127.0.0.1:8000/api/authors/222/inbox/


#### **Response** (if follower exists)
 ```json
{
    "type": "follow",
    "summary": "Greg wants to follow Lara",
    "actor": {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/111",
        "host": "http://127.0.0.1:8000/api/",
        "displayName": "Greg Johnson",
        "github": "http://github.com/gjohnson",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg",
        "page": "http://127.0.0.1:8000/authors/greg"
    },
    "object": {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/222",
        "host": "http://127.0.0.1:8000/api/",
        "displayName": "Lara Croft",
        "github": "http://github.com/laracroft",
        "profileImage": "https://i.imgur.com/abc123.jpg",
        "page": "http://127.0.0.1:8000/authors/lara"
    }
}

 ```



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


## Comments

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

type (string): always set to comments becuase it is a comments object.
page (string, URL): the URL of the page where the comments are displayed.
id (string, URL): the unique identifier of the post's comments.
page_number (int): the current page number of the comments.
size (int): the number of comments per page.
count (int): the total number of comments.
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

type (string): always set to comments becuase it is a comments object.
page (string, URL): the URL of the page where the comments are displayed.
id (string, URL): the unique identifier of the post's comments.
page_number (int): the current page number of the comments.
size (int): the number of comments per page.
count (int): the total number of comments.
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

type (string): always set to comment becuase it is a comment object.
author (object): the author of the comment in the form of an author object.
comment (string): the text content of the comment.
contentType (string): the type of content in the comment.
published (string): the date and time the comment was published.
id (string, URL): the unique identifier of the comment.
post (string, URL): the URL of the post the comment is on.
page (string, URL): the URL of the page where the comment is displayed.
likes (object): the likes object of the comment listing all likes.


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

type (string): always set to comment becuase it is a comment object.
author (object): the author of the comment in the form of an author object.
comment (string): the text content of the comment.
contentType (string): the type of content in the comment.
published (string): the date and time the comment was published.
id (string, URL): the unique identifier of the comment.
post (string, URL): the URL of the post the comment is on.
page (string, URL): the URL of the page where the comment is displayed.
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

type (string): always set to comment becuase it is a comment object.
author (object): the author of the comment in the form of an author object.
comment (string): the text content of the comment.
contentType (string): the type of content in the comment.
published (string): the date and time the comment was published.
id (string, URL): the unique identifier of the comment.
post (string, URL): the URL of the post the comment is on.
page (string, URL): the URL of the page where the comment is displayed.
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

type (string): always set to comment becuase it is a comment object.
author (object): the author of the comment in the form of an author object.
comment (string): the text content of the comment.
contentType (string): the type of content in the comment.
published (string): the date and time the comment was published.
id (string, URL): the unique identifier of the comment.
post (string, URL): the URL of the post the comment is on.
page (string, URL): the URL of the page where the comment is displayed.
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

type (string): always set to comment becuase it is a comment object.
author (object): the author of the comment in the form of an author object.
comment (string): the text content of the comment.
contentType (string): the type of content in the comment.
published (string): the date and time the comment was published.
id (string, URL): the unique identifier of the comment.
post (string, URL): the URL of the post the comment is on.
page (string, URL): the URL of the page where the comment is displayed.
likes (object): the likes object of the comment listing all likes.




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

type (string): always set to likes becuase it is a likes object.
page (string, URL): the URL of the page where the likes are displayed.
id (string, URL): the unique identifier of the likes.
page_number (int): the current page number of the likes.
size (int): the number of likes per page.
count (int): the total number of likes.
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

type (string): always set to likes becuase it is a likes object.
page (string, URL): the URL of the page where the likes are displayed.
id (string, URL): the unique identifier of the likes.
page_number (int): the current page number of the likes.
size (int): the number of likes per page.
count (int): the total number of likes.
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

type (string): always set to likes becuase it is a likes object.
page (string, URL): the URL of the page where the likes are displayed.
id (string, URL): the unique identifier of the likes.
page_number (int): the current page number of the likes.
size (int): the number of likes per page.
count (int): the total number of likes.
src (list): a list of "like" objects.

#### Interesting Features
Pagination: The likes are paginated, with the page number and size specified in the response.
- To use pagination, the client can use the "page" and "size" query parameters in the request URL.


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

type (string): always set to likes becuase it is a likes object.
page (string, URL): the URL of the page where the likes are displayed.
id (string, URL): the unique identifier of the likes.
page_number (int): the current page number of the likes.
size (int): the number of likes per page.
count (int): the total number of likes.
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

type (string): always set to like becuase it is a like object.
author (object): the author who liked the object in the form of an author object.
published (string): the date and time the like was published.
id (string, URL): the unique identifier of the like.
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

type (string): always set to likes becuase it is a likes object.
page (string, URL): the URL of the page where the likes are displayed.
id (string, URL): the unique identifier of the likes.
page_number (int): the current page number of the likes.
size (int): the number of likes per page.
count (int): the total number of likes.
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

type (string): always set to like becuase it is a like object.
author (object): the author who liked the object in the form of an author object.
published (string): the date and time the like was published.
id (string, URL): the unique identifier of the like.
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
