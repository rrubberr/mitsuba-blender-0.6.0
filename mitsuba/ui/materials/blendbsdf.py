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

import bpy, bl_ui
from ... import MitsubaAddon

from ...ui.materials import mitsuba_material_sub

@MitsubaAddon.addon_register_class
class ui_material_blendbsdf(mitsuba_material_sub, bpy.types.Panel):
	bl_label = 'Mitsuba Blend Material'

	MTS_COMPAT = {'blendbsdf'}

	display_property_groups = [
		( ('material', 'mitsuba_material'), 'mitsuba_mat_blendbsdf' )
	]

	def draw(self, context):
		super().draw(context)

		mat = bl_ui.properties_material.active_node_mat(context.material).mitsuba_material.mitsuba_mat_blendbsdf
		missing = False
		selfRef = False

		for i in range(1,2):
			name = getattr(mat, "mat%i_name" % i)
			if name == '':
				missing = True
			elif name == context.material.name:
				selfRef = True
		if selfRef:
			row = self.layout.row()
			row.label("Warning: self references not allowed!")
		if missing:
			row = self.layout.row()
			row.label("Warning: missing material reference!")
