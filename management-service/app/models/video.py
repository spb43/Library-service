from mongoengine import Document, StringField, ObjectIdField, ReferenceField, DateTimeField, ListField, EmbeddedDocument, EmbeddedDocumentField
from storage_type import StorageType
# {
#     "_id": "ObjectId()",
#     "title": "String",
#     "fileName": "String",
#     "storageId": "ObjectId()", // Reference to the Storage collection
#     "storageBucket": "String", // Name of the storage bucket/container
#     "sourceId": "String", // Identifier for the original source of the video, uav, ground station, etc.
#     "filePath": "String", // Path within the storage bucket
#     "uploadDate": "ISODate('YYYY-MM-DDTHH:MM:SSZ')",
#     "metadata": {
#       "duration": "Number",
#       "format": "String", // e.g., "mp4", "hls"
#       "resolution": "String", // e.g., "1920x1080"
#       "tags": ["String"] // Array of tags
#     },
#     "description": "String" // Optional description of the video
# }

class VideoMetadata(EmbeddedDocument):
    duration = StringField()
    format = StringField()  # e.g., "mp4", "hls"
    resolution = StringField()  # e.g., "1920x1080"
    tags = ListField(StringField())  # List of tags

class Video(Document):
    title = StringField(required=True)
    file_name = StringField(required=True)
    storage = ReferenceField(StorageType, required=True)
    file_path = StringField(required=True)
    upload_date = DateTimeField()
    metadata = EmbeddedDocumentField(VideoMetadata)
    description = StringField()
    source_id = StringField()
