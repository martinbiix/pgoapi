# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/pokemon_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.enums import pokemon_rarity_pb2 as pogoprotos_dot_enums_dot_pokemon__rarity__pb2
from pogoprotos.enums import pokemon_type_pb2 as pogoprotos_dot_enums_dot_pokemon__type__pb2
from pogoprotos.enums import pokemon_move_pb2 as pogoprotos_dot_enums_dot_pokemon__move__pb2
from pogoprotos.enums import pokemon_family_id_pb2 as pogoprotos_dot_enums_dot_pokemon__family__id__pb2
from pogoprotos.settings.master.pokemon import stats_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_stats__attributes__pb2
from pogoprotos.settings.master.pokemon import camera_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_camera__attributes__pb2
from pogoprotos.settings.master.pokemon import encounter_attributes_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_encounter__attributes__pb2
from pogoprotos.settings.master.pokemon import evolution_branch_pb2 as pogoprotos_dot_settings_dot_master_dot_pokemon_dot_evolution__branch__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/pokemon_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n1pogoprotos/settings/master/pokemon_settings.proto\x12\x1apogoprotos.settings.master\x1a\x1bpogoprotos/enums/form.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a%pogoprotos/enums/pokemon_rarity.proto\x1a#pogoprotos/enums/pokemon_type.proto\x1a#pogoprotos/enums/pokemon_move.proto\x1a(pogoprotos/enums/pokemon_family_id.proto\x1a\x39pogoprotos/settings/master/pokemon/stats_attributes.proto\x1a:pogoprotos/settings/master/pokemon/camera_attributes.proto\x1a=pogoprotos/settings/master/pokemon/encounter_attributes.proto\x1a\x39pogoprotos/settings/master/pokemon/evolution_branch.proto\"\x81\n\n\x0fPokemonSettings\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x13\n\x0bmodel_scale\x18\x03 \x01(\x02\x12+\n\x04type\x18\x04 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonType\x12-\n\x06type_2\x18\x05 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonType\x12\x44\n\x06\x63\x61mera\x18\x06 \x01(\x0b\x32\x34.pogoprotos.settings.master.pokemon.CameraAttributes\x12J\n\tencounter\x18\x07 \x01(\x0b\x32\x37.pogoprotos.settings.master.pokemon.EncounterAttributes\x12\x42\n\x05stats\x18\x08 \x01(\x0b\x32\x33.pogoprotos.settings.master.pokemon.StatsAttributes\x12\x32\n\x0bquick_moves\x18\t \x03(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x36\n\x0f\x63inematic_moves\x18\n \x03(\x0e\x32\x1d.pogoprotos.enums.PokemonMove\x12\x16\n\x0e\x61nimation_time\x18\x0b \x03(\x02\x12\x32\n\revolution_ids\x18\x0c \x03(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x16\n\x0e\x65volution_pips\x18\r \x01(\x05\x12/\n\x06rarity\x18\x0e \x01(\x0e\x32\x1f.pogoprotos.enums.PokemonRarity\x12\x18\n\x10pokedex_height_m\x18\x0f \x01(\x02\x12\x19\n\x11pokedex_weight_kg\x18\x10 \x01(\x02\x12\x36\n\x11parent_pokemon_id\x18\x11 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x16\n\x0eheight_std_dev\x18\x12 \x01(\x02\x12\x16\n\x0eweight_std_dev\x18\x13 \x01(\x02\x12\x1c\n\x14km_distance_to_hatch\x18\x14 \x01(\x02\x12\x34\n\tfamily_id\x18\x15 \x01(\x0e\x32!.pogoprotos.enums.PokemonFamilyId\x12\x17\n\x0f\x63\x61ndy_to_evolve\x18\x16 \x01(\x05\x12\x19\n\x11km_buddy_distance\x18\x17 \x01(\x02\x12I\n\nbuddy_size\x18\x18 \x01(\x0e\x32\x35.pogoprotos.settings.master.PokemonSettings.BuddySize\x12\x14\n\x0cmodel_height\x18\x19 \x01(\x02\x12M\n\x10\x65volution_branch\x18\x1a \x03(\x0b\x32\x33.pogoprotos.settings.master.pokemon.EvolutionBranch\x12\x16\n\x0emodel_scale_v2\x18\x1b \x01(\x02\x12$\n\x04\x66orm\x18\x1c \x01(\x0e\x32\x16.pogoprotos.enums.Form\"b\n\tBuddySize\x12\x10\n\x0c\x42UDDY_MEDIUM\x10\x00\x12\x12\n\x0e\x42UDDY_SHOULDER\x10\x01\x12\r\n\tBUDDY_BIG\x10\x02\x12\x10\n\x0c\x42UDDY_FLYING\x10\x03\x12\x0e\n\nBUDDY_BABY\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__rarity__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__type__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__move__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__family__id__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_stats__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_camera__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_encounter__attributes__pb2.DESCRIPTOR,pogoprotos_dot_settings_dot_master_dot_pokemon_dot_evolution__branch__pb2.DESCRIPTOR,])



