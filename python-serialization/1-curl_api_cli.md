# 1. Consuming Data from an API using cURL

## 1. Verifying cURL Installation

```bash
curl --version
```

* **Expected**: Version information and supported protocols (e.g., HTTP, HTTPS, FTP).

## 2. Basic HTTP GET Request

Fetch the content of a simple webpage:

```bash
curl http://example.com
```

* **Output**: Raw HTML of the Example.com homepage.

## 3. Retrieving JSON Data from JSONPlaceholder

Use the public API at [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com):

```bash
curl https://jsonplaceholder.typicode.com/posts
```

* **Output**: A JSON array of posts, each with fields `userId`, `id`, `title`, and `body`.

## 4. Inspecting Response Headers Only

Retrieve only the headers without the body:

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

* **Output**: Status line (e.g., `HTTP/1.1 200 OK`) and response headers like `Content-Type` and `Cache-Control`.

## 5. Making a POST Request

Simulate creating a new post:

```bash
curl -X POST \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "title=foo&body=bar&userId=1" \
     https://jsonplaceholder.typicode.com/posts
```

* **Output**: JSON of the created resource, typically including `"id": 101` (simulation).

## 6. Tips & Best Practices

* **`-I`**: Fetch headers only. Useful for checking status codes and server settings.
* **`-X`**: Specify HTTP method (e.g., `POST`, `PUT`, `DELETE`).
* **`-d`**: Send form data (`application/x-www-form-urlencoded`) in request body.
* **`-H`**: Set or override headers (e.g., `Content-Type: application/json`).
* **Piping to `jq`**: For formatted JSON output:

  ```bash
  curl https://jsonplaceholder.typicode.com/posts | jq .
  ```

## 7. Expected Behavior Summary

| Command                                           | Description                 | Expected Result                            |
| ------------------------------------------------- | --------------------------- | ------------------------------------------ |
| `curl --version`                                  | Verify installation         | cURL version and supported protocols       |
| `curl http://example.com`                         | GET plain webpage           | HTML markup                                |
| `curl https://jsonplaceholder.typicode.com/posts` | GET sample API data         | JSON array of post objects                 |
| `curl -I https://.../posts`                       | HEAD request                | HTTP status line + headers                 |
| `curl -X POST -d ... https://.../posts`           | Create new post (simulated) | JSON with new `id` field (e.g., `id: 101`) |
