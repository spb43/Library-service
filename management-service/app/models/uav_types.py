from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, IntField, ListField

# {
#     "_id": "ObjectId()",
#     "model": "String",
#     "manufacturer": "String",
#     "serialNumber": "String",
#     "specifications": {
#       "maxFlightTime": "Number", // Maximum flight time in minutes
#       "maxSpeed": "Number", // Maximum speed in km/h
#       "weight": "Number", // Weight in grams
#       "operationalRange": "Number", // Operational range in meters
#       "cameraResolution": "String", // Camera resolution in megapixels
#       "batteryCapacity": "Number", // Battery capacity in mAh
#     },
#     "status": "String", // e.g., "active", "maintenance", "decommissioned"
#     "tags": ["String"], // Array of tags for categorization or notes
#     "notes": "String" // Optional field for additional notes or comments
# }

class Specifications(EmbeddedDocument):
    maxFlightTime = IntField()  # Maximum flight time in minutes
    maxSpeed = IntField()  # Maximum speed in km/h
    weight = IntField()  # Weight in grams
    operationalRange = IntField()  # Operational range in meters
    cameraResolution = StringField()  # Camera resolution in megapixels
    batteryCapacity = IntField()  # Battery capacity in mAh
    cameraType = StringField()  # Camera type

class UAV(Document):
    model = StringField()
    manufacturer = StringField()
    serialNumber = StringField()
    specifications = EmbeddedDocumentField(Specifications)
    status = StringField(choices=("active", "maintenance", "decommissioned"))
    tags = ListField(StringField())
    notes = StringField()

