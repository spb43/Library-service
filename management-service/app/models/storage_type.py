from mongoengine import Document, StringField

class StorageType(Document):
    name = StringField(required=True)
    description = StringField()
