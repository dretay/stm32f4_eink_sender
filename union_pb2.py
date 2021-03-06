# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: union.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='union.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bunion.proto\"\xbc\x02\n\x07Weather\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x14.Weather.WeatherType\x12\r\n\x05start\x18\x02 \x02(\r\x12\x13\n\x0bhuman_start\x18\x03 \x02(\t\x12\x0b\n\x03idx\x18\x04 \x02(\r\x12\x13\n\x0btemperature\x18\x05 \x02(\x05\"\xc6\x01\n\x0bWeatherType\x12\x11\n\rCHANCEOFSTORM\x10\x00\x12\n\n\x06\x43LOUDS\x10\x01\x12\n\n\x06\x46OGDAY\x10\x02\x12\x0c\n\x08\x46OGNIGHT\x10\x03\x12\x0e\n\nLITTLERAIN\x10\x04\x12\x0e\n\nLITTLESNOW\x10\x05\x12\x08\n\x04MOON\x10\x06\x12\x13\n\x0fPARTLYCLOUDYDAY\x10\x07\x12\x15\n\x11PARTLYCLOUDYNIGHT\x10\x08\x12\x08\n\x04RAIN\x10\t\x12\t\n\x05SLEET\x10\n\x12\x08\n\x04SNOW\x10\x0b\x12\t\n\x05STORM\x10\x0c\"j\n\x07Meeting\x12\r\n\x05start\x18\x01 \x02(\r\x12\x13\n\x0bhuman_start\x18\x02 \x02(\t\x12\x11\n\thuman_end\x18\x03 \x02(\t\x12\r\n\x05title\x18\x04 \x02(\t\x12\x0c\n\x04room\x18\x05 \x02(\t\x12\x0b\n\x03idx\x18\x06 \x02(\r\"2\n\x04Todo\x12\r\n\x05title\x18\x01 \x02(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\x12\x0b\n\x03idx\x18\x03 \x02(\r\"\x87\x01\n\x0eRetrivalStatus\x12*\n\x06status\x18\x01 \x02(\x0e\x32\x1a.RetrivalStatus.StatusType\x12\x0f\n\x07message\x18\x02 \x01(\t\"8\n\nStatusType\x12\t\n\x05START\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\t\n\x05\x46LUSH\x10\x02\x12\x08\n\x04\x46\x41IL\x10\x03\"\x7f\n\x04Time\x12\x0c\n\x04year\x18\x01 \x02(\r\x12\r\n\x05month\x18\x02 \x02(\r\x12\x0c\n\x04\x64\x61te\x18\x03 \x02(\r\x12\x0f\n\x07weekday\x18\x04 \x02(\r\x12\r\n\x05hours\x18\x05 \x02(\r\x12\x0f\n\x07minutes\x18\x06 \x02(\r\x12\x0f\n\x07seconds\x18\x07 \x02(\r\x12\n\n\x02\x61m\x18\x08 \x02(\x08\"\x18\n\x06Header\x12\x0e\n\x06length\x18\x01 \x02(\r\"\xa7\x01\n\x0cUnionMessage\x12\x1e\n\x05state\x18\x01 \x01(\x0b\x32\x0f.RetrivalStatus\x12\x19\n\x07meeting\x18\x02 \x01(\x0b\x32\x08.Meeting\x12\x13\n\x04todo\x18\x03 \x01(\x0b\x32\x05.Todo\x12\x19\n\x07weather\x18\x04 \x01(\x0b\x32\x08.Weather\x12\x13\n\x04time\x18\x05 \x01(\x0b\x32\x05.Time\x12\x17\n\x06header\x18\x06 \x01(\x0b\x32\x07.Header')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_WEATHER_WEATHERTYPE = _descriptor.EnumDescriptor(
  name='WeatherType',
  full_name='Weather.WeatherType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHANCEOFSTORM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOUDS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOGDAY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOGNIGHT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LITTLERAIN', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LITTLESNOW', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOON', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTLYCLOUDYDAY', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTLYCLOUDYNIGHT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAIN', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLEET', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SNOW', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORM', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=134,
  serialized_end=332,
)
_sym_db.RegisterEnumDescriptor(_WEATHER_WEATHERTYPE)

_RETRIVALSTATUS_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='RetrivalStatus.StatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLUSH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=574,
  serialized_end=630,
)
_sym_db.RegisterEnumDescriptor(_RETRIVALSTATUS_STATUSTYPE)


_WEATHER = _descriptor.Descriptor(
  name='Weather',
  full_name='Weather',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Weather.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='Weather.start', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='human_start', full_name='Weather.human_start', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='idx', full_name='Weather.idx', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='Weather.temperature', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WEATHER_WEATHERTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=332,
)


