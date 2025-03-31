# Inbox:

### 1. Send Follow Request:

**Endpoint:** `POST /api/authors/{AUTHOR_ID}/inbox/`

#### **When to Use**
Use this endpoint when an author (actor) wants to send a follow request to another author (object) via their inbox. This is typically used for node-to-node communication.

#### **How to Use**
Send a POST request to /api/authors/{AUTHOR_ID}/inbox/, replacing {AUTHOR_ID} with the UUID of the target author. The body should be a JSON object representing the follow request.

#### **Why to Use**
 - Use this endpoint when implementing node to node follow functionality.

 #### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the target author (e.g., `222`).

- **Body**:

    - A follow request object

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

- **Status Code**: `200 OK` (Already Exists), `201 Created` (Success), `400 Bad Request` (Missing actor data in POST body), `404 Not Found` (Target author (object) not found in database)


#### Example:
Request: POST http://127.0.0.1:8000/api/authors/222/inbox/


#### **Response** 

- If actor information is missing in POST body:
```json
  {
    "detail": "Missing actor data."
  }
```

- If target author (object) does not exist in the local database:
```json
  {
    "detail": "Sender author not found in database."
  }
```

- If follow request already exists in our database and can be viewed by the target author:
```json
  {
    "detail": "detail": "Follow request already exists."
  }
```

  - If follow request is successfully created in our database and can be viewed by the target author:
```json
  {
    "detail": "Follow request created."
  }
```

---

### 2. Send a Post Like:

**Endpoint:** `POST /api/authors/{AUTHOR_ID}/inbox/`

#### **When to Use**
Use this endpoint when an an author wants to send a like on a post (object) created by author with author uuid = {AUTHOR_ID} via their inbox. This endpoint is also used to unlike a post through the same method since it checks if the post like already exists in our database and then deletes it. This is typically used for node-to-node communication.

#### **How to Use**
Send a POST request to /api/authors/{AUTHOR_ID}/inbox/, replacing {AUTHOR_ID} with the UUID of the author whose post is being liked. The body should be a JSON object representing the like.

#### **Why to Use**
 - Use this endpoint when implementing node to node like functionality for a post.

 #### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the target author whose post is being liked (e.g., `222`).

- **Body**:

```json
{
    "type":"like",
    "author":{
        "type":"author",
        "id":"http://nodeaaaa/api/authors/111",
        "page":"http://nodeaaaa/authors/greg",
        "host":"http://nodeaaaa/api/",
        "displayName":"Greg Johnson",
        "github": "http://github.com/gjohnson",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "id":"http://nodeaaaa/api/authors/111/liked/166",
    "object": "http://nodebbbb/api/authors/222/posts/249"
}
```

- **Status Code**: `401 Unauthorized` (Request from an unauthorrized node), `200 OK` (Post like removed since it already exists in our database), `201 Created` (Post like successfuly created), `400 Bad Request` (Missing author/object data in POST body and if object type for like is neither a post or comment), `404 Not Found` (Target post (object)/ author not found in database)


#### Example:
Request: POST http://127.0.0.1:8000/api/authors/222/inbox/


#### **Response** 

- If an unauthorized node sends the request:
```json
  {
    "detail": "Unauthorized"
  }
```

- If author information is missing in the POST body:
```json
  {
    "detail": "Missing author data."
  }
```

- If post (object) is missing in the POST body:
```json
  {
    "detail": "Missing object field."
  }
```

- If post (object) is not found in the database:
```json
  {
    "detail": "Target post not found."
  }
```

- If author (sender of the request) is not found in the database:
```json
  {
    "detail": "Sender author not found in database."
  }
```

- If post like doesn't already exist in the database and is successfully created:
```json
  {
    "detail": "Post like stored."
  }
```

- If post like already exists in the database and is successfully removed (unliked):
```json
  {
    "detail": "Post like removed."
  }
```

- If object is neither a post or a comment:
```json
  {
    "detail": "Unrecognized object type for like."
  }
```

---