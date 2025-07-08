# DW_Homework_4

# นาย ณัฏฐชัย สีใส 65114540170

ข้อมูลที่ใช้ NYC Taxi Trips Overview (เปลี่ยนจาก Terabyte Click Logs from Criteo เนื่องจากไม่มีที่ให้ Download)

ทำการสร้างฐานข้อมูลเพื่อทำการรองรับข้อมูลใน clickhouse (./clickhouse client (เมื่อต้องการทำการเพิ่มข้อมูล))

ทำการ Insert ข้อมูลผ่านคำสั่ง FROM s3(
    'https://datasets-documentation.s3.eu-west-3.amazonaws.com/nyc-taxi/trips_{0..2}.gz',
    'TabSeparatedWithNames'
);

เมื่อทำการเพิ่มข้อมูลเสร็จสิ่น ให้ทำการ เปิด server clickhouse ด้เวยคำสั่ง
./clickhouse server

สร้างไฟล์ views.py เพื่อทำการเชื่อมต่อและดึงข้อมูลมาแสดงผล

แสดงผลด้วย HTML ny_taxi_template.html 

จากนั้นทำการ py manage.py runserver

end


### 1. ติดตั้ง Dependencies

cd homework2

pip install -r requirements.txt
