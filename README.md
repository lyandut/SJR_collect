SJR_collect
===
**Microsoft database Processing**


## 环境依赖
**Python 2.7**

**MongoDB 3.6**

## 运行步骤

1. 安装python第三方库
   
   `pip install xxx`
   
   ```
   lxml==4.2.2
	pymongo==3.6.1
	requests==2.18.1
	virtualenv==16.0.0
   ```

2. 克隆到本地仓库
   
   `git clone https://github.com/lyandut/SJR_collect.git` 

3. 运行程序
   
   `python run.py`

## 目录结构
```
├── README.md           
├── static_info.py      // 静态参数配置文件 
├── main.py             // 单线程爬虫程序,用于测试和输出样例
├── run.py              // 运行程序，多线程爬虫 + 写入数据库
├── SJR_mongodb.py      // class SJR_mongodb,提供数据库访问功能
├── SJR_spider.py       // class SJR_spider,爬虫程序
└── logger.py           // class Logger,提供日志记录功能,
                        // 日志写入SJR_collect.log          
```

## 配置说明
### 爬虫参数

以`subject area = Materials Science`为例：

分析url，根据需求修改领域参数`AREA_CODE`和种类参数`CATEGORY_CODE`

Materials Science的`AREA_CODE`为2500，`CATEGORY_CODE`为[2501,2509]

设置`START_CODE`为第一个种类参数，`END_CODE`为最后一个种类参数+1

```python
# https://www.scimagojr.com/journalrank.php?category=2502&area=2500&page=2&total_size=91
BASE_URL = 'https://www.scimagojr.com/journalrank.php'

# subject area
AREA_CODE = 2500

# subject categories
CATEGORY_CODE = {2501: 'Materials Science (miscellaneous)',
                 2502: 'Biomaterials',
                 2503: 'Ceramics and Composites',
                 2504: 'Electronic, Optical and Magnetic Materials',
                 2505: 'Materials Chemistry',
                 2506: 'Metals and Alloys',
                 2507: 'Polymers and Plastics',
                 2508: 'Surfaces, Coatings and Films',
                 2509: 'Nanoscience and Nanotechnology',
                 }
START_CODE = 2501
END_CODE = 2510

```

### 数据库参数

根据自己的需求修改`JOURNAL_COLLECTION`和`MATCH_COLLECTION`

登陆mongodb数据库建立相应的collection

运行程序完毕，两个集合中的结果分别对应两个需求

```python
# ps:命名不能有空格，神坑!
# sb建表不报错，删表删不掉，用getCollection().renameCollection()重命名
JOURNAL_COLLECTION = "Materials_Science"
MATCH_COLLECTION = "Materials_Science_2"
SUBJECT_AREA = "Materials Science"
```

## 成果展示
### 运行截图
原数据集中有大量数据不包含"venue"字段，无法做领域划分匹配

![Alt text](https://github.com/lyandut/SJR_collect/blob/master/Screenshots/run.PNG)
### 需求1
![Alt text](https://github.com/lyandut/SJR_collect/blob/master/Screenshots/demand1.PNG)
### 需求2
![Alt text](https://github.com/lyandut/SJR_collect/blob/master/Screenshots/demand2.PNG)

## 总结

- MongoDB 好用也好坑……

- 以后再写。
