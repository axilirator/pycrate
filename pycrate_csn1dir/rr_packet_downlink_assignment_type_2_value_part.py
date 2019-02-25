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
# * File Name : pycrate_csn1dir/rr_packet_downlink_assignment_type_2_value_part.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 10.5.2.25e RR Packet Downlink Assignment Type 2
# top-level object: RR Packet Downlink Assignment Type 2 value part

# external references
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.power_control_parameters_ie import power_control_parameters_ie
from pycrate_csn1dir.egprs_level_ie import egprs_level_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit

additional_pfcs_struct = CSN1List(name='additional_pfcs_struct', list=[
  CSN1Bit(name='downlink_tfi_assignment', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Bit(name='pfi', bit=7)])

rlc_entity_struct = CSN1List(name='rlc_entity_struct', list=[
  CSN1Bit(name='downlink_tfi_assignment', bit=5),
  CSN1Bit(name='rlc_mode'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='pfi', bit=7)])

downlink_tbf_assignment_2_struct = CSN1List(name='downlink_tbf_assignment_2_struct', list=[
  CSN1Bit(name='pfi', bit=7),
  CSN1Bit(name='rlc_mode'),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Bit(name='control_ack'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Bit(name='event_based_fanr'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])})])

rtti_multiple_downlink_assignment_dc_struct = CSN1List(name='rtti_multiple_downlink_assignment_dc_struct', list=[
  CSN1Bit(name='rtti_downlink_pdch_pair_assignment_dc', bit=8),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_2_struct)]),
  CSN1Val(name='', val='0')])

btti_multiple_downlink_assignment_struct = CSN1List(name='btti_multiple_downlink_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot', bit=3)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='timeslot_allocation_c1', bit=8)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='timeslot_allocation_c2', bit=8)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_2_struct)]),
  CSN1Val(name='', val='0')])

rtti_multiple_downlink_assignment_sc_struct = CSN1List(name='rtti_multiple_downlink_assignment_sc_struct', list=[
  CSN1Bit(name='rtti_downlink_pdch_pair_assignment_sc', bit=4),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_2_struct)]),
  CSN1Val(name='', val='0')])

rr_packet_downlink_assignment_type_2_value_part = CSN1List(name='rr_packet_downlink_assignment_type_2_value_part', list=[
  CSN1Bit(name='rlc_mode'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0_c1', bit=4),
    CSN1Bit(name='pr_mode_c1'),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='p0_c2', bit=4),
      CSN1Bit(name='pr_mode_c2')])})])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='power_control_parameters_c1', obj=power_control_parameters_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='power_control_parameters_c2', obj=power_control_parameters_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='downlink_tfi_assignment', bit=5)])}),
  CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie),
  CSN1Bit(name='link_quality_measurement_mode', bit=2),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='fanr'),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='btti_multiple_downlink_assignment', obj=btti_multiple_downlink_assignment_struct)]),
    CSN1Val(name='', val='0')]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', [
      CSN1Alt(alt={
        '00': ('', []),
        '01': ('', []),
        '10': ('', [
        CSN1Bit(name='downlink_pdch_pairs_c1', bit=8),
        CSN1Bit(name='uplink_pdch_pairs_c1', bit=8)])}),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='rtti_multiple_downlink_assignment_sc', obj=rtti_multiple_downlink_assignment_sc_struct)]),
      CSN1Val(name='', val='0')]),
      '1': ('', [
      CSN1Alt(alt={
        '00': ('', []),
        '01': ('', []),
        '10': ('', [
        CSN1Bit(name='downlink_pdch_pairs_c1', bit=8),
        CSN1Bit(name='downlink_pdch_pairs_c2', bit=8),
        CSN1Bit(name='uplink_pdch_pairs_c1', bit=8),
        CSN1Bit(name='uplink_pdch_pairs_c2', bit=8)])}),
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Ref(name='rtti_multiple_downlink_assignment_dc', obj=rtti_multiple_downlink_assignment_dc_struct)]),
      CSN1Val(name='', val='0')])})])}),
  CSN1Ref(name='downlink_egprs_level', obj=egprs_level_ie),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(bit=-1)]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Bit(name='measurement_control_e_utran'),
        CSN1Bit(name='e_utran_frequency_index', bit=3),
        CSN1List(num=-1, list=[
          CSN1Val(name='', val='1'),
          CSN1Bit(name='e_utran_frequency_index', bit=3)]),
        CSN1Val(name='', val='0')]),
      CSN1Val(name='', val='0')])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1List(num=-1, list=[
        CSN1Val(name='', val='1'),
        CSN1Bit(name='measurement_control_utran'),
        CSN1Bit(name='utran_frequency_index', bit=5),
        CSN1List(num=-1, list=[
          CSN1Val(name='', val='1'),
          CSN1Bit(name='utran_frequency_index', bit=5)]),
        CSN1Val(name='', val='0')]),
      CSN1Val(name='', val='0')])}),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(bit=-1)]),
      '1': ('', [
      CSN1Alt(alt={
        '0': ('', []),
        '1': ('', [
        CSN1Ref(name='rlc_entity_2', obj=rlc_entity_struct),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='rlc_entity_3', obj=rlc_entity_struct)])})])}),
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(bit=-1)]),
        '1': ('', [
        CSN1List(num=-1, list=[
          CSN1Val(name='', val='1'),
          CSN1Ref(name='emsr_additional_pfcs_1', obj=additional_pfcs_struct)]),
        CSN1Val(name='', val='0'),
        CSN1List(num=-1, list=[
          CSN1Val(name='', val='1'),
          CSN1Ref(name='emsr_additional_pfcs_2', obj=additional_pfcs_struct)]),
        CSN1Val(name='', val='0'),
        CSN1List(num=-1, list=[
          CSN1Val(name='', val='1'),
          CSN1Ref(name='emsr_additional_pfcs_3', obj=additional_pfcs_struct)]),
        CSN1Val(name='', val='0'),
        CSN1Alt(alt={
          '0': ('', [
          CSN1Bit(bit=-1)]),
          '1': ('', [
          CSN1Bit(name='egprs_packet_downlink_ack_nack_type_3_support'),
          CSN1Ref(obj=spare_bit, num=-1)]),
          None: ('', [])})]),
        None: ('', [])})]),
      None: ('', [])})]),
    None: ('', [])})])

