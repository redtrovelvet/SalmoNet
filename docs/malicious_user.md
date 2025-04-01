# API Security and Rate Limiting Test Documentation

## Overview
These API security and rate-limiting tests are designed to validate the robustness of the system against various types of malicious activities. The tests cover:
- Rate limiting enforcement
- Non-standard and malicious input handling
- Image upload validation
- System overload attempts
- Code injection prevention

These tests **should only be performed by the instructor or TAs** to avoid disrupting other groups.

---

## API Endpoints Tested

### 1. `GET /authors/`
**Purpose:** Retrieves all authors in the system.
- **When to use:** To fetch a list of registered authors.
- **How to use:** Send a `GET` request to `/authors/`.
- **Why this endpoint is tested:** This endpoint is vulnerable to excessive requests that may overload the system.

**Request:**
```json
{
  "method": "GET",
  "url": "/authors/"
}
```

**Response:**
```json
{
  "status": 200,
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "username": "testuser",
      "display_name": "Test User",
      "github": "https://github.com/testuser",
      "profile_image": null,
      "host": "http://127.0.0.1:8000"
    }
  ]
}
```

- **Interesting Notes:** This endpoint enforces rate limiting (maximum 100 requests per minute per user). Exceeding this limit returns:
  ```json
  {
    "status": 429,
    "error": "Rate limit exceeded. Try again later."
  }
  ```

---

### 2. `POST /authors/{author_id}/posts/{post_id}/`
**Purpose:** Allows users to submit content.
- **When to use:** When submitting a new post.
- **How to use:** Send a `POST` request with JSON data.
- **Why this endpoint is tested:** To check for SQL injection, XSS, and unexpected MIME types.

**Request:**
```json
{
  "content": "<script>alert('XSS');</script>",
  "visibility": "'; DROP TABLE users; --",
  "content_type": "application/x-httpd-php"
}
```

**Expected Response:**
```json
{
  "status": 405,
  "error": "Method Not Allowed"
}
```

- **Interesting Notes:** This endpoint rejects malicious input and ensures that script execution or SQL injections are not processed.

---

### 3. `POST /upload/`
**Purpose:** Uploads images to the system.
- **When to use:** When uploading an image.
- **How to use:** Send a `POST` request with an image file.
- **Why this endpoint is tested:** To ensure that only valid image formats (JPG, JPEG, PNG) are accepted and other formats (GIF, BMP, TIFF, etc.) are rejected.

**Valid Request:**
```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
}
```

**Valid Response:**
```json
{
  "status": 200,
  "message": "Image uploaded successfully."
}
```

**Invalid Request:** (GIF file upload attempt)
```json
{
  "image": "data:image/gif;base64,R0lGODlh..."
}
```

**Expected Response:**
```json
{
  "status": 400,
  "error": "Invalid image format. Only JPG, JPEG, and PNG are allowed."
}
```

---

### 4. `GET /authors/` (System Overload Test)
**Purpose:** Simulates a DDoS attack by sending multiple concurrent requests.
- **When to use:** To check the system’s resilience to high request loads.
- **How to use:** Send multiple concurrent requests using threads.
- **Why this endpoint is tested:** To ensure that the system enforces rate limiting and does not crash under excessive load.

**Simulated Attack:**
- 10 parallel threads each sending 50 requests.

**Expected Response:**
```json
{
  "status": 429,
  "error": "Rate limit exceeded. Try again later."
}
```

- **Interesting Notes:** The rate limiter prevents the system from being overwhelmed by excessive requests.

---

### 5. `GET /authors/{author_id}/posts/{post_id}/` (Code Injection Test)
**Purpose:** Tests whether code payloads execute in the system.
- **When to use:** When retrieving a specific post.
- **How to use:** Send a `GET` request to retrieve post details.
- **Why this endpoint is tested:** To ensure that malicious code payloads are treated as plain text and do not execute.

**Malicious Request:**
```json
{
  "content": "print('Hello, World!')"
}
```

**Expected Response:**
```json
{
  "status": 200,
  "content": "print('Hello, World!')"
}
```

- **Interesting Notes:** The system correctly treats the payload as text rather than executing it, preventing remote code execution vulnerabilities.

---

## Summary Table
| Test Case | Endpoint | Expected Behavior |
|-----------|---------|------------------|
| Rate Limiting | `GET /authors/` | 100 requests allowed per minute, 101st returns 429 |
| Non-standard Input | `POST /authors/{author_id}/posts/{post_id}/` | Rejects SQL/XSS injection payloads with 405 |
| Invalid Image Format | `POST /upload/` | Rejects non-JPG/JPEG/PNG uploads with 400 |
| System Overload | `GET /authors/` | Returns 429 when excessive requests detected |
| Code Injection | `GET /authors/{author_id}/posts/{post_id}/` | Returns content as text, preventing execution |

---

## Conclusion
These tests ensure the robustness of the system against malicious activities. The rate limiter prevents excessive requests, input validation blocks SQL and XSS attacks, and strict content-type handling ensures only valid data is processed. Only instructors and TAs should run these tests to maintain system stability.

