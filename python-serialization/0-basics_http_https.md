# Basics of HTTP/HTTPS

## 1. Summary of Differences between HTTP and HTTPS

* **Encryption & Security**: HTTP transmits data in plaintext, while HTTPS uses SSL/TLS to encrypt content, protecting it from eavesdropping and tampering.
* **Default Port**: HTTP uses port 80, while HTTPS uses port 443.
* **Trust & Credibility**: Browsers display a padlock icon for HTTPS sites, indicating a secure connection.
* **Performance**: HTTPS can introduce slight latency due to the encryption handshake, but HTTP/2 (which requires HTTPS) offers performance improvements.

## 2. HTTP Request and Response Structure

### HTTP Request Example

```http
GET /path/to/resource.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 ...
Accept: text/html

# Request body (for POST or PUT)
```

### HTTP Response Example

```http
HTTP/1.1 200 OK
Date: Sat, 14 Jun 2025 18:00:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 137

<html>...page content...</html>
```

## 3. Common HTTP Methods

| Method | Description                                  | Use Case                             |
| ------ | -------------------------------------------- | ------------------------------------ |
| GET    | Retrieve data without modifying server state | Loading a web page or API data       |
| POST   | Submit data to create a new resource         | Submitting a registration form       |
| PUT    | Replace an existing resource entirely        | Updating a user record completely    |
| DELETE | Remove a resource                            | Deleting a post or comment           |
| PATCH  | Partially update an existing resource        | Modifying a single field in a record |

## 4. Common HTTP Status Codes

| Status Code               | Description                                 | Example Scenario                               |
| ------------------------- | ------------------------------------------- | ---------------------------------------------- |
| 200 OK                    | The request was successful                  | Successfully loading a web page                |
| 301 Moved Permanently     | Resource moved permanently                  | Redirecting `example.com` to `www.example.com` |
| 400 Bad Request           | The server could not understand the request | Sending malformed data in a form               |
| 404 Not Found             | The requested resource was not found        | Accessing a deleted page link                  |
| 500 Internal Server Error | A generic server error                      | Database failure during request processing     |
