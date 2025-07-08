from django.http import JsonResponse
from clickhouse_driver import Client
from django.shortcuts import render

def hw04_view(request):
    client = Client(host='localhost', port='9000', database='nyc_taxi')  # เชื่อมต่อกับ ClickHouse
    query = "SELECT trip_id, pickup_datetime, dropoff_datetime, passenger_count, trip_distance, fare_amount FROM trips_small LIMIT 20"
    
    # รัน query และดึงข้อมูล
    result = client.execute(query)
    
    # แปลงผลลัพธ์เป็น dictionary สำหรับส่งไปยัง JsonResponse
    data = []
    for row in result:
        data.append({
            "id": row[0],
            "pickup_datetime": row[1],
            "dropoff_datetime": row[2],
            "passenger_count": row[3],
            "trip_distance": row[4],
            "fare_amount": row[5]
        })
    
    return render(request, 'ny_taxi_template.html', {'data': data})
