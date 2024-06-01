from enum import Enum

class EVENT(Enum):
    """
    A class containing all the events that can be emitted by the server.
    """
    SERVER_START = "server_start"  # Sent when the server starts.
    TICK = "tick"  # Sent every tick. Be careful, this event could cause performance issues if used incorrectly.
    PACKET_RECEIVED = "packet_received"  # Sent when a packet is received from a client.
    PACKET_SENT = "packet_sent"  # Sent when a packet is sent to a client.
    CLIENT_LOGIN = "client_login"  # Sent when a client first connects to the server. Does not guarantee that the client
    # has successfully logged in.
    CLIENT_LOGIN_SUCCESS = "client_login_success"  # Sent when a client has successfully logged in.
    CLIENT_LOGIN_FAILURE = "client_login_failure"  # Sent when a client has failed to log in.
    CLIENT_DISCONNECT = "client_disconnect"  # Sent when a client disconnects from the server.
    CLIENT_RESOURCE_PACKS_REFUSED = "client_resource_packs_refused"  # Sent when a client refuses the server's resource
    # packs.
    CLIENT_RESOURCE_PACKS_COMPLETED = "client_resource_packs_completed"  # Sent when a client has completed downloading
    # the server's resource packs.
    CLIENT_TEXT = "client_text"  # Sent when a client sends a chat message.
    SLASH_COMMAND = "slash_command"  # Sent when a slash command is executed, either by a player or the console.
    TIME_SYNC = "time_sync"  # Sent when the server sends a time sync packet to a client.
    PLAYER_ADD = "player_add"  # Sent when a player is shown to other players.
    CLIENT_JOIN = "client_join"  # Sent when a client has fully joined the server.
    ENTITY_ADD = "entity_add"  # Sent when an entity is added to the server.
    ENTITY_REMOVE = "entity_remove"  # Sent when an entity is removed from the server.
    ITEM_ADD = "item_add"  # Sent when an item is added to the server.
    ITEM_PICKUP = "item_pickup"  # Sent when an item is picked up by a player.
    ITEM_TAKE = "item_take"  # Sent when an item is taken by a player.
    ENTITY_MOVED_ABSOLUTE = "entity_moved_absolute"  # Sent when an entity is moved to an absolute position.
    PLAYER_MOVED = "player_moved"  # Sent when a player is moved.
    RIDER_JUMP = "rider_jump"  # Sent when a rideable entity jumps while being ridden (e.g. a horse).
    BLOCK_UPDATE = "block_update"  # Sent when a block is updated.
    PAINTING_ADD = "painting_add"  # Sent when a painting is added to the server.
    TICK_SYNC = "tick_sync"  # Sent when the server sends a tick sync packet to a client.
    LEVEL_SOUND_EVENT = "level_sound_event"  # Sent when a level sound event is played.
    LEVEL_EVENT = "level_event"  # Sent when a level event is triggered.
    BLOCK_EVENT = "block_event"  # Sent when a block event is triggered.
    ENTITY_EVENT = "entity_event"  # Sent when an entity event is triggered.
    MOB_EFFECT = "mob_effect"  # Sent when a mob effect is added, modified, or removed.
    INVENTORY_TRANSACTION = "inventory_transaction"  # Sent when an inventory transaction is processed.
    MOB_EQUIPMENT = "mob_equipment"  # Sent when a mob's equipment is modified.
    MOB_ARMOR_EQUIPMENT = "mob_armor_equipment"  # Sent when a mob's armor equipment is modified.
    INTERACT = "interact"  # Sent when a player interacts with an entity.
    BLOCK_PICK_REQUEST = "block_pick_request"  # Sent when a player requests to pick a block.
    ENTITY_PICK_REQUEST = "entity_pick_request"  # Sent when a player requests to pick an entity.
    PLAYER_ACTION = "player_action"  # Sent when a player performs an action.
    ENTITY_FALL_INSECURE = "entity_fall"  # Sent when an entity falls at a distance which should cause fall damage.
    # Warning: this event should not be used, as it can easily be abused by hackers.
    ENTITY_FALL = "entity_fall"  # Sent when the server detects that an entity has fallen (any distance).
    HURT_ARMOUR_INSECURE = "hurt_armour"  # Sent when a player is damaged while wearing armor. Warning: this event
    # will only be called when the insecure hurt armor packet is sent, which will not be sent by PieMC.
    HURT_ARMOUR = "hurt_armour"  # Sent when a player is damaged while wearing armor.
    SET_ENTITY_DATA = "set_entity_data"  # Sent when an entity's data is set.
    SET_ENTITY_MOTION = "set_entity_motion"  # Sent when an entity's motion is set.
    SET_ENTITY_LINK = "set_entity_link"  # Sent when an entity's link is set.
    SET_SPAWN_POSITION = "set_spawn_position"  # Sent when the server sets the spawn position.
    ANIMATE = "animate"  # Sent when a player performs an animation.
    RESPAWN = "respawn"  # Sent when a player respawns.
    CONTAINER_OPEN = "container_open"  # Sent when a player opens a container.
    CONTAINER_CLOSE = "container_close"  # Sent when a player closes a container.
    PLAYER_HOTBAR = "player_hotbar"  # Sent when a player's hotbar is updated.
    INVENTORY_CONTENT = "inventory_content"  # Sent when an inventory's content is updated.
    INVENTORY_SLOT = "inventory_slot"  # Sent when an inventory slot is updated.
    CONTAINER_SET_DATA = "container_set_data"  # Sent when a container's data is set.
    CRAFTING_DATA = "crafting_data"  # Sent when crafting data is sent to a client.
    CRAFTING_EVENT = "crafting_event"  # Sent when a crafting event is triggered.
    ADVENTURE_SETTINGS = "adventure_settings"  # Sent when adventure settings are updated.
    BLOCK_ENTITY_DATA = "block_entity_data"  # Sent when a block entity's data is set.
    PLAYER_INPUT = "player_input"  # Sent when a player is moving, but not using the move player packet (e.g. when
    # the player is moving a boat).
    LEVEL_CHUNK = "level_chunk"  # Sent when a level chunk is sent to a client.
    SET_COMMANDS_ENABLED = "set_commands_enabled"  # Sent when the server enables or disables commands.
    SET_DIFFICULTY = "set_difficulty"  # Sent when the server sets the difficulty.
    CHANGE_DIMENSION = "change_dimension"  # Sent when a player changes dimension.
    SET_PLAYER_GAME_TYPE = "set_player_game_type"  # Sent when a player's game mode is set.
    PLAYER_LIST = "player_list"  # Sent when the player list is sent to a client.
    SIMPLE_EVENT = "simple_event"  # Usage is not clear.
    EVENT = "event"  # Usage is not clear.
    SPAWN_EXPERIENCE_ORB = "spawn_experience_orb"  # Sent when an experience orb is spawned.
    MAP_ITEM_DATA = "map_item_data"  # Sent when map item data is sent to a client.
    MAP_INFO_REQUEST = "map_info_request"  # Sent when a client requests map info.
    REQUEST_CHUNK_RADIUS = "request_chunk_radius"  # Sent when a client requests a chunk radius.
    CHUNK_RADIUS_UPDATED = "chunk_radius_updated"  # Sent when the chunk radius is updated.
    ITEM_FRAME_DROP_ITEM = "item_frame_drop_item"  # Sent when a creative mode player removes an item from an item
    # frame.
    GAME_RULES_CHANGED = "game_rules_changed"  # Sent when game rules are changed.
    CAMERA = "camera"  # Usage is not clear.
    BOSS_EVENT = "boss_event"  # Sent when a boss event is triggered.
    SHOW_CREDITS = "show_credits"  # Sent when the credits are shown.
    AVAILABLE_COMMANDS = "available_commands"  # Sent when available commands are updated.
    COMMAND_REQUEST = "command_request"  # Sent when a command is requested.
    COMMAND_BLOCK_UPDATE = "command_block_update"  # Sent when a command block is updated.
    COMMAND_OUTPUT = "command_output"  # Sent when a command output is sent.
    UPDATE_TRADE = "update_trade"  # Sent when a trade is updated.
    UPDATE_EQUIP = "update_equip"  # Usage is not clear.
    RESOURCE_PACK_DATA_INFO = "resource_pack_data_info"  # Sent when resource pack data info is sent to a client.
    RESOURCE_PACK_CHUNK_DATA = "resource_pack_chunk_data"  # Sent when resource pack chunk data is sent to a client.
    RESOURCE_PACK_CHUNK_REQUEST = "resource_pack_chunk_request"  # Sent when a client requests a resource pack chunk.
    TRANSFER = "transfer"  # Sent when a client is transferred to another server.
    PLAY_SOUND = "play_sound"  # Sent when a sound is played to a client (client-side sounds will not trigger this).
    STOP_SOUND = "stop_sound"  # Sent when a sound is stopped for a client.
    SET_TITLE = "set_title"  # Sent when a title is set for a client.
    STRUCTURE_BLOCK_UPDATE = "structure_block_update"  # Sent when a structure block is updated.
    SHOW_STORE_OFFER = "show_store_offer"  # Sent when a store offer is shown. Partnered servers only.
    PURCHASE_RECEIPT = "purchase_receipt"  # Sent when a purchase receipt is received. Partnered servers only.
    PLAYER_SKIN = "player_skin"  # Sent when a player's skin is updated.
    SUB_CLIENT_LOGIN = "sub_client_login"  # Sent when a sub-client (split-screen player) logs in.
    AUTOMATION_CLIENT_CONNECT = "automation_client_connect"  # Sent when the server requests that the client connects to
    # the automation server.
    BOOK_EDIT = "book_edit"  # Sent when a book is edited.
    NPC_REQUEST = "npc_request"  # Sent when a player interacts with an NPC.
    PHOTO_TRANSFER = "photo_transfer"  # Sent when a photo is transferred. Education Edition only.
    MODAL_FORM_REQUEST = "modal_form_request"  # Sent when the server requests a client to show a modal form.
    MODAL_FORM_RESPONSE = "modal_form_response"  # Sent when a modal form response is received.
    SERVER_SETTINGS_REQUEST = "server_settings_request"  # Sent when the client requests server settings.
    SERVER_SETTINGS_RESPONSE = "server_settings_response"  # Sent when server settings are received.
    SHOW_PROFILE = "show_profile"  # Sent when a player's profile is shown.
    SET_DEFAULT_GAME_TYPE = "set_default_game_type"  # Sent when the default game mode is set.
    REMOVE_OBJECTIVE = "remove_objective"  # Sent when an objective is removed.
    SET_DISPLAY_OBJECTIVE = "set_display_objective"  # Sent when a display objective is set.
    SET_SCORE = "set_score"  # Sent when a scoreboard is updated.
    LAB_TABLE = "lab_table"  # Sent when a lab table is used. Education Edition feature.
    UPDATE_BLOCK_SYNCED = "update_block_synced"  # Sent from the server to update falling and moving blocks.
    MOVE_ENTITY_DELTA = "move_entity_delta"  # Sent when an entity is moved by a delta.
    SET_SCOREBOARD_IDENTITY = "set_scoreboard_identity"  # Sent when a scoreboard identity is set.
    SET_LOCAL_PLAYER_AS_INITIALIZED = "set_local_player_as_initialized"  # Sent when the local player is initialized.
    UPDATE_SOFT_ENUM = "update_soft_enum"  # Sent when a soft (dynamic) enum is updated.
    NETWORK_STACK_LATENCY = "network_stack_latency"  # Sent when network stack latency is updated.
    SCRIPT_CUSTOM_EVENT = "script_custom_event"  # Sent when a custom script event is received or sent.
    SPAWN_PARTICLE_EFFECT = "spawn_particle_effect"  # Sent when a particle effect is spawned.
    AVAILABLE_ACTOR_IDENTIFIERS = "available_actor_identifiers"  # Sent when available actor identifiers are updated.
    NETWORK_CHUNK_PUBLISHER_UPDATE = "network_chunk_publisher_update"  # Sent when a network chunk publisher is updated.
    BIOME_DEFINITION_LIST = "biome_definition_list"  # Sent when a biome definition list is updated.
    LEVEL_EVENT_GENERIC = "level_event_generic"  # Sent when a generic level event is triggered.
    LECTERN_UPDATE = "lectern_update"  # Sent when a lectern is updated.
    VIDEO_STREAM_CONNECT = "video_stream_connect"  # Usage is not clear.
    CLIENT_CACHE_STATUS = "client_cache_status"  # Sent when the client joins to specify whether blob cache is
    # supported.
    ON_SCREEN_TEXTURE_ANIMATION = "on_screen_texture_animation"  # Sent when an on-screen texture animation is
    # triggered.
    MAP_CREATE_LOCKED_COPY = "map_create_locked_copy"  # Sent when a locked copy of a map is created.
    STRUCTURE_TEMPLATE_DATA_EXPORT_REQUEST = "structure_template_data_export_request"  # Sent when a structure template
    # data export request is received.
    STRUCTURE_TEMPLATE_DATA_EXPORT_RESPONSE = "structure_template_data_export_response"  # Sent when a structure
    # template data export response is sent.
    UPDATE_BLOCK_PROPERTIES = "update_block_properties"  # Sent when block properties are updated.
    CLIENT_CACHE_BLOB_STATUS = "client_cache_blob_status"  # Sent when the client cache blob status is updated.
    CLIENT_CACHE_MISS_RESPONSE = "client_cache_miss_response"  # Sent when a client cache miss response is received.
    NETWORK_SETTINGS = "network_settings"  # Sent when network settings are updated.
    PLAYER_AUTH_INPUT = "player_auth_input"  # Sent when a player authentication input is received.
    CREATIVE_CONTENT = "creative_content"  # Sent when creative content is updated.
    PLAYER_ENCHANT_OPTIONS = "player_enchant_options"  # Sent when player enchant options are updated.
    ITEM_STACK_REQUEST = "item_stack_request"  # Sent when an item stack request is received.
    ITEM_STACK_RESPONSE = "item_stack_response"  # Sent when an item stack response is sent.
    PLAYER_ARMOR_DAMAGE = "player_armor_damage"  # Sent when a player's armor is damaged.
    CODE_BUILDER = "code_builder"  # Sent when a code builder event is triggered. Education Edition only.
    UPDATE_PLAYER_GAME_TYPE = "update_player_game_type"  # Sent when a player's game mode is updated.
    EMOTE_LIST = "emote_list"  # Sent when the server receives a client's emote list.
    POSITION_TRACKING_DB_SERVER_BROADCAST = "position_tracking_db_server_broadcast"  # Sent when a position tracking DB
    # server broadcast is dispatched to all clients.
    POSITION_TRACKING_DB_CLIENT_REQUEST = "position_tracking_db_client_request"  # Sent when a position tracking
    # database client request is received.
    PACKET_VIOLATION_WARNING = "packet_violation_warning"  # Sent when the client receives an invalid packet.
    ANIMATE_ENTITY = "animate_entity"  # Sent when an entity is animated.
    ITEM_COMPONENT = "item_component"  # Sent when an item component is updated.
    FILTER_TEXT = "filter_text"  # Sent when an item is renamed.
    REQUEST_NETWORK_SETTINGS = "request_network_settings"  # Sent when network settings are requested.
