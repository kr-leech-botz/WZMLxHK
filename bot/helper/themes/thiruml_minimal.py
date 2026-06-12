#!/usr/bin/env python3
class tamilmlStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = "Owner"
    ST_BN1_URL = "https://t.me/V_Sbotmaker"
    ST_BN2_NAME = "Updates"
    ST_BN2_URL = "https://t.me/Animeworld_zone"
    ST_MSG = """<b><i>ᴛʜɪs ʙᴏᴛ ᴄᴀɴ ᴍɪʀʀᴏʀ ᴀʟʟ ʏᴏᴜʀ ʟɪɴᴋs|ғɪʟᴇs|ᴛᴏʀʀᴇɴᴛs ᴛᴏ ɢᴏᴏɢʟᴇ ᴅʀɪᴠᴇ ᴏʀ ᴀɴʏ ʀᴄʟᴏɴᴇ ᴄʟᴏᴜᴅ ᴏʀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴏʀ ᴛᴏ ᴅᴅʟ sᴇʀᴠᴇʀs.</i></b>
<b><i>ᴛʏᴘᴇ {help_command} ᴛᴏ ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs</i></b>"""
    ST_BOTPM = """<b><i>ɴᴏᴡ, ᴛʜɪs ʙᴏᴛ ᴡɪʟʟ sᴇɴᴅ ᴀʟʟ ʏᴏᴜʀ ғɪʟᴇs ᴀɴᴅ ʟɪɴᴋs ʜᴇʀᴇ. sᴛᴀʀᴛ ᴜsɪɴɢ ...</i></b>"""
    ST_UNAUTH = """<b><i>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀ! ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ WZML-X ᴍɪʀʀᴏʀ-ʟᴇᴇᴄʜ ʙᴏᴛ</i></b>"""
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b><i>Tᴇᴍᴘ Tᴏᴋᴇɴ:</i></b> <code>{token}</code>
<b><i>Vᴀʟɪᴅɪᴛʏ:</i></b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''⌬ <b><i>BOT STATISTICS :</i></b>
┖ <b><i>⏰ Bᴏᴛ Uᴘᴛɪᴍᴇ :</i></b> {bot_uptime}

┎ <b><i>🧠 RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b><i>U :</i></b> {ram_u} | <b><i>💾 F :</i></b> {ram_f} | <b><i>T :</i></b> {ram_t}

┎ <b><i>SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b><i>U :</i></b> {swap_u} | <b><i>💾 F :</i></b> {swap_f} | <b><i>T :</i></b> {swap_t}

┎ <b><i>💾 DISK :</i></b>
┃ {disk_bar} {disk}%
┃ <b><i>📖 Tᴏᴛᴀʟ Dɪsᴋ Rᴇᴀᴅ :</i></b> {disk_read}
┃ <b><i>📝 Tᴏᴛᴀʟ Dɪsᴋ Wʀɪᴛᴇ :</i></b> {disk_write}
┖ <b><i>U :</i></b> {disk_u} | <b><i>💾 F :</i></b> {disk_f} | <b><i>T :</i></b> {disk_t}
    
    '''
    SYS_STATS = '''⌬ <b><i>OS SYSTEM :</i></b>
┠ <b><i>⏰ OS Uᴘᴛɪᴍᴇ :</i></b> {os_uptime}
┠ <b><i>🖥 OS Vᴇʀsɪᴏɴ :</i></b> {os_version}
┖ <b><i>🏛 OS Aʀᴄʜ :</i></b> {os_arch}

⌬ <b><i>NETWORK STATS :</i></b>
┠ <b><i>📤 Uᴘʟᴏᴀᴅ Dᴀᴛᴀ:</i></b> {up_data}
┠ <b><i>📥 Dᴏᴡɴʟᴏᴀᴅ Dᴀᴛᴀ:</i></b> {dl_data}
┠ <b><i>📦 Pᴋᴛs Sᴇɴᴛ:</i></b> {pkt_sent}k
┠ <b><i>📥 Pᴋᴛs Rᴇᴄᴇɪᴠᴇᴅ:</i></b> {pkt_recv}k
┖ <b><i>📊 Tᴏᴛᴀʟ I/O Dᴀᴛᴀ:</i></b> {tl_data}

