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
# * File Name : pycrate_csn1dir/packet_channel_description.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.25a Packet Channel Description
# top-level object: Packet Channel Description



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit

packet_channel_description = CSN1List(name='packet_channel_description', list=[
  CSN1Bit(name='channel_type', bit=5),
  CSN1Bit(name='tn', bit=3),
  CSN1Bit(name='tsc', bit=3),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Alt(alt={
      '0': ('', [
      CSN1Ref(obj=spare_bit),
      CSN1Bit(name='arfcn', bit=10)]),
      '1': ('', [
      CSN1Ref(obj=spare_bit),
      CSN1Bit(name='maio', bit=6),
      CSN1Bit(name='ma_number_ind'),
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(name='spare_bits', bit=2)]),
        '1': ('', [
        CSN1Bit(name='change_mark_1', bit=2)])})])})]),
    '1': ('', [
    CSN1Bit(name='maio', bit=6),
    CSN1Bit(name='hsn', bit=6)])})])

