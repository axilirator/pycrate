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
# * File Name : pycrate_csn1dir/mbms_neighbouring_cell_information_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.40 MBMS Neighbouring Cell Information
# top-level object: MBMS Neighbouring Cell Information message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.mprach_control_parameters_ie import mprach_control_parameters_ie
from pycrate_csn1dir.mbms_in_band_signalling_indicator_ie import mbms_in_band_signalling_indicator_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

mbms_frequency_list_struct = CSN1List(name='mbms_frequency_list_struct', list=[
  CSN1Bit(name='freq_list_number', bit=2),
  CSN1Bit(name='length_of_frequency_list_contents', bit=4),
  CSN1Bit(name='frequency_list_contents', bit=8, num=([1], lambda x: x + 3))])

pbcch_information_struct = CSN1List(name='pbcch_information_struct', list=[
  CSN1Bit(name='pb', bit=4),
  CSN1Bit(name='tsc', bit=3),
  CSN1Bit(name='tn', bit=3),
  CSN1Alt(alt={
    '00': ('', []),
    '01': ('', [
    CSN1Bit(name='arfcn', bit=10)]),
    '1': ('', [
    CSN1Bit(name='length_of_neighbour_mbms_bearer_identity', bit=3),
    CSN1Bit(name='neighbour_mbms_bearer_identity', bit=([1], lambda x: x))])})])

mbms_p_t_m_frequency_parameters_struct = CSN1List(name='mbms_p_t_m_frequency_parameters_struct', list=[
  CSN1Bit(name='tsc', bit=3),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='arfcn', bit=10)]),
    '1': ('', [
    CSN1Bit(name='maio', bit=6),
    CSN1Bit(name='hsn', bit=6),
    CSN1Bit(name='freq_list_number', bit=2)])})])

mbms_neighbouring_cell_information_message_content = CSN1List(name='mbms_neighbouring_cell_information_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Bit(name='neighbour_cell_index', bit=7),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='bsic', bit=6)])}),
    CSN1Bit(name='mbms_ptm_change_mark', bit=2),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Bit(name='length_of_mbms_bearer_identity', bit=3),
      CSN1Bit(name='mbms_bearer_identity', bit=([1], lambda x: x)),
      CSN1Bit(name='absence_cause', bit=2)]),
    CSN1Val(name='', val='0'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='mbms_frequency_list', obj=mbms_frequency_list_struct)]),
    CSN1Val(name='', val='0'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='mbms_p_t_m_frequency_parameters', obj=mbms_p_t_m_frequency_parameters_struct),
      CSN1Bit(name='downlink_timeslot_allocation', bit=8),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Bit(name='length_of_serving_mbms_bearer_identity', bit=3),
        CSN1Bit(name='serving_mbms_bearer_identity', bit=([1], lambda x: x)),
        CSN1Bit(name='length_of_neighbour_mbms_bearer_identity', bit=3),
        CSN1Bit(name='neighbour_mbms_bearer_identity', bit=([3], lambda x: x)),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='downlink_timeslot_allocation', bit=8)])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='timeslot_allocation_uplink_feedback_channel', bit=3)])}),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='mbms_radio_bearer_starting_time', bit=16)])}),
        CSN1Ref(name='mbms_in_band_signalling_indicator', obj=mbms_in_band_signalling_indicator_ie),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='npm_transfer_time', bit=5)])})]),
      CSN1Val(name='', val='0')]),
    CSN1Val(name='', val='0'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='pbcch_information', obj=pbcch_information_struct)])})]),
  CSN1Val(name='', val='0'),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(bit=-1)]),
    '1': ('', [
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Bit(name='usf', bit=3),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='mprach_control_parameters', obj=mprach_control_parameters_ie)])})])})]),
    CSN1Val(name='', val='0')]),
    None: ('', [])}),
  CSN1Ref(obj=padding_bits)])

