# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blockchain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='blockchain.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x62lockchain.proto\"2\n\x05Proof\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x18\n\x04type\x18\x02 \x01(\x0e\x32\n.ProofType\"\xd6\x01\n\x0b\x42lockHeader\x12\x10\n\x08prevhash\x18\x01 \x01(\x0c\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\x12\n\nstate_root\x18\x04 \x01(\x0c\x12\x19\n\x11transactions_root\x18\x05 \x01(\x0c\x12\x15\n\rreceipts_root\x18\x06 \x01(\x0c\x12\x10\n\x08gas_used\x18\x07 \x01(\x04\x12\x11\n\tgas_limit\x18\x08 \x01(\x04\x12\x15\n\x05proof\x18\t \x01(\x0b\x32\x06.Proof\x12\x10\n\x08proposer\x18\n \x01(\x0c\"&\n\x06Status\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x0e\n\x06height\x18\x02 \x01(\x04\"\xa8\x01\n\x0f\x41\x63\x63ountGasLimit\x12\x18\n\x10\x63ommon_gas_limit\x18\x01 \x01(\x04\x12\x42\n\x12specific_gas_limit\x18\x02 \x03(\x0b\x32&.AccountGasLimit.SpecificGasLimitEntry\x1a\x37\n\x15SpecificGasLimitEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"K\n\nRichStatus\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\r\n\x05nodes\x18\x03 \x03(\x0c\x12\x10\n\x08interval\x18\x04 \x01(\x04\"\x92\x01\n\x0bTransaction\x12\n\n\x02to\x18\x01 \x01(\t\x12\r\n\x05nonce\x18\x02 \x01(\t\x12\r\n\x05quota\x18\x03 \x01(\x04\x12\x19\n\x11valid_until_block\x18\x04 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12\r\n\x05value\x18\x06 \x01(\x0c\x12\x10\n\x08\x63hain_id\x18\x07 \x01(\r\x12\x0f\n\x07version\x18\x08 \x01(\r\"f\n\x15UnverifiedTransaction\x12!\n\x0btransaction\x18\x01 \x01(\x0b\x32\x0c.Transaction\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x17\n\x06\x63rypto\x18\x03 \x01(\x0e\x32\x07.Crypto\"j\n\x11SignedTransaction\x12\x34\n\x14transaction_with_sig\x18\x01 \x01(\x0b\x32\x16.UnverifiedTransaction\x12\x0f\n\x07tx_hash\x18\x02 \x01(\x0c\x12\x0e\n\x06signer\x18\x03 \x01(\x0c\"5\n\tBlockBody\x12(\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x12.SignedTransaction\"P\n\x05\x42lock\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x1c\n\x06header\x18\x02 \x01(\x0b\x32\x0c.BlockHeader\x12\x18\n\x04\x62ody\x18\x03 \x01(\x0b\x32\n.BlockBody\"<\n\x0e\x42lockWithProof\x12\x13\n\x03\x62lk\x18\x01 \x01(\x0b\x32\x06.Block\x12\x15\n\x05proof\x18\x02 \x01(\x0b\x32\x06.Proof\"4\n\x08\x42lockTxs\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x18\n\x04\x62ody\x18\x03 \x01(\x0b\x32\n.BlockBody\"3\n\tBlackList\x12\x12\n\nblack_list\x18\x01 \x03(\x0c\x12\x12\n\nclear_list\x18\x02 \x03(\x0c*2\n\tProofType\x12\x12\n\x0e\x41uthorityRound\x10\x00\x12\x08\n\x04Raft\x10\x01\x12\x07\n\x03\x42\x66t\x10\x02*\x1b\n\x06\x43rypto\x12\x08\n\x04SECP\x10\x00\x12\x07\n\x03SM2\x10\x01\x62\x06proto3')
)

_PROOFTYPE = _descriptor.EnumDescriptor(
  name='ProofType',
  full_name='ProofType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AuthorityRound', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Raft', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Bft', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1244,
  serialized_end=1294,
)
_sym_db.RegisterEnumDescriptor(_PROOFTYPE)

ProofType = enum_type_wrapper.EnumTypeWrapper(_PROOFTYPE)
_CRYPTO = _descriptor.EnumDescriptor(
  name='Crypto',
  full_name='Crypto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SECP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SM2', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1296,
  serialized_end=1323,
)
_sym_db.RegisterEnumDescriptor(_CRYPTO)

