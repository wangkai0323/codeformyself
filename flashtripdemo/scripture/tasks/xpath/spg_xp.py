RELATED_LINKS = '//*[@id="backgroundtable"]/tr/td/table[2]/tr/td/table[' \
                '2]/tr/td/table/tr/td/table/tr/td/table/tr/td/table/tr/td[' \
                '2]//a/@href'
RELATED_TEXT = '//*[@id="backgroundtable"]/tr/td/table[2]/tr/td/table[' \
                '2]/tr/td/table/tr/td/table/tr/td/table/tr/td/table/tr/td[' \
                '2]//a/text()'
ADDRESS_BASE = '//*[@id="backgroundtable"]/tr/td/table[2]/tr/td/table[1]/tr/td/table/tr/td/table/tr/td/table/tr/td/table/tr/td[2]/table/tr/td/table'
HOTEL_NAME = ADDRESS_BASE + '/tr[1]/td/a/text()'
HOTEL_LINK = ADDRESS_BASE + '/tr[1]/td/a/@href'
ADDRESS = '//span[@class="ios_body"]/text()'  # the first two |CONFIRM_NUM 4
PHONE = '//span[@class="ios_body"]/a/text()'
FAX = '//span[@class="faxMobileView"]/text()'
RESERVATION_BASE = '//*[@id="backgroundtable"]/tr/td/table[4]/tr/td/table/tr/td/table/tr/td/table/tr/td[1]/table/tr/td/table[1]/tr/td/table[2]/tr/td/table[1]'
RESERVATION_INFO_KEYS = RESERVATION_BASE + '/tr/td/table/tr/td/table/tr/td[1]/text()'
RESERVATION_INFO_VALUES = RESERVATION_BASE + '/tr/td/table/tr/td/table/tr/td[2]/text()'
EXPLANATION = RESERVATION_BASE + '/tr[2]/td/text()'
ACCOMMODATION_BASE = '//*[@id="backgroundtable"]/tr/td/table[4]/tr/td/table/tr/td/table/tr/td/table/tr/td[2]/table/tr/td/table/tr/td/table[2]/tr/td/table'
ACCOMMODATION_INFO_KEYS = ACCOMMODATION_BASE + '/tr[1]/td/table/tr/td/table/tr/td[1]/text()'
ACCOMMODATION_INFO_VALUES = ACCOMMODATION_BASE + '/tr[1]/td/table/tr/td/table/tr/td[2]/text()'
ACCOMMODATION_DETAILS = ACCOMMODATION_BASE + '/tr[2]/td/table/tr/td/table/tr/td[2]/text()'
ROOM_DESCRIPTION = ACCOMMODATION_BASE + '/tr[2]/td/table/tr/td/table/tr[1]/td/text()'
RATE_BASE = '//*[@id="backgroundtable"]/tr/td/table[4]/tr/td/table/tr/td/table/tr/td/table/tr/td[1]/table/tr/td/table[2]/tr/td/table[2]/tr/td/table'
CURRENCY = '//res_currency_cd/text()'
PER_ROOM_RATE = '//res_room_rate/text()'
TOTAL_ROOM_RATE = '//res_room_rate_total/text()'
OTHER_COST_KEYS = RATE_BASE + '/tr[3]/td/table/tr[4]/td/table/tr/td/table/tr/td[1]/text()'
OTHER_COST_VALUES_1 = RATE_BASE + '/tr[3]/td/table/tr[4]/td/table/tr/td/table/tr/td[2]/text()'
OTHER_COST_VALUES_2 = RATE_BASE + '/tr[3]/td/table/tr[4]/td/table/tr/td/table/tr/td[3]/text()'
ESTIMATED_TOTAL_1 = '//summary_total_per_room_per_night/text()'
ESTIMATED_TOTAL_2 = '//summary_total_amount/text()'
EXPLANATION_PRICE = RATE_BASE + '/tr[4]/td/text()'
CANCELLATION = RATE_BASE + '/tr[6]/td/text()'
OTHER_INFO = RATE_BASE + '/tr[7]/td/text()'
PRIVACY_BASE = '//*[@id="backgroundtable"]/tr/td/table[5]/tr/td/table/tr/td/table/tr/td/table[2]/tr/td/table'
PRIVACY = PRIVACY_BASE + '/tr/td'
PRIVACY_LINK = PRIVACY_BASE + '//a/@href'
PRIVACY_LINK_TEXT = PRIVACY_BASE + '//a/text()'
DISCLOSURE_BASE = '//*[@id="backgroundtable"]/tr/td/table[6]/tr/td/table/tr/td/table/tr/td/table[2]/tr/td/table'
DISCLOSURE = DISCLOSURE_BASE + '/tr/td'
DISCLOSURE_LINK = DISCLOSURE_BASE + '/tr/td/a/@href'
DISCLOSURE_TEXT = DISCLOSURE_BASE + '/tr/td/a/text()'