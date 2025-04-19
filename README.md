# Redis Docker Environment

This repository provides a Dockerized setup for running a Redis instance, along with a simple Flask web application and an Nginx reverse proxy. It demonstrates how to orchestrate services using Docker Compose.

## Project Structure

The repository is organized as follows:

```
.
├── docker-compose.yml        # Docker Compose configuration for Redis, Flask, and Nginx
├── nginx/
│   └── nginx.conf            # Nginx configuration file
├── web/
│   ├── app.py                # Minimal Flask app connecting to Redis
│   ├── Dockerfile            # Instructions for the container flask
│   └── requirements.txt      # Python dependencies for the Flask app
├── web/
│   └── index.html            # HTML page for testing
└── redis.conf (optional)     # Custom Redis configuration (if needed)
```

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/voirinprof/redis_docker.git
   cd redis_docker
   ```

2. **Build and run the containers:**

   ```bash
   docker-compose up --build
   ```

3. **Access the services:**

   - Web application (via Nginx): [http://localhost](http://localhost)
   - Redis: Accessible inside containers at `redis://redis:6379`

## Usage

This setup allows you to:

- Run a Redis instance in a Docker container.
- Connect a Python Flask app to Redis for storing or retrieving data.
- Route incoming HTTP requests through Nginx to the Flask application.
- Easily manage and scale services using Docker Compose.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).