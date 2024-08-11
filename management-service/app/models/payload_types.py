from mongoengine import Document, StringField, ReferenceField, ListField

class Payload(Document):
    payloadId = StringField()  # Unique identifier for the Payload
    name = StringField()
    typeId = ReferenceField('PayloadType')  # Reference to the payloads collection
    operationalStatus = StringField(choices=("active", "maintenance", "inactive"))
    compatibility = ListField(ReferenceField('UAV'))  # Reference to the UAVs collection
    notes = StringField()

class PayloadType(Document):
    # Define the fields for payload types if needed
    pass  # For now, we don't specify additional fields

class UAV(Document):
    # Define the fields for UAVs if needed
    pass  # For now, we don't specify additional fields
