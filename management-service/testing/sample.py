# app.py

import os
from dotenv import load_dotenv
from mongoengine import connect, ObjectIdField, DateTimeField  # Import ObjectIdField and DateTimeField here
from video_models import Video, Metadata  # Importing the classes from models.py

# Load environment variables from .env file
load_dotenv()

# Fetch the MongoDB URI from the environment variables
MONGODB_URI = os.getenv('MONGODB_URI')

if not MONGODB_URI:
    raise EnvironmentError("Missing MONGODB_URI in .env file or environment. Cannot connect to MongoDB.")

# Connect to MongoDB
try:
    connect(host=MONGODB_URI)
    print("Successfully connected to MongoDB.")
except Exception as e:
    raise ConnectionError(f"Failed to connect to MongoDB with URI {MONGODB_URI}. Error: {e}")

# Function to add a video document to the MongoDB collection
def add_video_document():
    new_video = Video(
        title="Sample Video",
        fileName="sample_video.mp4",
        # storageId=ObjectIdField("af21"),  # This usage is correct now with the import
        filePath="/path/to/sample_video.mp4",
        # uploadDate=DateTimeField("2023-02-23"),  # Correct usage with the import
        metadata=Metadata(
            duration="3 mins",
            format="mp4",
            resolution="1920x1080",
            tags=["sample", "test"]
        ),
        description="This is a sample video document.",
        sourceId="source123"
    )
    
    # Save the video document to MongoDB
    try:
        new_video.save()
        print(f"Video saved successfully with ID: {new_video.id}")
    except Exception as e:
        print(f"Failed to save video document. Error: {e}")

# Example usage
if __name__ == '__main__':
    add_video_document()
