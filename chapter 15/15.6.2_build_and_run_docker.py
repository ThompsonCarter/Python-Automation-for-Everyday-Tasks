# Docker build and run commands
docker build -t report-bot .
docker run -d --name bot -e API_KEY=$API_KEY report-bot
