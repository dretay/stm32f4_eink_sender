#! /usr/bin/python
import union_pb2
import sys
import pigpio
import re
import datetime
from time import sleep

class EInk(object):
    def __init__(self):
        self.pi = pigpio.pi()         
        self.h = self.pi.i2c_open(1, 0x03)
    
    def send_message_header(self, serialized_msg):
        union_message_header = union_pb2.UnionMessage()
        union_message_header.header.length = len(serialized_msg)    
        serialized_header = union_message_header.SerializeToString()
        print(f"serialized a {len(serialized_header)} byte header for a {union_message_header.header.length} byte message")
        print(f"({serialized_header.hex()}) {serialized_msg.hex()}")    
        self.pi.i2c_write_device(self.h, serialized_header)        

    def send_message(self, union_message):
        serialized_msg = union_message.SerializeToString()
        self.send_message_header(serialized_msg)     
        self.pi.i2c_write_device(self.h, serialized_msg)

    def parse_meeting_start(self, meeting_string):
        re_string = '(\d+)\:(\d+)\s(\w+).*'
        m = re.search(re_string, meeting_string)
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)

        hours = int(m.group(1))
        if(m.group(3) == "PM" and hours != 12):
            hours = 12 + hours

        minutes = int(m.group(2))
        start_time = now.replace(
            hour=hours, minute=minutes, second=0, microsecond=0)

        return int((start_time - midnight).seconds / 60)

    def send_meeting(self, idx, meeting_string):
        re_string = "(\d{2}\:\d{2}\s\w{2})\s\-\s(\d{2}\:\d{2}\s\w{2})\s,\s([^;]+);?(.*)"
        m = re.search(re_string, meeting_string)
        union_message = union_pb2.UnionMessage()
        try:
            union_message.meeting.start = self.parse_meeting_start(m.group(1))
            union_message.meeting.human_start = m.group(1)
            union_message.meeting.human_end = m.group(2)
            union_message.meeting.title = m.group(3)
            if len(m.groups()) == 4:
                union_message.meeting.room = m.group(4)                
            union_message.meeting.idx = idx
            print(f"{union_message.meeting.start}, {union_message.meeting.human_start}, {union_message.meeting.human_end}, {union_message.meeting.title}, {union_message.meeting.room}")
            self.send_message(union_message)
        except AttributeError as e:
            print(f"could not parse meeting {meeting_string}: {e}")

    def send_todo(self, idx, todo):
        union_message = union_pb2.UnionMessage()
        union_message.todo.idx = idx
        union_message.todo.title = todo
        print(f"{union_message.todo.idx}, {union_message.todo.title}")
        self.send_message(union_message)


    def send_flush(self):
        union_message = union_pb2.UnionMessage()
        union_message.state.status = union_pb2.RetrivalStatus.FLUSH
        self.send_message(union_message)


    def send_start(self):
        union_message = union_pb2.UnionMessage()
        union_message.state.status = union_pb2.RetrivalStatus.START
        self.send_message(union_message)


    def send_localtime(self):
        now = datetime.datetime.now()
        union_message = union_pb2.UnionMessage()

        union_message.time.year = int(now.strftime("%y"))
        union_message.time.month = int(now.strftime("%m"))
        union_message.time.date = int(now.strftime("%d"))
        union_message.time.weekday = int(now.strftime("%w"))
        union_message.time.hours = int(now.strftime("%I"))
        union_message.time.minutes = int(now.strftime("%M"))
        union_message.time.seconds = int(now.strftime("%S"))
        union_message.time.am = now.strftime("%p") == "AM"

        print(f"{union_message.time.month}, {union_message.time.date},{union_message.time.weekday}, {union_message.time.hours}, {union_message.time.minutes}, {union_message.time.seconds}, {union_message.time.am}")
        self.send_message(union_message)

    def truncate_weather_start(self, weather_string):
        re_string = '(\d+):\d{2}\s(\w+).*'
        m = re.search(re_string, weather_string)
        return f"{m.group(1)} {m.group(2)}"
    def parse_weather_start(self, weather_string):
        re_string = '(\d+):\d{2}\s(\w+).*'
        m = re.search(re_string, weather_string)
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)

        hours = int(m.group(1))
        if(m.group(2) == "PM" and hours != 12):
            hours = 12 + hours

        start_time = now.replace(hour=hours, minute=0, second=0, microsecond=0)

        return int((start_time - midnight).seconds / 60)


    def send_weather(self, idx, start, description):
        # todo: need to map am/pm to day or night values
        weather_lookup = {
            "Mostly Sunny": union_pb2.Weather.MOON,
            "Sunny": union_pb2.Weather.MOON,  # this needs to be a sun

            "Mostly Clear": union_pb2.Weather.MOON,
            "Clear": union_pb2.Weather.MOON,  # clear = moon

            "Partly Cloudy": union_pb2.Weather.PARTLYCLOUDYDAY,
            "Cloudy": union_pb2.Weather.PARTLYCLOUDYDAY,
            "Mostly Cloudy": union_pb2.Weather.PARTLYCLOUDYDAY,

            "Few Showers": union_pb2.Weather.LITTLERAIN,
            "Showers": union_pb2.Weather.LITTLERAIN,

            "Light Rain": union_pb2.Weather.LITTLERAIN,
            "Rain": union_pb2.Weather.RAIN,

            "Scattered Thunderstorms": union_pb2.Weather.RAIN,
            "Isolated Thunderstorms": union_pb2.Weather.RAIN,
            "Thunderstorms": union_pb2.Weather.RAIN,
        }
        union_message = union_pb2.UnionMessage()
        union_message.weather.start = self.parse_weather_start(start)
        union_message.weather.human_start = self.truncate_weather_start(start)
        union_message.weather.type = weather_lookup.get(description)
        union_message.weather.idx = idx        
        print(f"{idx},{start},{description} = {union_message.weather.idx}, {union_message.weather.human_start}, {union_message.weather.start}, {union_message.weather.type}")
        self.send_message(union_message)