Crypto = enum_type_wrapper.EnumTypeWrapper(_CRYPTO)
AuthorityRound = 0
Raft = 1
Bft = 2
SECP = 0
SM2 = 1



_PROOF = _descriptor.Descriptor(
  name='Proof',
  full_name='Proof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='Proof.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Proof.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=70,
)


_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prevhash', full_name='BlockHeader.prevhash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='BlockHeader.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='BlockHeader.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_root', full_name='BlockHeader.state_root', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transactions_root', full_name='BlockHeader.transactions_root', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receipts_root', full_name='BlockHeader.receipts_root', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_used', full_name='BlockHeader.gas_used', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_limit', full_name='BlockHeader.gas_limit', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='BlockHeader.proof', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proposer', full_name='BlockHeader.proposer', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=287,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='Status.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='Status.height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=327,
)


_ACCOUNTGASLIMIT_SPECIFICGASLIMITENTRY = _descriptor.Descriptor(
  name='SpecificGasLimitEntry',
  full_name='AccountGasLimit.SpecificGasLimitEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='AccountGasLimit.SpecificGasLimitEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='AccountGasLimit.SpecificGasLimitEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=498,
)

_ACCOUNTGASLIMIT = _descriptor.Descriptor(
  name='AccountGasLimit',
  full_name='AccountGasLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_gas_limit', full_name='AccountGasLimit.common_gas_limit', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='specific_gas_limit', full_name='AccountGasLimit.specific_gas_limit', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACCOUNTGASLIMIT_SPECIFICGASLIMITENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=498,
)


_RICHSTATUS = _descriptor.Descriptor(
  name='RichStatus',
  full_name='RichStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='RichStatus.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='RichStatus.height', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='RichStatus.nodes', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='RichStatus.interval', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=575,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='Transaction.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='Transaction.nonce', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quota', full_name='Transaction.quota', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_until_block', full_name='Transaction.valid_until_block', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='Transaction.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Transaction.value', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='Transaction.chain_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='Transaction.version', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=724,
)


_UNVERIFIEDTRANSACTION = _descriptor.Descriptor(
  name='UnverifiedTransaction',
  full_name='UnverifiedTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction', full_name='UnverifiedTransaction.transaction', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='UnverifiedTransaction.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crypto', full_name='UnverifiedTransaction.crypto', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=726,
  serialized_end=828,
)


_SIGNEDTRANSACTION = _descriptor.Descriptor(
  name='SignedTransaction',
  full_name='SignedTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transaction_with_sig', full_name='SignedTransaction.transaction_with_sig', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='SignedTransaction.tx_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signer', full_name='SignedTransaction.signer', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=830,
  serialized_end=936,
)


_BLOCKBODY = _descriptor.Descriptor(
  name='BlockBody',
  full_name='BlockBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='BlockBody.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=938,
  serialized_end=991,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Block.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='Block.header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='Block.body', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1073,
)


_BLOCKWITHPROOF = _descriptor.Descriptor(
  name='BlockWithProof',
  full_name='BlockWithProof',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blk', full_name='BlockWithProof.blk', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='BlockWithProof.proof', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1075,
  serialized_end=1135,
)


_BLOCKTXS = _descriptor.Descriptor(
  name='BlockTxs',
  full_name='BlockTxs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='BlockTxs.height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='BlockTxs.body', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1137,
  serialized_end=1189,
)


_BLACKLIST = _descriptor.Descriptor(
  name='BlackList',
  full_name='BlackList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='black_list', full_name='BlackList.black_list', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_list', full_name='BlackList.clear_list', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1191,
  serialized_end=1242,
)

