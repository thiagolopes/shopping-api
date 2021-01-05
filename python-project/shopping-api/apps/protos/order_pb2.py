# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='order.proto',
  package='order',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0border.proto\x12\x05order\"&\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndate_birth\x18\x02 \x01(\x03\"$\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\"0\n\x08\x44iscount\x12\x12\n\npercentage\x18\x01 \x01(\x02\x12\x10\n\x08\x64iscount\x18\x02 \x01(\x02\"D\n\x05Order\x12 \n\x08products\x18\x01 \x03(\x0b\x32\x0e.order.Product\x12\x19\n\x04user\x18\x02 \x01(\x0b\x32\x0b.order.User\"t\n\x11OrderWithDiscount\x1a_\n\x07Product\x12\x31\n\x07product\x18\x01 \x01(\x0b\x32 .order.OrderWithDiscount.Product\x12!\n\x08\x64iscount\x18\x02 \x01(\x0b\x32\x0f.order.Discount2S\n\x0f\x44iscountService\x12@\n\x16\x43\x61lculateOrderDiscount\x12\x0c.order.Order\x1a\x18.order.OrderWithDiscountb\x06proto3'
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='order.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='order.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_birth', full_name='order.User.date_birth', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=60,
)


_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='order.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='order.Product.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='order.Product.price', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=62,
  serialized_end=98,
)


_DISCOUNT = _descriptor.Descriptor(
  name='Discount',
  full_name='order.Discount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='percentage', full_name='order.Discount.percentage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discount', full_name='order.Discount.discount', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=100,
  serialized_end=148,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='order.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='products', full_name='order.Order.products', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='order.Order.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=150,
  serialized_end=218,
)


_ORDERWITHDISCOUNT_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='order.OrderWithDiscount.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='product', full_name='order.OrderWithDiscount.Product.product', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discount', full_name='order.OrderWithDiscount.Product.discount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=241,
  serialized_end=336,
)

_ORDERWITHDISCOUNT = _descriptor.Descriptor(
  name='OrderWithDiscount',
  full_name='order.OrderWithDiscount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_ORDERWITHDISCOUNT_PRODUCT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=336,
)

_ORDER.fields_by_name['products'].message_type = _PRODUCT
_ORDER.fields_by_name['user'].message_type = _USER
_ORDERWITHDISCOUNT_PRODUCT.fields_by_name['product'].message_type = _ORDERWITHDISCOUNT_PRODUCT
_ORDERWITHDISCOUNT_PRODUCT.fields_by_name['discount'].message_type = _DISCOUNT
_ORDERWITHDISCOUNT_PRODUCT.containing_type = _ORDERWITHDISCOUNT
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
DESCRIPTOR.message_types_by_name['Discount'] = _DISCOUNT
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['OrderWithDiscount'] = _ORDERWITHDISCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.User)
  })
_sym_db.RegisterMessage(User)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.Product)
  })
_sym_db.RegisterMessage(Product)

Discount = _reflection.GeneratedProtocolMessageType('Discount', (_message.Message,), {
  'DESCRIPTOR' : _DISCOUNT,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.Discount)
  })
_sym_db.RegisterMessage(Discount)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.Order)
  })
_sym_db.RegisterMessage(Order)

OrderWithDiscount = _reflection.GeneratedProtocolMessageType('OrderWithDiscount', (_message.Message,), {

  'Product' : _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
    'DESCRIPTOR' : _ORDERWITHDISCOUNT_PRODUCT,
    '__module__' : 'order_pb2'
    # @@protoc_insertion_point(class_scope:order.OrderWithDiscount.Product)
    })
  ,
  'DESCRIPTOR' : _ORDERWITHDISCOUNT,
  '__module__' : 'order_pb2'
  # @@protoc_insertion_point(class_scope:order.OrderWithDiscount)
  })
_sym_db.RegisterMessage(OrderWithDiscount)
_sym_db.RegisterMessage(OrderWithDiscount.Product)



_DISCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='DiscountService',
  full_name='order.DiscountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=338,
  serialized_end=421,
  methods=[
  _descriptor.MethodDescriptor(
    name='CalculateOrderDiscount',
    full_name='order.DiscountService.CalculateOrderDiscount',
    index=0,
    containing_service=None,
    input_type=_ORDER,
    output_type=_ORDERWITHDISCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOUNTSERVICE)

DESCRIPTOR.services_by_name['DiscountService'] = _DISCOUNTSERVICE

# @@protoc_insertion_point(module_scope)