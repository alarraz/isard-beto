# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engine/grpc/proto/template.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='engine/grpc/proto/template.proto',
  package='template',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n engine/grpc/proto/template.proto\x12\x08template\x1a\x19google/protobuf/any.proto\"\xd9\x01\n\x0bHardwareNew\x12\r\n\x05vcpus\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x05\x12\x17\n\x0f\x62oot_disk_rpath\x18\x03 \x01(\t\x12\x15\n\rboot_disk_bus\x18\x04 \x01(\t\x12\x16\n\x0e\x62oot_disk_size\x18\x05 \x01(\x05\x12\x0e\n\x06videos\x18\x06 \x03(\t\x12\x10\n\x08graphics\x18\x07 \x03(\t\x12\r\n\x05\x62oots\x18\x08 \x03(\t\x12\x12\n\ninterfaces\x18\t \x03(\t\x12\x0c\n\x04isos\x18\n \x03(\t\x12\x10\n\x08\x66loppies\x18\x0b \x03(\t\"\xc5\x01\n\x0fHardwareDerived\x12\r\n\x05vcpus\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x05\x12\x17\n\x0f\x62oot_disk_rpath\x18\x03 \x01(\t\x12\x15\n\rboot_disk_bus\x18\x04 \x01(\t\x12\x0e\n\x06videos\x18\x05 \x03(\t\x12\x10\n\x08graphics\x18\x06 \x03(\t\x12\r\n\x05\x62oots\x18\x07 \x03(\t\x12\x12\n\ninterfaces\x18\x08 \x03(\t\x12\x0c\n\x04isos\x18\t \x03(\t\x12\x10\n\x08\x66loppies\x18\n \x03(\t\"\xab\x01\n\x0eHardwareUpdate\x12\r\n\x05vcpus\x18\x01 \x01(\x05\x12\x0e\n\x06memory\x18\x02 \x01(\x05\x12\x15\n\rboot_disk_bus\x18\x07 \x01(\t\x12\x0e\n\x06videos\x18\x03 \x03(\t\x12\x10\n\x08graphics\x18\x04 \x03(\t\x12\r\n\x05\x62oots\x18\x05 \x03(\t\x12\x12\n\ninterfaces\x18\x06 \x03(\t\x12\x0c\n\x04isos\x18\x08 \x03(\t\x12\x10\n\x08\x66loppies\x18\t \x03(\t\"!\n\nGetRequest\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\"5\n\x0bGetResponse\x12&\n\x08template\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"\r\n\x0bListRequest\"!\n\x0cListResponse\x12\x11\n\ttemplates\x18\x01 \x03(\t\"$\n\rDeleteRequest\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\"~\n\x0e\x44\x65leteResponse\x12-\n\x05state\x18\x01 \x01(\x0e\x32\x1e.template.DeleteResponse.State\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\"-\n\x05State\x12\x0b\n\x07\x44\x45LETED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\"P\n\rUpdateRequest\x12\x13\n\x0btemplate_id\x18\x01 \x01(\t\x12*\n\x08hardware\x18\x02 \x01(\x0b\x32\x18.template.HardwareUpdate\"~\n\x0eUpdateResponse\x12-\n\x05state\x18\x01 \x01(\x0e\x32\x1e.template.UpdateResponse.State\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\"-\n\x05State\x12\x0b\n\x07STOPPED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\"\x80\x01\n\x12\x46romDesktopRequest\x12\x12\n\ndesktop_id\x18\x01 \x01(\t\x12\x13\n\x0btemplate_id\x18\x02 \x01(\t\x12+\n\x08hardware\x18\x03 \x01(\x0b\x32\x19.template.HardwareDerived\x12\x14\n\x0cnext_actions\x18\x04 \x03(\t\"\x88\x01\n\x13\x46romDesktopResponse\x12\x32\n\x05state\x18\x01 \x01(\x0e\x32#.template.FromDesktopResponse.State\x12\x0e\n\x06\x64\x65tail\x18\x02 \x01(\t\"-\n\x05State\x12\x0b\n\x07STOPPED\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x32\xc5\x02\n\x08Template\x12\x34\n\x03Get\x12\x14.template.GetRequest\x1a\x15.template.GetResponse\"\x00\x12\x37\n\x04List\x12\x15.template.ListRequest\x1a\x16.template.ListResponse\"\x00\x12=\n\x06\x44\x65lete\x12\x17.template.DeleteRequest\x1a\x18.template.DeleteResponse\"\x00\x12=\n\x06Update\x12\x17.template.UpdateRequest\x1a\x18.template.UpdateResponse\"\x00\x12L\n\x0b\x46romDesktop\x12\x1c.template.FromDesktopRequest\x1a\x1d.template.FromDesktopResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])



_DELETERESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='template.DeleteResponse.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=926,
  serialized_end=971,
)
_sym_db.RegisterEnumDescriptor(_DELETERESPONSE_STATE)

_UPDATERESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='template.UpdateResponse.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1136,
  serialized_end=1181,
)
_sym_db.RegisterEnumDescriptor(_UPDATERESPONSE_STATE)

_FROMDESKTOPRESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='template.FromDesktopResponse.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1136,
  serialized_end=1181,
)
_sym_db.RegisterEnumDescriptor(_FROMDESKTOPRESPONSE_STATE)


_HARDWARENEW = _descriptor.Descriptor(
  name='HardwareNew',
  full_name='template.HardwareNew',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vcpus', full_name='template.HardwareNew.vcpus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='template.HardwareNew.memory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk_rpath', full_name='template.HardwareNew.boot_disk_rpath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk_bus', full_name='template.HardwareNew.boot_disk_bus', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk_size', full_name='template.HardwareNew.boot_disk_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videos', full_name='template.HardwareNew.videos', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graphics', full_name='template.HardwareNew.graphics', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boots', full_name='template.HardwareNew.boots', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaces', full_name='template.HardwareNew.interfaces', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isos', full_name='template.HardwareNew.isos', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floppies', full_name='template.HardwareNew.floppies', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=291,
)


_HARDWAREDERIVED = _descriptor.Descriptor(
  name='HardwareDerived',
  full_name='template.HardwareDerived',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vcpus', full_name='template.HardwareDerived.vcpus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='template.HardwareDerived.memory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk_rpath', full_name='template.HardwareDerived.boot_disk_rpath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk_bus', full_name='template.HardwareDerived.boot_disk_bus', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videos', full_name='template.HardwareDerived.videos', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graphics', full_name='template.HardwareDerived.graphics', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boots', full_name='template.HardwareDerived.boots', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaces', full_name='template.HardwareDerived.interfaces', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isos', full_name='template.HardwareDerived.isos', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floppies', full_name='template.HardwareDerived.floppies', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=491,
)


_HARDWAREUPDATE = _descriptor.Descriptor(
  name='HardwareUpdate',
  full_name='template.HardwareUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vcpus', full_name='template.HardwareUpdate.vcpus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='template.HardwareUpdate.memory', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boot_disk_bus', full_name='template.HardwareUpdate.boot_disk_bus', index=2,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='videos', full_name='template.HardwareUpdate.videos', index=3,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graphics', full_name='template.HardwareUpdate.graphics', index=4,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boots', full_name='template.HardwareUpdate.boots', index=5,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaces', full_name='template.HardwareUpdate.interfaces', index=6,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isos', full_name='template.HardwareUpdate.isos', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floppies', full_name='template.HardwareUpdate.floppies', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=665,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='template.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='template.GetRequest.template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=667,
  serialized_end=700,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='template.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template', full_name='template.GetResponse.template', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=755,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='template.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=770,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='template.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='templates', full_name='template.ListResponse.templates', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=772,
  serialized_end=805,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='template.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='template.DeleteRequest.template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=807,
  serialized_end=843,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='template.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='template.DeleteResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='template.DeleteResponse.detail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DELETERESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=971,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='template.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='template.UpdateRequest.template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hardware', full_name='template.UpdateRequest.hardware', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=973,
  serialized_end=1053,
)


_UPDATERESPONSE = _descriptor.Descriptor(
  name='UpdateResponse',
  full_name='template.UpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='template.UpdateResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='template.UpdateResponse.detail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATERESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1055,
  serialized_end=1181,
)


