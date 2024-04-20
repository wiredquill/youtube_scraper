# Use the base image from SUSE
FROM registry.suse.com/bci/python:3.11

# Set the maintainer
MAINTAINER Your Name <your_email@example.com>

# Set labels for the image
LABEL Author=Your Name
LABEL Description=A Python script to download YouTube transcripts and videos
LABEL Version=1.0
LABEL Image=youtube-scraper

# Set the working directory in the container
WORKDIR /app

# Install Python requirements
RUN pip install requests beautifulsoup4 pytube

# Copy the script into the container
COPY . /app/

# Make port 80 available to the world outside this container
EXPOSE 80
# Run the command to start the application when the container starts
CMD ["python", "youtube-scrape.py"]
