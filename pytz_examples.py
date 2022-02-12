import pytz
import datetime

kiev = 'Europe/Kiev'
tz_kiev = pytz.timezone(kiev)
kiev_time = datetime.datetime.now(tz=tz_kiev)
print(kiev_time)                      # 2022-01-21 09:55:16.061753+02:00

print(datetime.datetime.today())      # 2022-01-21 08:49:28.257910
print(datetime.datetime.now())        # 2022-01-21 08:49:28.257909
print(datetime.datetime.utcnow())     # 2022-01-21 07:49:28.257909

for tz in pytz.all_timezones:
    print(tz)
#     Africa/Abidjan
# Africa/Accra
# Africa/Addis_Ababa
# Africa/Algiers
# Africa/Asmara
# Africa/Asmera
# Africa/Bamako
# Africa/Bangui
# Africa/Banjul
# Africa/Bissau
# Africa/Blantyre
# Africa/Brazzaville
# Africa/Bujumbura
# Africa/Cairo
# Africa/Casablanca
# Africa/Ceuta
# Africa/Conakry
# Africa/Dakar
# Africa/Dar_es_Salaam
# Africa/Djibouti
# Africa/Douala
# Africa/El_Aaiun
# Africa/Freetown
# Africa/Gaborone
# Africa/Harare
# Africa/Johannesburg
# Africa/Juba
# Africa/Kampala
# Africa/Khartoum
# Africa/Kigali
# Africa/Kinshasa
# Africa/Lagos
# Africa/Libreville
# Africa/Lome
# Africa/Luanda
# Africa/Lubumbashi
# Africa/Lusaka
# Africa/Malabo
# Africa/Maputo
# Africa/Maseru
# Africa/Mbabane
# Africa/Mogadishu
# Africa/Monrovia
# Africa/Nairobi
# Africa/Ndjamena
# Africa/Niamey
# Africa/Nouakchott
# Africa/Ouagadougou
# Africa/Porto-Novo
# Africa/Sao_Tome
# Africa/Timbuktu
# Africa/Tripoli
# Africa/Tunis
# Africa/Windhoek
# America/Adak
# America/Anchorage
# America/Anguilla
# America/Antigua
# America/Araguaina
# America/Argentina/Buenos_Aires
# America/Argentina/Catamarca
# America/Argentina/ComodRivadavia
# America/Argentina/Cordoba
# America/Argentina/Jujuy
# America/Argentina/La_Rioja
# America/Argentina/Mendoza
# America/Argentina/Rio_Gallegos
# America/Argentina/Salta
# America/Argentina/San_Juan
# America/Argentina/San_Luis
# America/Argentina/Tucuman
# America/Argentina/Ushuaia
# America/Aruba
# America/Asuncion
# America/Atikokan
# America/Atka
# America/Bahia
# America/Bahia_Banderas
# America/Barbados
# America/Belem
# America/Belize
# America/Blanc-Sablon
# America/Boa_Vista
# America/Bogota
# America/Boise
# America/Buenos_Aires
# America/Cambridge_Bay
# America/Campo_Grande
# America/Cancun
# America/Caracas
# America/Catamarca
# America/Cayenne
# America/Cayman
# America/Chicago
# America/Chihuahua
# America/Coral_Harbour
# America/Cordoba
# America/Costa_Rica
# America/Creston
# America/Cuiaba
# America/Curacao
# America/Danmarkshavn
# America/Dawson
# America/Dawson_Creek
# America/Denver
# America/Detroit
# America/Dominica
# America/Edmonton
# America/Eirunepe
# America/El_Salvador
# America/Ensenada
# America/Fort_Nelson
# America/Fort_Wayne
# America/Fortaleza
# America/Glace_Bay
# America/Godthab
# America/Goose_Bay
# America/Grand_Turk
# America/Grenada
# America/Guadeloupe
# America/Guatemala
# America/Guayaquil
# America/Guyana
# America/Halifax
# America/Havana
# America/Hermosillo
# America/Indiana/Indianapolis
# America/Indiana/Knox
# America/Indiana/Marengo
# America/Indiana/Petersburg
# America/Indiana/Tell_City
# America/Indiana/Vevay
# America/Indiana/Vincennes
# America/Indiana/Winamac
# America/Indianapolis
# America/Inuvik
# America/Iqaluit
# America/Jamaica
# America/Jujuy
# America/Juneau
# America/Kentucky/Louisville
# America/Kentucky/Monticello
# America/Knox_IN
# America/Kralendijk
# America/La_Paz
# America/Lima
# America/Los_Angeles
# America/Louisville
# America/Lower_Princes
# America/Maceio
# America/Managua
# America/Manaus
# America/Marigot
# America/Martinique
# America/Matamoros
# America/Mazatlan
# America/Mendoza
# America/Menominee
# America/Merida
# America/Metlakatla
# America/Mexico_City
# America/Miquelon
# America/Moncton
# America/Monterrey
# America/Montevideo
# America/Montreal
# America/Montserrat
# America/Nassau
# America/New_York
# America/Nipigon
# America/Nome
# America/Noronha
# America/North_Dakota/Beulah
# America/North_Dakota/Center
# America/North_Dakota/New_Salem
# America/Nuuk
# America/Ojinaga
# America/Panama
# America/Pangnirtung
# America/Paramaribo
# America/Phoenix
# America/Port-au-Prince
# America/Port_of_Spain
# America/Porto_Acre
# America/Porto_Velho
# America/Puerto_Rico
# America/Punta_Arenas
# America/Rainy_River
# America/Rankin_Inlet
# America/Recife
# America/Regina
# America/Resolute
# America/Rio_Branco
# America/Rosario
# America/Santa_Isabel
# America/Santarem
# America/Santiago
# America/Santo_Domingo
# America/Sao_Paulo
# America/Scoresbysund
# America/Shiprock
# America/Sitka
# America/St_Barthelemy
# America/St_Johns
# America/St_Kitts
# America/St_Lucia
# America/St_Thomas
# America/St_Vincent
# America/Swift_Current
# America/Tegucigalpa
# America/Thule
# America/Thunder_Bay
# America/Tijuana
# America/Toronto
# America/Tortola
# America/Vancouver
# America/Virgin
# America/Whitehorse
# America/Winnipeg
# America/Yakutat
# America/Yellowknife
# Antarctica/Casey
# Antarctica/Davis
# Antarctica/DumontDUrville
# Antarctica/Macquarie
# Antarctica/Mawson
# Antarctica/McMurdo
# Antarctica/Palmer
# Antarctica/Rothera
# Antarctica/South_Pole
# Antarctica/Syowa
# Antarctica/Troll
# Antarctica/Vostok
# Arctic/Longyearbyen
# Asia/Aden
# Asia/Almaty
# Asia/Amman
# Asia/Anadyr
# Asia/Aqtau
# Asia/Aqtobe
# Asia/Ashgabat
# Asia/Ashkhabad
# Asia/Atyrau
# Asia/Baghdad
# Asia/Bahrain
# Asia/Baku
# Asia/Bangkok
# Asia/Barnaul
# Asia/Beirut
# Asia/Bishkek
# Asia/Brunei
# Asia/Calcutta
# Asia/Chita
# Asia/Choibalsan
# Asia/Chongqing
# Asia/Chungking
# Asia/Colombo
# Asia/Dacca
# Asia/Damascus
# Asia/Dhaka
# Asia/Dili
# Asia/Dubai
# Asia/Dushanbe
# Asia/Famagusta
# Asia/Gaza
# Asia/Harbin
# Asia/Hebron
# Asia/Ho_Chi_Minh
# Asia/Hong_Kong
# Asia/Hovd
# Asia/Irkutsk
# Asia/Istanbul
# Asia/Jakarta
# Asia/Jayapura
# Asia/Jerusalem
# Asia/Kabul
# Asia/Kamchatka
# Asia/Karachi
# Asia/Kashgar
# Asia/Kathmandu
# Asia/Katmandu
# Asia/Khandyga
# Asia/Kolkata
# Asia/Krasnoyarsk
# Asia/Kuala_Lumpur
# Asia/Kuching
# Asia/Kuwait
# Asia/Macao
# Asia/Macau
# Asia/Magadan
# Asia/Makassar
# Asia/Manila
# Asia/Muscat
# Asia/Nicosia
# Asia/Novokuznetsk
# Asia/Novosibirsk
# Asia/Omsk
# Asia/Oral
# Asia/Phnom_Penh
# Asia/Pontianak
# Asia/Pyongyang
# Asia/Qatar
# Asia/Qostanay
# Asia/Qyzylorda
# Asia/Rangoon
# Asia/Riyadh
# Asia/Saigon
# Asia/Sakhalin
# Asia/Samarkand
# Asia/Seoul
# Asia/Shanghai
# Asia/Singapore
# Asia/Srednekolymsk
# Asia/Taipei
# Asia/Tashkent
# Asia/Tbilisi
# Asia/Tehran
# Asia/Tel_Aviv
# Asia/Thimbu
# Asia/Thimphu
# Asia/Tokyo
# Asia/Tomsk
# Asia/Ujung_Pandang
# Asia/Ulaanbaatar
# Asia/Ulan_Bator
# Asia/Urumqi
# Asia/Ust-Nera
# Asia/Vientiane
# Asia/Vladivostok
# Asia/Yakutsk
# Asia/Yangon
# Asia/Yekaterinburg
# Asia/Yerevan
# Atlantic/Azores
# Atlantic/Bermuda
# Atlantic/Canary
# Atlantic/Cape_Verde
# Atlantic/Faeroe
# Atlantic/Faroe
# Atlantic/Jan_Mayen
# Atlantic/Madeira
# Atlantic/Reykjavik
# Atlantic/South_Georgia
# Atlantic/St_Helena
# Atlantic/Stanley
# Australia/ACT
# Australia/Adelaide
# Australia/Brisbane
# Australia/Broken_Hill
# Australia/Canberra
# Australia/Currie
# Australia/Darwin
# Australia/Eucla
# Australia/Hobart
# Australia/LHI
# Australia/Lindeman
# Australia/Lord_Howe
# Australia/Melbourne
# Australia/NSW
# Australia/North
# Australia/Perth
# Australia/Queensland
# Australia/South
# Australia/Sydney
# Australia/Tasmania
# Australia/Victoria
# Australia/West
# Australia/Yancowinna
# Brazil/Acre
# Brazil/DeNoronha
# Brazil/East
# Brazil/West
# CET
# CST6CDT
# Canada/Atlantic
# Canada/Central
# Canada/Eastern
# Canada/Mountain
# Canada/Newfoundland
# Canada/Pacific
# Canada/Saskatchewan
# Canada/Yukon
# Chile/Continental
# Chile/EasterIsland
# Cuba
# EET
# EST
# EST5EDT
# Egypt
# Eire
# Etc/GMT
# Etc/GMT+0
# Etc/GMT+1
# Etc/GMT+10
# Etc/GMT+11
# Etc/GMT+12
# Etc/GMT+2
# Etc/GMT+3
# Etc/GMT+4
# Etc/GMT+5
# Etc/GMT+6
# Etc/GMT+7
# Etc/GMT+8
# Etc/GMT+9
# Etc/GMT-0
# Etc/GMT-1
# Etc/GMT-10
# Etc/GMT-11
# Etc/GMT-12
# Etc/GMT-13
# Etc/GMT-14
# Etc/GMT-2
# Etc/GMT-3
# Etc/GMT-4
# Etc/GMT-5
# Etc/GMT-6
# Etc/GMT-7
# Etc/GMT-8
# Etc/GMT-9
# Etc/GMT0
# Etc/Greenwich
# Etc/UCT
# Etc/UTC
# Etc/Universal
# Etc/Zulu
# Europe/Amsterdam
# Europe/Andorra
# Europe/Astrakhan
# Europe/Athens
# Europe/Belfast
# Europe/Belgrade
# Europe/Berlin
# Europe/Bratislava
# Europe/Brussels
# Europe/Bucharest
# Europe/Budapest
# Europe/Busingen
# Europe/Chisinau
# Europe/Copenhagen
# Europe/Dublin
# Europe/Gibraltar
# Europe/Guernsey
# Europe/Helsinki
# Europe/Isle_of_Man
# Europe/Istanbul
# Europe/Jersey
# Europe/Kaliningrad
# Europe/Kiev
# Europe/Kirov
# Europe/Lisbon
# Europe/Ljubljana
# Europe/London
# Europe/Luxembourg
# Europe/Madrid
# Europe/Malta
# Europe/Mariehamn
# Europe/Minsk
# Europe/Monaco
# Europe/Moscow
# Europe/Nicosia
# Europe/Oslo
# Europe/Paris
# Europe/Podgorica
# Europe/Prague
# Europe/Riga
# Europe/Rome
# Europe/Samara
# Europe/San_Marino
# Europe/Sarajevo
# Europe/Saratov
# Europe/Simferopol
# Europe/Skopje
# Europe/Sofia
# Europe/Stockholm
# Europe/Tallinn
# Europe/Tirane
# Europe/Tiraspol
# Europe/Ulyanovsk
# Europe/Uzhgorod
# Europe/Vaduz
# Europe/Vatican
# Europe/Vienna
# Europe/Vilnius
# Europe/Volgograd
# Europe/Warsaw
# Europe/Zagreb
# Europe/Zaporozhye
# Europe/Zurich
# GB
# GB-Eire
# GMT
# GMT+0
# GMT-0
# GMT0
# Greenwich
# HST
# Hongkong
# Iceland
# Indian/Antananarivo
# Indian/Chagos
# Indian/Christmas
# Indian/Cocos
# Indian/Comoro
# Indian/Kerguelen
# Indian/Mahe
# Indian/Maldives
# Indian/Mauritius
# Indian/Mayotte
# Indian/Reunion
# Iran
# Israel
# Jamaica
# Japan
# Kwajalein
# Libya
# MET
# MST
# MST7MDT
# Mexico/BajaNorte
# Mexico/BajaSur
# Mexico/General
# NZ
# NZ-CHAT
# Navajo
# PRC
# PST8PDT
# Pacific/Apia
# Pacific/Auckland
# Pacific/Bougainville
# Pacific/Chatham
# Pacific/Chuuk
# Pacific/Easter
# Pacific/Efate
# Pacific/Enderbury
# Pacific/Fakaofo
# Pacific/Fiji
# Pacific/Funafuti
# Pacific/Galapagos
# Pacific/Gambier
# Pacific/Guadalcanal
# Pacific/Guam
# Pacific/Honolulu
# Pacific/Johnston
# Pacific/Kanton
# Pacific/Kiritimati
# Pacific/Kosrae
# Pacific/Kwajalein
# Pacific/Majuro
# Pacific/Marquesas
# Pacific/Midway
# Pacific/Nauru
# Pacific/Niue
# Pacific/Norfolk
# Pacific/Noumea
# Pacific/Pago_Pago
# Pacific/Palau
# Pacific/Pitcairn
# Pacific/Pohnpei
# Pacific/Ponape
# Pacific/Port_Moresby
# Pacific/Rarotonga
# Pacific/Saipan
# Pacific/Samoa
# Pacific/Tahiti
# Pacific/Tarawa
# Pacific/Tongatapu
# Pacific/Truk
# Pacific/Wake
# Pacific/Wallis
# Pacific/Yap
# Poland
# Portugal
# ROC
# ROK
# Singapore
# Turkey
# UCT
# US/Alaska
# US/Aleutian
# US/Arizona
# US/Central
# US/East-Indiana
# US/Eastern
# US/Hawaii
# US/Indiana-Starke
# US/Michigan
# US/Mountain
# US/Pacific
# US/Samoa
# UTC
# Universal
# W-SU
# WET
# Zulu

