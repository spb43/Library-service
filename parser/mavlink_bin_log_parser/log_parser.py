import json
import time
import argparse
from pymavlink import mavutil
import pandas as pd

def parse_binary_to_all_formats(input_log_filename):
    time_epoch = int(time.time()* 1000)
    json_file_name = f'{input_log_filename.replace(".", "_")}_{time_epoch}.json'
    mlog = mavutil.mavlink_connection(input_log_filename)
    
    with open(json_file_name, 'a') as f:
        while True:
            msg = mlog.recv_msg()
            if msg is None:
                break
            f.write(f'{json.dumps(msg.to_dict(), default=str)}\n')
    
    log = pd.read_json(json_file_name, lines=True).sort_values('mavpackettype')
    log.to_csv(json_file_name.replace('.json','.csv'), index=False)
    log.to_parquet(json_file_name.replace('.json','.parquet'), index=False)
    del log

def main():
    parser = argparse.ArgumentParser(description='Convert MAVLink log to JSON, CSV and PARQUET format.')
    parser.add_argument('--input_file', help='Input MAVLink log file (.bin or .tlog)')
    args = parser.parse_args()

    parse_binary_to_all_formats(args.input_file)

if __name__ == "__main__":
    main()
