from mongoengine import Document, StringField, DateTimeField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, ListField
from .storage_type import StorageType
from .image_type import ImageType

class ImageMetadata(EmbeddedDocument):
    resolution = StringField()  # e.g., "1920x1080"
    tags = ListField(StringField())  # List of tags
    captured_date = DateTimeField()  # Date when the image was captured
    camera_model = StringField()  # Camera model used to capture the image

class Image(Document):
    title = StringField(required=True)
    file_name = StringField(required=True)
    image_type = ReferenceField(ImageType, required=True)
    storage = ReferenceField(StorageType, required=True)
    file_path = StringField(required=True)
    upload_date = DateTimeField()
    metadata = EmbeddedDocumentField(ImageMetadata)
    description = StringField()
    source_id = StringField()
