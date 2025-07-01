from clickhouse_connect import get_client

client = get_client(host='localhost', username='default', port=8123 ,password='')

print("Connecting to ClickHouse...")

def query_clickhouse(sql):
    result = client.query(sql)
    print("✅ ClickHouse connected: ", result.result_rows)
    return result.result_rows

if __name__ == '__main__':
    print("Testing query...")
    query_clickhouse("SELECT count() FROM events")