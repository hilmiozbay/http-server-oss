# HTTP Web Server

A simple HTTP server implementation from scratch using Python's socket programming capabilities.

## Features

- Handles GET requests
- Serves static files (HTML, CSS, JS) from `/static` directory
- Provides JSON responses through `/api/hello` endpoint
- Proper MIME type handling
- Multi-threaded connection handling
- Basic error handling (404, 500)
- Docker containerization support

## Project Structure

```
/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── NOTICE.md
├── CODE_OF_CONDUCT.md
├── Dockerfile
├── server.py
├── routes/
├── static/
└── .dockerignore
```

## Requirements

- Python 3.8+
- Docker (for containerization)

## Running the Server

### Local Development

1. Clone the repository
2. Run the server:
   ```bash
   python server.py
   ```
3. Access the server at `http://localhost:8080`

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t http-server .
   ```
2. Run the container:
   ```bash
   docker run -p 8080:8080 http-server
   ```

## API Endpoints

- `GET /api/hello` - Returns a JSON response
- `GET /static/*` - Serves static files

## License

MIT License - See LICENSE file for details 