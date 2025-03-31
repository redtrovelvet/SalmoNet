# Inbox:

### 1. Send Follow Request:

**Endpoint:** `POST /api/authors/{AUTHOR_ID}/inbox/`

#### **When to Use**
Use this endpoint when an author (actor) wants to send a follow request to another author (object) via their inbox. This is typically used for node-to-node communication.

#### **How to Use**
Send a POST request to /api/authors/<uuid:author_id>/inbox/, replacing <uuid:author_id> with the UUID of the target author. The request body should be a JSON object representing the follow request.

#### **Why to Use**
 - Use this endpoint when implementing node to node follow functionality.

 #### **Request**

- **URL Parameters**:
  - `AUTHOR_ID`: UUID of the target author (e.g., `222`).

- **Body**:

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