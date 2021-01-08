###################################################
# header_common.py
# This file contains common declarations.
# DO NOT EDIT THIS FILE!
###################################################

#client events
multiplayer_event_set_item_selection                          = 0
multiplayer_event_set_bot_selection                           = 1
multiplayer_event_admin_start_map                             = 2
multiplayer_event_admin_set_max_num_players                   = 3
multiplayer_event_admin_set_num_bots_in_team                  = 4
multiplayer_event_admin_set_friendly_fire                     = 5
multiplayer_event_admin_set_ghost_mode                        = 6
multiplayer_event_admin_set_control_block_dir                 = 7
multiplayer_event_admin_set_add_to_servers_list               = 8
multiplayer_event_admin_set_respawn_period                    = 9
multiplayer_event_admin_set_game_max_minutes                  = 10
multiplayer_event_admin_set_round_max_seconds                 = 11
multiplayer_event_admin_set_game_max_points                   = 12
multiplayer_event_admin_set_point_gained_from_flags           = 13
multiplayer_event_admin_set_point_gained_from_capturing_flag  = 14
multiplayer_event_admin_set_server_name                       = 15
multiplayer_event_admin_set_game_password                     = 16
multiplayer_event_admin_set_team_faction                      = 17
multiplayer_event_open_admin_panel                            = 18
multiplayer_event_change_team_no                              = 19
multiplayer_event_change_troop_id                             = 20
multiplayer_event_start_new_poll                              = 21
multiplayer_event_answer_to_poll                              = 22
multiplayer_event_admin_kick_player                           = 23
multiplayer_event_admin_ban_player                            = 24
multiplayer_event_admin_set_num_bots_voteable                 = 25
multiplayer_event_admin_set_factions_voteable                 = 26
multiplayer_event_admin_set_maps_voteable                     = 27
multiplayer_event_admin_set_player_respawn_as_bot             = 28
multiplayer_event_admin_set_combat_speed                      = 29
multiplayer_event_admin_set_respawn_count                     = 30
multiplayer_event_admin_set_kick_voteable                     = 31
multiplayer_event_admin_set_ban_voteable                      = 32
multiplayer_event_admin_set_valid_vote_ratio                  = 33
multiplayer_event_admin_set_auto_team_balance_limit           = 34
multiplayer_event_admin_set_welcome_message                   = 35
multiplayer_event_admin_set_initial_gold_multiplier           = 36
multiplayer_event_admin_set_battle_earnings_multiplier        = 37
multiplayer_event_admin_set_round_earnings_multiplier         = 38
multiplayer_event_admin_set_melee_friendly_fire               = 39
multiplayer_event_admin_set_friendly_fire_damage_self_ratio   = 40
multiplayer_event_admin_set_friendly_fire_damage_friend_ratio = 41
multiplayer_event_admin_set_allow_player_banners              = 42
multiplayer_event_admin_set_force_default_armor               = 43
multiplayer_event_admin_set_anti_cheat                        = 44
multiplayer_event_open_game_rules                             = 45
multiplayer_event_offer_duel                                  = 46
multiplayer_event_admin_set_disallow_ranged_weapons           = 47
#INVASION MODE START
multiplayer_event_other_events                                = 48


#other client events
multiplayer_event_other_event_set_bot_purchase                = 0
multiplayer_event_other_event_ccoop_lock_companions           = 1
multiplayer_event_coop_set_agent_team_and_group               = 2
multiplayer_event_other_event_ccoop_count_down_visible		  = 3
multiplayer_event_other_event_ccoop_count_down_invisible	  = 4
multiplayer_event_other_spawn_prison_cart					  = 5
multiplayer_event_other_destroy_prison_cart					  = 6

multiplayer_event_other_event_ccoop_update_spawn_data_1		  = 7
multiplayer_event_other_event_ccoop_update_spawn_data_2		  = 8
multiplayer_event_other_event_ccoop_update_spawn_data_3		  = 9
multiplayer_event_other_event_ccoop_update_spawn_data_4		  = 10
multiplayer_event_other_event_ccoop_update_spawn_data_5		  = 11
multiplayer_event_other_event_ccoop_update_spawn_data_6		  = 12

