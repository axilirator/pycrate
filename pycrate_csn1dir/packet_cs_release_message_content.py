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
# * File Name : pycrate_csn1dir/packet_cs_release_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.37 Packet CS Release Indication
# top-level object: Packet CS Release message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.global_packet_timing_advance_ie import global_packet_timing_advance_ie
from pycrate_csn1dir.frequency_parameters_ie import frequency_parameters_ie
from pycrate_csn1dir.egprs_mode_2_ie import egprs_mode_2_ie
from pycrate_csn1dir.egprs_window_size_ie import egprs_window_size_ie
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.dual_carrier_frequency_parameters_ie import dual_carrier_frequency_parameters_ie
from pycrate_csn1dir.egprs_modulation_and_coding_scheme_ie import egprs_modulation_and_coding_scheme_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

downlink_tbf_assignment_struct = CSN1List(name='downlink_tbf_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7)])}),
  CSN1Bit(name='downlink_rlc_mode'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot', bit=3)])}),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Bit(name='control_ack'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])})])

rlc_entity_struct = CSN1List(name='rlc_entity_struct', list=[
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Bit(name='rlc_mode'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='pfi', bit=7)])

assignment_info_struct = CSN1List(name='assignment_info_struct', list=[
  CSN1Bit(name='assignment_type', bit=2),
  CSN1Bit(name='carrier_id')])

timeslot_description_struct = CSN1Alt(name='timeslot_description_struct', alt={
  '0': ('', [
  CSN1Bit(name='ms_timeslot_allocation', bit=8)]),
  '1': ('', [
  CSN1Bit(name='alpha', bit=4),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn0', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn1', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn2', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn3', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn4', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn5', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn6', bit=5)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='gamma_tn7', bit=5)])})])})

multiple_downlink_assignment_struct = CSN1List(name='multiple_downlink_assignment_struct', list=[
  CSN1Bit(name='timeslot_allocation', bit=8),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='uplink_control_timeslot', bit=3)])}),
  CSN1List(num=-1, list=[
    CSN1Val(name='', val='1'),
    CSN1Ref(name='downlink_tbf_assignment', obj=downlink_tbf_assignment_struct)]),
  CSN1Val(name='', val='0')])

uplink_tbf_assignment_struct = CSN1List(name='uplink_tbf_assignment_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='pfi', bit=7)])}),
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='channel_coding_command', bit=2)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
  CSN1Bit(name='usf_granularity'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tbf_timeslot_allocation', bit=('# unprocessed: (N)', lambda: 0))])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='usf_allocation', bit=3)]),
    '1': ('', [
    CSN1Bit(name='usf_allocation', bit=3),
    CSN1Alt(num=('# unprocessed: (M-1)', lambda: 0), alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='usf_allocation', bit=3)])})])})])

additional_pfcs_struct = CSN1List(name='additional_pfcs_struct', list=[
  CSN1Bit(name='tfi_assignment', bit=5),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='npm_transfer_time', bit=5)])}),
  CSN1Bit(name='pfi', bit=7)])

multiple_uplink_assignment_struct = CSN1List(name='multiple_uplink_assignment_struct', list=[
  CSN1Bit(name='extended_dynamic_allocation'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0', bit=4),
    CSN1Bit(name='pr_mode')])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Ref(name='global_timeslot_description', obj=timeslot_description_struct),
    CSN1List(num=-1, list=[
      CSN1Val(name='', val='1'),
      CSN1Ref(name='uplink_tbf_assignment', obj=uplink_tbf_assignment_struct)]),
    CSN1Val(name='', val='0')])})])