┎ <b><i>💻 CPU :</i></b>
┃ {cpu_bar} {cpu}%
┠ <b><i>🕒 CPU Fʀᴇǫᴜᴇɴᴄʏ :</i></b> {cpu_freq}
┠ <b><i>⚖️ Sʏsᴛᴇᴍ Aᴠɢ Lᴏᴀᴅ :</i></b> {sys_load}
┠ <b><i>🔢 P-Cᴏʀᴇ(s) :</i></b> {p_core} | <b><i>🔢 V-Cᴏʀᴇ(s) :</i></b> {v_core}
┠ <b><i>🔢 Tᴏᴛᴀʟ Cᴏʀᴇ(s) :</i></b> {total_core}
┖ <b><i>🔢 Usᴀʙʟᴇ CPU(s) :</i></b> {cpu_use}
    '''
    REPO_STATS = '''⌬ <b><i>REPO STATISTICS :</i></b>
┠ <b><i>⏰ Bᴏᴛ Uᴘᴅᴀᴛᴇᴅ :</i></b> {last_commit}
┠ <b><i>🔖 Cᴜʀʀᴇɴᴛ Vᴇʀsɪᴏɴ :</i></b> {bot_version}
┠ <b><i>🔖 Lᴀᴛᴇsᴛ Vᴇʀsɪᴏɴ :</i></b> {lat_version}
┖ <b><i>📝 Lᴀsᴛ CʜᴀɴɢᴇLᴏɢ :</i></b> {commit_details}

⌬ <b><i>REMARKS :</i></b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''⌬ <b><i>BOT LIMITATIONS :</i></b>
┠ <b><i>📥 Dɪʀᴇᴄᴛ Lɪᴍɪᴛ :</i></b> {DL} GB
┠ <b><i>🌊 Tᴏʀʀᴇɴᴛ Lɪᴍɪᴛ :</i></b> {TL} GB
┠ <b><i>☁️ GDʀɪᴠᴇ Lɪᴍɪᴛ :</i></b> {GL} GB
┠ <b><i>🎥 YT-DLP Lɪᴍɪᴛ :</i></b> {YL} GB
┠ <b><i>📜 Pʟᴀʏʟɪsᴛ Lɪᴍɪᴛ :</i></b> {PL}
┠ <b><i>📤 Mᴇɢᴀ Lɪᴍɪᴛ :</i></b> {ML} GB
┠ <b><i>♻️ Cʟᴏɴᴇ Lɪᴍɪᴛ :</i></b> {CL} GB
┖ <b><i>📦 Lᴇᴇᴄʜ Lɪᴍɪᴛ :</i></b> {LL} GB

