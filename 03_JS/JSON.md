# JSON

## 先弄懂这件事

JSON 是用文本表示数据的格式。对象的键和字符串要用双引号，数字和布尔值不用。用 `JSON.parse()` 读取，用 `JSON.stringify()` 生成。

### 写法

- 对象用 `{}`，数组用 `[]`。
- 对象的键和字符串用双引号。数字、布尔值和 `null` 直接写。
- JSON 可以嵌套对象和数组，不能写注释，也不能在最后一项后加逗号。

```json
{"name": "小林", "age": 20, "active": true}
```

### 和 JavaScript 互转

- `JSON.parse(text)` 把 JSON 文本转成 JavaScript 值。
- `JSON.stringify(value)` 把可序列化的 JavaScript 值转成 JSON 文本。
