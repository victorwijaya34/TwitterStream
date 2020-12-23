import pandas as pd
from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086, database='testi')

file_path = r'/home/pi/Kafka-Test/please/sentiment3.csv'

csvReader = pd.read_csv(file_path)

print(csvReader.shape)
print(csvReader.columns)

for row_index, row in csvReader.iterrows():
    tags = row[0]
    fieldValue = row[1]
    json_body = [
        {
            "measurement": "TwitterSentiment2",
            "tags":{
                'timestamp': tags
            },
            "fields": {
                "tweet_sentiment": fieldValue,
                'user_id': fieldValue,
                'user': fieldValue,
                'tweet': fieldValue
            }
        }
    ]
    print(json_body)
    client.write_points(json_body)