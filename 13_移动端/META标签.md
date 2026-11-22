# META标签

## 先弄懂这件事

视口设置通常放在页面 `<head>` 里。`width=device-width, initial-scale=1` 让布局宽度对应设备宽度，并设置初始缩放比例。

### 常见写法

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

- `width=device-width` 让布局视口宽度对应设备宽度。
- `initial-scale=1` 把打开页面时的缩放比例设为 1。
- 用户还可以捏合缩放。缩放后，用户此刻看到的范围可能比布局视口小。
