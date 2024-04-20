# Use the base image from SUSE
FROM registry.suse.com/bci/python:3.11

# Set maintainer and labels for the image

LABEL Author=Wiredquill
LABEL Description=A Python script to download YouTube transcripts and videos
LABEL Version=1.0
LABEL ImageName=youtube-scraper

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
