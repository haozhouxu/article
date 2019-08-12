# 致远速联_api接口说明

## 接口：get_file_indicator

### 输入参数
| 字段名 | 字段类型 | 字段中文名 | 是否必须 | 描述 | 默认值 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| files | list | 文件列表 | 是 | | |
| ServerRelativeUrl | string | 文件SharePoint的相对路径 | 是 | | |
| UIVersionLabel | string | 文件版本号 | 否 | | |

### 输入样例
```json
{
    "para":{
        "files":[
            {
                "ServerRelativeUrl":"/sites/main/DocLib8/定义模板/业务定义/业务分析/标准指标/测试指标计算文件.xlsx",
                "UIVersionLabel":"1.0"
            },
            {
                "ServerRelativeUrl":"/sites/main/DocLib8/定义模板/业务定义/业务分析/标准指标/测试指标计算文件.xlsx"
            }
        ]
    }
}
```

### 输出参数
| 字段名 | 字段类型 | 字段中文名 | 描述 |
| :--- | :--- | :--- | :--- |
| re | int | 返回码 | 0：成功，其他：失败 |
| data | list | 解析的内容 |  |

### 输出样例
```json
{
    "re":0,
    "data":[
        {
            "guid":"0123456789",
            "file_name":"测试指标计算文件.xlsx",
            "sheet_name":"直接指标",
            "指标编码":"CW000100",
            "指标缩写":"ldbl",
            "指标名称":"流动比率指标",
            "计算公式":"流动资产合计/流动负债合计",
            "特征":"资本结构指标",
            "适用主体":"机构",
            "适用维度":"财报期",
            "指标描述（意义）":"反应企业基本财务结构是否稳定",
            "计算编码":""
        },
        {
            "guid":"0123456789",
            "file_name":"测试指标计算文件.xlsx",
            "sheet_name":"直接指标",
            "指标编码":"CW000100",
            "指标缩写":"ldbl",
            "指标名称":"流动比率指标",
            "计算公式":"流动资产合计/流动负债合计",
            "特征":"资本结构指标",
            "适用主体":"机构",
            "适用维度":"财报期",
            "指标描述（意义）":"反应企业基本财务结构是否稳定",
            "计算编码":""
        }
    ]
}
```

## 接口：create_sp_folder

### 输入参数
| 字段名 | 字段类型 | 字段中文名 | 是否必须 | 描述 | 默认值 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| site | string | 网站名称 | 否 | | 空字符串 |
| path | string | SharePoint文件夹的相对路径 | 是 | | |

### 输入样例
```json
{
    "para":{
        "path":"Doclib8/xuhaozhou"
    }
}
```

### 输出参数
| 字段名 | 字段类型 | 字段中文名 | 描述 |
| :--- | :--- | :--- | :--- |
| re | int | 返回码 | 0：成功，其他：失败 |
| data | list | 解析的内容 |  |

### 输出样例
```json
{
    "re":0,
    "data":{
        "Name":"xuhaozhou",
        "ServerRelativeUrl":"/sites/main/Doclib8/xuhaozhou"
    }
}
```