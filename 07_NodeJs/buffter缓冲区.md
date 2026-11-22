# Buffer 缓冲区

## 先弄懂这件事

`Buffer` 保存字节，适合处理文件和网络数据。把它转成文字时，需要使用正确的字符编码。

### 从字符串得到字节

```js
const bytes = Buffer.from('你好', 'utf8');
console.log(bytes.length);           // 6 个字节
console.log(bytes.toString('utf8')); // 你好
```

- 一个字节有 8 位。`bytes[0]` 读取第一个字节的数值。
- `Buffer.alloc(4)` 创建一个长度为 4、初始值全为 0 的缓冲区。
- 把字节解码成字符串时，用与生成字节时一致的编码。
