# Inbox:

### 1. Send Follow Request:

**Endpoint:** `POST /api/authors/{AUTHOR_ID}/inbox/`

#### **When to Use**
Use this endpoint when an author (actor) wants to send a follow request to another author (object). This is typically used for node-to-node communication.

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
Use this endpoint when an an author wants to send a like on a post (object) created by author with author uuid = {AUTHOR_ID}. This endpoint is also used to unlike a post through the same method since it checks if the post like already exists in {AUTHOR_ID}'s database and then deletes it. This is typically used for node-to-node communication.

#### **How to Use**
Send a POST request to /api/authors/{AUTHOR_ID}/inbox/, replacing {AUTHOR_ID} with the UUID of the author whose post is being liked. The body should be a JSON object representing the like.

#### **Why to Use**
 - Use this endpoint when implementing node to node functionality for liking a post.

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

- **Status Code**: `401 Unauthorized` (Request from an unauthorized node), `200 OK` (Post like removed since it already exists in our database), `201 Created` (Post like successfuly created), `400 Bad Request` (Missing author/object data in POST body and if object type for like is neither a post or comment), `404 Not Found` (Target post (object)/ author not found in database)


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

### 3. Send a Comment Like:

**Endpoint:** `POST /api/authors/{AUTHOR_ID}/inbox/`

#### **When to Use**
Use this endpoint when an an author wants to send a like on a comment (object) created by author with author uuid = {AUTHOR_ID}. This endpoint is also used to unlike a comment through the same method since it checks if the comment like already exists in {AUTHOR_ID}'s database and then deletes it. This is typically used for node-to-node communication.

#### **How to Use**
Send a POST request to /api/authors/{AUTHOR_ID}/inbox/, replacing {AUTHOR_ID} with the UUID of the author whose comment is being liked. The body should be a JSON object representing the like.

#### **Why to Use**
 - Use this endpoint when implementing node to node functionality for liking a comment.

 #### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the target author whose comment is being liked (e.g., `111`).

- **Body**:

```json
{
    "type":"like",
    "author":{
        "type":"author",
        "id":"http://nodebbbb/api/authors/222",
        "host":"http://nodebbbb/api/",
        "displayName":"Lara Croft",
        "page":"http://nodebbbb/authors/222",
        "github": "http://github.com/laracroft",
        "profileImage": "http://nodebbbb/api/authors/222/posts/217/image"
    },
    "published":"2015-03-09T13:07:04+00:00",
    "id": "http://nodeaaaa/api/authors/222/liked/255",
    "object": "http://nodeaaaa/api/authors/111/commented/130"
}
```

- **Status Code**: `401 Unauthorized` (Request from an unauthorized node), `200 OK` (Comment like removed since it already exists in our database), `201 Created` (Comment like successfuly created), `400 Bad Request` (Missing author/object data in POST body and if object type for like is neither a post or comment), `404 Not Found` (Target comment (object)/ author not found in database)


#### Example:
Request: POST http://127.0.0.1:8000/api/authors/111/inbox/


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

- If comment (object) is missing in the POST body:
```json
  {
    "detail": "Missing object field."
  }
```

- If comment (object) is not found in the database:
```json
  {
    "detail": "Target comment not found."
  }
```

- If author (sender of the request) is not found in the database:
```json
  {
    "detail": "Sender author not found in database."
  }
```

- If comment like doesn't already exist in the database and is successfully created:
```json
  {
    "detail": "Comment like stored."
  }
```

- If comment like already exists in the database and is successfully removed (unliked):
```json
  {
    "detail": "Comment like removed."
  }
```

- If object is neither a post or a comment:
```json
  {
    "detail": "Unrecognized object type for like."
  }
```

---

### 4. Send a Comment:

**Endpoint:** `POST /api/authors/{AUTHOR_ID}/inbox/`

#### **When to Use**
Use this endpoint when an an author wants to send a comment to a post created by author with author uuid = {AUTHOR_ID}. This is typically used for node-to-node communication.

#### **How to Use**
Send a POST request to /api/authors/{AUTHOR_ID}/inbox/, replacing {AUTHOR_ID} with the UUID of the author whose post the comment is being made on. The body should be a JSON object representing the comment.

#### **Why to Use**
 - Use this endpoint when implementing node to node functionality for sending a comment to a post.

 #### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the target author whose post is being commented on (e.g., `222`).

- **Body**:

```json
{
    "type":"comment",
    "author":{
        "type":"author",
        "id":"http://nodeaaaa/api/authors/111",
        "page":"http://nodeaaaa/authors/greg",
        "host":"http://nodeaaaa/api/",
        "displayName":"Greg Johnson",
        "github": "http://github.com/gjohnson",
        "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
    },
    "comment":"Sick Olde English",
    "contentType":"text/markdown",
    "published":"2015-03-09T13:07:04+00:00",
    "id": "http://nodeaaaa/api/authors/111/commented/130",
    "post": "http://nodebbbb/api/authors/222/posts/249",
    "likes":{
        "type":"likes",
        "page":"http://nodeaaaa/authors/222/posts/249",
        "id":"http://nodeaaaa/api/authors/111/commented/130/likes",
        "page_number":1,
        "size":50,
        "count": 9001,
        "src":[
            {
                "type":"like",
                "author":{
                    "type":"author",
                    "id":"http://nodebbbb/api/authors/222",
                    "host":"http://nodebbbb/api/",
                    "displayName":"Lara Croft",
                    "page":"http://nodebbbb/authors/222",
                    "github": "http://github.com/laracroft",
                    "profileImage": "http://nodebbbb/api/authors/222/posts/217/image"
                },
                "published":"2015-03-09T13:07:04+00:00",
                "id": "http://nodeaaaa/api/authors/222/liked/255",
                "object": "http://nodeaaaa/api/authors/111/commented/130"
            }
        ]
    },
}
```

