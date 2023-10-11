FROM python:3.11

# Install youtube-dl dependencies
RUN apt-get update && apt-get install -y youtube-dl ffmpeg

# Install python requirements
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install 

# COPY . .

