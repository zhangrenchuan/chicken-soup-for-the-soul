## Buffer 缓冲区

- JS语言本身只有字符串类型. 没有二进制数据类型
- 操作磁盘数据等操作必须使用二进制数据
- Buffer操作内存二进制数据

		new Buffer(size)
		new Buffer(str)
		size: 申请对应长度的空间
		str: 用字符串填充对应长度的空间
		
		字节: 计算机里存储数据最小的单位.
		一个字节代表有8个0/1的二进制数. 显示出来是一个十六位进制的数字
		
		fill(0) 初始化buffer 指填充
		Buffer.toString()获取字符串
		Buffer[0] + 2 第一个字节+2