multiplayer_event_other_events_change_companion_level 		  = 13
multiplayer_event_admin_set_ccoop_difficulty                  = 14
multiplayer_event_other_event_unequip_item			 		  = 15
multiplayer_event_other_event_equip_item			 		  = 16
multiplayer_event_coop_send_drop_assignment_to_server         = 17
multiplayer_event_coop_set_agent_team_and_group               = 18
#INVASION MODE END

#server events
multiplayer_event_return_max_num_players                      = 50
multiplayer_event_return_num_bots_in_team                     = 51
multiplayer_event_return_friendly_fire                        = 52
multiplayer_event_return_ghost_mode                           = 53
multiplayer_event_return_control_block_dir                    = 54
multiplayer_event_return_combat_speed                         = 55
multiplayer_event_return_add_to_servers_list                  = 56
multiplayer_event_return_respawn_period                       = 57
multiplayer_event_return_game_max_minutes                     = 58
multiplayer_event_return_round_max_seconds                    = 59
multiplayer_event_return_game_max_points                      = 60
multiplayer_event_return_point_gained_from_flags              = 61
multiplayer_event_return_point_gained_from_capturing_flag     = 62
multiplayer_event_return_server_name                          = 63
multiplayer_event_return_game_password                        = 64
multiplayer_event_return_game_type                            = 65
multiplayer_event_return_confirmation                         = 66
multiplayer_event_return_rejection                            = 67
multiplayer_event_show_multiplayer_message                    = 68
multiplayer_event_draw_this_round                             = 69
multiplayer_event_set_attached_scene_prop                     = 70
multiplayer_event_set_team_flag_situation                     = 71
multiplayer_event_set_team_score                              = 72
multiplayer_event_set_num_agents_around_flag                  = 73
multiplayer_event_ask_for_poll                                = 74
multiplayer_event_change_flag_owner                           = 75
multiplayer_event_use_item                                    = 76
multiplayer_event_set_scene_prop_open_or_close                = 77
multiplayer_event_set_round_start_time                        = 78
multiplayer_event_force_start_team_selection                  = 79
multiplayer_event_start_death_mode                            = 80
multiplayer_event_return_num_bots_voteable                    = 81
multiplayer_event_return_factions_voteable                    = 82
multiplayer_event_return_maps_voteable                        = 83
multiplayer_event_return_next_team_faction                    = 84
multiplayer_event_return_player_respawn_as_bot                = 85
multiplayer_event_set_player_score_kill_death                 = 86
multiplayer_event_set_day_time                                = 87
multiplayer_event_return_respawn_count                        = 88
multiplayer_event_return_player_respawn_spent                 = 89
multiplayer_event_return_kick_voteable                        = 90
multiplayer_event_return_ban_voteable                         = 91
multiplayer_event_return_valid_vote_ratio                     = 92
multiplayer_event_return_auto_team_balance_limit              = 93
multiplayer_event_return_initial_gold_multiplier              = 94
multiplayer_event_return_battle_earnings_multiplier           = 95
multiplayer_event_return_round_earnings_multiplier            = 96
multiplayer_event_return_renaming_server_allowed              = 97
multiplayer_event_return_changing_game_type_allowed           = 98
multiplayer_event_return_melee_friendly_fire                  = 99
multiplayer_event_return_friendly_fire_damage_self_ratio      = 100
multiplayer_event_return_friendly_fire_damage_friend_ratio    = 101
multiplayer_event_return_allow_player_banners                 = 102
multiplayer_event_return_force_default_armor                  = 103
multiplayer_event_return_anti_cheat                           = 104
multiplayer_event_return_open_game_rules                      = 105
multiplayer_event_return_max_num_bots                         = 106
multiplayer_event_return_server_mission_timer_while_player_joined = 107
multiplayer_event_show_duel_request                           = 108
multiplayer_event_start_duel                                  = 109
multiplayer_event_cancel_duel                                 = 110
multiplayer_event_show_server_message                         = 111
multiplayer_event_return_disallow_ranged_weapons              = 112
#INVASION MODE START
multiplayer_event_return_set_bot_selection                    = 113 
multiplayer_event_return_team_ratio                           = 114
multiplayer_event_return_squad_size                           = 115
multiplayer_event_return_disallow_granades                    = 116
multiplayer_event_return_sound_at_pos                         = 117
multiplayer_event_return_enable_cbf_squad_ratio				  = 118
multiplayer_event_return_cbf_squad_ratio					  = 119
multiplayer_event_coop_drop_item                              = 120
multiplayer_event_coop_chest_opened                           = 121
multiplayer_event_return_ccoop_difficulty                     = 122
multiplayer_event_ccoop_victory_message                       = 123
multiplayer_event_ccoop_return_of_the_king                    = 124
#INVASION MODE END

