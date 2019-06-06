HOTEL_NAME = '//td[@class="fullgmail"]/table[@class="full"][1]/tr/td/table[2]/tr/td/text()'
ADDRESS = '//td[@class="fullgmail"]/table[@class="full"][1]/tr/td/table[3]/tr/td[2]/span[1]/text()'
PHONE = '//td[@class="fullgmail"]/table[@class="full"][1]/tr/td/table[4]/tr/td/table[1]/tr/td[2]/text()'
RELATED_LINK = '//td[@class="fullgmail"]/table[@class="full"][1]/tr/td/table[4]/tr/td/table/tr/td/a/@href'
RELATED_TEXT = '//td[@class="fullgmail"]/table[@class="full"][1]/tr/td/table[4]/tr/td/table/tr/td/a/text()'
CONFIRM_NUM = '//td[@class="fullgmail"]/table[@class="full"][3]/tr/td/table/tr[1]/td/text()'
GUEST = '//td[@class="fullgmail"]/table[@class="full"][3]/tr/td/table/tr[2]/td/table[1]/tr/td/text()'
CHECK_IN_OUT_DATE = '//td[@class="fullgmail"]/table[@class="full"][3]/tr/td/table/tr[3]/td/table/tr/td/table/tr[1]/td/table[2]/tr/td/text()'
# CHECK_IN_OUT_DATETIME = '//td[@class="fullgmail"]/table[@class="full"][3]/tr/td/table/tr[3]//td/text()'
CHECK_IN_OUT_TIME = '//td[@class="fullgmail"]/table[@class="full"][3]/tr/td/table/tr[3]/td/table/tr/td/table/tr[2]/td/table/tr/td[2]/table/tr/td/text()'
EXPAND_LINK = '//a[@class="linkexpand"]/@href'
EXPAND_TEXT = '//a[@class="linkexpand"]/text()'
ROOM_DETAILS_BASE = '/html/body/table/tr/td/div[2]/table/tr/td/div/table[1]/tr/td'
ROOM_TYPE = ROOM_DETAILS_BASE + '/table[1]/tr/td/table/tr/td/table[2]/tr/td/table[1]/tr/td/text()'
ROOM_TYPE_VALUE = ROOM_DETAILS_BASE + '/table[1]/tr/td/table/tr/td/table[2]/tr/td/table[2]/tr/td/a/text()'
ROOM_NUM_GUEST = ROOM_DETAILS_BASE + '/table[1]/tr/td/table/tr/td/table[3]//td/text()'
GUARANTEED_METHOD = ROOM_DETAILS_BASE + '/table[1]/tr/td/table/tr/td/table[4]//td/text()'
HOTEL_ALERT = ROOM_DETAILS_BASE + '/table[2]//td/text()'
CHARGE_BASE = '/html/body/table/tr/td/div[3]/table/tr/td/div/table[1]/tr/td'
CHARGE_DESCRIPTION = CHARGE_BASE + '/table[1]/tr/td/text()'
RATES = CHARGE_BASE + '/table[2]//td/text()'
TAXES = CHARGE_BASE + '/table[3]//td/text()'
TOTAL = CHARGE_BASE + '/table[4]//td/text()'
OTHER_CHARGE = CHARGE_BASE + '/table[5]//td/text()'
RATE_CANCELLATION_BASE = '/html/body/table/tr/td/div[4]/table/tr/td/div/table[1]/tr/td/table[1]/tr/td'
RATE_CANCELLATION_DETAILS = RATE_CANCELLATION_BASE + '/table[1]'
RATE_GUARANTEE_TITLE = RATE_CANCELLATION_BASE + '/table[2]/tr[1]/td/text()'
RATE_GUARANTEE = RATE_CANCELLATION_BASE + '/table[2]/tr[2]//td/text()'
ADDITION_INFO_TITLE = RATE_CANCELLATION_BASE + '/table[3]/tr[1]/td/text()'
ADDITION_INFO_LINK = RATE_CANCELLATION_BASE + '/table[3]//a/@href'
ADDITION_INFO_TEXT = RATE_CANCELLATION_BASE + '/table[3]//a/text()'
EXCLUSIVE = '/html/body/table/tr/td/div[5]/table/tr/td/div/table[1]/tr/td/table/tr/td/table/tr/td/text()'
CONTACT = '/html/body/table/tr/td/div[6]/table/tr/td/div/table[1]/tr[1]/td/table/tr/td'
CONTACT_1 = CONTACT + '//td/text()'
CONTACT_LINK = CONTACT + '//a/@href'
CONTACT_TEXT = CONTACT + '//a/text()'