for country in pytz.country_names:
    print(country, pytz.country_names[country], pytz.country_timezones.get(country))
    # AD Andorra ['Europe/Andorra']
    # AE United Arab Emirates ['Asia/Dubai']
    # AF Afghanistan ['Asia/Kabul']
    # AG Antigua & Barbuda ['America/Antigua']
    # AI Anguilla ['America/Anguilla']
    # AL Albania ['Europe/Tirane']
    # AM Armenia ['Asia/Yerevan']
    # AO Angola ['Africa/Luanda']
    # AQ Antarctica ['Antarctica/McMurdo', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Mawson', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok']
    # AR Argentina ['America/Argentina/Buenos_Aires', 'America/Argentina/Cordoba', 'America/Argentina/Salta', 'America/Argentina/Jujuy', 'America/Argentina/Tucuman', 'America/Argentina/Catamarca', 'America/Argentina/La_Rioja', 'America/Argentina/San_Juan', 'America/Argentina/Mendoza', 'America/Argentina/San_Luis', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Ushuaia']
    # AS Samoa (American) ['Pacific/Pago_Pago']
    # AT Austria ['Europe/Vienna']
    # AU Australia ['Australia/Lord_Howe', 'Antarctica/Macquarie', 'Australia/Hobart', 'Australia/Melbourne', 'Australia/Sydney', 'Australia/Broken_Hill', 'Australia/Brisbane', 'Australia/Lindeman', 'Australia/Adelaide', 'Australia/Darwin', 'Australia/Perth', 'Australia/Eucla']
    # AW Aruba ['America/Aruba']
    # AX Åland Islands ['Europe/Mariehamn']
    # AZ Azerbaijan ['Asia/Baku']
    # BA Bosnia & Herzegovina ['Europe/Sarajevo']
    # BB Barbados ['America/Barbados']
    # BD Bangladesh ['Asia/Dhaka']
    # BE Belgium ['Europe/Brussels']
    # BF Burkina Faso ['Africa/Ouagadougou']
    # BG Bulgaria ['Europe/Sofia']
    # BH Bahrain ['Asia/Bahrain']
    # BI Burundi ['Africa/Bujumbura']
    # BJ Benin ['Africa/Porto-Novo']
    # BL St Barthelemy ['America/St_Barthelemy']
    # BM Bermuda ['Atlantic/Bermuda']
    # BN Brunei ['Asia/Brunei']
    # BO Bolivia ['America/La_Paz']
    # BQ Caribbean NL ['America/Kralendijk']
    # BR Brazil ['America/Noronha', 'America/Belem', 'America/Fortaleza', 'America/Recife', 'America/Araguaina', 'America/Maceio', 'America/Bahia', 'America/Sao_Paulo', 'America/Campo_Grande', 'America/Cuiaba', 'America/Santarem', 'America/Porto_Velho', 'America/Boa_Vista', 'America/Manaus', 'America/Eirunepe', 'America/Rio_Branco']
    # BS Bahamas ['America/Nassau']
    # BT Bhutan ['Asia/Thimphu']
    # BV Bouvet Island None
    # BW Botswana ['Africa/Gaborone']
    # BY Belarus ['Europe/Minsk']
    # BZ Belize ['America/Belize']
    # CA Canada ['America/St_Johns', 'America/Halifax', 'America/Glace_Bay', 'America/Moncton', 'America/Goose_Bay', 'America/Blanc-Sablon', 'America/Toronto', 'America/Nipigon', 'America/Thunder_Bay', 'America/Iqaluit', 'America/Pangnirtung', 'America/Atikokan', 'America/Winnipeg', 'America/Rainy_River', 'America/Resolute', 'America/Rankin_Inlet', 'America/Regina', 'America/Swift_Current', 'America/Edmonton', 'America/Cambridge_Bay', 'America/Yellowknife', 'America/Inuvik', 'America/Creston', 'America/Dawson_Creek', 'America/Fort_Nelson', 'America/Whitehorse', 'America/Dawson', 'America/Vancouver']
    # CC Cocos (Keeling) Islands ['Indian/Cocos']
    # CD Congo (Dem. Rep.) ['Africa/Kinshasa', 'Africa/Lubumbashi']
    # CF Central African Rep. ['Africa/Bangui']
    # CG Congo (Rep.) ['Africa/Brazzaville']
    # CH Switzerland ['Europe/Zurich']
    # CI Côte d'Ivoire ['Africa/Abidjan']
    # CK Cook Islands ['Pacific/Rarotonga']
    # CL Chile ['America/Santiago', 'America/Punta_Arenas', 'Pacific/Easter']
    # CM Cameroon ['Africa/Douala']
    # CN China ['Asia/Shanghai', 'Asia/Urumqi']
    # CO Colombia ['America/Bogota']
    # CR Costa Rica ['America/Costa_Rica']
    # CU Cuba ['America/Havana']
    # CV Cape Verde ['Atlantic/Cape_Verde']
    # CW Curaçao ['America/Curacao']
    # CX Christmas Island ['Indian/Christmas']
    # CY Cyprus ['Asia/Nicosia', 'Asia/Famagusta']
    # CZ Czech Republic ['Europe/Prague']
    # DE Germany ['Europe/Berlin', 'Europe/Busingen']
    # DJ Djibouti ['Africa/Djibouti']
    # DK Denmark ['Europe/Copenhagen']
    # DM Dominica ['America/Dominica']
    # DO Dominican Republic ['America/Santo_Domingo']
    # DZ Algeria ['Africa/Algiers']
    # EC Ecuador ['America/Guayaquil', 'Pacific/Galapagos']
    # EE Estonia ['Europe/Tallinn']
    # EG Egypt ['Africa/Cairo']
    # EH Western Sahara ['Africa/El_Aaiun']
    # ER Eritrea ['Africa/Asmara']
    # ES Spain ['Europe/Madrid', 'Africa/Ceuta', 'Atlantic/Canary']
    # ET Ethiopia ['Africa/Addis_Ababa']
    # FI Finland ['Europe/Helsinki']
    # FJ Fiji ['Pacific/Fiji']
    # FK Falkland Islands ['Atlantic/Stanley']
    # FM Micronesia ['Pacific/Chuuk', 'Pacific/Pohnpei', 'Pacific/Kosrae']
    # FO Faroe Islands ['Atlantic/Faroe']
    # FR France ['Europe/Paris']
    # GA Gabon ['Africa/Libreville']
    # GB Britain (UK) ['Europe/London']
    # GD Grenada ['America/Grenada']
    # GE Georgia ['Asia/Tbilisi']
    # GF French Guiana ['America/Cayenne']
    # GG Guernsey ['Europe/Guernsey']
    # GH Ghana ['Africa/Accra']
    # GI Gibraltar ['Europe/Gibraltar']
    # GL Greenland ['America/Nuuk', 'America/Danmarkshavn', 'America/Scoresbysund', 'America/Thule']
    # GM Gambia ['Africa/Banjul']
    # GN Guinea ['Africa/Conakry']
    # GP Guadeloupe ['America/Guadeloupe']
    # GQ Equatorial Guinea ['Africa/Malabo']
    # GR Greece ['Europe/Athens']
    # GS South Georgia & the South Sandwich Islands ['Atlantic/South_Georgia']
    # GT Guatemala ['America/Guatemala']
    # GU Guam ['Pacific/Guam']
    # GW Guinea-Bissau ['Africa/Bissau']
    # GY Guyana ['America/Guyana']
    # HK Hong Kong ['Asia/Hong_Kong']
    # HM Heard Island & McDonald Islands None
    # HN Honduras ['America/Tegucigalpa']
    # HR Croatia ['Europe/Zagreb']
    # HT Haiti ['America/Port-au-Prince']
    # HU Hungary ['Europe/Budapest']
    # ID Indonesia ['Asia/Jakarta', 'Asia/Pontianak', 'Asia/Makassar', 'Asia/Jayapura']
    # IE Ireland ['Europe/Dublin']
    # IL Israel ['Asia/Jerusalem']
    # IM Isle of Man ['Europe/Isle_of_Man']
    # IN India ['Asia/Kolkata']
    # IO British Indian Ocean Territory ['Indian/Chagos']
    # IQ Iraq ['Asia/Baghdad']
    # IR Iran ['Asia/Tehran']
    # IS Iceland ['Atlantic/Reykjavik']
    # IT Italy ['Europe/Rome']
    # JE Jersey ['Europe/Jersey']
    # JM Jamaica ['America/Jamaica']
    # JO Jordan ['Asia/Amman']
    # JP Japan ['Asia/Tokyo']
    # KE Kenya ['Africa/Nairobi']
    # KG Kyrgyzstan ['Asia/Bishkek']
    # KH Cambodia ['Asia/Phnom_Penh']
    # KI Kiribati ['Pacific/Tarawa', 'Pacific/Kanton', 'Pacific/Kiritimati']
    # KM Comoros ['Indian/Comoro']
    # KN St Kitts & Nevis ['America/St_Kitts']
    # KP Korea (North) ['Asia/Pyongyang']
    # KR Korea (South) ['Asia/Seoul']
    # KW Kuwait ['Asia/Kuwait']
    # KY Cayman Islands ['America/Cayman']
    # KZ Kazakhstan ['Asia/Almaty', 'Asia/Qyzylorda', 'Asia/Qostanay', 'Asia/Aqtobe', 'Asia/Aqtau', 'Asia/Atyrau', 'Asia/Oral']
    # LA Laos ['Asia/Vientiane']
    # LB Lebanon ['Asia/Beirut']
    # LC St Lucia ['America/St_Lucia']
    # LI Liechtenstein ['Europe/Vaduz']
    # LK Sri Lanka ['Asia/Colombo']
    # LR Liberia ['Africa/Monrovia']
    # LS Lesotho ['Africa/Maseru']
    # LT Lithuania ['Europe/Vilnius']
    # LU Luxembourg ['Europe/Luxembourg']
    # LV Latvia ['Europe/Riga']
    # LY Libya ['Africa/Tripoli']
    # MA Morocco ['Africa/Casablanca']
    # MC Monaco ['Europe/Monaco']
    # MD Moldova ['Europe/Chisinau']
    # ME Montenegro ['Europe/Podgorica']
    # MF St Martin (French) ['America/Marigot']
    # MG Madagascar ['Indian/Antananarivo']
    # MH Marshall Islands ['Pacific/Majuro', 'Pacific/Kwajalein']
    # MK North Macedonia ['Europe/Skopje']
    # ML Mali ['Africa/Bamako']
    # MM Myanmar (Burma) ['Asia/Yangon']
    # MN Mongolia ['Asia/Ulaanbaatar', 'Asia/Hovd', 'Asia/Choibalsan']
    # MO Macau ['Asia/Macau']
    # MP Northern Mariana Islands ['Pacific/Saipan']
    # MQ Martinique ['America/Martinique']
    # MR Mauritania ['Africa/Nouakchott']
    # MS Montserrat ['America/Montserrat']
    # MT Malta ['Europe/Malta']
    # MU Mauritius ['Indian/Mauritius']
    # MV Maldives ['Indian/Maldives']
    # MW Malawi ['Africa/Blantyre']
    # MX Mexico ['America/Mexico_City', 'America/Cancun', 'America/Merida', 'America/Monterrey', 'America/Matamoros', 'America/Mazatlan', 'America/Chihuahua', 'America/Ojinaga', 'America/Hermosillo', 'America/Tijuana', 'America/Bahia_Banderas']
    # MY Malaysia ['Asia/Kuala_Lumpur', 'Asia/Kuching']
    # MZ Mozambique ['Africa/Maputo']
    # NA Namibia ['Africa/Windhoek']
    # NC New Caledonia ['Pacific/Noumea']
    # NE Niger ['Africa/Niamey']
    # NF Norfolk Island ['Pacific/Norfolk']
    # NG Nigeria ['Africa/Lagos']
    # NI Nicaragua ['America/Managua']
    # NL Netherlands ['Europe/Amsterdam']
    # NO Norway ['Europe/Oslo']
    # NP Nepal ['Asia/Kathmandu']
    # NR Nauru ['Pacific/Nauru']
    # NU Niue ['Pacific/Niue']
    # NZ New Zealand ['Pacific/Auckland', 'Pacific/Chatham']
    # OM Oman ['Asia/Muscat']
    # PA Panama ['America/Panama']
    # PE Peru ['America/Lima']
    # PF French Polynesia ['Pacific/Tahiti', 'Pacific/Marquesas', 'Pacific/Gambier']
    # PG Papua New Guinea ['Pacific/Port_Moresby', 'Pacific/Bougainville']
    # PH Philippines ['Asia/Manila']
    # PK Pakistan ['Asia/Karachi']
    # PL Poland ['Europe/Warsaw']
    # PM St Pierre & Miquelon ['America/Miquelon']
    # PN Pitcairn ['Pacific/Pitcairn']
    # PR Puerto Rico ['America/Puerto_Rico']
    # PS Palestine ['Asia/Gaza', 'Asia/Hebron']
    # PT Portugal ['Europe/Lisbon', 'Atlantic/Madeira', 'Atlantic/Azores']
    # PW Palau ['Pacific/Palau']
    # PY Paraguay ['America/Asuncion']
    # QA Qatar ['Asia/Qatar']
    # RE Réunion ['Indian/Reunion']
    # RO Romania ['Europe/Bucharest']
    # RS Serbia ['Europe/Belgrade']
    # RU Russia ['Europe/Kaliningrad', 'Europe/Moscow', 'Europe/Kirov', 'Europe/Volgograd', 'Europe/Astrakhan', 'Europe/Saratov', 'Europe/Ulyanovsk', 'Europe/Samara', 'Asia/Yekaterinburg', 'Asia/Omsk', 'Asia/Novosibirsk', 'Asia/Barnaul', 'Asia/Tomsk', 'Asia/Novokuznetsk', 'Asia/Krasnoyarsk', 'Asia/Irkutsk', 'Asia/Chita', 'Asia/Yakutsk', 'Asia/Khandyga', 'Asia/Vladivostok', 'Asia/Ust-Nera', 'Asia/Magadan', 'Asia/Sakhalin', 'Asia/Srednekolymsk', 'Asia/Kamchatka', 'Asia/Anadyr']
    # RW Rwanda ['Africa/Kigali']
    # SA Saudi Arabia ['Asia/Riyadh']
    # SB Solomon Islands ['Pacific/Guadalcanal']
    # SC Seychelles ['Indian/Mahe']
    # SD Sudan ['Africa/Khartoum']
    # SE Sweden ['Europe/Stockholm']
    # SG Singapore ['Asia/Singapore']
    # SH St Helena ['Atlantic/St_Helena']
    # SI Slovenia ['Europe/Ljubljana']
    # SJ Svalbard & Jan Mayen ['Arctic/Longyearbyen']
    # SK Slovakia ['Europe/Bratislava']
    # SL Sierra Leone ['Africa/Freetown']
    # SM San Marino ['Europe/San_Marino']
    # SN Senegal ['Africa/Dakar']
    # SO Somalia ['Africa/Mogadishu']
    # SR Suriname ['America/Paramaribo']
    # SS South Sudan ['Africa/Juba']
    # ST Sao Tome & Principe ['Africa/Sao_Tome']
    # SV El Salvador ['America/El_Salvador']
    # SX St Maarten (Dutch) ['America/Lower_Princes']
    # SY Syria ['Asia/Damascus']
    # SZ Eswatini (Swaziland) ['Africa/Mbabane']
    # TC Turks & Caicos Is ['America/Grand_Turk']
    # TD Chad ['Africa/Ndjamena']
    # TF French Southern & Antarctic Lands ['Indian/Kerguelen']
    # TG Togo ['Africa/Lome']
    # TH Thailand ['Asia/Bangkok']
    # TJ Tajikistan ['Asia/Dushanbe']
    # TK Tokelau ['Pacific/Fakaofo']
    # TL East Timor ['Asia/Dili']
    # TM Turkmenistan ['Asia/Ashgabat']
    # TN Tunisia ['Africa/Tunis']
    # TO Tonga ['Pacific/Tongatapu']
    # TR Turkey ['Europe/Istanbul']
    # TT Trinidad & Tobago ['America/Port_of_Spain']
    # TV Tuvalu ['Pacific/Funafuti']
    # TW Taiwan ['Asia/Taipei']
    # TZ Tanzania ['Africa/Dar_es_Salaam']
    # UA Ukraine ['Europe/Simferopol', 'Europe/Kiev', 'Europe/Uzhgorod', 'Europe/Zaporozhye']
    # UG Uganda ['Africa/Kampala']
    # UM US minor outlying islands ['Pacific/Midway', 'Pacific/Wake']
    # US United States ['America/New_York', 'America/Detroit', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Indiana/Indianapolis', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Vevay', 'America/Chicago', 'America/Indiana/Tell_City', 'America/Indiana/Knox', 'America/Menominee', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/North_Dakota/Beulah', 'America/Denver', 'America/Boise', 'America/Phoenix', 'America/Los_Angeles', 'America/Anchorage', 'America/Juneau', 'America/Sitka', 'America/Metlakatla', 'America/Yakutat', 'America/Nome', 'America/Adak', 'Pacific/Honolulu']
    # UY Uruguay ['America/Montevideo']
    # UZ Uzbekistan ['Asia/Samarkand', 'Asia/Tashkent']
    # VA Vatican City ['Europe/Vatican']
    # VC St Vincent ['America/St_Vincent']
    # VE Venezuela ['America/Caracas']
    # VG Virgin Islands (UK) ['America/Tortola']
    # VI Virgin Islands (US) ['America/St_Thomas']
    # VN Vietnam ['Asia/Ho_Chi_Minh']
    # VU Vanuatu ['Pacific/Efate']
    # WF Wallis & Futuna ['Pacific/Wallis']
    # WS Samoa (western) ['Pacific/Apia']
    # YE Yemen ['Asia/Aden']
    # YT Mayotte ['Indian/Mayotte']
    # ZA South Africa ['Africa/Johannesburg']
    # ZM Zambia ['Africa/Lusaka']
    # ZW Zimbabwe ['Africa/Harare']