#multiplayer message types
multiplayer_message_type_auto_team_balance_done      = 2
multiplayer_message_type_auto_team_balance_next      = 3
multiplayer_message_type_capture_the_flag_score      = 4
multiplayer_message_type_flag_returned_home          = 5
multiplayer_message_type_capture_the_flag_stole      = 6
multiplayer_message_type_poll_result                 = 7
multiplayer_message_type_flag_neutralized            = 8
multiplayer_message_type_flag_captured               = 9
multiplayer_message_type_flag_is_pulling             = 10
multiplayer_message_type_auto_team_balance_no_need   = 11
multiplayer_message_type_round_result_in_battle_mode = 12
multiplayer_message_type_round_result_in_siege_mode  = 13
multiplayer_message_type_round_draw                  = 14
multiplayer_message_type_target_destroyed            = 15
multiplayer_message_type_defenders_saved_n_targets   = 16
multiplayer_message_type_attackers_won_the_round     = 17
multiplayer_message_type_start_death_mode            = 18

#multiplayer game type indices
multiplayer_game_type_deathmatch             = 0
multiplayer_game_type_team_deathmatch        = 1
multiplayer_game_type_battle                 = 2
multiplayer_game_type_destroy                = 3
multiplayer_game_type_capture_the_flag       = 4
multiplayer_game_type_headquarters           = 5
multiplayer_game_type_siege                  = 6
multiplayer_game_type_duel                   = 7
#INVASION MODE START
multiplayer_game_type_captain_coop           = 8
multiplayer_num_game_types                   = 9
#INVASION MODE END

#admin panel value ranges
multiplayer_round_max_seconds_min            = 60
multiplayer_round_max_seconds_max            = 901
multiplayer_respawn_period_min               = 3
multiplayer_respawn_period_max               = 31 #can only be 30 seconds max (due to agent deletion after that period)

multiplayer_siege_mod_defender_team_extra_respawn_time = 27 #It was 20 in 1.113 but it is increased it to 25 in 1.121 because defenders were mostly defeating enemy.
multiplayer_new_agents_finish_spawning_time = 30
multiplayer_max_possible_player_id = 1000

#team 1 and team 2 are 0 and 1 respectively
multi_team_spectator = 2
multi_team_unassigned = multi_team_spectator + 1

