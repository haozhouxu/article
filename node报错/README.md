# node报错：：/usr/bin/env:node:没有那个文件或目录

## 概要
本文描述分析和解决这个问题的思路和方案

## 分析
根据提示，找不到node，但是我们已经有创建了软连接:
```
ln -s /usr/node-v10.16.0-linux-x64/bin/node /usr/local/bin/node
ln -s /usr/node-v10.16.0-linux-x64/bin/npm /usr/local/bin/npm
```

那么就是说，系统使用node的时候，不是从下面的路径获取node：
```
/usr/local/bin/
```


查询资料得到，系统是从这个路径获取
```
/usr/bin/node
```

## 解决方案
创建新的软连接
```
ln -s /usr/node-v10.16.0-linux-x64/bin/node /usr/bin/node
ln -s /usr/node-v10.16.0-linux-x64/bin/npm /usr/bin/npm
```

## 总结
根据错误分析问题

## 参考
[【node错误】/usr/bin/env: node: No such file or directory](https://www.cnblogs.com/jwentest/p/8259770.html)