- **Status Code**: `401 Unauthorized` (Request from an unauthorized node), `201 Created` (Comment & likes successfully created), `400 Bad Request` (Missing author/post/comment text/comment fqid data in POST body), `404 Not Found` (Target post/ sender not found in database)


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

- If comment text/ comment fqid is missing in the POST body:
```json
  {
    "detail": "Missing comment text or comment fqid."
  }
```

- If post information is missing in the POST body:
```json
  {
    "detail": "Missing post field."
  }
```

- If target post is not found in the database:
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

- If comment and its associated comment likes are not in the database and are successfully created:
```json
  {
    "detail": "Comment and embedded likes stored."
  }
```

---

### 5. Send a Post:

**Endpoint:** `POST /api/authors/{AUTHOR_ID}/inbox/`

#### **When to Use**
Use this endpoint when an an author wants to send a post to an author with author uuid = {AUTHOR_ID}. This is typically used for node-to-node communication for sending posts to remote followers/friends.

#### **How to Use**
Send a POST request to /api/authors/{AUTHOR_ID}/inbox/, replacing {AUTHOR_ID} with the UUID of the author to who the post is being sent to. The body should be a JSON object representing the post.

#### **Why to Use**
 - Use this endpoint when implementing node to node functionality for sending a post to remote followes/friends.
 - Also used to send a post to remote followers/friends after the post has been edited or deleted.

 #### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the target author who the post is being sent to (e.g., `222`).

- **Body**:

```json
{
    "type":"post",
    "title":"plain text post",
    "id":"http://nodebbbb/api/authors/222/posts/249",
    "page": "http://nodebbbb/authors/222/posts/293",
    "description":"plain text post",

    "contentType":"text/plain",
    "content":"Test Post"
    "author":{
        "type":"author",
        "id":"http://nodebbbb/api/authors/222",
        "host":"http://nodebbbb/api/",
        "displayName":"Lara Croft",
        "page":"http://nodebbbb/authors/222",
        "github": "http://github.com/laracroft",
        "profileImage": "http://nodebbbb/api/authors/222/posts/217/image"
    },
    "comments":{
        "type":"comments",
        "page":"http://nodebbbb/authors/222/posts/249",
        "id":"http://nodebbbb/api/authors/222/posts/249/comments"
        "page_number":1,
        "size":5,
        "count": 1023,
        "src":[
            {
                "type":"comment",
                "author":{
                    "type":"author",
                    "id":"http://nodeaaaa/api/authors/111",
                    "page":"http://nodeaaaa/authors/greg",
                    "host":"http://nodeaaaa/api/",
                    "displayName":"Greg Johnson",
                    "github": "http://github.com/gjohnson",
                    "profileImage": "https://i.imgur.com/k7XVwpB.jpeg"
                },
                "comment":"Sick Olde English",
                "contentType":"text/markdown",
                "published":"2015-03-09T13:07:04+00:00",
                "id":"http://nodeaaaa/api/authors/111/commented/130",
                "post": "http://nodebbbb/api/authors/222/posts/249",
                "page": "http://nodebbbb/authors/222/posts/249"
                "likes": {
                    "type": "likes",
                    "id": "http://nodeaaaa/api/authors/111/commented/130/likes",
                    "page": "http://nodeaaaa/authors/greg/comments/130/likes",
                    "page_number": 1,
                    "size": 50,
                    "count": 0,
                    "src": [],
                },
            }
        ]
    },
    "likes":{
        "type":"likes",
        "page":"http://nodeaaaa/authors/222/posts/249",
        "id":"http://nodeaaaa/api/authors/222/posts/249/likes",
        "page_number":1,
        "size":50,
        "count": 9001,
        "src":[
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
                "object": "http://nodebbbb/authors/222/posts/249"
            }
        ]
    },
    "published":"2015-03-09T13:07:04+00:00",
    "visibility":"PUBLIC"
}
```

- **Status Code**: `401 Unauthorized` (Request from an unauthorized node), `201 Created` (Post and associated objects created/updated/deleted), `400 Bad Request` (Missing author data/post id in POST body and unsupported request/type for inbox)


#### Example:
Request: POST http://127.0.0.1:8000/api/authors/111/inbox/


#### **Response** 

- If an unauthorized node sends the request:
```json
  {
    "detail": "Unauthorized"
  }
```

- If author information/post id is missing in the POST body:
```json
  {
    "detail": "Missing post ID or author data."
  }
```

- If POST body does not contain an object of type Like, Comment, Post, Follow Request:
```json
  {
    "detail": "Unsupported type for inbox."
  }
```

If request is neither remote or local:
```json
  {
    "detail": "Unsupported request."
  }
```

- If the Post is created along with its associated objects - Comments, Post Likes, Comment Likes:
```json
  {
    "detail": "Post and associated objects processed."
  }
```

- If the Post and its associated objects are updated:
```json
  {
    "detail": "Post and associated objects processed."
  }
```

- If the Post and its associated objects are deleted (soft delete by changing visibility of post and deleting likes, comments):
```json
  {
    "detail": "Post and associated objects processed."
  }
```

---