multi_data_maps_for_game_type_begin = 0
multi_data_maps_for_game_type_end = multi_data_maps_for_game_type_begin + 30
multi_data_troop_button_indices_begin = multi_data_maps_for_game_type_end
multi_data_troop_button_indices_end = multi_data_troop_button_indices_begin + 16 #maximum 16 troops per faction
multi_data_item_button_indices_begin = multi_data_troop_button_indices_end
multi_data_item_button_indices_end = multi_data_item_button_indices_begin + 100 #maximum 100 items per troop
multi_data_flag_owner_begin = multi_data_item_button_indices_end
multi_data_flag_owner_end = multi_data_flag_owner_begin + 10 #maximum of 10 flags per scene
multi_data_flag_players_around_begin = multi_data_flag_owner_end 
multi_data_flag_players_around_end = multi_data_flag_players_around_begin + 10 #maximum of 10 flags per scene
multi_data_flag_owned_seconds_begin = multi_data_flag_players_around_end
multi_data_flag_owned_seconds_end = multi_data_flag_owned_seconds_begin + 10 #maximum of 10 flags per scene
multi_data_flag_pull_code_begin = multi_data_flag_owned_seconds_end
multi_data_flag_pull_code_end = multi_data_flag_pull_code_begin + 10 #maximum of 10 flags per scene
#INVASION MODE START
multi_data_ccoop_wave_spawn_data_begin = multi_data_flag_pull_code_end
multi_data_ccoop_wave_spawn_data_end = multi_data_ccoop_wave_spawn_data_begin + 16 #maximum of 5 different troop types, amounts and entry points (+ 1 for count)
multi_data_equipment_holder_begin = multi_data_ccoop_wave_spawn_data_end
multi_data_equipment_holder_end = multi_data_equipment_holder_begin + 9
multi_data_player_index_list_begin = multi_data_equipment_holder_end
#INVASION MODE END

#Entry points 100..109 is used for showing initial points for moveable and usable scene props like siege ladder.
multi_entry_points_for_usable_items_start = 100
multi_entry_points_for_usable_items_end = multi_entry_points_for_usable_items_start + 10


#multi_item_class_type_other = 0
multi_item_class_type_sword = 1
multi_item_class_type_axe = 2
multi_item_class_type_blunt = 3
multi_item_class_type_war_picks = 4
multi_item_class_type_cleavers = 5
multi_item_class_type_two_handed_sword = 6
multi_item_class_type_two_handed_axe = 7
multi_item_class_type_spear = 8
multi_item_class_type_lance = 9
multi_item_class_type_small_shield = 10
multi_item_class_type_large_shield = 11
multi_item_class_type_bow = 12
multi_item_class_type_crossbow = 13
multi_item_class_type_arrow = 14
multi_item_class_type_bolt = 15
multi_item_class_type_throwing = 16
multi_item_class_type_throwing_axe = 17
multi_item_class_type_horse = 18
multi_item_class_type_light_armor = 19
multi_item_class_type_medium_armor = 20
multi_item_class_type_heavy_armor = 21
multi_item_class_type_light_helm = 22
multi_item_class_type_heavy_helm = 23
multi_item_class_type_light_foot = 24
multi_item_class_type_heavy_foot = 25
multi_item_class_type_glove = 26

multi_item_class_type_melee_weapons_begin = multi_item_class_type_sword
multi_item_class_type_melee_weapons_end = multi_item_class_type_small_shield
multi_item_class_type_ranged_weapons_begin = multi_item_class_type_bow
multi_item_class_type_ranged_weapons_end = multi_item_class_type_horse
multi_item_class_type_shields_begin = multi_item_class_type_melee_weapons_end
multi_item_class_type_shields_end = multi_item_class_type_bow

multi_item_class_type_weapons_begin = multi_item_class_type_sword
multi_item_class_type_weapons_end = multi_item_class_type_horse
multi_item_class_type_horses_begin = multi_item_class_type_weapons_end
multi_item_class_type_horses_end = multi_item_class_type_light_armor
multi_item_class_type_bodies_begin = multi_item_class_type_horses_end
multi_item_class_type_bodies_end = multi_item_class_type_light_helm
multi_item_class_type_heads_begin = multi_item_class_type_bodies_end
multi_item_class_type_heads_end = multi_item_class_type_light_foot
multi_item_class_type_feet_begin = multi_item_class_type_heads_end
multi_item_class_type_feet_end = multi_item_class_type_glove
multi_item_class_type_gloves_begin = multi_item_class_type_feet_end
multi_item_class_type_gloves_end = multi_item_class_type_glove + 1

