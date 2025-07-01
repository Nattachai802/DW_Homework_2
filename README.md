# DW_Homework_2

นาย ณัฏฐชัย สีใส 65114540170
ระบบนี้ใช้ Django + clickhouse เพื่อที่จะท่ำการตรวจสอบว่า มีข้อมูลใน table event เท่าไหร่แบบ realtime ('SELECT count() FROM events') โดยใช้งาน websocket

อัปเดตจำนวน event แบบ real-time ผ่าน WebSocket และ แสดงผลด้วยการใช้งานร่วมกับ Alpine.JS

ในระบบนี้ใช้ clickhouse ที่ทำการติดตั้งบน wsl โดยใช้ port 8123 

ก่อนจะทำการรันต้องใช้คำสั่ง
./clickhouse server

./clickhouse client (เมื่อต้องการทำการเพิ่มข้อมูล)

### 1. ติดตั้ง Dependencies

pip install -r requirements.txt
