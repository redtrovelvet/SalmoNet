# Inbox:

### 1. Send Follow Request:

**Endpoint:** 'POST /api/authors/<uuid:author_id>/inbox/'

#### When to use this endpoint:
Use this endpoint when an author (actor) wants to send a follow request to another author (object) via their inbox. This is typically used for node-to-node communication.

#### How the API endpoint should be used:
Send a POST request to /api/authors/<uuid:author_id>/inbox/, replacing <uuid:author_id> with the UUID of the target author. The request body should be a JSON object representing the follow request.

#### Why the API endpoint should or should not be used
 - Use this endpoint when implementing node to node follow functionality.
 - Do not use this endpoint when the follow request is local; in that case, use the regular follow endpoint.

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