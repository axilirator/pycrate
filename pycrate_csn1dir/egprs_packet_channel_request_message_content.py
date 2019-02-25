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
# * File Name : pycrate_csn1dir/egprs_packet_channel_request_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.5a EGPRS Packet Channel Request
# top-level object: EGPRS Packet channel request message content



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

egprs_packet_channel_request_message_content = CSN1Alt(name='egprs_packet_channel_request_message_content', alt={
  '0': ('one_phase_access_request', [
  CSN1Bit(name='multislotclass', bit=5),
  CSN1Bit(name='priority', bit=2),
  CSN1Bit(name='randombits', bit=3)]),
  '100': ('short_access_request', [
  CSN1Bit(name='numberofblocks', bit=3),
  CSN1Bit(name='priority', bit=2),
  CSN1Bit(name='randombits', bit=3)]),
  '101': ('one_phase_access_request_by_reduced_latency_ms', [
  CSN1Bit(name='multislotclassgroup', bit=3),
  CSN1Bit(name='priority', bit=2),
  CSN1Bit(name='randombits', bit=3)]),
  '110000': ('two_phase_access_request', [
  CSN1Bit(name='priority', bit=2),
  CSN1Bit(name='randombits', bit=3)]),
  '110011': ('signalling', [
  CSN1Bit(name='randombits', bit=5)]),
  '110101': ('one_phase_access_request_in_rlc_unack_mode', [
  CSN1Bit(name='randombits', bit=5)]),
  '110110': ('dedicated_channel_request', [
  CSN1Bit(name='randombits', bit=5)]),
  '110111': ('emergency_call', [
  CSN1Bit(name='randombits', bit=5)]),
  '111000': ('two_phase_access_request_by_ipa_capable_ms', [
  CSN1Bit(name='priority', bit=2),
  CSN1Bit(name='randombits', bit=3)]),
  '111001': ('signalling_by_ipa_capable_ms', [
  CSN1Bit(name='randombits', bit=5)])})

egprs_packet_channel_request_message_content_for_peo_one_phase_access_request = CSN1List(name='egprs_packet_channel_request_message_content_for_peo_one_phase_access_request', list=[
  CSN1Bit(name='access_cause', bit=2),
  CSN1Bit(name='peo_priority'),
  CSN1Bit(name='random_bits', bit=3),
  CSN1Bit(name='egprs_capability'),
  CSN1Bit(name='spare')])