multi_troop_class_other = 0
multi_troop_class_infantry = 1
multi_troop_class_spearman = 2
multi_troop_class_cavalry = 3
multi_troop_class_archer = 4
multi_troop_class_crossbowman = 5
multi_troop_class_mounted_archer = 6
multi_troop_class_mounted_crossbowman = 7

multi_num_valid_entry_points = 64
multi_num_valid_entry_points_div_2 = 32

#normal money management system
multi_battle_round_team_money_add = 500
multi_destroy_save_or_destroy_target_money_add = 100
multi_destroy_target_money_add = 1500
multi_initial_gold_value = 1000
multi_max_gold_that_can_be_stored = 15000

multi_killer_agent_standard_money_add = 150 #(2/3 = 100 for battle & destroy, 3/3 = 150 for siege, 4/3 = 200 for deathmatch/team deathmatch/capture the flag/headquarters)
multi_killer_agent_loot_percentage_share = 12 #(2/3 = 8% for battle & destroy, 3/3 = 12% for siege, 4/3 = 16% for deathmatch/team deathmatch/capture the flag/headquarters)
multi_dead_agent_loot_percentage_share = 48 #(2/3 = 32% for battle & destroy, 3/3 = 48% for siege, 4/3 = 64% for deathmatch/team deathmatch/capture the flag/headquarters)
multi_minimum_gold = 1000 #(same in all modes)

multi_minimum_target_health = 1200

multi_max_seconds_flag_can_stay_in_ground = 60

multi_capture_the_flag_score_flag_returning = 1

multi_initial_spawn_point_team_1 = 0
multi_initial_spawn_point_team_2 = 32
multi_base_point_team_1 = 64
multi_base_point_team_2 = 65
multi_siege_flag_point = 66
multi_death_mode_point = 67

multi_headquarters_pole_height = 900
multi_headquarters_flag_height_to_win = 800 #used in sd death mode
multi_headquarters_flag_initial_height = 100 #used in sd death mode
multi_headquarters_max_distance_sq_to_raise_flags = 1600 #4m * 4m * 100 = 1600
multi_headquarters_distance_sq_to_set_flag = 8100 #9m * 9m * 100 = 8100 
multi_headquarters_distance_sq_to_change_flag = 400 #2m * 2m * 100 = 400 
multi_headquarters_distance_to_change_flag = 200 #2m * 100 = 200 
multi_distance_sq_to_use_belfry = 36 #6m * 6m = 36 (there is no * 100 for this one because it uses get_sq_distance_between_positions_in_meters instead of get_sq_distance_between_positions)
multi_max_sq_dist_between_agents_to_longer_mof_time = 49 #7m * 7m = 49m
min_allowed_flag_height_difference_to_make_score = 50

#these two values are about when master of field will be kicked
multiplayer_battle_formula_value_a = 15
multiplayer_battle_formula_value_b = 18000 #think about 18000-20000 if death mod very much happens.

multiplayer_spawn_above_opt_enemy_dist_point = 32 #while finding most suitable spawn point if nearest enemy is further than 32 meters give negative points to that spawn point
multiplayer_spawn_min_enemy_dist_limit = 45 #while finding most suitable spawn point if nearest enemy is closer than 45 meters give negative points to that spawn point, (squared increase)

multiplayer_poll_disable_period = 900 #15 minutes

#INVASION MODE START
multi_distance_to_captain_spaw_point = 15*100
multi_killer_captain_add = 60
multi_captain_recomended_players_max = 16
multi_killer_captain_coop_add = 200
#multi_captain_coop_round_duration_in_sec = 600 # 10 minutes
#INVASION MODE END

#menu variables
escape_menu_item_height = 40



bignum = 0x40000000000000000000000000000000

op_num_value_bits = 24 + 32