_POKEMONSETTINGS_BUDDYSIZE = _descriptor.EnumDescriptor(
  name='BuddySize',
  full_name='pogoprotos.settings.master.PokemonSettings.BuddySize',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUDDY_MEDIUM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_SHOULDER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_BIG', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_FLYING', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_BABY', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1725,
  serialized_end=1823,
)
_sym_db.RegisterEnumDescriptor(_POKEMONSETTINGS_BUDDYSIZE)


_POKEMONSETTINGS = _descriptor.Descriptor(
  name='PokemonSettings',
  full_name='pogoprotos.settings.master.PokemonSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.settings.master.PokemonSettings.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_scale', full_name='pogoprotos.settings.master.PokemonSettings.model_scale', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.settings.master.PokemonSettings.type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_2', full_name='pogoprotos.settings.master.PokemonSettings.type_2', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera', full_name='pogoprotos.settings.master.PokemonSettings.camera', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter', full_name='pogoprotos.settings.master.PokemonSettings.encounter', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='pogoprotos.settings.master.PokemonSettings.stats', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quick_moves', full_name='pogoprotos.settings.master.PokemonSettings.quick_moves', index=7,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cinematic_moves', full_name='pogoprotos.settings.master.PokemonSettings.cinematic_moves', index=8,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='animation_time', full_name='pogoprotos.settings.master.PokemonSettings.animation_time', index=9,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_ids', full_name='pogoprotos.settings.master.PokemonSettings.evolution_ids', index=10,
      number=12, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_pips', full_name='pogoprotos.settings.master.PokemonSettings.evolution_pips', index=11,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rarity', full_name='pogoprotos.settings.master.PokemonSettings.rarity', index=12,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_height_m', full_name='pogoprotos.settings.master.PokemonSettings.pokedex_height_m', index=13,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_weight_kg', full_name='pogoprotos.settings.master.PokemonSettings.pokedex_weight_kg', index=14,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_pokemon_id', full_name='pogoprotos.settings.master.PokemonSettings.parent_pokemon_id', index=15,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_std_dev', full_name='pogoprotos.settings.master.PokemonSettings.height_std_dev', index=16,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_std_dev', full_name='pogoprotos.settings.master.PokemonSettings.weight_std_dev', index=17,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_distance_to_hatch', full_name='pogoprotos.settings.master.PokemonSettings.km_distance_to_hatch', index=18,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family_id', full_name='pogoprotos.settings.master.PokemonSettings.family_id', index=19,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy_to_evolve', full_name='pogoprotos.settings.master.PokemonSettings.candy_to_evolve', index=20,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_buddy_distance', full_name='pogoprotos.settings.master.PokemonSettings.km_buddy_distance', index=21,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buddy_size', full_name='pogoprotos.settings.master.PokemonSettings.buddy_size', index=22,
      number=24, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_height', full_name='pogoprotos.settings.master.PokemonSettings.model_height', index=23,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_branch', full_name='pogoprotos.settings.master.PokemonSettings.evolution_branch', index=24,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_scale_v2', full_name='pogoprotos.settings.master.PokemonSettings.model_scale_v2', index=25,
      number=27, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='form', full_name='pogoprotos.settings.master.PokemonSettings.form', index=26,
      number=28, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POKEMONSETTINGS_BUDDYSIZE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=1823,
)

_POKEMONSETTINGS.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
_POKEMONSETTINGS.fields_by_name['type_2'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
_POKEMONSETTINGS.fields_by_name['camera'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_camera__attributes__pb2._CAMERAATTRIBUTES
_POKEMONSETTINGS.fields_by_name['encounter'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_encounter__attributes__pb2._ENCOUNTERATTRIBUTES
_POKEMONSETTINGS.fields_by_name['stats'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_stats__attributes__pb2._STATSATTRIBUTES
_POKEMONSETTINGS.fields_by_name['quick_moves'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['cinematic_moves'].enum_type = pogoprotos_dot_enums_dot_pokemon__move__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['evolution_ids'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['rarity'].enum_type = pogoprotos_dot_enums_dot_pokemon__rarity__pb2._POKEMONRARITY
_POKEMONSETTINGS.fields_by_name['parent_pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['family_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__family__id__pb2._POKEMONFAMILYID
_POKEMONSETTINGS.fields_by_name['buddy_size'].enum_type = _POKEMONSETTINGS_BUDDYSIZE
_POKEMONSETTINGS.fields_by_name['evolution_branch'].message_type = pogoprotos_dot_settings_dot_master_dot_pokemon_dot_evolution__branch__pb2._EVOLUTIONBRANCH
_POKEMONSETTINGS.fields_by_name['form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEMONSETTINGS_BUDDYSIZE.containing_type = _POKEMONSETTINGS
DESCRIPTOR.message_types_by_name['PokemonSettings'] = _POKEMONSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonSettings = _reflection.GeneratedProtocolMessageType('PokemonSettings', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONSETTINGS,
  __module__ = 'pogoprotos.settings.master.pokemon_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.PokemonSettings)
  ))
_sym_db.RegisterMessage(PokemonSettings)


# @@protoc_insertion_point(module_scope)
