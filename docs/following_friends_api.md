# Following/Friends:

### 1.Send Follow Request:

**Endpoint:** 'POST /authors/<uuid:author_id>/follow/'

#### When to use this endpoint:
Use this endpoint when an authenticated author wants to follow another author. This sends a follow request from the current user to the target author.

#### How the API endpoint should be used:
Send a POST request to /authors/<uuid:author_id>/follow/, replacing <uuid:author_id> with the UUID of the target author.

#### Why the API endpoint should or should not be used
- Use this endpoint when you want to send a follow request.
- Do not use this endpoint when you are building node-to-node communication. In that case, use the inbox endpoint.

#### Response:
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

#### Why the API endpoint should or should not be used
- Use this endpoint to approve follow requests.
- Do not use this endpoint if you are not the recipient of the follow request.

#### Response:
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

#### Why the API endpoint should or should not be used
 - Use this endpoint to decline follow requests.
 - Do not use this endpoint if you are not the recipient of the follow request.

#### Response:
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

#### Why the API endpoint should or should not be used
 - Use this endpoint to remove an author from your following list.
 - Do not use this endpoint if you are not currently following the target author.

#### Response:
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

#### Why the API endpoint should or should not be used
 - Use these endpoints when you need a to see details of all followers.
 - Do not use these endpoints if you need raw JSON data.

#### Example:
Request: GET http://127.0.0.1:8000/profile/followers/

Response: An HTML page is returned listing all followers of the current user.

### 6. Get Followers List:

**Endpoint:** 'GET /api/authors/<uuid:author_id>/followers/'

#### When to use this endpoint:
Retrieve a JSON list of all authors who follow the specified author.

#### How the API endpoint should be used:
Send a GET request to /api/authors/<uuid:author_id>/followers/, replacing <uuid:author_id> with the target author's UUID.

#### Why the API endpoint should or should not be used
 - Use this endpoint you want to see who follows a specific author.
 - Do not use this endpoint if you only need to display the list in a web browser.

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

#### Why the API endpoint should or should not be used
 - Use this endpoint to check if a particular foreign author is in the followers list.
 - Do not use this endpoint if you want a complete list of all followers; use the GET followers list endpoint instead.

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

#### Why the API endpoint should or should not be used
 - Use this endpoint when you need to add a follower .
 - Do not use this endpoint if you are using the web interface for follow requests.

#### **Response**
On success, returns the added follower’s author object as JSON with a 200 status code.

### 9. Remove a Follower:

**Endpoint:** 'DELETE /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/'

#### When to use this endpoint:
Remove a foreign author from the followers list of the specified author.

#### How the API endpoint should be used:
Send a DELETE request to /api/authors/<uuid:author_id>/followers/<path:foreign_author_fqid>/.

#### Why the API endpoint should or should not be used
 - Use this endpoint to  remove a follower.
 - Do not use this endpoint for bulk operations; it is designed for single removal.

#### **Response**
On success, returns a 204 No Content status code.

### 10. Send Follow Request:

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