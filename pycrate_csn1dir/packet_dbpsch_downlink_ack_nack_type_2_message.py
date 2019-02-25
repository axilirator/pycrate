# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/packet_dbpsch_downlink_ack_nack_type_2_message.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.6c Packet DBPSCH Downlink Ack/Nack Type 2
# top-level object: Packet DBPSCH Downlink Ack/Nack Type 2 message

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.egprs_channel_quality_report_ie import egprs_channel_quality_report_ie
from pycrate_csn1dir.flo_ack_nack_description_ie import flo_ack_nack_description_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

packet_dbpsch_downlink_ack_nack_type_2_message = CSN1List(name='packet_dbpsch_downlink_ack_nack_type_2_message', list=[
  CSN1Val(name='message_type', val='000010'),
  CSN1Bit(name='rb_id', bit=5),
  CSN1Ref(name='egprs_channel_quality_report', obj=egprs_channel_quality_report_ie),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='flo_ack_nack_description', obj=flo_ack_nack_description_ie)])})]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='starting_sequence_number', bit=4),
      CSN1Bit(name='received_block_bitmap', bit=8)])})])}),
  CSN1Ref(obj=padding_bits)])