_FROMDESKTOPREQUEST = _descriptor.Descriptor(
  name='FromDesktopRequest',
  full_name='template.FromDesktopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='desktop_id', full_name='template.FromDesktopRequest.desktop_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='template.FromDesktopRequest.template_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hardware', full_name='template.FromDesktopRequest.hardware', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_actions', full_name='template.FromDesktopRequest.next_actions', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1184,
  serialized_end=1312,
)


_FROMDESKTOPRESPONSE = _descriptor.Descriptor(
  name='FromDesktopResponse',
  full_name='template.FromDesktopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='template.FromDesktopResponse.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='template.FromDesktopResponse.detail', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FROMDESKTOPRESPONSE_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1315,
  serialized_end=1451,
)

_GETRESPONSE.fields_by_name['template'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_DELETERESPONSE.fields_by_name['state'].enum_type = _DELETERESPONSE_STATE
_DELETERESPONSE_STATE.containing_type = _DELETERESPONSE
_UPDATEREQUEST.fields_by_name['hardware'].message_type = _HARDWAREUPDATE
_UPDATERESPONSE.fields_by_name['state'].enum_type = _UPDATERESPONSE_STATE
_UPDATERESPONSE_STATE.containing_type = _UPDATERESPONSE
_FROMDESKTOPREQUEST.fields_by_name['hardware'].message_type = _HARDWAREDERIVED
_FROMDESKTOPRESPONSE.fields_by_name['state'].enum_type = _FROMDESKTOPRESPONSE_STATE
_FROMDESKTOPRESPONSE_STATE.containing_type = _FROMDESKTOPRESPONSE
DESCRIPTOR.message_types_by_name['HardwareNew'] = _HARDWARENEW
DESCRIPTOR.message_types_by_name['HardwareDerived'] = _HARDWAREDERIVED
DESCRIPTOR.message_types_by_name['HardwareUpdate'] = _HARDWAREUPDATE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponse'] = _UPDATERESPONSE
DESCRIPTOR.message_types_by_name['FromDesktopRequest'] = _FROMDESKTOPREQUEST
DESCRIPTOR.message_types_by_name['FromDesktopResponse'] = _FROMDESKTOPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HardwareNew = _reflection.GeneratedProtocolMessageType('HardwareNew', (_message.Message,), {
  'DESCRIPTOR' : _HARDWARENEW,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.HardwareNew)
  })
_sym_db.RegisterMessage(HardwareNew)

HardwareDerived = _reflection.GeneratedProtocolMessageType('HardwareDerived', (_message.Message,), {
  'DESCRIPTOR' : _HARDWAREDERIVED,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.HardwareDerived)
  })
_sym_db.RegisterMessage(HardwareDerived)

HardwareUpdate = _reflection.GeneratedProtocolMessageType('HardwareUpdate', (_message.Message,), {
  'DESCRIPTOR' : _HARDWAREUPDATE,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.HardwareUpdate)
  })
_sym_db.RegisterMessage(HardwareUpdate)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

FromDesktopRequest = _reflection.GeneratedProtocolMessageType('FromDesktopRequest', (_message.Message,), {
  'DESCRIPTOR' : _FROMDESKTOPREQUEST,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.FromDesktopRequest)
  })
_sym_db.RegisterMessage(FromDesktopRequest)

FromDesktopResponse = _reflection.GeneratedProtocolMessageType('FromDesktopResponse', (_message.Message,), {
  'DESCRIPTOR' : _FROMDESKTOPRESPONSE,
  '__module__' : 'engine.grpc.proto.template_pb2'
  # @@protoc_insertion_point(class_scope:template.FromDesktopResponse)
  })
_sym_db.RegisterMessage(FromDesktopResponse)



_TEMPLATE = _descriptor.ServiceDescriptor(
  name='Template',
  full_name='template.Template',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1454,
  serialized_end=1779,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='template.Template.Get',
    index=0,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='template.Template.List',
    index=1,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='template.Template.Delete',
    index=2,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='template.Template.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FromDesktop',
    full_name='template.Template.FromDesktop',
    index=4,
    containing_service=None,
    input_type=_FROMDESKTOPREQUEST,
    output_type=_FROMDESKTOPRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEMPLATE)

DESCRIPTOR.services_by_name['Template'] = _TEMPLATE

# @@protoc_insertion_point(module_scope)