tag_register        =  1
tag_variable        =  2
tag_string          =  3
tag_item            =  4
tag_troop           =  5
tag_faction         =  6
tag_quest           =  7
tag_party_tpl       =  8
tag_party           =  9
tag_scene           = 10
tag_mission_tpl     = 11
tag_menu            = 12
tag_script          = 13
tag_particle_sys    = 14
tag_scene_prop      = 15
tag_sound           = 16
tag_local_variable  = 17
tag_map_icon        = 18
tag_skill           = 19
tag_mesh            = 20
tag_presentation    = 21
tag_quick_string    = 22
tag_track	    = 23
tag_tableau         = 24
tag_animation       = 25
tags_end            = 26


opmask_register             =  tag_register       << op_num_value_bits
opmask_variable             =  tag_variable       << op_num_value_bits
##opmask_string             =  tag_string         << op_num_value_bits
##opmask_item_index         =  tag_item           << op_num_value_bits
##opmask_troop_index        =  tag_troop          << op_num_value_bits
##opmask_faction_index      =  tag_faction        << op_num_value_bits
opmask_quest_index          =  tag_quest          << op_num_value_bits
##opmask_p_template_index   =  tag_party_tpl      << op_num_value_bits
##opmask_party_index        =  tag_party          << op_num_value_bits
##opmask_scene_index        =  tag_scene          << op_num_value_bits
##opmask_mission_tpl_index  =  tag_mission_tpl    << op_num_value_bits
##opmask_menu_index         =  tag_menu           << op_num_value_bits
##opmask_script             =  tag_script         << op_num_value_bits
##opmask_particle_sys       =  tag_particle_sys   << op_num_value_bits
##opmask_scene_prop         =  tag_scene_prop     << op_num_value_bits
##opmask_sound              =  tag_sound          << op_num_value_bits
##opmask_map_icon           =  tag_map_icon       << op_num_value_bits
opmask_local_variable       =  tag_local_variable << op_num_value_bits
opmask_quick_string         =  tag_quick_string   << op_num_value_bits


def reg(reg_no):
  if (reg_no < 0):
    print ("Error register_no negative")
    cause_error()
  return opmask_register | reg_no

def find_object(objects,object_id):
  result = -1
  num_objects = len(objects)
  i_object = 0
  object_id_lowercase = object_id.lower()
  while (i_object < num_objects) and (result == -1):
    object = objects[i_object]
    if (object[0].lower() == object_id_lowercase):
      result = i_object
    i_object += 1
  return result

s0  =  0
s1  =  1
s2  =  2
s3  =  3
s4  =  4
s5  =  5
s6  =  6
s7  =  7
s8  =  8
s9  =  9
s10 = 10
s11 = 11
s12 = 12
s13 = 13
s14 = 14
s15 = 15
s16 = 16
s17 = 17
s18 = 18
s19 = 19
s20 = 20
s21 = 21
s22 = 22
s23 = 23
s24 = 24
s25 = 25
s26 = 26
s27 = 27
s28 = 28
s29 = 29
s30 = 30
s31 = 31
s32 = 32
s33 = 33
s34 = 34
s35 = 35
s36 = 36
s37 = 37
s38 = 38
s39 = 39
s40 = 40
s41 = 41
s42 = 42
s43 = 43
s44 = 44
s45 = 45
s46 = 46
s47 = 47
s48 = 48
s49 = 49
s50 = 50
s51 = 51
s52 = 52
s53 = 53
s54 = 54
s55 = 55
s56 = 56
s57 = 57
s58 = 58
s59 = 59
s60 = 60
s61 = 61
s62 = 62
s63 = 63

s64 = 64
s65 = 65
s66 = 66
s67 = 67


