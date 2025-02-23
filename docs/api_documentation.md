# API documentation requirements for SocialDistribution

## Identity:

### 1.Get all Authors:

**Endpoint:** 'GET /api/authors/'

#### When the API endpoint should be used:
Use this endpoint when you want to retrieve a list of all authors in the local node.

#### How the API endpoint should be used:
Send a GET request to '/api/authors/'.

#### Why the API endpoint should or should not be used:
- use it to display all available authors
- Maybe don't use if database is really large because API might time-out, use pagnation instead, but not implemented yet.

#### 1st Example:
Request: GET http://127.0.0.1:8000/api/authors/
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

#### 2nd Example:
Request: GET http://127.0.0.1:8000/api/authors/
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

#### Explantion of JSON Field:
type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
host (string, URL): url of the node where the author is.


### 2.Get Specific Author:

**Endpoint:** 'GET /api/authors/{author_id}/'

#### When the API endpoint should be used:
Use this endpoint when you want to retrieve details about a specific author using their unique identifier.

#### How the API endpoint should be used:
Send a GET request to '/api/authors/{author_id}'.
Replace {author_id} with the actual UUID of the author. 

#### Why the API endpoint should or should not be used:
- use it to display author details for a specific author.
- Don't use if you don't know the author id.

#### 1st Example:
Request: GET http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c/
Response: A JSON object representing the author's details:
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c",
    "username": "example",
    "display_name": "Example",
    "github": "https://www.google.com/",
    "profile_image": "images/pexels-pixabay-158063_8FOC3DL.jpg",
    "host": "http://127.0.0.1:8000"
}

#### 2nd Example:
Request: GET http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a/
Response: A JSON object representing the author's details:
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a",
    "username": "anotherexample",
    "display_name": "Another Example",
    "github": "http://www.github.com",
    "profile_image": "images/pexels-pixabay-158063.jpg",
    "host": "http://127.0.0.1:8000"
}

#### Explantion of JSON Field:
type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
host (string, URL): url of the node where the author is.


### 3.Create Author:

**Endpoint:** 'POST /api/authors/create/'

#### When the API endpoint should be used:
Use this endpoint when you want to create a new author.

#### How the API endpoint should be used:
Send a POST request to '/api/authors/create' with the required fields. 

#### Why the API endpoint should or should not be used:
- use it to create a new author.
- Don't use if you want to update existing author.

#### 1st Example:
Request: POST http://127.0.0.1:8000/api/authors/create/
{
    "username": "new_user",
    "host": "http://127.0.0.1:8000"
}
Response: A JSON object representing the created author's details:
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0",
    "username": "new_user",
    "display_name": "Display Name",
    "github": null,
    "profile_image": "",
    "host": "http://127.0.0.1:8000"
}

#### 2nd Example: 
Request: POST http://127.0.0.1:8000/api/authors/create/
{
    "username": "another_new_user",
    "host": "http://127.0.0.1:8000"
}
Response: A JSON object representing the created author's details:
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7",
    "username": "another_new_user",
    "display_name": "Display Name",
    "github": null,
    "profile_image": "",
    "host": "http://127.0.0.1:8000"
}

#### Explantion of JSON Field:
type (string): always set to author because this object represents an author.
id (string, URL): the unique identifier of the author.
username (string): the author's unique username.
display_name (string): the display name of the author.
github (string, URL): author's github link.
profile_mage (string, URL): a link to the author's profile image.
host (string, URL): url of the node where the author is.

### 4.Update a Specific Author:

**Endpoint:** 'POST /api/authors/{author_id}/update/'

#### When the API endpoint should be used:
Use this endpoint when you want to update an author's profile.

#### How the API endpoint should be used:
Send a POST request to '/api/authors/{author_id}/update/'.
Replace {author_id} with the actual UUID of the author. 

#### Why the API endpoint should or should not be used:
- use it to change an exisitng author's details.
- Don't use if you don't know the author id or author does not exist.

#### 1st Example:
Request: POST http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0/update/
{
    "display_name": "Updated User"
}
Response:  A JSON object representing the updated author's details:
{
    "id": "http://127.0.0.1:8000/api/authors/4f3f038c-f87e-4f54-bc53-f4a213be97d0",
    "username": "new_user",
    "display_name": "Updated User",
    "github": null,
    "profile_image": "",
    "host": "http://127.0.0.1:8000"
}

#### 2nd Example:
Request: POST http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7/update/
{
    "github": "http://www.github.com/updated_user/",
}
Response:  A JSON object representing the updated author's details:
{
    "id": "http://127.0.0.1:8000/api/authors/c3f33e5b-c9af-49a1-a2eb-995c00e209d7",
    "username": "another_new_user",
    "display_name": "Display Name",
    "github": "http://www.github.com/updated_user/",
    "profile_image": "",
    "host": "http://127.0.0.1:8000"
}

#### Explantion of JSON Field:
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
Use this endpoint when an authenticated author (the receiver) wants to approve a follow request they received.

#### How the API endpoint should be used:
Send a POST request to /follow_requests/<int:request_id>/approve/, replacing <int:request_id> with the numeric identifier of the follow request.

### Response:
On success, the follow request's status is updated to "ACCEPTED", the sender is added as a follower, and the endpoint redirects (HTTP 302) to a confirmation page or the all authors page.

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

### 4. View Followers, Following, and Friends:

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



