from mongoengine import Document, StringField, DateTimeField, ReferenceField, EmbeddedDocument, EmbeddedDocumentField, ListField
from .storage_type import StorageType

class StorageData(EmbeddedDocument):
    storageType = ReferenceField(StorageType, required=True)
    storageBucket = StringField(required=True)
    storageLink = StringField(required=True)

class TelementryLogs(Document):
    storageData = EmbeddedDocumentField(StorageData)
    logFormat = StringField(required=True)
    uploadDate = DateTimeField()
    sourceType = StringField()
    sourceId = StringField(required=True)
    tags = StringField()
    description = StringField()
    alias = StringField(required=True) #Alias for group of logs

# {
#     "_id": "ObjectId()",
#     "storagedata":{
#       "storageType": "ObjectId()",//StorageTypes.json
#       "storageBucket": "your-storage-bucket-name",
#       "storageLink": "s3://exports/data_export.csv",
#       "fileType": "csv"
#     },
#     "logType": "csv",
#     "uploadDate": "ISODate('2024-02-03T10:45:00Z')",
#     "sourceId": "ObjectId()", //uavs.json, groundStations.json Identifier for the original source of the log file
#     "tags": "Field_tests",
#     "description": "Monthly customer purchase data export."
# }
  