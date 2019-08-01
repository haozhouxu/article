# filebeat收集多行的日志到一行的日志记录

## 主题
本文用于描述如何把多行的日志，通过filebeat，收集为一条的记录

## 适用场景
- 错误的堆栈

## 操作
- 打开需要收集的日志，我们这边收集的是docker的日志，确定以{"log":"2019-08-01开头的数据为开始的一条记录
```
{"log":"2019-08-01 5:28:45 AM hudson.model.AsyncPeriodicWork$1 run\n","stream":"stderr","time":"2019-08-01T05:28:45.037216425Z"}
...
```
- 找到filebeat.yml文件
- 增加filebeat.inputs下面的节点信息，与type同级
```
multiline.pattern: '^\{"log":"\d{4}-\d{2}-\d{2}'
multiline.negate: true
multiline.match: after
```
- 重启filebeat的容器
- 新收集的数据，则会匹配上面的规则

## 参考资料
- (Manage multiline messages)[https://www.elastic.co/guide/en/beats/filebeat/current/multiline-examples.html]
- (Regular expression support)[https://www.elastic.co/guide/en/beats/filebeat/current/regexp-support.html]