packet_cs_release_message_content = CSN1List(name='packet_cs_release_message_content', list=[
  CSN1Bit(name='page_mode', bit=2),
  CSN1List(list=[
    CSN1Ref(name='global_tfi', obj=global_tfi_ie),
    CSN1Bit(name='enhanced_dtm_cs_release_indication'),
    CSN1Ref(name='global_packet_timing_advance', obj=global_packet_timing_advance_ie),
    CSN1Alt(alt={
      '00': ('', [
      CSN1Ref(obj=padding_bits)]),
      '01': ('', [
      CSN1Ref(obj=padding_bits)]),
      '10': ('', [
      CSN1Alt(alt={
        '0': ('', [
        CSN1List(list=[
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Ref(name='frequency_parameters', obj=frequency_parameters_ie)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1List(num=-1, list=[
              CSN1Val(name='', val='1'),
              CSN1Ref(name='multiple_downlink_assignment', obj=multiple_downlink_assignment_struct)]),
            CSN1Val(name='', val='0')])}),
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='channel_coding_command', bit=2)])}),
            CSN1Ref(name='multiple_uplink_assignment', obj=multiple_uplink_assignment_struct)])}),
          CSN1Alt(alt={
            '0': ('', [
            CSN1Bit(bit=-1)]),
            '1': ('', [
            CSN1Bit(name='primary_tsc_set'),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='secondary_dl_tsc_set'),
              CSN1Bit(name='secondary_dl_tsc_value', bit=3)])}),
            CSN1Ref(obj=padding_bits)]),
            None: ('', [])})])]),
        '1': ('', [
        CSN1Alt(alt={
          '00': ('', [
          CSN1List(list=[
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Ref(name='frequency_parameters', obj=frequency_parameters_ie)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='bep_period2', bit=4)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='downlink_egprs_window_size', obj=egprs_window_size_ie)])}),
              CSN1Bit(name='link_quality_measurement_mode', bit=2),
              CSN1List(num=-1, list=[
                CSN1Val(name='', val='1'),
                CSN1Ref(name='multiple_downlink_assignment', obj=multiple_downlink_assignment_struct)]),
              CSN1Val(name='', val='0')])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='egprs_channel_coding_command', obj=egprs_modulation_and_coding_scheme_ie)])}),
              CSN1Bit(name='resegment'),
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='uplink_egprs_window_size', obj=egprs_window_size_ie)])}),
              CSN1Ref(name='multiple_uplink_assignment', obj=multiple_uplink_assignment_struct)])}),
            CSN1Alt(alt={
              '0': ('', [
              CSN1Bit(bit=-1)]),
              '1': ('', [
              CSN1List(num=-1, list=[
                CSN1Val(name='', val='1'),
                CSN1Alt(alt={
                  '0': ('', []),
                  '1': ('', [
                  CSN1Bit(name='npm_transfer_time', bit=5)])})]),
              CSN1Val(name='', val='0'),
              CSN1Alt(alt={
                '0': ('', [
                CSN1Bit(bit=-1)]),
                '1': ('', [
                CSN1Bit(name='enhanced_flexible_timeslot_assignment'),
                CSN1Alt(alt={
                  '0': ('', []),
                  '1': ('', [
                  CSN1Ref(name='downlink_rlc_entity_2', obj=rlc_entity_struct),
                  CSN1Alt(alt={
                    '0': ('', []),
                    '1': ('', [
                    CSN1Ref(name='downlink_rlc_entity_3', obj=rlc_entity_struct)])})])}),
                CSN1Alt(alt={
                  '0': ('', []),
                  '1': ('', [
                  CSN1Ref(name='uplink_rlc_entity_2', obj=rlc_entity_struct),
                  CSN1Alt(alt={
                    '0': ('', []),
                    '1': ('', [
                    CSN1Ref(name='uplink_rlc_entity_3', obj=rlc_entity_struct)])})])}),
                CSN1Alt(alt={
                  '0': ('', [
                  CSN1Bit(bit=-1)]),
                  '1': ('', [
                  CSN1Alt(alt={
                    '0': ('', []),
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
                    CSN1Val(name='', val='0')])}),
                  CSN1Alt(alt={
                    '0': ('', []),
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
                    CSN1Val(name='', val='0')])}),
                  CSN1Alt(alt={
                    '0': ('', [
                    CSN1Bit(bit=-1)]),
                    '1': ('', [
                    CSN1Bit(name='primary_tsc_set'),
                    CSN1Alt(alt={
                      '0': ('', []),
                      '1': ('', [
                      CSN1Bit(name='secondary_dl_tsc_set'),
                      CSN1Bit(name='secondary_dl_tsc_value', bit=3)])}),
                    CSN1Ref(obj=padding_bits)]),
                    None: ('', [])})]),
                  None: ('', [])})]),
                None: ('', [])})]),
              None: ('', [])})])]),
          '01': ('', [
          CSN1List(list=[
            CSN1Ref(name='assignment_info', obj=assignment_info_struct),
            CSN1Alt(alt={
              '00': ('', []),
              '01': ('', [
              CSN1Ref(name='frequency_parameters_c1', obj=frequency_parameters_ie),
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='frequency_parameters_c2', obj=frequency_parameters_ie)])})]),
              '10': ('', [
              CSN1Ref(name='dual_carrier_frequency_parameters', obj=dual_carrier_frequency_parameters_ie)])}),
            CSN1Alt(alt={
              '0': ('', []),
              '1': ('', [
              CSN1Bit(name='packet_extended_timing_advance', bit=2)])}),
            CSN1Ref(name='egprs_mode', obj=egprs_mode_2_ie),
            CSN1Alt(alt={
              '0': ('', [
              CSN1Bit(bit=-1)]),
              '1': ('', [
              CSN1Bit(name='enhanced_flexible_timeslot_assignment'),
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='downlink_rlc_entity_2', obj=rlc_entity_struct),
                CSN1Alt(alt={
                  '0': ('', []),
                  '1': ('', [
                  CSN1Ref(name='downlink_rlc_entity_3', obj=rlc_entity_struct)])})])}),
              CSN1Alt(alt={
                '0': ('', []),
                '1': ('', [
                CSN1Ref(name='uplink_rlc_entity_2', obj=rlc_entity_struct),
                CSN1Alt(alt={
                  '0': ('', []),
                  '1': ('', [
                  CSN1Ref(name='uplink_rlc_entity_3', obj=rlc_entity_struct)])})])}),
              CSN1Alt(alt={
                '0': ('', [
                CSN1Bit(bit=-1)]),
                '1': ('', [
                CSN1Alt(alt={
                  '0': ('', []),
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
                  CSN1Val(name='', val='0')])}),
                CSN1Alt(alt={
                  '0': ('', []),
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
                  CSN1Val(name='', val='0')])}),
                CSN1Alt(alt={
                  '0': ('', [
                  CSN1Bit(bit=-1)]),
                  '1': ('', [
                  CSN1Bit(name='egprs_packet_downlink_ack_nack_type_3_support'),
                  CSN1Alt(alt={
                    '0': ('', [
                    CSN1Bit(bit=-1)]),
                    '1': ('', [
                    CSN1Bit(name='primary_tsc_set'),
                    CSN1Alt(alt={
                      '0': ('', []),
                      '1': ('', [
                      CSN1Bit(name='secondary_dl_tsc_set'),
                      CSN1Bit(name='secondary_dl_tsc_value', bit=3)])}),
                    CSN1Ref(obj=padding_bits)]),
                    None: ('', [])})]),
                  None: ('', [])})]),
                None: ('', [])})]),
              None: ('', [])})])])})])})]),
      '11': ('', [
      CSN1Ref(obj=padding_bits)])})])])

