# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/categorical.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.lib.python import list_pb2 as proto_dot_lib_dot_python_dot_list__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/categorical.proto",
    package="pandas",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x17proto/categorical.proto\x12\x06pandas\x1a%proto/core/common/common_object.proto\x1a\x1bproto/lib/python/list.proto"w\n\x16PandasCategoricalDtype\x12!\n\x02id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12)\n\ncategories\x18\x02 \x01(\x0b\x32\x15.syft.lib.python.List\x12\x0f\n\x07ordered\x18\x03 \x01(\x08"\x98\x01\n\x11PandasCategorical\x12!\n\x02id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12$\n\x05\x63odes\x18\x02 \x01(\x0b\x32\x15.syft.lib.python.List\x12)\n\ncategories\x18\x03 \x01(\x0b\x32\x15.syft.lib.python.List\x12\x0f\n\x07ordered\x18\x04 \x01(\x08\x62\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_lib_dot_python_dot_list__pb2.DESCRIPTOR,
    ],
)


_PANDASCATEGORICALDTYPE = _descriptor.Descriptor(
    name="PandasCategoricalDtype",
    full_name="pandas.PandasCategoricalDtype",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="pandas.PandasCategoricalDtype.id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="categories",
            full_name="pandas.PandasCategoricalDtype.categories",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ordered",
            full_name="pandas.PandasCategoricalDtype.ordered",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=103,
    serialized_end=222,
)


_PANDASCATEGORICAL = _descriptor.Descriptor(
    name="PandasCategorical",
    full_name="pandas.PandasCategorical",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="pandas.PandasCategorical.id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="codes",
            full_name="pandas.PandasCategorical.codes",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="categories",
            full_name="pandas.PandasCategorical.categories",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ordered",
            full_name="pandas.PandasCategorical.ordered",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=225,
    serialized_end=377,
)

_PANDASCATEGORICALDTYPE.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_PANDASCATEGORICALDTYPE.fields_by_name[
    "categories"
].message_type = proto_dot_lib_dot_python_dot_list__pb2._LIST
_PANDASCATEGORICAL.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_PANDASCATEGORICAL.fields_by_name[
    "codes"
].message_type = proto_dot_lib_dot_python_dot_list__pb2._LIST
_PANDASCATEGORICAL.fields_by_name[
    "categories"
].message_type = proto_dot_lib_dot_python_dot_list__pb2._LIST
DESCRIPTOR.message_types_by_name["PandasCategoricalDtype"] = _PANDASCATEGORICALDTYPE
DESCRIPTOR.message_types_by_name["PandasCategorical"] = _PANDASCATEGORICAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PandasCategoricalDtype = _reflection.GeneratedProtocolMessageType(
    "PandasCategoricalDtype",
    (_message.Message,),
    {
        "DESCRIPTOR": _PANDASCATEGORICALDTYPE,
        "__module__": "proto.categorical_pb2"
        # @@protoc_insertion_point(class_scope:pandas.PandasCategoricalDtype)
    },
)
_sym_db.RegisterMessage(PandasCategoricalDtype)

PandasCategorical = _reflection.GeneratedProtocolMessageType(
    "PandasCategorical",
    (_message.Message,),
    {
        "DESCRIPTOR": _PANDASCATEGORICAL,
        "__module__": "proto.categorical_pb2"
        # @@protoc_insertion_point(class_scope:pandas.PandasCategorical)
    },
)
_sym_db.RegisterMessage(PandasCategorical)


# @@protoc_insertion_point(module_scope)