_MEETING = _descriptor.Descriptor(
  name='Meeting',
  full_name='Meeting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='Meeting.start', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='human_start', full_name='Meeting.human_start', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='human_end', full_name='Meeting.human_end', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='Meeting.title', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='room', full_name='Meeting.room', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='idx', full_name='Meeting.idx', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=440,
)


_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='Todo.title', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Todo.status', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='idx', full_name='Todo.idx', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=492,
)


_RETRIVALSTATUS = _descriptor.Descriptor(
  name='RetrivalStatus',
  full_name='RetrivalStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RetrivalStatus.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='RetrivalStatus.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RETRIVALSTATUS_STATUSTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=630,
)


_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='Time.year', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='month', full_name='Time.month', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='Time.date', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weekday', full_name='Time.weekday', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hours', full_name='Time.hours', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='Time.minutes', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='Time.seconds', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='am', full_name='Time.am', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=632,
  serialized_end=759,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='Header.length', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=761,
  serialized_end=785,
)


_UNIONMESSAGE = _descriptor.Descriptor(
  name='UnionMessage',
  full_name='UnionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='UnionMessage.state', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meeting', full_name='UnionMessage.meeting', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='todo', full_name='UnionMessage.todo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weather', full_name='UnionMessage.weather', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='UnionMessage.time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='UnionMessage.header', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=788,
  serialized_end=955,
)

_WEATHER.fields_by_name['type'].enum_type = _WEATHER_WEATHERTYPE
_WEATHER_WEATHERTYPE.containing_type = _WEATHER
_RETRIVALSTATUS.fields_by_name['status'].enum_type = _RETRIVALSTATUS_STATUSTYPE
_RETRIVALSTATUS_STATUSTYPE.containing_type = _RETRIVALSTATUS
_UNIONMESSAGE.fields_by_name['state'].message_type = _RETRIVALSTATUS
_UNIONMESSAGE.fields_by_name['meeting'].message_type = _MEETING
_UNIONMESSAGE.fields_by_name['todo'].message_type = _TODO
_UNIONMESSAGE.fields_by_name['weather'].message_type = _WEATHER
_UNIONMESSAGE.fields_by_name['time'].message_type = _TIME
_UNIONMESSAGE.fields_by_name['header'].message_type = _HEADER
DESCRIPTOR.message_types_by_name['Weather'] = _WEATHER
DESCRIPTOR.message_types_by_name['Meeting'] = _MEETING
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['RetrivalStatus'] = _RETRIVALSTATUS
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['UnionMessage'] = _UNIONMESSAGE

Weather = _reflection.GeneratedProtocolMessageType('Weather', (_message.Message,), dict(
  DESCRIPTOR = _WEATHER,
  __module__ = 'union_pb2'
  # @@protoc_insertion_point(class_scope:Weather)
  ))
_sym_db.RegisterMessage(Weather)

Meeting = _reflection.GeneratedProtocolMessageType('Meeting', (_message.Message,), dict(
  DESCRIPTOR = _MEETING,
  __module__ = 'union_pb2'
  # @@protoc_insertion_point(class_scope:Meeting)
  ))
_sym_db.RegisterMessage(Meeting)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), dict(
  DESCRIPTOR = _TODO,
  __module__ = 'union_pb2'
  # @@protoc_insertion_point(class_scope:Todo)
  ))
_sym_db.RegisterMessage(Todo)

RetrivalStatus = _reflection.GeneratedProtocolMessageType('RetrivalStatus', (_message.Message,), dict(
  DESCRIPTOR = _RETRIVALSTATUS,
  __module__ = 'union_pb2'
  # @@protoc_insertion_point(class_scope:RetrivalStatus)
  ))
_sym_db.RegisterMessage(RetrivalStatus)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), dict(
  DESCRIPTOR = _TIME,
  __module__ = 'union_pb2'
  # @@protoc_insertion_point(class_scope:Time)
  ))
_sym_db.RegisterMessage(Time)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'union_pb2'
  # @@protoc_insertion_point(class_scope:Header)
  ))
_sym_db.RegisterMessage(Header)

UnionMessage = _reflection.GeneratedProtocolMessageType('UnionMessage', (_message.Message,), dict(
  DESCRIPTOR = _UNIONMESSAGE,
  __module__ = 'union_pb2'
  # @@protoc_insertion_point(class_scope:UnionMessage)
  ))
_sym_db.RegisterMessage(UnionMessage)


# @@protoc_insertion_point(module_scope)