# send_localtime()
# send_start()
# send_meeting(0,"9:15 AM - 9:45 AM , backlog scrub; Conf Rm - Reston, VA, 8th Floor - Nexen (8)")
# send_meeting(1,"10:45 AM - 11:15 AM , ESPIR Unified Standup Vol. 2; Same room ENDPOINT / UAC uses")
# send_meeting(2,"10:45 AM - 11:00 AM , Endpoint Standup; Conf Rm - Reston, VA, 8th Floor - New York Times (8)")
# send_meeting(3,"11:15 AM - 11:45 AM , project planning; fixme")
# send_meeting(4,"12:30 PM - 1:30 PM , 1:1; fixme")
# send_meeting(5,"1:30 PM - 2:30 PM , Drew/Chris 1:1; 8")
# send_meeting(6,"2:30 PM - 3:00 PM , ESPIR weekly project meeting; Conf Rm - Reston, VA, 8th Floor - Brocade (10)")
# send_meeting(7,"3:30 PM - 4:00 PM , Machine Learning in MD; Conf Rm - Reston, VA, 8th Floor - New York Times (8)")
# send_meeting(8,"4:00 PM - 5:00 PM , ESPIR desk scrub; Conf Rm - Reston, VA, 8th Floor - New York Times (8)")
# send_meeting(9,"4:00 PM - 4:45 PM , Weekly Helix + Cloud Srvcs Program meeting; Conf Rm - 601 - U1L - Bespin (8 - 12)")
# send_todo(0, "Proper Preparation Prevents Poor...")
# send_todo(1, "dates need to be in UTC")
# send_todo(2, "add created time to agent tasks")
# send_todo(3, "remove limit from agent tables e...")
# send_todo(4, "remove need to unify task result...")
# send_todo(5, "add loading mask to acquisition ...")
# send_todo(6, "check if sb works on incident pa...")
# send_todo(7, "new task api needs to display er...")
# send_todo(8, "check with anthony - audits used...")
# send_todo(9, "verify modal pops up everywhere")
# send_todo(10, "add md5 click action back into a...")
# send_weather(0, "2 AM", "Showers")

# send_flush()

# f = open('deleteme', "wb")
# f.write(multipart_message.SerializeToString())
# f.close()

# multipart_message = multipart_message_pb2.MultipartMessage()
# try:
#   f = open('deleteme', "rb")
#   multipart_message.ParseFromString(f.read())
#   f.close()
# except IOError:
#   print("Could not open file")
#   exit(1)

# for record in multipart_message.meeting.records:
# 	print(record.title)

# for record in multipart_message.weather.records:
# 	print(record.type)
