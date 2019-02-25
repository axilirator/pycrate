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
# * File Name : pycrate_csn1dir/mprach_description_ie.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 12.38 MPRACH description
# top-level object: MPRACH description IE

# external references
from pycrate_csn1dir.frequency_parameters_ie import frequency_parameters_ie
from pycrate_csn1dir.mprach_control_parameters_ie import mprach_control_parameters_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

mprach_description_ie = CSN1List(name='mprach_description_ie', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='frequency_parameters', obj=frequency_parameters_ie)])}),
  CSN1Bit(name='mprach_timeslot_number', bit=3),
  CSN1Bit(name='usf', bit=3),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='mprach_control_parameters', obj=mprach_control_parameters_ie)])})])

