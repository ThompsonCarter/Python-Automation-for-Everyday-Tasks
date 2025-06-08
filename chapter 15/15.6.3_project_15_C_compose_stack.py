# docker-compose.yaml for project
version: "3"
services:
  bot:
    build: .
    env_file: .env
    volumes: ["./logs:/app/logs"]
    restart: unless-stopped
# Run: docker compose up -d