_PROOF.fields_by_name['type'].enum_type = _PROOFTYPE
_BLOCKHEADER.fields_by_name['proof'].message_type = _PROOF
_ACCOUNTGASLIMIT_SPECIFICGASLIMITENTRY.containing_type = _ACCOUNTGASLIMIT
_ACCOUNTGASLIMIT.fields_by_name['specific_gas_limit'].message_type = _ACCOUNTGASLIMIT_SPECIFICGASLIMITENTRY
_UNVERIFIEDTRANSACTION.fields_by_name['transaction'].message_type = _TRANSACTION
_UNVERIFIEDTRANSACTION.fields_by_name['crypto'].enum_type = _CRYPTO
_SIGNEDTRANSACTION.fields_by_name['transaction_with_sig'].message_type = _UNVERIFIEDTRANSACTION
_BLOCKBODY.fields_by_name['transactions'].message_type = _SIGNEDTRANSACTION
_BLOCK.fields_by_name['header'].message_type = _BLOCKHEADER
_BLOCK.fields_by_name['body'].message_type = _BLOCKBODY
_BLOCKWITHPROOF.fields_by_name['blk'].message_type = _BLOCK
_BLOCKWITHPROOF.fields_by_name['proof'].message_type = _PROOF
_BLOCKTXS.fields_by_name['body'].message_type = _BLOCKBODY
DESCRIPTOR.message_types_by_name['Proof'] = _PROOF
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['AccountGasLimit'] = _ACCOUNTGASLIMIT
DESCRIPTOR.message_types_by_name['RichStatus'] = _RICHSTATUS
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['UnverifiedTransaction'] = _UNVERIFIEDTRANSACTION
DESCRIPTOR.message_types_by_name['SignedTransaction'] = _SIGNEDTRANSACTION
DESCRIPTOR.message_types_by_name['BlockBody'] = _BLOCKBODY
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['BlockWithProof'] = _BLOCKWITHPROOF
DESCRIPTOR.message_types_by_name['BlockTxs'] = _BLOCKTXS
DESCRIPTOR.message_types_by_name['BlackList'] = _BLACKLIST
DESCRIPTOR.enum_types_by_name['ProofType'] = _PROOFTYPE
DESCRIPTOR.enum_types_by_name['Crypto'] = _CRYPTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Proof = _reflection.GeneratedProtocolMessageType('Proof', (_message.Message,), dict(
  DESCRIPTOR = _PROOF,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Proof)
  ))
_sym_db.RegisterMessage(Proof)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKHEADER,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:BlockHeader)
  ))
_sym_db.RegisterMessage(BlockHeader)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  ))
_sym_db.RegisterMessage(Status)

AccountGasLimit = _reflection.GeneratedProtocolMessageType('AccountGasLimit', (_message.Message,), dict(

  SpecificGasLimitEntry = _reflection.GeneratedProtocolMessageType('SpecificGasLimitEntry', (_message.Message,), dict(
    DESCRIPTOR = _ACCOUNTGASLIMIT_SPECIFICGASLIMITENTRY,
    __module__ = 'blockchain_pb2'
    # @@protoc_insertion_point(class_scope:AccountGasLimit.SpecificGasLimitEntry)
    ))
  ,
  DESCRIPTOR = _ACCOUNTGASLIMIT,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:AccountGasLimit)
  ))
_sym_db.RegisterMessage(AccountGasLimit)
_sym_db.RegisterMessage(AccountGasLimit.SpecificGasLimitEntry)

RichStatus = _reflection.GeneratedProtocolMessageType('RichStatus', (_message.Message,), dict(
  DESCRIPTOR = _RICHSTATUS,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:RichStatus)
  ))
_sym_db.RegisterMessage(RichStatus)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

UnverifiedTransaction = _reflection.GeneratedProtocolMessageType('UnverifiedTransaction', (_message.Message,), dict(
  DESCRIPTOR = _UNVERIFIEDTRANSACTION,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:UnverifiedTransaction)
  ))
_sym_db.RegisterMessage(UnverifiedTransaction)

SignedTransaction = _reflection.GeneratedProtocolMessageType('SignedTransaction', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDTRANSACTION,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:SignedTransaction)
  ))
_sym_db.RegisterMessage(SignedTransaction)

BlockBody = _reflection.GeneratedProtocolMessageType('BlockBody', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKBODY,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:BlockBody)
  ))
_sym_db.RegisterMessage(BlockBody)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  ))
_sym_db.RegisterMessage(Block)

BlockWithProof = _reflection.GeneratedProtocolMessageType('BlockWithProof', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKWITHPROOF,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:BlockWithProof)
  ))
_sym_db.RegisterMessage(BlockWithProof)

BlockTxs = _reflection.GeneratedProtocolMessageType('BlockTxs', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKTXS,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:BlockTxs)
  ))
_sym_db.RegisterMessage(BlockTxs)

BlackList = _reflection.GeneratedProtocolMessageType('BlackList', (_message.Message,), dict(
  DESCRIPTOR = _BLACKLIST,
  __module__ = 'blockchain_pb2'
  # @@protoc_insertion_point(class_scope:BlackList)
  ))
_sym_db.RegisterMessage(BlackList)


_ACCOUNTGASLIMIT_SPECIFICGASLIMITENTRY.has_options = True
_ACCOUNTGASLIMIT_SPECIFICGASLIMITENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
