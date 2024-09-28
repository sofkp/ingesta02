import pymysql
import pandas as pd
import boto3

def export_mysql_to_s3(host, port, user, password, database, table, output_file, bucket_name):
    connection = pymysql.connect(
        host=host,
        port=int(port),
        user=user,
        password=password,
        database=database
    )
    df = pd.read_sql(f"SELECT * FROM {table}", connection)
    df.to_csv(output_file, index=False)
    connection.close()

    boto3.client('s3').upload_file(output_file, bucket_name, output_file)

export_mysql_to_s3('52.72.186.244', 8008, 'root', 'utec', 'tienda', 'fabricantes', 'data.csv', 'skp-output-ingesta02')

print("Ingesta completada")
