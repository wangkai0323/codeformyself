# coding: utf-8
import logging
import re
from . import api_v1
import random
from .formatter_response import rest_result

main_tag = {
    "ATM": "ATM",
    "SPA": "SPA",
    "wifi": "Wi-Fi",
    "保姆": "保姆",
    "停车": "停车",
    "光疗": "光疗",
    "公寓": "公寓",
    "划船": "划船",
    "别墅": "别墅",
    "壁球": "壁球",
    "复印": "复印",
    "打印": "复印",
    "客房": "客房",
    "套房": "客房",
    "报纸": "报纸",
    "书籍": "报纸",
    "图书": "报纸",
    "拖鞋": "拖鞋",
    "擦鞋": "擦鞋",
    "早餐": "早餐",
    "暖气": "暖气",
    "服务": "服务",
    "染发": "染发",
    "桌游": "桌游",
    "桑拿": "桑拿",
    "水果": "水果",
    "零食": "水果",
    "泳具": "泳具",
    "洗衣": "洗衣",
    "浮潜": "浮潜",
    "浴室": "浴室",
    "海滩": "海滩",
    "沙滩": "海滩",
    "淋浴": "淋浴",
    "滑雪": "滑雪",
    "熨斗": "熨斗",
    "班车": "班车",
    "接车": "班车",
    "送车": "班车",
    "接机": "班车",
    "送机": "班车",
    "瑜伽": "瑜伽",
    "电梯": "电梯",
    "电视": "电视",
    "电话": "电话",
    "监控": "监控",
    "盲文": "盲文",
    "神殿": "神殿",
    "票务": "票务",
    "租车": "租车",
    "空调": "空调",
    "网络": "网络",
    "花园": "花园",
    "赌场": "赌场",
    "酒吧": "酒吧",
    "酒廊": "酒吧",
    "露台": "露台",
    "风扇": "风扇",
    "餐厅": "餐厅",
    "骑马": "骑马",
    "卡拉OK": "卡拉OK",
    "乒乓球": "乒乓球",
    "会议室": "会议室",
    "保龄球": "保龄球",
    "健身": "健身房",
    "吸烟区": "吸烟区",
    "吹风机": "吹风机",
    "夜总会": "夜总会",
    "婴儿": "婴幼儿",
    "宠物": "宠物碗",
    "日光浴": "日光浴",
    "泳池": "游泳池",
    "烘干机": "烘干机",
    "网球场": "网球场",
    "自行车": "自行车",
    "贵宾室": "贵宾室",
    "遮阳伞": "遮阳伞",
    "野餐": "野餐区",
    "主题晚餐": "主题晚餐",
    "看护": "儿童看护",
    "禁烟": "全面禁烟",
    "卫星频道": "卫星频道",
    "温泉": "天然温泉",
    "娱乐设施": "娱乐设施",
    "户外家具": "户外家具",
    "旅游": "旅游咨询",
    "水上": "水上滑梯",
    "沏茶": "沏茶设备",
    "码头": "游船码头",
    "烧烤设施": "烧烤设施",
    "综合": "综合设施",
    "美容中心": "美容中心",
    "行李": "行李寄存",
    "寄存": "行李寄存",
    "货币兑换": "货币兑换",
    "外币": "货币兑换",
    "表演": "音乐表演",
    "风帆": "风帆运动",
    "飞镖": "飞镖运动",
    "无障碍设施": "无障碍设施",
    "羽毛球用具": "羽毛球用具",
    "自动售货机": "自动售货机",
    "高尔夫球场": "高尔夫球场",
}

