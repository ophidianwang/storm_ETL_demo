100000 records in pure pykafka client ; kafka 1 part 1 rep ; auto-commit off:
---
3.34873104095 seconds  
3.31827497482 seconds  
3.47082304955 seconds  

===

100000 records in pure pykafka client ; kafka 1 part 1 rep ; auto-commit on:
---
3.38462710381 seconds  
3.4059150219 seconds  
3.69096517563 seconds  

===

100000 records in spout ; kafka 1 part 1 rep ; storm 1 worker 1 spout 1 split:
---
14.079999923706055 seconds  
15.100000143051147 seconds  
14.06000018119812 seconds  

===

100000 records in spout ; kafka 1 part 1 rep ; storm 3 worker 1 spout 1 split:
---
14.31000018119812  
14.71999979019165  
10.109999895095825  
15.980000019073486  

===

100000 records in spout ; kafka 1 part 1 rep ; storm 3 worker 1 spout 6 split:
---
11.019999980926514 seconds  
10.380000114440918 seconds  
11.700000047683716 seconds  
10.880000114440918 seconds  

===

100000 records in spout ; kafka 1 part 1 rep ; storm 3 worker 1 spout 12 split:
---
11.960000038146973  
12.02999997138977  
11.569999933242798  
11.97000002861023  

===

100000 records ; fluentd 1 ; kafka 1 part 1 rep ; storm 1 worker 1 spout 1 split 1 group 1 output ; mongodb 3 shard:
---
ETL start at 1453263777.71 , 2016-01-20 04:22:57  
Storm Spout get all message from kafka 1453263800.03 , 2016-01-20 04:23:20  
Storm Bolt start dumping to mongodb at 1453263800.96 , 2016-01-20 04:23:20  
ETL end at 1453263851.03 , 2016-01-20 04:24:11  
(fluentd, kafka, spout) spend 22.3202159405 seconds processing 100000 records.  
realtime lag of storm is 0.928633928299 seconds  
(bolt, mongodb) spend 50.0737860203 seconds processing 100000 records.  
ETL spend 73.3226358891 seconds processing 100000 records.  

===

100000 records ; fluentd 1 ; kafka 1 part 1 rep ; storm 3 worker 1 spout 1 split 1 group 1 output ; mongodb 3 shard:
---
ETL start at 1453264271.14 , 2016-01-20 04:31:11  
Storm Spout get all message from kafka 1453264296.12 , 2016-01-20 04:31:36  
Storm Bolt start dumping to mongodb at 1453264296.12 , 2016-01-20 04:31:36  
ETL end at 1453264347.1 , 2016-01-20 04:32:27  
(fluentd, kafka, spout) spend 24.9781107903 seconds processing 100000 records.  
realtime lag of storm is 0.00213623046875 seconds  
(bolt, mongodb) spend 50.9771537781 seconds processing 100000 records.  
ETL spend 75.9574007988 seconds processing 100000 records.  

===

100000 records ; fluentd 1 ; kafka 1 part 1 rep ; storm 3 worker 1 spout 1 split 1 group 3 output ; mongodb 3 shard:  
---
ETL start at 1453263355.68 , 2016-01-20 04:15:55  
Storm Spout get all message from kafka 1453263378.38 , 2016-01-20 04:16:18  
Storm Bolt start dumping to mongodb at 1453263378.82 , 2016-01-20 04:16:18  
ETL end at 1453263395.45 , 2016-01-20 04:16:35  
(fluentd, kafka, spout) spend 22.6990160942 seconds processing 100000 records.  
realtime lag of storm is 0.441990852356 seconds  
(bolt, mongodb) spend 16.6323399544 seconds processing 100000 records.  
ETL spend 39.7733469009 seconds processing 100000 records.  

===

100000 records ; fluentd 1 ; kafka 1 part 1 rep ; storm 3 worker 1 spout 1 split 1 group 6 output ; mongodb 3 shard:
---
ETL start at 1453266603.19 , 2016-01-20 05:10:03  
Storm Spout get all message from kafka 1453266624.68 , 2016-01-20 05:10:24  
Storm Bolt start dumping to mongodb at 1453266624.78 , 2016-01-20 05:10:24  
ETL end at 1453266634.21 , 2016-01-20 05:10:34  
(fluentd, kafka, spout) spend 21.4943470955 seconds processing 100000 records.  
realtime lag of storm is 0.104948043823 seconds  
(bolt, mongodb) spend 9.42479681969 seconds processing 100000 records.  
ETL spend 31.024091959 seconds processing 100000 records.  

