# Author

### 1.Get all Authors

**Endpoint:** 'GET /api/authors/'

#### When the API endpoint should be used

Use this endpoint when you want to retrieve a list of all authors in the local node.

#### How the API endpoint should be used

- Send a GET request to '/api/authors/'.
- You may include optional query parameters:
    page (integer): Which page of results to fetch (default: 1).
    size (integer): How many authors per page (default: 5).

#### Why the API endpoint should or should not be used

- use it to display all available authors
- Maybe don't use if database is really large because API might time-out, use pagnation instead.

#### 1st Example

Request: GET <http://127.0.0.1:8000/api/authors/>
Response: A JSON array of author objects is returned
``` json
{
  "type": "authors",
  "authors": [
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c",
        "host": "http://127.0.0.1:8000/api/",
        "displayName": "Example",
        "github": "https://www.google.com/",
        "profileImage": "http://127.0.0.1:8000/media/images/pexels-pixabay-158063_8FOC3DL.jpg",
        "page": "http://127.0.0.1:8000/authors/3ed7f38d-86f6-45cc-8f29-e498163f1d4c"
    },
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/22460264-0965-4950-84b9-2a86a4205c0a",
        "host": "http://127.0.0.1:8000/api/",
        "displayName": "Another Example",
        "github": "http://www.github.com/",
        "profileImage": "http://127.0.0.1:8000/media/images/pexels-pixabay-158063.jpg",
        "page": "http://127.0.0.1:8000/authors/22460264-0965-4950-84b9-2a86a4205c0a"
    }
  ]
}
```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/?page=2&size=2>
Response: A JSON array of author objects is returned
``` json
{
  "type": "authors",
  "authors": [
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/72a7003a-b440-457d-99ac-17469b9f3076",
        "host": "http://127.0.0.1:8000/api/",
        "displayName": "Example Three",
        "github": "http://www.github.com/example_three",
        "profileImage": "",
        "page": "http://127.0.0.1:8000/authors/72a7003a-b440-457d-99ac-17469b9f3076"
    },
    {
        "type": "author",
        "id": "http://127.0.0.1:8000/api/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b",
        "host": "http://127.0.0.1:8000/api/",
        "displayName": "Greg Johnson",
        "github": "http://github.com/gjohnson",
        "profileImage": "http://127.0.0.1:8000/media/images/pexels-some-other-pic.jpg",
        "page": "http://127.0.0.1:8000/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b"
    }
  ]
}
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
host (string, URL): url of the node where the author is.
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
page (string, URL): The HTML page to view this author’s public profile.<br />

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

Request: GET <http://127.0.0.1:8000/api/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b/>
Response: A JSON object representing the author's details:
``` json
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b",
    "host": "http://127.0.0.1:8000/api/",
    "displayName": "Greg Johnson",
    "github": "http://github.com/gjohnson",
    "profileImage": "http://127.0.0.1:8000/media/images/pexels-some-other-pic.jpg",
    "page": "http://127.0.0.1:8000/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b"
}
```

#### 2nd Example

Request: GET <http://127.0.0.1:8000/api/authors/72a7003a-b440-457d-99ac-17469b9f3076/>
Response: A JSON object representing the author's details:
``` json
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/72a7003a-b440-457d-99ac-17469b9f3076",
    "host": "http://127.0.0.1:8000/api/",
    "displayName": "Example Three",
    "github": "http://www.github.com/example_three",
    "profileImage": "",
    "page": "http://127.0.0.1:8000/authors/72a7003a-b440-457d-99ac-17469b9f3076"
}
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
host (string, URL): url of the node where the author is.
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
page (string, URL): The HTML page to view this author’s public profile.<br />


### 3.Update a Specific Author

**Endpoint:** 'PUT /api/authors/{author_id}/'

#### When the API endpoint should be used

Use this endpoint when you want to update an author's profile.

#### How the API endpoint should be used

Send a PUT request to '/api/authors/{author_id}/'.
Replace {author_id} with the actual UUID of the author.

#### Why the API endpoint should or should not be used

- use it to change an exisitng author's details.
- Don't use if you don't know the author id or author does not exist.

#### 1st Example

