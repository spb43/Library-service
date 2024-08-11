from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, ListField

class GroundStationRadio(EmbeddedDocument):
    antennaType = StringField()
    frequencyRange = StringField()
    maxRange = StringField()

class GroundStationSpecifications(EmbeddedDocument):
    radio1 = EmbeddedDocumentField(GroundStationRadio)
    radio2 = EmbeddedDocumentField(GroundStationRadio)
    workingTime = StringField()
    supply = StringField()

class GroundStation(Document):
    meta = {'collection': 'groundStations'}
    groundStationId = StringField()  # Unique identifier for the Ground Station
    name = StringField()
    specifications = EmbeddedDocumentField(GroundStationSpecifications)
    operationalStatus = StringField(choices=("prototype", "active", "maintenance", "offline"))
    capabilities = ListField(StringField())
    developer = StringField()
    tags = ListField(StringField())
    notes = StringField()