===

100000 records ; fluentd 1 ; kafka 1 part 1 rep ; storm 3 worker 1 spout 1 split 1 group 12 output ; mongodb 3 shard:
---
ETL start at 1453272672.42 , 2016-01-20 06:51:12  
Storm Spout get all message from kafka 1453272693.72 , 2016-01-20 06:51:33  
Storm Bolt start dumping to mongodb at 1453272694.29 , 2016-01-20 06:51:34  
ETL end at 1453272702.3 , 2016-01-20 06:51:42  
(fluentd, kafka, spout) spend 21.2981910706 seconds processing 100000 records.  
realtime lag of storm is 0.571376085281 seconds  
(bolt, mongodb) spend 8.00957584381 seconds processing 100000 records.  
ETL spend 29.8791429996 seconds processing 100000 records.  

===

100000 records ; fluentd 1 ; kafka 3 part 1 rep ; storm 1 worker 1 spout 1 split 1 group 1 output ; mongodb 3 shard:
---
ETL start at 1453269598.22 , 2016-01-20 05:59:58  
Storm Spout get all message from kafka 1453269620.32 , 2016-01-20 06:00:20  
Storm Bolt start dumping to mongodb at 1453269620.5 , 2016-01-20 06:00:20  
ETL end at 1453269671.37 , 2016-01-20 06:01:11  
(fluentd, kafka, spout) spend 22.1035878658 seconds processing 100000 records.  
realtime lag of storm is 0.176622152328 seconds  
(bolt, mongodb) spend 50.8684937954 seconds processing 100000 records.  
ETL spend 73.1487038136 seconds processing 100000 records.  

===

100000 records ; fluentd 1 ; kafka 1 part 2 rep ; storm 1 worker 1 spout 1 split 1 group 1 output ; mongodb 3 shard:
---
ETL start at 1453271206.8 , 2016-01-20 06:26:46  
Storm Spout get all message from kafka 1453271226.24 , 2016-01-20 06:27:06  
Storm Bolt start dumping to mongodb at 1453271226.36 , 2016-01-20 06:27:06  
ETL end at 1453271277.84 , 2016-01-20 06:27:57  
(fluentd, kafka, spout) spend 19.4356970787 seconds processing 100000 records.  
realtime lag of storm is 0.117017030716 seconds  
(bolt, mongodb) spend 51.4854400158 seconds processing 100000 records.  
ETL spend 71.0381541252 seconds processing 100000 records.  

===

100000 records ; fluentd 1 ; kafka 3 part 2 rep ; storm 1 worker 1 spout 1 split 1 group 1 output ; mongodb 3 shard:
---
ETL start at 1453271738.51 , 2016-01-20 06:35:38  
Storm Spout get all message from kafka 1453271759.22 , 2016-01-20 06:35:59  
Storm Bolt start dumping to mongodb at 1453271759.27 , 2016-01-20 06:35:59  
ETL end at 1453271810.06 , 2016-01-20 06:36:50  
(fluentd, kafka, spout) spend 20.7069990635 seconds processing 100000 records.  
realtime lag of storm is 0.0506680011749 seconds  
(bolt, mongodb) spend 50.7908120155 seconds processing 100000 records.  
ETL spend 71.5484790802 seconds processing 100000 records.  

===

1085620 records ; fluentd 3 ; kafka 3 part 2 rep ; storm 3 worker 1 spout 6 split 1 group 12 output ; mongodb 3 shard:
---
ETL start at 1453283039.58 , 2016-01-20 09:43:59  
Storm Spout get all message from kafka 1453283329.81 , 2016-01-20 09:48:49  
Storm Bolt start dumping to mongodb at 1453283070.16 , 2016-01-20 09:44:30  
ETL end at 1453283348.64 , 2016-01-20 09:49:08  
(fluentd, kafka, spout) spend 290.231462955 seconds processing 1085420 records.  
realtime lag of storm is -259.650850058 seconds  
(bolt, mongodb) spend 278.477876186 seconds processing 1085420 records.  
ETL spend 309.058489084 seconds processing 1085420 records.  