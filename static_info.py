# !usr/bin/env python
# _*_ coding:utf-8 _*_

MAX_THREAD_COUNT = 10

# https://www.scimagojr.com/journalrank.php?category=2502&area=2500&page=2&total_size=91
BASE_URL = 'https://www.scimagojr.com/journalrank.php'

AREA_CODE = 2500

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

# ps:命名不能有空格，神坑
# sb建表不报错，删表删不掉，用getCollection().renameCollection()重命名
JOURNAL_COLLECTION = "Materials_Science"
MATCH_COLLECTION = "Materials_Science_2"
SUBJECT_AREA = "Materials Science"

LOG_FILE_INFO = './SJR_collect.log'