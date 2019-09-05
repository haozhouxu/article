# Docker学习笔记

## 修改docker的默认时区
- 编写Dockerfile的时候，添加下面两句

```
RUN rm -f /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```
![dockerfile](images/1.png)

- docker的时间

![dockerfile](images/2.png)

- 服务日志的时间

![dockerfile](images/3.png)