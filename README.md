![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Skill](https://img.shields.io/badge/type-AI_Skill-purple)

# 库迪咖啡（IC设计产业园店）AI Skill

库迪咖啡（IC设计产业园店）的专属 AI 信息服务 Skill——安装后，你的 AI 助手就能查询库迪咖啡的信息：门店地址、几点开门、有什么活动、能团餐吗、个性化推荐、低卡饮品推荐等。

## 关于库迪咖啡

库迪咖啡（Cotti Coffee）是一家专注于精品咖啡的品牌，IC设计产业园店位于成都郫都区，为咖啡爱好者提供专业的咖啡服务。

| 项目 | 内容 |
| --- | --- |
| 门店名称 | 库迪咖啡（IC设计产业园店） |
| 营业时间 | 工作日 07:30-19:30，周末 08:00-18:00 |
| 门店地址 | 四川省成都市郫都区合作街道合顺路2号IC设计产业园1栋1层底商 |
| 联系电话 | 17708104478 |

## 这个 Skill 能做什么

库迪咖啡（IC设计产业园店）的专属信息服务，包含完整的门店咨询能力：

| 能力 | 你可以问 | 说明 |
| --- | --- | --- |
| 门店信息 | "库迪在哪？""几点开门？" | 地址、营业时间、门店环境 |
| 优惠活动 | "有什么活动？""新客有优惠吗" | 新客福利、日常优惠、群内专享 |
| 团餐服务 | "能团餐吗？""团餐怎么订" | 团餐政策、预定方式、配送服务 |
| 饮品推荐 | "推荐什么？""有什么低卡饮品" | 必点推荐、低卡选择、无茶无咖 |
| 定制服务 | "能少冰吗？""能调节糖度吗" | 糖度、温度 |
| 店内设施 | "有休息区吗？""环境怎么样" | 用餐环境、堂食空间、办公环境 |

## 特色功能

### 🎯 智能避峰引导
当你问"现在人多吗？"或"怎么点单快？"时，AI 会引导你使用库迪小程序提前下单，选择"到店自取"，节省等待时间。

### 🎉 优惠信息聚合
一次性获取所有优惠信息：新客券、特价饮品、群内专享、团餐特惠，确保你享受最优惠的价格。

### 📦 团餐专业咨询
详细了解团餐政策：满10杯赠1杯(不与其他活动叠加使用)、美式咖啡套餐≧20杯85折、3公里内免费配送，AI 会为你计算最划算的方案。

### ☕ 个性化推荐
根据你的需求推荐饮品：必点爆款、低卡选择、无咖啡因选项，总有一款适合你。

## 目录结构

```
cotti-ic-skill/
├── SKILL.md                 # 核心文件：元数据 + Agent 指令
├── skill.json               # 机器可读配置
├── references/              # 参考文档与内嵌 Skill（预留）
├── assets/                  # 模板与示例
│   └── mcp-config-example.json  # MCP 配置示例（适用于所有 MCP 客户端）
├── README.md
└── LICENSE
```

## 安装

### 最简单的方式：告诉你的 AI 助手

直接拷贝下面这句话发给你的 AI 助手：

> 帮我安装库迪咖啡 Skill，仓库地址：https://github.com/collaofatema648-gif/cotti

Agent 会自动克隆仓库并安装到对应的 Skill 目录。

### 其他安装方式

**通过 ClawHub CLI 安装：**

```
npx clawhub install https://github.com/collaofatema648-gif/cotti
```

**手动克隆到 Skill 目录：**

将本仓库克隆到你项目下的 Skill 目录，不同 IDE 对应的路径：

| IDE | Skill 目录 |
| --- | --- |
| Qoder | `.qoder/skills/cotti-ic-skill/` |
| Cursor | `.cursor/skills/cotti-ic-skill/` |
| Trae | `.trae/skills/cotti-ic-skill/` |
| Windsurf | `.windsurf/skills/cotti-ic-skill/` |
| Claude Code | `.claude/skills/cotti-ic-skill/` |
| 通用 | `.agents/skills/cotti-ic-skill/` |

```
# 示例：安装到 Qoder
git clone https://github.com/collaofatema648-gif/cotti.git \
  .qoder/skills/cotti-ic-skill
```

只要目录下有 `SKILL.md`，Agent 下次启动就会自动加载这个 Skill。

## 使用示例

安装成功后，你可以这样与 AI 助手对话：

**查询门店信息**
> 你：库迪咖啡在哪？
> AI：📍 我们店位于 **IC设计产业园1栋1层底商**（合顺路2号，2号门车库入口）。如果您在园区内，下楼即达！

**咨询优惠活动**
> 你：有什么优惠活动？
> AI：🎉 我们有丰富的优惠活动：
> - **新客福利**：扫码领8.8元券
> - **日常优惠**：9.9元特价饮品
> - **群内专享**：咨询门店，扫码进群，周周3.9元
> - **团餐特惠**：满10杯赠1杯(不与其他活动叠加使用)、美式咖啡套餐≧20杯85折

**饮品推荐**
> 你：推荐什么喝的？
> AI：✨ **必点推荐**（闭眼点不踩雷）：
> - 金奖深烘美式
> - 生椰拿铁（轻盈版）
> - 橙C美式
> - 潘帕斯蓝西柚水
>
> 如果您在意卡路里，可以试试金奖美式（≈5kcal）或橙C美式（≈135kcal）。

**团餐咨询**
> 你：能团餐吗？我们要订30杯。
> AI：📦 当然可以！30杯可以享受85折优惠。建议您提前3小时拨打 17708104478 预定，可以享受3公里内免费配送服务。

## 发布平台

- GitHub：https://github.com/collaofatema648-gif/cotti
- ClawHub：（待发布）

## 技术协议

| 项目 | 说明 |
| --- | --- |
| 协议 | MCP (Model Context Protocol) |
| 传输 | Streamable HTTP |
| 部署 | 腾讯云 CloudBase 云函数（可选） |

## MCP 接入方式（可选）

> 注意：直接配置 MCP 服务器仅当次会话生效，不会持久化。推荐使用上方「安装」方式，Skill 安装后永久可用。

在支持 MCP 协议的 AI 客户端中添加以下配置即可接入：

```json
{
  "mcpServers": {
    "cotti-ic-skill": {
      "type": "streamable-http",
      "url": "http://1.14.108.53:3000/mcp"
    }
  }
}
```

## 版本
> 体验版1.0.0 (AI回答仅供参考,更多信息欢迎致电了解唷~)

当前版本：1.0.0

## License

MIT