pos0  =  0
pos1  =  1
pos2  =  2
pos3  =  3
pos4  =  4
pos5  =  5
pos6  =  6
pos7  =  7
pos8  =  8
pos9  =  9
pos10 = 10
pos11 = 11
pos12 = 12
pos13 = 13
pos14 = 14
pos15 = 15
pos16 = 16
pos17 = 17
pos18 = 18
pos19 = 19
pos20 = 20
pos21 = 21
pos22 = 22
pos23 = 23
pos24 = 24
pos25 = 25
pos26 = 26
pos27 = 27
pos28 = 28
pos29 = 29
pos30 = 30
pos31 = 31
pos32 = 32
pos33 = 33
pos34 = 34
pos35 = 35
pos36 = 36
pos37 = 37
pos38 = 38
pos39 = 39
pos40 = 40
pos41 = 41
pos42 = 42
pos43 = 43
pos44 = 44
pos45 = 45
pos46 = 46
pos47 = 47
pos48 = 48
pos49 = 49
pos50 = 50
pos51 = 51
pos52 = 52
pos53 = 53
pos54 = 54
pos55 = 55
pos56 = 56
pos57 = 57
pos58 = 58
pos59 = 59
pos60 = 60
pos61 = 61
pos62 = 62
pos63 = 63
pos_belfry_begin = 64

reg0   = opmask_register| 0
reg1   = opmask_register| 1
reg2   = opmask_register| 2
reg3   = opmask_register| 3
reg4   = opmask_register| 4
reg5   = opmask_register| 5
reg6   = opmask_register| 6
reg7   = opmask_register| 7
reg8   = opmask_register| 8
reg9   = opmask_register| 9
reg10  = opmask_register|10
reg11  = opmask_register|11
reg12  = opmask_register|12
reg13  = opmask_register|13
reg14  = opmask_register|14
reg15  = opmask_register|15
reg16  = opmask_register|16
reg17  = opmask_register|17
reg18  = opmask_register|18
reg19  = opmask_register|19
reg20  = opmask_register|20
reg21  = opmask_register|21
reg22  = opmask_register|22
reg23  = opmask_register|23
reg24  = opmask_register|24
reg25  = opmask_register|25
reg26  = opmask_register|26
reg27  = opmask_register|27
reg28  = opmask_register|28
reg29  = opmask_register|29
reg30  = opmask_register|30
reg31  = opmask_register|31
reg32  = opmask_register|32
reg33  = opmask_register|33
reg34  = opmask_register|34
reg35  = opmask_register|35
reg36  = opmask_register|36
reg37  = opmask_register|37
reg38  = opmask_register|38
reg39  = opmask_register|39
reg40  = opmask_register|40
reg41  = opmask_register|41
reg42  = opmask_register|42
reg43  = opmask_register|43
reg44  = opmask_register|44
reg45  = opmask_register|45
reg46  = opmask_register|46
reg47  = opmask_register|47
reg48  = opmask_register|48
reg49  = opmask_register|49
reg50  = opmask_register|50
reg51  = opmask_register|51
reg52  = opmask_register|52
reg53  = opmask_register|53
reg54  = opmask_register|54
reg55  = opmask_register|55
reg56  = opmask_register|56
reg57  = opmask_register|57
reg58  = opmask_register|58
reg59  = opmask_register|59
reg60  = opmask_register|60
reg61  = opmask_register|61
reg62  = opmask_register|62
reg63  = opmask_register|63

reg65  = opmask_register|65

spf_all_teams_are_enemy                      = 0x00000001, 
spf_is_horseman                              = 0x00000002,
spf_examine_all_spawn_points                 = 0x00000004,
spf_team_0_spawn_far_from_entry_32           = 0x00000008,
spf_team_1_spawn_far_from_entry_0            = 0x00000010,
spf_team_1_spawn_far_from_entry_66           = 0x00000020,
spf_team_0_spawn_near_entry_0                = 0x00000040,
spf_team_0_spawn_near_entry_66               = 0x00000080,
spf_team_1_spawn_near_entry_32               = 0x00000100,
spf_team_0_walkers_spawn_at_high_points      = 0x00000200,
spf_team_1_walkers_spawn_at_high_points      = 0x00000400,
spf_try_to_spawn_close_to_at_least_one_enemy = 0x00000800,
spf_care_agent_to_agent_distances_less       = 0x00001000,
