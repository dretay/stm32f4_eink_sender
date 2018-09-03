#! /usr/bin/python
import union_pb2
import sys
import pigpio
import re
import datetime
from time import sleep
import pytz

PRING_MSG_HEAERS = False
PRINT_RAW_MSG = False

class EInk(object):
    def __init__(self):
        self.pi = pigpio.pi()
        self.h = self.pi.i2c_open(1, 0x03)

    def send_message_header(self, serialized_msg):
        union_message_header = union_pb2.UnionMessage()
        union_message_header.header.length = len(serialized_msg)
        serialized_header = union_message_header.SerializeToString()
        if(PRING_MSG_HEAERS):
            print(f"serialized a {len(serialized_header)} byte header for a {union_message_header.header.length} byte message")
        if(PRINT_RAW_MSG):
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

        hours = int(m.group(1))
        if(m.group(3) == "PM" and hours != 12): hours += 12

        minutes = int(m.group(2))
        start_time = now.replace(hour=hours, minute=minutes, second=0, microsecond=0)
        start_time -= datetime.timedelta(hours=4)

        return int(start_time.timestamp())


    def send_meeting(self, idx, meeting_string):
        re_string = "(\d{1,2}\:\d{2}\s\w{2})\s\-\s(\d{1,2}\:\d{2}\s\w{2})\s,\s([^;]+);?(.*)"
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
            print(f"{idx}, {union_message.meeting.start}, {union_message.meeting.human_start}, {union_message.meeting.human_end}, {union_message.meeting.title}, {union_message.meeting.room}")
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


    def send_localtime(self, now=datetime.datetime.now()):

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


    def send_weather(self, idx, description, start_time=datetime.datetime.now()):
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

        start_time = start_time.replace(minute=0, second=0, microsecond=0)
        # start_time -= datetime.timedelta(hours=4)
        start_time += datetime.timedelta(hours=idx)


        union_message.weather.start = int(start_time.timestamp())
        union_message.weather.human_start = start_time.strftime("%I %p")
        union_message.weather.type = weather_lookup.get(description)
        union_message.weather.idx = idx
        print(f"{union_message.weather.idx}, {union_message.weather.human_start}, {union_message.weather.start}, {union_message.weather.type}")
        self.send_message(union_message)