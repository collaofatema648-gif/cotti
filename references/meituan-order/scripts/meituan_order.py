#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
库迪咖啡美团点单引导脚本
正确逻辑：引导用户打开美团App，跳转到库迪咖啡店铺，用户在美团App完成点单
"""

import json
import qrcode
import os
from typing import Dict, Optional


class MeituanOrderGuide:
    """美团点单引导"""

    def __init__(self, config_path: str = "config.json"):
        """初始化引导器"""
        self.config = self._load_config(config_path)

    def _load_config(self, config_path: str) -> dict:
        """加载配置文件"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # 返回默认配置
            return {
                "store_name": "库迪咖啡（IC设计园店）",
                "store_address": "郫都区高新区合顺路2号IC设计产业园1栋1层底商",
                "store_phone": "18181753605",
                "meituan_share_link": "http://dpurl.cn/6ArVHn4z",
                "meituan_search_keyword": "库迪咖啡 IC设计园店"
            }

    def get_store_info(self) -> dict:
        """
        获取店铺信息

        Returns:
            店铺信息字典
        """
        return {
            "store_name": self.config.get("store_name", "库迪咖啡（IC设计园店）"),
            "address": self.config.get("store_address", "郫都区高新区合顺路2号IC设计产业园1栋1层底商"),
            "phone": self.config.get("store_phone", "18181753605"),
            "business_hours": "工作日 07:30-19:30，周末 08:00-18:00"
        }

    def get_meituan_link(self) -> str:
        """
        获取美团店铺分享链接

        Returns:
            美团店铺链接
        """
        return self.config.get("meituan_share_link", "http://dpurl.cn/6ArVHn4z")

    def get_order_guide_with_link(self) -> str:
        """
        获取包含链接的点单指引（用于AI回复）

        Returns:
            包含美团链接的点单指引文本
        """
        link = self.get_meituan_link()
        store_info = self.get_store_info()

        return f"""☕ 好的！为您推荐库迪咖啡的必点饮品：

✨ **必点推荐**（闭眼点不踩雷）
- **金奖深烘美式** ¥12 - 甄选全球金奖阿拉比卡豆
- **生椰拿铁** ¥18 - 轻盈版，口感清爽
- **橙C美式** ¥16 - 维C满满，清爽果咖

📱 **点单方式：**
点击下方链接直接跳转到美团店铺：
{link}

或者：
1. 打开美团 App
2. 搜索「{store_info['store_name']}」
3. 进入店铺选择饮品和规格

💡 **小贴士：**
- 满¥30免配送费
- 新客可领8.8元券
- 建议选择「冰饮/半糖」口味更佳

📍 **店铺信息：**
- 地址：{store_info['address']}
- 电话：{store_info['phone']}
- 营业时间：{store_info['business_hours']}
"""

    def get_quick_reply(self) -> str:
        """
        获取快速回复（简洁版）

        Returns:
            简洁的点单指引
        """
        link = self.get_meituan_link()
        return f"""📱 【美团点单链接】
{link}

点击链接即可在美团App中打开「库迪咖啡（IC设计园店）」完成点单！

☕ 推荐：金奖深烘美式、生椰拿铁、橙C美式
💰 满¥30免配送费 | 新客8.8元券"""

    def get_search_instruction(self) -> str:
        """
        获取搜索指引（备选方案）

        Returns:
            搜索美团店铺的指引
        """
        keyword = self.config.get("meituan_search_keyword", "库迪咖啡 IC设计园店")
        return f"""📱 **美团点单步骤：**

1. 打开美团 App
2. 点击搜索框
3. 输入「{keyword}」
4. 点击进入店铺
5. 选择饮品和规格（温度/糖度/奶制品）
6. 添加到购物车
7. 结算支付

💡 **小贴士：**
- 满¥30免配送费
- 新客可领8.8元券
- 高峰期建议提前下单"""

    def generate_qrcode(self, save_path: str = "meituan_shop_qrcode.png") -> str:
        """
        生成美团店铺二维码

        Args:
            save_path: 保存路径

        Returns:
            二维码文件路径
        """
        link = self.get_meituan_link()
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save(save_path)

            return save_path
        except Exception as e:
            print(f"⚠️ 生成二维码失败: {e}")
            return ""

    def get_drink_recommendations(self) -> dict:
        """
        获取饮品推荐（从MCP获取，这里仅做示例）

        Returns:
            推荐饮品列表
        """
        return {
            "must_try": [
                {"name": "金奖深烘美式", "price": "¥12", "reason": "甄选全球金奖阿拉比卡豆"},
                {"name": "生椰拿铁", "price": "¥18", "reason": "轻盈版，口感清爽"},
                {"name": "橙C美式", "price": "¥16", "reason": "维C满满，清爽果咖"}
            ],
            "low_calorie": [
                {"name": "金奖美式", "price": "¥12", "calorie": "≈5kcal"},
                {"name": "橙C美式", "price": "¥16", "calorie": "≈135kcal"}
            ],
            "no_caffeine": [
                {"name": "杨枝甘露", "price": "¥20"},
                {"name": "黑糖啵啵牛乳", "price": "¥18"}
            ]
        }


def main():
    """主函数 - 命令行接口"""
    import argparse

    parser = argparse.ArgumentParser(description="库迪咖啡美团点单引导")
    parser.add_argument("--action", required=True,
                       choices=["store_info", "link", "guide", "quick", "search", "qrcode", "recommend"],
                       help="操作类型")
    parser.add_argument("--output", default="meituan_shop_qrcode.png", help="二维码输出路径")

    args = parser.parse_args()

    guide = MeituanOrderGuide()

    if args.action == "store_info":
        info = guide.get_store_info()
        print("📍 店铺信息:")
        print(f"店名: {info['store_name']}")
        print(f"地址: {info['address']}")
        print(f"电话: {info['phone']}")
        print(f"营业时间: {info['business_hours']}")

    elif args.action == "link":
        link = guide.get_meituan_link()
        print(f"🔗 美团店铺链接:")
        print(f"{link}")
        print(f"\n💡 用户点击链接即可在美团App中打开店铺")

    elif args.action == "guide":
        guide_text = guide.get_order_guide_with_link()
        print(guide_text)

    elif args.action == "quick":
        quick_text = guide.get_quick_reply()
        print(quick_text)

    elif args.action == "search":
        search_text = guide.get_search_instruction()
        print(search_text)

    elif args.action == "qrcode":
        qrcode_path = guide.generate_qrcode(args.output)
        if qrcode_path:
            print(f"✅ 二维码已生成: {qrcode_path}")
            print(f"💡 用户扫描二维码即可打开美团店铺")
            print(f"🔗 链接: {guide.get_meituan_link()}")

    elif args.action == "recommend":
        recommendations = guide.get_drink_recommendations()
        print("☕ 饮品推荐:")
        print("\n✨ 必点推荐:")
        for drink in recommendations["must_try"]:
            print(f"  - {drink['name']} ({drink['price']})")
            print(f"    {drink['reason']}")

        print("\n💪 低卡选择:")
        for drink in recommendations["low_calorie"]:
            print(f"  - {drink['name']} ({drink['price']}) - {drink['calorie']}")

        print("\n🚫 无咖啡因:")
        for drink in recommendations["no_caffeine"]:
            print(f"  - {drink['name']} ({drink['price']})")


if __name__ == "__main__":
    main()
