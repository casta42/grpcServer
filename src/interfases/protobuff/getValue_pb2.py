# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getValue.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egetValue.proto\x12\rgetCoordinate\x1a\x1bgoogle/protobuf/empty.proto\"\"\n\ncoordinate\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x32W\n\x11\x63oordinateService\x12\x42\n\rgetCoordinate\x12\x16.google.protobuf.Empty\x1a\x19.getCoordinate.coordinateb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'getValue_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COORDINATE._serialized_start=62
  _COORDINATE._serialized_end=96
  _COORDINATESERVICE._serialized_start=98
  _COORDINATESERVICE._serialized_end=185
# @@protoc_insertion_point(module_scope)