Request: PUT <http://127.0.0.1:8000/api/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b/>
``` json
{
    "display_name": "Updated User"
}
```
Response:  A JSON object representing the updated author's details:
``` json
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b",
    "host": "http://127.0.0.1:8000/api/",
    "displayName": "Updated User",
    "github": "http://github.com/gjohnson",
    "profileImage": "http://127.0.0.1:8000/media/images/pexels-some-other-pic.jpg",
    "page": "http://127.0.0.1:8000/authors/ef9619aa-23d5-4329-bbef-c59e263f5a8b"
}
```

#### 2nd Example

Request: PUT <http://127.0.0.1:8000/api/authors/72a7003a-b440-457d-99ac-17469b9f3076/>
``` json
{
    "github": "<http://www.github.com/updated_user/>",
}
```
Response:  A JSON object representing the updated author's details:
``` json
{
    "type": "author",
    "id": "http://127.0.0.1:8000/api/authors/72a7003a-b440-457d-99ac-17469b9f3076",
    "host": "http://127.0.0.1:8000/api/",
    "displayName": "Example Three",
    "github": "http://www.github.com/updated_user",
    "profileImage": "",
    "page": "http://127.0.0.1:8000/authors/72a7003a-b440-457d-99ac-17469b9f3076"
}
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
host (string, URL): url of the node where the author is.
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
page (string, URL): The HTML page to view this author’s public profile.<br />

### 3.Get a Specific Author through Fqid

**Endpoint:** 'GET /api/authors/{author_fqid}/'

#### When the API endpoint should be used

Use this endpoint when you need to retrieve details for a specific author by providing their fqid.
This endpoint works for both local and remote authors; the FQID should be provided in a percent‑encoded format if it contains special characters.

#### How the API endpoint should be used

Send a GET request to '/api/authors/{author_fqid}/'.
Replace {author_id} with the actual FQID of the author.

#### Why the API endpoint should or should not be used

- Use when you only have an author’s FQID and need to obtain their full details. Typically for authors of remote nodes
- Don't use if have the local UUID of an author, then use GET '/api/authors/{author_id}/'

#### 1st Example

Request: GET <http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/api/authors/http://%5B2605:fd00:4:1001:f816:3eff:fe15:dafe%5D/api/authors/bf530b3d-fa9b-4bf6-a42a-e9a44a331fa2/>

Response:  A JSON object representing the updated author's details:
``` json
{
    "type": "author",
    "id": "http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/api/authors/bf530b3d-fa9b-4bf6-a42a-e9a44a331fa2",
    "host": "http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/api/",
    "displayName": "git",
    "github": "http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/authors/bf530b3d-fa9b-4bf6-a42a-e9a44a331fa2/edit/None",
    "profileImage": "https://static.vecteezy.com/system/resources/thumbnails/028/126/843/small/close-up-of-blue-flowers-with-drops-of-water-on-dark-background-beautiful-macro-colorful-flowers-generative-ai-photo.jpg",
    "page": "http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/authors/bf530b3d-fa9b-4bf6-a42a-e9a44a331fa2"
}
```

#### 2nd Example

Request: GET <http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/api/authors/http://%5B2605:fd00:4:1001:f816:3eff:fe15:dafe%5D/api/authors/873c326a-aea5-47dc-84f6-d91c0e0dfe06/>

Response:  A JSON object representing the updated author's details:
``` json
{
    "type": "author",
    "id": "http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/api/authors/873c326a-aea5-47dc-84f6-d91c0e0dfe06",
    "host": "http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/api/",
    "displayName": "cat",
    "github": null,
    "profileImage": null,
    "page": "http://[2605:fd00:4:1001:f816:3eff:fe15:dafe]/authors/873c326a-aea5-47dc-84f6-d91c0e0dfe06"
}
```

#### Explantion of JSON Field

type (string): always set to author because this object represents an author.<br />
id (string, URL): the unique identifier of the author.<br />
host (string, URL): url of the node where the author is.
display_name (string): the display name of the author.<br />
github (string, URL): author's github link.<br />
profile_mage (string, URL): a link to the author's profile image.<br />
page (string, URL): The HTML page to view this author’s public profile.<br />
