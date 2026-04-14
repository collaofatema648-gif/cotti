# 库迪咖啡美团点单脚本使用指南

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置

编辑 `config.json` 文件，填入你的美团 API 密钥（如需要）：

```json
{
  "api_key": "your_api_key_here",
  "api_secret": "your_api_secret_here"
}
```

### 3. 使用示例

#### 查看菜单
```bash
python meituan_order.py --action get_menu
```

#### 搜索饮品
```bash
python meituan_order.py --action search --keyword "拿铁"
```

#### 添加到购物车
```bash
python meituan_order.py --action add \
  --drink_id latte_coconut \
  --quantity 2 \
  --temperature "冰饮" \
  --sugar "半糖" \
  --milk "默认"
```

#### 查看购物车
```bash
python meituan_order.py --action view_cart
```

#### 结算订单
```bash
python meituan_order.py --action checkout
```

#### 查询订单状态
```bash
python meituan_order.py --action status --order_id ORDER123456
```

## Python API 使用

你也可以在 Python 代码中直接使用：

```python
from meituan_order import MeituanOrderClient

# 创建客户端
client = MeituanOrderClient()

# 获取菜单
menu = client.get_menu()
print(menu)

# 搜索饮品
results = client.search_drink("拿铁")
print(results)

# 添加到购物车
client.add_to_cart("latte_coconut", quantity=2)

# 查看购物车
cart = client.view_cart()
print(cart)

# 结算
order = client.checkout()
print(order)
```

## 注意事项

1. **API 密钥**：如果使用真实的美团 API，需要申请开放平台账号
2. **网络连接**：确保网络连接正常
3. **配置文件**：首次使用前请检查配置文件
4. **数据持久化**：订单会保存到 `last_order.json`

## 故障排除

### 问题：无法获取菜单
**解决方案**：
- 检查网络连接
- 确认 API 配置正确
- 查看错误日志

### 问题：添加到购物车失败
**解决方案**：
- 确认饮品 ID 正确
- 检查门店营业时间
- 查看具体错误信息

### 问题：结算失败
**解决方案**：
- 确认购物车不为空
- 检查配送地址是否在范围内
- 联系门店确认

## 联系方式

如有问题，请联系库迪咖啡（IC设计产业园店）：
- 电话：17708104478
- 地址：四川省成都市郫都区合作街道合顺路2号IC设计产业园1栋1层底商