facilities = {
    "电动车充电站": "综合设施",
    "电视": "卫星频道",
    "滑雪设施": "滑雪",
    "Spa及健康中心": "SPA",
    "住宿方允许客人携带宠物入住，但需事先提出请求。 住宿方可能会收取额外费用。": "其他",
    "在客房享用早餐": "早餐",
    "桌面游戏/拼图": "娱乐设施",
    "街边停车场": "停车",
    "餐厅和酒吧/酒廊": "酒吧",
    "主题晚餐之夜": "其他",
    "旅游/票务服务": "票务",
    "熨衣设备": "熨斗",
    "住宿方于客房提供WiFi，收费标准：每小时 USD  , 。": "Wi-Fi",
    "按摩椅": "SPA",
    "需提前预订：住宿场所设有私人停车设施，收费标准：每日JPY。": "停车",
    "免费WiFi、免费停车": "停车",
    "从机场到酒店的免费接送": "班车",
    "康体设施": "健身房",
    "停车场": "停车",
    "娱乐场": "娱乐设施",
    "趾甲护理": "美容中心",
    "海景": "遮阳伞",
    "天然温泉": "天然温泉",
    "私人海滩区": "海滩",
    "土耳其浴": "淋浴",
    "礼宾服务": "服务",
    "电梯": "电梯",
    "可使用优惠券": "其他",
    "美体按摩（另外付费）": "SPA",
    "健身设施": "健身房",
    "需提前预订：住宿场所设有公共停车设施，收费标准：每日EUR。": "停车",
    "票务服务": "票务",
    "间别墅": "别墅",
    "会议室": "会议室",
    "个室外网球场": "网球场",
    "滑雪装备租赁": "滑雪",
    "室外游泳池（全年开放）": "游泳池",
    "热水浴池/按摩浴缸": "淋浴",
    "网络Wi-Fi": "Wi-Fi",
    "洗衣设施": "熨斗",
    "在海滩": "海滩",
    "大堂 WiFi": "Wi-Fi",
    "机场班车": "班车",
    "免费欧式早餐、免费 WiFi、免费停车": "停车",
    "防过敏客房": "客房",
    "瓶装水": "综合设施",
    "免费儿童俱乐部": "婴幼儿",
    "徒步活动": "其他",
    "免费主题公园班车": "班车",
    "滑雪": "滑雪",
    "SPA及健康中心": "SPA",
    "客房附带露天浴池": "天然温泉",
    "自动售货机（饮品）": "自动售货机",
    "自行车骑行": "自行车",
    "骑马": "骑马",
    "私人浴池": "淋浴",
    "大堂楼层提供上网": "Wi-Fi",
    "游泳池": "游泳池",
    "无线网络": "Wi-Fi",
    "视觉辅助：布莱叶盲文": "盲文",
    "SPA 浴缸": "SPA",
    "染发": "美容中心",
    "带扶手": "综合设施",
    "池边酒吧": "酒吧",
    "客房服务": "服务",
    "无需预订：住宿场所设有私人停车设施，收费标准：每次入住JPY。": "停车",
    "飞镖游戏": "飞镖运动",
    "自动提款机（酒店内部）": "ATM",
    "垂钓": "其他",
    "室外网球场": "网球场",
    "壁球": "壁球",
    "机场接送": "班车",
    "平板电视": "卫星频道",
    "Spa休息区": "SPA",
    "免费停车、免费Wifi": "停车",
    "免费早餐、免费WiFi、免费停车": "停车",
    "露台": "露台",
    "阳光露台": "露台",
    "美发护发": "美容中心",
    "旅游咨询台": "服务",
    "不设停车设施。": "停车",
    "保龄球": "保龄球",
    "网络-WIFI": "Wi-Fi",
    "无需预订：住宿场所设有公共停车设施，收费标准：每日EUR。": "停车",
    "室内网球场和室外网球场": "网球场",
    "豪华轿车或公务车服务": "租车",
    "免费上网、免费停车": "停车",
    "班车服务（免费）": "班车",
    "酒店各处禁烟": "全面禁烟",
    "无法提前预订：住宿附近设有公共停车设施，收费标准：每日EUR。": "停车",
    "室内游泳池和室外游泳池": "游泳池",
    "在客房享用晚餐": "其他",
    "无障碍停车场": "停车",
    "瑜伽课程": "瑜伽",
    "免费火车站接车服务": "班车",
    "共用休息室/电视区": "其他",
    "迷你高尔夫": "高尔夫球场",
    "储物柜": "综合设施",
    "Bar Barolo": "酒吧",
    "风帆运动": "风帆运动",
    "个室外游泳池": "游泳池",
    "家庭间": "客房",
    "区内班车（收费）": "班车",
    "个室内网球场和  个室外网球场": "网球场",
    "户外家具": "户外家具",
    "房内按摩服务": "SPA",
    "婴儿推车": "婴幼儿",
    "公共区电视": "综合设施",
    "免费WiFi": "Wi-Fi",
    "免费自行车": "自行车",
    "无需预订：住宿场所设有公共停车设施，收费标准：每日USD。": "停车",
    "住宿方于公共场所提供WiFi（收费）。": "Wi-Fi",
    "洗衣服务": "洗衣",
    "SPA 服务": "SPA",
    "游乐厅/游戏室": "娱乐设施",
    "接送服务": "班车",
    "大堂壁炉": "综合设施",
    "游戏室": "娱乐设施",
    "书籍、DVD、儿童音乐设施": "报纸",
    "免费海滩小屋": "海滩",
    "叫醒服务": "服务",
    "ATM/银行服务": "ATM",
    "餐厅和池畔酒吧": "餐厅",
    "车站徒步分内": "其他",
    "电风扇": "风扇",
    "全套 SPA 服务": "SPA",
    "温泉税": "其他",
    "宠物碗": "宠物碗",
    "客房内 WiFI": "Wi-Fi",
    "间餐厅和  间池畔酒吧": "餐厅",
    "住宿方于各处提供WiFi，收费标准：每小时 USD  , 。": "Wi-Fi",
    "带监控": "监控",
    "快速办理入住/退房手续": "服务",
    "欢乐时光": "其他",
    "新娘套房": "客房",
    "免费儿童看护/活动": "儿童看护",
    "池畔酒吧": "酒吧",
    "住宿方于客房提供WiFi（免费）。": "Wi-Fi",
    "手部按摩": "SPA",
    "温泉浴": "天然温泉",
    "靠近海滩": "海滩",
    "熨裤机": "熨斗",
    "卡拉OK": "卡拉OK",
    "盥洗盆较低": "其他",
    "温泉": "天然温泉",
    "水果": "水果",
    "酒吧/酒廊": "酒吧",
    "报纸": "报纸",
    "免费班车": "班车",
    "露天浴池": "天然温泉",
    "无障碍服务": "无障碍设施",
    "漂流河和  个室外游泳池": "游泳池",
    "景点或演出门票": "票务",
    "吸烟区": "吸烟区",
    "收费代客停车": "停车",
    "免费区内班车": "班车",
    "免费全套早餐、免费 WiFi、免费停车": "停车",
    "餐厅和间酒吧/酒廊": "餐厅",
    "干洗": "熨斗",
    "家餐厅": "餐厅",
    "花园": "花园",
    "保姆服务": "保姆",
    "理发": "美容中心",
    "婚庆服务": "服务",
    "供应早餐": "早餐",
    "代客停车": "停车",
    "划独木舟": "划船",
    "宠物篮": "宠物碗",
    "海滩": "海滩",
    "游泳池（室外）": "游泳池",
    "无需预订：住宿场所设有私人停车设施，收费标准：每日JPY。": "停车",
    "外币兑换": "货币兑换",
    "网球用品设施": "综合设施",
    "洗衣": "洗衣",
    "清洁服务": "洗衣",
    "需提前预订：住宿场所设有私人停车设施（收费）。": "停车",
    "室外游泳池（季节性开放）": "游泳池",
    "客人可携带宠物入住。 住宿方可能会收取额外费用。": "其他",
    "保险箱": "行李寄存",
    "机场接机": "班车",
    "Spa/养生套餐": "SPA",
    "免费无线网络连接": "Wi-Fi",
    "免费冷热自助式早餐和免费 WiFi": "早餐",
    "间餐厅": "餐厅",
    "自行车租赁（额外收费）": "自行车",
    "坐便器": "其他",
    "接收儿童住宿": "儿童看护",
    "停车设施（车位有限）": "停车",
    "无需预订：住宿场所设有私人停车设施，收费标准：每日USD。": "停车",
    "赌场": "赌场",
    "Spa设施": "SPA",
    "个室外游泳池和  个 SPA 浴缸": "游泳池",
    "网球场": "网球场",
    "个室内游泳池和  个室外游泳池": "游泳池",
    "间公寓": "客房",
    "需提前预订：住宿场所设有私人停车设施，收费标准：每日RUB。": "停车",
    "游泳池（室内）": "游泳池",
    "小时前台": "服务",
    "滚筒式烘干机": "烘干机",
    "餐厅和  间酒吧/酒廊": "酒吧",
    "自行车租赁": "自行车",
    "免费wifi": "Wi-Fi",
    "健身房": "健身房",
    "个网球场": "网球场",
    "间酒吧/酒廊": "酒吧",
    "日光浴躺椅/沙滩椅": "日光浴",
    "SPA": "SPA",
    "水上运动设施（酒店内部）": "水上滑梯",
    "文娱员工": "服务",
    "儿童游泳池": "游泳池",
    "租车服务": "租车",
    "蒸汽房": "淋浴",
    "间餐厅和  间海滩酒吧": "餐厅",
    "室外游泳池和SPA浴缸": "游泳池",
    "滑雪场班车": "班车",
    "私家海滩": "海滩",
    "身体去角质": "SPA",
    "公共交通票": "旅游咨询",
    "盒装午餐": "早餐",
    "厨艺课": "服务",
    "附近免费停车设施": "停车",
    "住宿方于客房提供有线网络，收费标准：每小时 EUR   。": "Wi-Fi",
    "住宿方于商务中心提供WiFi（免费）。": "Wi-Fi",
    "免费儿童看护/活动（专人监督）": "儿童看护",
    "自行车": "自行车",
    "商务设施": "商务中心",
    "部分时段客房送餐服务": "服务",
    "馆内为禁烟": "全面禁烟",
    "班车服务": "班车",
    "免费早餐、免费 WiFi": "Wi-Fi",
    "特别节食菜单（应要求提供）": "服务",
    "无障碍通道": "无障碍设施",
    "带紧急按钮的浴室": "淋浴",
    "擦鞋服务": "擦鞋",
    "保姆服务/儿童看护（收费）": "儿童看护",
    "准许携带宠物": "宠物碗",
    "个室内网球场": "网球场",
    "有露天浴池": "天然温泉",
    "间会议室": "会议室",
    "无障碍设施": "无障碍设施",
    "桑拿": "淋浴",
    "电脑站点": "其他",
    "公共区咖啡/茶": "其他",
    "交通服务": "服务",
    "贵宾室设施": "贵宾室",
    "滑雪用具寄存处": "滑雪",
    "行李储存室": "行李寄存",
    "无需预订：住宿场所设有私人停车设施，收费标准：每日EUR,。": "停车",
    "海滩躺椅": "海滩",
    "内部小超市": "自动售货机",
    "屋顶泳池": "游泳池",
    "空调": "空调",
    "免费即点即煮早餐": "早餐",
    "室外游泳池": "游泳池",
    "大堂免费上网": "Wi-Fi",
    "浴缸或淋浴": "淋浴",
    "大堂免费报纸": "报纸",
    "熨衣服务": "熨斗",
    "户外暖炉": "户外家具",
    "水上乐园": "水上滑梯",
    "间餐厅和  间酒吧/酒廊": "餐厅",
    "夜总会/DJ": "夜总会",
    "公共浴池": "淋浴",
    "独栋/小木屋": "别墅",
    "背部按摩": "SPA",
    "夜间娱乐": "夜总会",
    "服务项目": "服务",
    "内部咖啡店": "沏茶设备",
    "娱乐设施及家庭服务": "娱乐设施",
    "大堂楼层提供 WiFi": "Wi-Fi",
    "自动售货机（零食）": "自动售货机",
    "早餐（收费）": "早餐",
    "室内游泳池": "游泳池",
    "保姆服务/儿童看护": "保姆",
    "餐厅和海滨酒吧": "餐厅",
    "当地文化之旅/体验课": "旅游咨询",
    "免费欧式早餐和免费 WiFi": "早餐",
    "接机（收费）": "班车",
    "自行车（免费）": "自行车",
    "小时健身俱乐部": "健身房",
    "收费自助停车": "停车",
    "楼设有两间岩盘浴": "天然温泉",
    "餐饮服务": "早餐",
    "小时客房送餐服务": "早餐",
    "高尔夫球场": "高尔夫球场",
    "早餐": "早餐",
    "图书馆": "报纸",
    "室内游泳池（全年开放）": "游泳池",
    "儿童看护": "儿童看护",
    "临时艺术展": "其他",
    "住宿方于各处提供WiFi（免费）。": "Wi-Fi",
    "足浴": "SPA",
    "纤体": "美容中心",
    "有线频道": "卫星频道",
    "无法提前预订：住宿场所可提供公共停车设施（免费）。": "停车",
    "浮潜": "浮潜",
    "坐便器较高": "其他",
    "室外游泳池和  个 SPA 浴缸": "桌游",
    "室内游乐区": "娱乐设施",
    "免费保姆服务/儿童看护": "儿童看护",
    "购物中心班车": "班车",
    "停车库": "停车",
    "机场送机": "班车",
    "咖啡不错！": "其他",
    "冷水池": "淋浴",
    "免费洗浴用品": "服务",
    "■kanra lounge": "其他",
    "区内班车": "班车",
    "每日清洁服务": "服务",
    "间餐厅和酒吧/酒廊": "餐厅",
    "免费机场班车": "班车",
    "服务/额外服务": "服务",
    "健身中心": "健身房",
    "海滩小屋": "海滩",
    "住宿方允许客人携带宠物入住，但需事先提出请求。 住宿方不收取额外费用。": "其他",
    "免费自助式早餐和免费 WiFi": "早餐",
    "电话": "电话",
    "发型设计": "美容中心",
    "行李寄存": "行李寄存",
    "内设家餐饮场所": "餐厅",
    "免费即点即煮早餐和免费 WiFi": "早餐",
    "无边泳池": "游泳池",
    "光疗": "光疗",
    "无需预订：住宿场所设有公共停车设施，收费标准：每小时EUR。": "停车",
    "住宿方于各处提供WiFi，收费标准：每小时 AUD  , 。": "Wi-Fi",
    "住宿方于公共场所提供WiFi（免费）。": "Wi-Fi",
    "自动提款机": "ATM",
    "季节性开放的室外游泳池": "游泳池",
    "现场音乐/表演": "音乐表演",
    "健身/Spa更衣室": "SPA",
    "视觉辅助：可触摸图标": "盲文",
    "按摩・SPA设施": "SPA",
    "海滨": "海滩",
    "景观泳池": "游泳池",
    "泳池及康体设施": "游泳池",
    "红酒/香槟": "酒吧",
    "酒店内租车服务": "租车",
    "遮阳伞": "遮阳伞",
    "理发/美容中心": "美容中心",
    "间餐厅和  间酒廊": "餐厅",
    "渡轮码头接驳班车": "班车",
    "全部房间皆设有桧叶木制浴槽。": "淋浴",
    "在私人海滩上": "海滩",
    "大堂免费 WiFi": "Wi-Fi",
    "无法提前预订：住宿附近设有公共停车设施（收费）。": "停车",
    "烧烤设施": "烧烤设施",
    "桑拿浴": "淋浴",
    "儿童自助餐": "儿童看护",
    "免费停车": "停车",
    "无法提前预订：住宿场所设有私人停车设施，收费标准：每日EUR。": "停车",
    "儿童俱乐部": "儿童看护",
    "无需预订：住宿场所设有私人停车设施，收费标准：每日AUD,。": "停车",
    "免费自助式早餐": "早餐",
    "室内游泳池和  个室外游泳池": "游泳池",
    "沏茶/咖啡设备": "沏茶设备",
    "需提前预订：住宿附近设有公共停车设施，有可能收取费用。": "停车",
    "活动设施": "娱乐设施",
    "恒温泳池": "游泳池",
    "小吃吧": "水果",
    "盐水泳池": "游泳池",
    "会议/宴会设施": "会议室",
    "泳池/沙滩毛巾": "游泳池",
    "美甲": "美容中心",
    "接机服务": "班车",
    "无需预订：住宿场所设有私人停车设施，收费标准：每日EUR。": "停车",
    "免费代客购物服务": "服务",
    "无法提前预订：住宿场所可提供私人停车设施（免费）。": "停车",
    "野餐区": "野餐区",
    "Spa及健康中心（额外付费）": "SPA",
    "内部停车场": "停车",
    "客人可携带宠物入住。 住宿方不收取额外费用。": "其他",
    "游泳池盖": "游泳池",
    "儿童泳池": "游泳池",
    "巧克力或饼干": "水果",
    "咖啡馆": "沏茶设备",
    "酒吧": "酒吧",
    "餐厅": "餐厅",
    "机场免费接送": "班车",
    "火车站接车服务": "班车",
    "美容化妆": "美容中心",
    "房内儿童看护服务": "儿童看护",
    "夜总会": "夜总会",
    "商务中心": "商务中心",
    "间客房": "客房",
    "各种不同风格的浴池皆可包场使用，没在使用的浴池可以不限时间使用。": "主题晚餐",
    "小时商务中心": "商务中心",
    "台球": "娱乐设施",
    "无需预订：住宿场所设有公共停车设施，收费标准：每日CZK,。": "停车",
    "内设家餐厅": "餐厅",
    "吹风机": "吹风机",
    "暖气": "暖气",
    "高尔夫球场（公里内）": "高尔夫球场",
    "机场班车（免费）": "班车",
    "前台服务": "服务",
    "大堂免费 WiFi、免费停车": "停车",
    "办理私人登记入住/退房手续": "服务",
    "免费自助式早餐、免费 WiFi、免费停车": "停车",
    "滑雪场专用通道": "滑雪",
    "咖啡很好！": "沏茶设备",
    "蒸汽浴室": "淋浴",
    "免费自助式早餐、大堂免费 WiFi": "早餐",
    "按摩": "SPA",
    "会议场地": "会议中心",
    "无需预订：住宿场所设有私人停车设施，收费标准：每日GBP。": "停车",
    "儿童游乐场": "儿童看护",
    "室内网球场": "网球场",
    "情侣按摩": "SPA",
    "日光浴室": "日光浴",
    "足部按摩": "SPA",
    "宠物可入住": "其他",
    "浴池": "淋浴",
    "自助洗衣设施": "洗衣",
    "身体护理": "SPA",
    "间无烟公寓": "客房",
    "住宿方于各处提供WiFi，收费标准：每小时 EUR  , 。": "Wi-Fi",
    "羽毛球用品设施": "羽毛球用具",
    "禁烟客房": "客房",
    "每日客房清洁服务": "服务",
    "小时健身中心": "健身房",
    "收费保姆服务/儿童看护": "保姆",
    "屋顶露台": "露台",
    "乒乓球": "乒乓球",
    "住宿方于客房提供有线网络，收费标准：每小时 JPY   。": "Wi-Fi",
    "海景客房": "客房",
    "间无烟客房": "客房",
    "室外游泳池和漂流河": "游泳池",
    "小吃吧/熟食店": "水果",
    "DVD 播放器": "娱乐设施",
    "会说多种语言的服务员": "服务",
    "有氧运动": "健身房",
    "颈部按摩": "SPA",
    "夜景客房": "客房",
    "限时前台服务": "服务",
    "免费即点即煮早餐、免费 WiFi、免费停车": "停车",
    "综合设施": "综合设施",
    "卫星频道": "卫星频道",
    "恒温控制空调": "空调",
    "按摩/护理室": "SPA",
    "免费 WiFi、免费停车": "停车",
    "婴儿/儿童看护服务": "婴幼儿",
    "咖啡绝佳！": "沏茶设备",
    "儿童电视频道": "卫星频道",
    "健身俱乐部": "健身房",
    "班车服务（额外收费）": "班车",
    "隔音客房": "客房",
    "咖啡美味！": "沏茶设备",
    "需提前预订：住宿附近设有私人停车设施（收费）。": "停车",
    "在客房内享用早餐": "早餐",
    "免费早餐": "早餐",
    "无需预订：住宿附近设有公共停车设施（收费）。": "停车",
    "熨斗": "熨斗",
    "水上滑梯": "水上滑梯",
    "附淋浴间的浴室": "主题晚餐",
    "全身按摩": "SPA",
    "免费水上乐园": "综合设施",
    "杂货递送": "服务",
    "无需预订：住宿场所设有私人停车设施（收费）。": "停车",
    "唤醒服务": "服务",
    "咖啡完美！": "沏茶设备",
    "儿童餐": "早餐",
    "商店（酒店内部）": "商务中心",
    "迷你吧": "水果",
    "礼拜堂/神殿": "神殿",
    "「大露天浴池」、「竹林之汤」、「昭和之汤」、「七番汤」等。": "其他",
    "无需预订：住宿场所可提供私人停车设施（免费）。": "停车",
    "干洗/洗衣服务": "熨斗",
    "图书室": "报纸",
    "便利店": "自动售货机",
    "小时前台服务": "服务",
    "会议中心": "会议中心",
    "kanra spa": "SPA",
    "住宿方于客房提供WiFi（收费）。": "Wi-Fi",
    "前台保管箱": "行李寄存",
    "免费全套早餐和免费 WiFi": "Wi-Fi",
    "住宿方于客房提供WiFi，收费标准：每小时 JPY   。": "Wi-Fi",
    "间无烟公寓酒店": "客房",
    "大浴池": "主题晚餐",
    "头部按摩": "SPA",
    "店内遍布天然源泉挂流温泉浴池。": "天然温泉",
    "杂货店/便利店": "自动售货机",
    "体育赛事（现场转播）": "卫星频道",
    "游船码头": "游船码头",
    "脸部护理": "美容中心",
    "住宿方于客房提供WiFi，收费标准：每小时 EUR   。": "Wi-Fi",
    "收费的客房内儿童看护": "儿童看护",
    "礼品店/报摊": "报纸",
    "不同的浴池可使用的时间带不同（也有全天候可用的浴池）": "主题晚餐",
    "传真/复印": "电话",
    "拖鞋": "拖鞋",
    "往返机场班车": "班车",
    "私人教练": "健身房",
    "浅水池": "游泳池",
    "免费购物中心班车": "班车",
    "礼品店": "商务中心",
    "网络": "Wi-Fi",
    "送机服务": "班车",
    "美容/美体服务": "美容中心",
    "间公寓酒店": "客房",
    "脱毛服务": "美容中心",
    "盥洗用品": "其他",
    "机场班车（额外收费）": "班车",
    "室内游泳池（季节性开放）": "游泳池",
    "美发沙龙": "美容中心",
    "免费停车场": "停车",
    "户外儿童游乐设施": "娱乐设施",
    "潜水": "浮潜",
    "间餐厅和间酒吧/酒廊": "餐厅",
    "免费 WiFi": "Wi-Fi",
    "付费WiFi": "Wi-Fi",
    "私人浴室": "淋浴",
    "健身课程": "健身房",
}

logger = logging.getLogger(__name__)


@api_v1.route("/facilities", methods=["OPTIONS"])
async def _options(request):
    return rest_result(request, {"data": 200})


@api_v1.post("/facilities")
async def facilities_tags(request):
    logger = logging.getLogger(__name__)
    _facilities = request.json.get("facilities", [])
    for facility in _facilities:
        faci = re.sub(r"\d+", "", facility.get("facility", "")).strip()
        if not faci:
            continue
        if faci not in facilities:
            for k, v in main_tag.items():
                if k in faci:
                    url = v
                    break
            else:
                logger.warning(f"unknown facility : {faci}")
                url = f"facility-{random.randint(1,21)}"
        else:
            if facilities[faci] == "其他":
                url = f"facility-{random.randint(1,21)}"
            else:
                url = facilities[faci]
        facility[
            "image_url"
        ] = f"http://img3.weegotr.com/facilities/{url}.png"
    logger.info(f'_facilities:{_facilities}update success')
    return rest_result(request, {"data": _facilities, 'status': 200})
