from mongoengine import Document, StringField

# {
#     "_id": "ObjectId()",
#     "typeName": "String", // e.g., "JPEG", "PNG", "GIF"
#     "description": "String" // Optional description of the image type
# }

class ImageType(Document):
    typeName = StringField(required=True)
    description = StringField()
