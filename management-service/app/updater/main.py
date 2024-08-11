import yaml
import sys
import uuid
import logging
import os
sys.path.append('../')
from mongoengine import connect
from models.groundStations import GroundStation
from models.uav_types import UAV
# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MongoDBWriter:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGODB_URI")
        connect(host=self.mongo_uri)

    def update_uavs_collection(self, data):
        uav_data = UAV(**data)
        uav_data.save()

    def update_ground_stations_collection(self, data):
        gs_data = GroundStation(**data)
        gs_data.save()


def parse_yaml_config(file_path):
    with open(file_path, 'r') as yaml_file:
        try:
            parsed_yaml = yaml.safe_load(yaml_file)
            return parsed_yaml
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <yaml_config_file> <collection_to_update>")
        sys.exit(1)
    
    yaml_file_path = sys.argv[1]
    collection_name = sys.argv[2]
    
    config_data = parse_yaml_config(yaml_file_path)
    mongo_writer = MongoDBWriter()
    
    if collection_name == 'groundStations':
        config_data['groundStationId'] = str(uuid.uuid4())
        print(config_data)
        mongo_writer.update_ground_stations_collection(config_data)
    elif collection_name == 'uavs':
        print("Write to uav collection")