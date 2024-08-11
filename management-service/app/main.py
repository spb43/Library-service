import os
import hashlib
import json
import boto3
from tqdm import tqdm
from faker import Faker
import logging
from mongoengine import connect
from models.telemetry import TelementryLogs
# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# MongoDB connection
# connect('library')

storageData = {
    "storageType": "S3",
    "storageBucket": os.getenv('S3')
}

class LogConfig:
    def __init__(self, config_file):
        self.config_file = config_file

    def read_config(self):
        with open(self.config_file, 'r') as f:
            return json.load(f)

class S3Uploader:
    def __init__(self):
        self.bucket_name = os.getenv("S3_BUCKET_NAME")
        self.s3 = boto3.client('s3')

    def upload_file(self, file_path, object_key):
        with open(file_path, 'rb') as f:
            self.s3.upload_fileobj(f, self.bucket_name, object_key)

class MongoDBWriter:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGODB_URI")
        connect(host=self.mongo_uri)

    def write_telemetry_log(self, log_data):
        telem_log = TelementryLogs(**log_data)
        telem_log.save()

class LogUploader:
    def __init__(self, config_file):
        self.config_loader = LogConfig(config_file)
        # self.s3_uploader = S3Uploader()
        self.mongo_writer = MongoDBWriter()
        self.fake = Faker()

    def calculate_hash(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    def process_logs(self):
        config = self.config_loader.read_config()
        for log_entry in tqdm(config['logs'], desc="Processing Logs"):
            file_path = log_entry['path']
            file_name, file_ext = os.path.splitext(os.path.basename(file_path))
            file_type = log_entry['logFormat']
            source = log_entry['source']
            payload_id = log_entry.get('payload_id', None)  # Get payload_id, if available
            # object_key = f"{file_type}/{file_name}{file_ext}"
            # self.s3_uploader.upload_file(file_path, object_key)

            file_hash = self.calculate_hash(file_path)
            logger.info(f"file_hash ---> {file_hash}")
            # Prepare log data based on source
            log_data = {
                "hash": file_hash,
                "file_name": file_name,
                "file_type": file_type,
                "payload_id": payload_id
            }
            logger.info(f'SOURCE ---> {source}')
            if source['type'] == "telemetry":
                logging.info(f'***Uploading telemetry logs to S3***')

                sourceType = source['sourceType']
                sourceId = source['sourceId']

                gs_logs_s3_path = f"s3://{os.getenv("S3_BUCKET_NAME")}/groundStation/telemetry"
                
                # storageData.update({"storageLink": "})
                # log_data = {
                #     "storageData": {
                #         storageType:
                #     }
                # }
            elif source['type'] == "video":
                logging.info(f'***Uploading video logs to S3***')
if __name__ == "__main__":
    uploader = LogUploader("config.json")
    uploader.process_logs()
