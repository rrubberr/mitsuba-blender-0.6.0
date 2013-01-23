# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from .. import MitsubaAddon

from extensions_framework import declarative_property_group
from extensions_framework import util as efutil

def MediumParameter(attr, name):
	return [
		{
			'attr': '%s_medium' % attr,
			'type': 'string',
			'name': '%s_medium' % attr,
			'description': '%s; blank means vacuum' % name,
			'save_in_preset': True
		},
		{
			'type': 'prop_search',
			'attr': attr,
			'src': lambda s,c: s.scene.mitsuba_media,
			'src_attr': 'media',
			'trg': lambda s,c: c.mitsuba_camera,
			'trg_attr': '%s_medium' % attr,
			'name': name
		}
	]


@MitsubaAddon.addon_register_class
class mitsuba_camera(declarative_property_group):
	ef_attach_to = ['Camera']

	controls = [
		'film',
		'pixelFormat',
		'exposure',
		'banner',
		'exterior'
	]

	visibility = {
		'exposure': { 'film': 'ldrfilm'},
	}
	properties = [
		{
			'type': 'bool',
			'attr': 'use_film',
			'name': 'Camera Film',
			'description': 'Override global settings',
			'default': False,
			'save_in_preset': True
		},
		{
			'type': 'enum',
			'attr': 'film',
			'name': 'Output format',
			'description': 'Select output file format to override Scene global setting',
			'items': [
				('hdrfilm', 'EXR', 'hdrfilm'),
				('ldrfilm', 'PNG', 'ldrfilm')
			],
			'default': 'ldrfilm',
			'save_in_preset': True
		},
		{
			'type': 'enum',
			'attr': 'pixelFormat',
			'name': 'Pixel Format',
			'description': 'Select Pixel Format to override Scene global setting',
			'items': [
				('rgb', 'RGB', 'rgb'),
				('rgba', 'RGBA', 'rgba'),
				('luminance', 'Luminance', 'luminance'),
				('luminanceAlpha', 'Luminance Alpha', 'luminanceAlpha')
			],
			'default': 'rgb',
			'save_in_preset': True
		},
		{
			'type': 'bool',
			'attr': 'banner',
			'name': 'Mitsuba logo',
			'description': 'Render will containg small Mitsuba logo',
			'default': True,
			'save_in_preset': True
		},
		{
			'attr': 'exposure',
			'type': 'float',
			'description' : 'Reinhard tonemapping exposure',
			'name' : 'Film exposure',
			'default' : 1.0,
			'min': -10.0,
			'max': 10.0,
			'save_in_preset': True
		},
		{
			'type': 'bool',
			'attr': 'useDOF',
			'name': 'Use camera DOF',
			'description': 'Camera DOF',
			'default': False,
			'save_in_preset': True
		},
		{
			'attr': 'apertureRadius',
			'type': 'float',
			'description' : 'DOF Aperture Radius',
			'name' : 'Aperture Radius',
			'default' : 0.03,
			'min': 0.01,
			'max': 1.0,
			'save_in_preset': True
		}
	] + MediumParameter('exterior', 'Exterior medium')
