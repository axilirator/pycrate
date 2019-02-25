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
# * File Name : pycrate_csn1dir/multiple_tbf_downlink_assignment_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.7a Multiple TBF Downlink Assignment
# top-level object: Multiple TBF Downlink Assignment message content

# external references
from pycrate_csn1dir.starting_frame_number_description_ie import starting_frame_number_description_ie
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.tlli_g_rnti_ie import tlli_g_rnti_ie
from pycrate_csn1dir.frequency_parameters_ie import frequency_parameters_ie
from pycrate_csn1dir.power_control_parameters_ie import power_control_parameters_ie
from pycrate_csn1dir.egprs_level_ie import egprs_level_ie
from pycrate_csn1dir.packet_timing_advance_ie import packet_timing_advance_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.dual_carrier_frequency_parameters_ie import dual_carrier_frequency_parameters_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

downlink_tbf_assignment_struct = CSN1List(name='downlink_tbf_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='rb_id', bit=5)]),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7),
    CSN1Bit(name='rlc_mode')])}),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Bit(name='control_ack'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='hfn_lsb')])})])

assignment_info_struct = CSN1List(name='assignment_info_struct', list=[
  CSN1Bit(name='assignment_type', bit=2),
  CSN1Bit(name='carrier_id')])

multiple_downlink_tbf_assignment_struct = CSN1List(name='multiple_downlink_tbf_assignment_struct', list=[
  CSN1Bit(name='timeslot_allocation', bit=8),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_struct)]),
  CSN1Val(name='', val='0')])

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

multiple_tbf_downlink_assignment_message_content = CSN1List(name='multiple_tbf_downlink_assignment_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='persistence_level', bit=16)])}),
  CSN1List(list=[
    CSN1Alt(alt={
      '0': ('', [
      CSN1Ref(name='global_tfi', obj=global_tfi_ie)]),
      '10': ('', [
      CSN1List(list=[
        CSN1Ref(name='tlli_g_rnti', obj=tlli_g_rnti_ie),
        CSN1Bit(name='g_rnti_extension', bit=4)])])}),
    CSN1Alt(alt={
      '0': ('', [
      CSN1List(trunc=True, list=[
        CSN1Ref(name='packet_timing_advance', obj=packet_timing_advance_ie),
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Bit(name='p0', bit=4),
          CSN1Bit(name='pr_mode')])}),
        CSN1List(list=[
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='frequency_parameters', obj=frequency_parameters_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='power_control_parameters', obj=power_control_parameters_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='tbf_starting_time', obj=starting_frame_number_description_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
            CSN1Bit(name='link_quality_measurement_mode', bit=2),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='bep_period2', bit=4)])})])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='uplink_control_timeslot', bit=3)])}),
          CSN1List(num=-1, list=[
            CSN1Val(name='', val='1'),
            CSN1Ref(name='multiple_downlink_tbf_assignment', obj=multiple_downlink_tbf_assignment_struct)]),
          CSN1Val(name='', val='0'),
          CSN1Alt(alt={
            '0': ('', [
            CSN1Bit(bit=-1)]),
            '1': ('', [
            CSN1List(list=[
              CSN1Val(name='', val='1'),
              CSN1Alt(num=-1, alt={
                '0': ('', []),
                '1': ('', [
                CSN1Bit(name='npm_transfer_time', bit=5)])}),
              CSN1Val(name='', val='0'),
              CSN1Ref(obj=padding_bits)])]),
            None: ('', [])})])])]),
      '1': ('', [
      CSN1List(list=[
        CSN1Val(name='', val='00'),
        CSN1List(trunc=True, list=[
          CSN1Ref(name='packet_timing_advance', obj=packet_timing_advance_ie),
          CSN1Ref(name='assignment_info', obj=assignment_info_struct),
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
          CSN1List(list=[
            CSN1Alt(alt={
              '00': ('', []),
              '01': ('', [
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='frequency_parameters_c1', obj=frequency_parameters_ie)])}),
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='frequency_parameters_c2', obj=frequency_parameters_ie)])})]),
              '10': ('', [
              CSN1Ref(name='dual_carrier_frequency_parameters', obj=dual_carrier_frequency_parameters_ie)])}),
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
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
              CSN1Bit(name='link_quality_measurement_mode', bit=2),
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Bit(name='bep_period2', bit=4)])})])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='uplink_control_timeslot_c1', bit=3)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='uplink_control_timeslot_c2', bit=3)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='fanr'),
              CSN1List(num=-1, list=[
                CSN1Val(name='', val='1'),
                CSN1Ref(name='btti_multiple_downlink_assignment', obj=btti_multiple_downlink_assignment_struct)]),
              CSN1Val(name='', val='0')])}),
            CSN1Alt(alt={
              '0': ('', []),
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
              CSN1List(num=-1, list=[
                CSN1Val(name='', val='1'),
                CSN1Bit(name='indication_of_upper_layer_pdu_start_for_rlc_um')]),
              CSN1Val(name='', val='0'),
              CSN1Ref(obj=padding_bits)]),
              None: ('', [])})])])])])})])])

