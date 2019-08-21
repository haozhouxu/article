# 运营部门_测试api容器上线

# 主题
用于描述运营部门_测试api容器上线的说明与步骤

# 内容

1. 修改jenkins的Docker-action配置，新增环境替换变量：{action_port}
2. 修改jenkins的Docker-data配置，新增环境替换变量：{data_port}
3. 修改jenkins的Docker-execute配置，新增环境替换变量：{execute_port}
4. 新增jenkins任务，名字为:Docker-action_test，集成Docker-action
5. 修改Docker-action_test任务：
   1. 修改cd到jenkins的workplace的路径，替换Docker-action为Docker-action_test
   2. 修改{action_port}端口为5006
   3. 修改--tag=action为--tag=action_test
   4. 修改下面action都为action_test
   5. 修改通知的action为action_test
6. 修改nginx的配置项：copy action的配置 
   1. 修改为test/action
   2. 修改端口为5006