┎ <b><i>🔑 Tᴏᴋᴇɴ Vᴀʟɪᴅɪᴛʏ :</i></b> {TV}
┠ <b><i>⏱️ Usᴇʀ Tɪᴍᴇ Lɪᴍɪᴛ :</i></b> {UTI} / task
┠ <b><i>🔢 Usᴇʀ Pᴀʀᴀʟʟᴇʟ Tᴀsᴋs :</i></b> {UT}
┖ <b><i>🔢 Bᴏᴛ Pᴀʀᴀʟʟᴇʟ Tᴀsᴋs :</i></b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Restarted Successfully!</i></b>
┠ <b><i>📅 Dᴀᴛᴇ:</i></b> {date}
┠ <b><i>⏰ Tɪᴍᴇ:</i></b> {time}
┠ <b><i>🌐 TɪᴍᴇZᴏɴᴇ:</i></b> {timz}
┖ <b><i>🔖 Vᴇʀsɪᴏɴ:</i></b> {version}'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Task Started</i></b>
┠ <b><i>📥 Mᴏᴅᴇ:</i></b> {Mode}
┖ <b><i>👤 Bʏ:</i></b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b><i>🔗 Sᴏᴜʀᴄᴇ:</i></b>
┖ <b><i>📅 Aᴅᴅᴇᴅ Oɴ:</i></b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>Task Started :</u></b>\n┃\n┖ <b><i>🔗 Lɪɴᴋ:</i></b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b><i>👤 Usᴇʀ :</i></b> {mention} ( #ID{uid} )\n┖ <b><i>🔗 Sᴏᴜʀᴄᴇ :</i></b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>{Name}</i></b>\n┃\n'
    SIZE =                  '┠ <b><i>📏 Sɪᴢᴇ: </i></b>{Size}\n'
    ELAPSE =                '┠ <b><i>⏳ Eʟᴀᴘsᴇᴅ: </i></b>{Time}\n'
    MODE =                  '┠ <b><i>📥 Mᴏᴅᴇ: </i></b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ <b><i>📄 Tᴏᴛᴀʟ Fɪʟᴇs: </i></b>{Files}\n'
    L_CORRUPTED_FILES =     '┠ <b><i>❌ Cᴏʀʀᴜᴘᴛᴇᴅ Fɪʟᴇs: </i></b>{Corrupt}\n'
    L_CC =                  '┖ <b><i>👤 Bʏ: </i></b>{Tag}\n\n'
    PM_BOT_MSG =            '➲ <b><i>File(s) have been Sent above</i></b>'
    L_BOT_MSG =             '➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>'
    L_LL_MSG =              '➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ <b><i>📋 Tʏᴘᴇ: </i></b>{Mimetype}\n'
    M_SUBFOLD =             '┠ <b><i>🗂 SᴜʙFᴏʟᴅᴇʀs: </i></b>{Folder}\n'
    TOTAL_FILES =           '┠ <b><i>📄 Fɪʟᴇs: </i></b>{Files}\n'
    RCPATH =                '┠ <b><i>📂 Pᴀᴛʜ: </i></b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b><i>👤 Bʏ: </i></b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ <b><i>🔄 Pʀᴏᴄᴇssᴇᴅ:</i></b> {Processed}'
    STATUS =            '\n┠ <b><i>📶 Sᴛᴀᴛᴜs:</i></b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b><i>⏱️ ETA:</i></b> {Eta}'
    SPEED =             '\n┠ <b><i>⚡ Sᴘᴇᴇᴅ:</i></b> {Speed}'
    ELAPSED =                                     ' | <b><i>⏳ Eʟᴀᴘsᴇᴅ:</i></b> {Elapsed}'
    ENGINE =            '\n┠ <b><i>⚙️ Eɴɢɪɴᴇ:</i></b> {Engine}'
    STA_MODE =          '\n┠ <b><i>📥 Mᴏᴅᴇ:</i></b> {Mode}'
    SEEDERS =           '\n┠ <b><i>🌱 Sᴇᴇᴅᴇʀs:</i></b> {Seeders} | '
    LEECHERS =                                           '<b><i>📥 Lᴇᴇᴄʜᴇʀs:</i></b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ <b><i>📏 Sɪᴢᴇ: </i></b>{Size}'
    SEED_SPEED =     '\n┠ <b><i>⚡ Sᴘᴇᴇᴅ: </i></b> {Speed} | '
    UPLOADED =                                     '<b><i>⬆️ Uᴘʟᴏᴀᴅᴇᴅ: </i></b> {Upload}'
    RATIO =          '\n┠ <b><i>📊 Rᴀᴛɪᴏ: </i></b> {Ratio} | '
    TIME =                                         '<b><i>⏱️ Tɪᴍᴇ: </i></b> {Time}'
    SEED_ENGINE =    '\n┠ <b><i>⚙️ Eɴɢɪɴᴇ:</i></b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ <b><i>📏 Sɪᴢᴇ: </i></b>{Size}'
    NON_ENGINE =     '\n┠ <b><i>⚙️ Eɴɢɪɴᴇ:</i></b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b><i>👤 Usᴇʀ:</i></b> <code>{User}</code> | '
    ID =                                                        '<b><i>🆔 ID:</i></b> <code>{Id}</code>'
    BTSEL =          '\n┠ <b><i>🔧 Sᴇʟᴇᴄᴛ:</i></b> {Btsel}'
    CANCEL =         '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌬ <b><i>Bot Stats</i></b>\n'
    TASKS =  '┠ <b><i>📋 Tᴀsᴋs:</i></b> {Tasks}\n'
    BOT_TASKS = '┠ <b><i>📋 Tᴀsᴋs:</i></b> {Tasks}/{Ttask} | <b><i>✅ AVL:</i></b> {Free}\n'
    Cpu = '┠ <b><i>💻 CPU:</i></b> {cpu}% | '
    FREE =                      '<b><i>💾 Fʀᴇᴇ:</i></b> {free} [{free_p}%]'
    Ram = '\n┠ <b><i>🧠 RAM:</i></b> {ram}% | '
    uptime =                     '<b><i>⏰ Uᴘᴛɪᴍᴇ:</i></b> {uptime}'
    DL = '\n┖ <b><i>📥 DL:</i></b> {DL}/s | '
    UL =                        '<b><i>📤 UL:</i></b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = '📄 Pᴀɢᴇs\n{Page}'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b><i>📏 Sɪᴢᴇ: </i></b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b><i>📋 Tʏᴘᴇ: </i></b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b><i>🗂 SᴜʙFᴏʟᴅᴇʀs: </i></b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b><i>📄 Fɪʟᴇs: </i></b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b><i>👤 Bʏ: </i></b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b><i>💻 CPU:</i></b> {cpu}% | <b><i>💾 Fʀᴇᴇ:</i></b> {free} [{free_p}%]
┖ <b><i>🧠 RAM:</i></b> {ram} | <b><i>⏰ Uᴘᴛɪᴍᴇ:</i></b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
┎<b><i>👤 Nᴀᴍᴇ :</i></b> {NAME} ( <code>{ID}</code> )
┠<b><i>📛 Usᴇʀɴᴀᴍᴇ :</i></b> {USERNAME}
┠<b><i>🌐 Tᴇʟᴇɢʀᴀᴍ DC :</i></b> {DC}
┖<b><i>🗣 Lᴀɴɢᴜᴀɢᴇ :</i></b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b><i>🎥 YT-DLP Oᴘᴛɪᴏɴs :</i></b> <b><code>{YT}</code></b>
┠<b><i>📅 Dᴀɪʟʏ Tᴀsᴋs :</i></b> <code>{DT}</code> per day
┠<b><i>🤖 Lᴀsᴛ Bᴏᴛ Usᴇᴅ :</i></b> <code>{LAST_USED}</code>
┠<b><i>📱 Usᴇʀ Sᴇssɪᴏɴ :</i></b> <code>{USESS}</code>
┠<b><i>📃 MᴇᴅɪᴀIɴғᴏ Mᴏᴅᴇ :</i></b> <code>{MEDIAINFO}</code>
┠<b><i>💾 Sᴀᴠᴇ Mᴏᴅᴇ :</i></b> <code>{SAVE_MODE}</code>
┖<b><i>📨 Usᴇʀ Bᴏᴛ PM :</i></b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b><i>♻️ RCʟᴏɴᴇ Cᴏɴғɪɢ :</i></b> <i>{RCLONE}</i>
┠<b><i>📛 Mɪʀʀᴏʀ Pʀᴇғɪx :</i></b> <code>{MPREFIX}</code>
┠<b><i>📛 Mɪʀʀᴏʀ Sᴜғғɪx :</i></b> <code>{MSUFFIX}</code>
┠<b><i>🔄 Mɪʀʀᴏʀ Rᴇᴍɴᴀᴍᴇ :</i></b> <code>{MREMNAME}</code>
┠<b><i>🌐 DDL Sᴇʀᴠᴇʀ(s) :</i></b> <i>{DDL_SERVER}</i>
┠<b><i>📂 Usᴇʀ TD Mᴏᴅᴇ :</i></b> <i>{TMODE}</i>
┠<b><i>📂 Tᴏᴛᴀʟ Usᴇʀ TD(s) :</i></b> <i>{USERTD}</i>
┖<b><i>📅 Dᴀɪʟʏ Mɪʀʀᴏʀ :</i></b> <code>{DM}</code> per day'''

    LEECH = '''㊂ <b><u>Leech Settings for {NAME}</u></b>

┎<b><i>📅 Dᴀɪʟʏ Lᴇᴇᴄʜ : </i></b><code>{DL}</code> per day
┠<b><i>📋 Lᴇᴇᴄʜ Tʏᴘᴇ :</i></b> <i>{LTYPE}</i>
┠<b><i>🖼 Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ :</i></b> <i>{THUMB}</i>
┠<b><i>📏 Lᴇᴇᴄʜ Sᴘʟɪᴛ Sɪᴢᴇ :</i></b> <code>{SPLIT_SIZE}</code>
┠<b><i>⚖️ Eǫᴜᴀʟ Sᴘʟɪᴛs :</i></b> <i>{EQUAL_SPLIT}</i>
┠<b><i>📦 Mᴇᴅɪᴀ Gʀᴏᴜᴘ :</i></b> <i>{MEDIA_GROUP}</i>
┠<b><i>📜 Lᴇᴇᴄʜ Cᴀᴘᴛɪᴏɴ :</i></b> <code>{LCAPTION}</code>
┠<b><i>📛 Lᴇᴇᴄʜ Pʀᴇғɪx :</i></b> <code>{LPREFIX}</code>
┠<b><i>📛 Lᴇᴇᴄʜ Sᴜғғɪx :</i></b> <code>{LSUFFIX}</code>
┠<b><i>🗑 Lᴇᴇᴄʜ Dᴜᴍᴘs :</i></b> <code>{LDUMP}</code>
┖<b><i>🔄 Lᴇᴇᴄʜ Rᴇᴍɴᴀᴍᴇ :</i></b> <code>{LREMNAME}</code>'''
