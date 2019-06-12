# 致远速联_通过docker快速搭建elk

## 概要
本文档描述如何通过docker，快速搭建elk，目前用于log，elk包括四个部分：
- elasticsearch
- logstash
- kibana
- filebeat

## 运行环境
- linux
- 安装了docker

## 第一步：搭建elasticsearch
- 拉取镜像，通过以下命令：

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.1.1
```

- 运行镜像：

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -d --name elasticsearch docker.elastic.co/elasticsearch/elasticsearch:7.1.1
```

- 检查是否运行了容器：

```
docker ps
```

- 验证是否正常运行：

```
curl http://localhost:9200
```

- 是否返回一下结果：

```
 { 
   "name" : "29667a6354f1", 
   "cluster_name" : "docker-cluster", 
   "clusteruuid" : "L26w6iQR0GfhMqNapQOKw", 
   "version" : { 
     "number" : "7.1.1", 
     "build_flavor" : "default", 
     "build_type" : "docker", 
     "build_hash" : "7a013de", 
     "build_date" : "2019-05-23T14:04:00.380842Z", 
     "build_snapshot" : false, 
     "lucene_version" : "8.0.0", 
     "minimumwirecompatibility_version" : "6.8.0", 
     "minimumindexcompatibility_version" : "6.0.0-beta1" 
   }, 
   "tagline" : "You Know, for Search" 
 } 
```

注意：
- 操作太快，会提示一下信息，需要等待一会：

```
curl: (52) Empty reply from server
```

## 第二步：搭建kibana
- 拉取镜像：
```
docker pull docker.elastic.co/kibana/kibana:7.1.1
```
- 运行镜像：
```
docker run -p 5601:5601 -d --name kibana -e ELASTICSEARCH_HOSTS=http://172.100.50.38:9200 -e I18N_LOCALE=zh-CN docker.elastic.co/kibana/kibana:7.1.1 
```
- 检查是否运行了容器：
```
docker ps
```
- 验证是否正常运行，通过浏览器运行：
```
http://localhost:5601
```

注意：
- 会出现：Kibana server is not ready yet，因为访问太快。
- The following settings have different default values when using the Docker images:
> server.name  kibana 
> server.host  "0" 
> elasticsearch.hosts  http://elasticsearch:9200 
> xpack.monitoring.ui.container.elasticsearch.enabled  true 
- ELASTICSEARCH_HOSTS不能修改为localhost，因为这样子是容器里面，而elasticsearch和kibana是在不同容器，所以需要制定本机ip

## 第三步：搭建logstash
- 拉取镜像：
```
docker pull docker.elastic.co/logstash/logstash:7.1.1
```
- 新建文件夹：
```
/usr/share/logstash/pipeline/
```
- 新建文件（logstash.conf）：
```
input {
    beats {
        port => 5044
    }
}
output {
    elasticsearch {
        hosts => [ "172.100.50.38:9200" ]
    }
}
```
- 运行镜像：
```
docker run --rm -it -p 5044:5044 -v /usr/share/logstash/pipeline/:/usr/share/logstash/pipeline/ docker.elastic.co/logstash/logstash:7.1.1
```

## 第四步：搭建filebeat
- 拉取镜像：
```
docker pull docker.elastic.co/beats/filebeat:7.1.1
```
- 新建文件夹：
```
/usr/share/filebeat/
```
- 新增：配置文件filebeat.docker.yml:
```
filebeat.inputs:
  - type: log
    paths:
      - /var/lib/docker/containers/*/*.log
  setup.kibana:
    host: "172.100.50.38:5601"
```
- 运行镜像：
```
docker run --name=filebeat -v /var/lib/docker/containers/:/var/lib/docker/containers/:ro -v /usr/share/filebeat/filebeat.docker.yml:/usr/share/filebeat/filebeat.yml docker.elastic.co/beats/filebeat:7.1.1
```

## 验证成果
- 打开浏览器，输入：http://localhost:5601
- 设置index pattern:*
- 选择时间轴
- 确定
- 跳转到discover
- 查看日志