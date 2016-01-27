environment
---
3 VM(4 core & 16G ram) on Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (4 core 8 thread)  
Kafka 3 part 3 replica ; pure pykafka client consume performance: 75.5896468163 seconds consuming 1085600 messages   
mongodb 3 shard 1 replica  
total 1085600 records (original file 347MB)  

===

3 worker emit_thread 1 split 1 group 6 output:
---
784370 records  
Spout spend 118.659999847 seconds consuming 1000000 messages  
Spout spend 118.669999838 seconds emitting 1000000 tuples  
Bolt spend 216.998996973 seconds dumping 1000000 records  
The 1th record walks through the topology in 2.0460858345 seconds  
The 1000000th record walks through the topology in 100.38508296 seconds  

---
784370 records  
Spout spend 117.230000019 seconds consuming 1000000 messages  
Spout spend 117.25999999 seconds emitting 1000000 tuples  
Bolt spend 218.165097952 seconds dumping 1000000 records  
The 1th record walks through the topology in 1.42766499519 seconds  
The 1000000th record walks through the topology in 102.362762928 seconds  

---
784370 records  
Spout spend 116.309999943 seconds consuming 1000000 messages  
Spout spend 116.319999933 seconds emitting 1000000 tuples  
Bolt spend 217.772272825 seconds dumping 1000000 records  
The 1th record walks through the topology in 1.47668504715 seconds  
The 1000000th record walks through the topology in 102.93895793 seconds  

===

3 worker emit_thread 1 split 1 group 9 output:
---
784370 records  
Spout spend 121.890000105 seconds consuming 1000000 messages  
Spout spend 121.920000076 seconds emitting 1000000 tuples  
Bolt spend 173.387877226 seconds dumping 1000000 records  
The 1th record walks through the topology in 1.59654593468 seconds  
The 1000000th record walks through the topology in 53.0944230556 seconds  

---
784370 records  
Spout spend 123.369999886 seconds consuming 1000000 messages  
Spout spend 123.399999857 seconds emitting 1000000 tuples  
Bolt spend 171.752408028 seconds dumping 1000000 records  
The 1th record walks through the topology in 4.47231793404 seconds  
The 1000000th record walks through the topology in 52.8547260761 seconds  

---
784370 records
Spout spend 122.770000219 seconds consuming 1000000 messages  
Spout spend 122.78000021 seconds emitting 1000000 tuples  
Bolt spend 175.213042974 seconds dumping 1000000 records  
The 1th record walks through the topology in 2.3935341835 seconds  
The 1000000th record walks through the topology in 54.8365769386 seconds  

===

3 worker emit_thread 1 split 1 group 12 output:
---
784370 records  
Spout spend 125.420000076 seconds consuming 1000000 messages  
Spout spend 125.420000076 seconds emitting 1000000 tuples  
Bolt spend 157.584609985 seconds dumping 1000000 records  
The 1th record walks through the topology in 1.57752108574 seconds  
The 1000000th record walks through the topology in 33.7421309948 seconds  

---
784370 records  
Spout spend 123.119999886 seconds consuming 1000000 messages  
Spout spend 123.129999876 seconds emitting 1000000 tuples  
Bolt spend 157.558741093 seconds dumping 1000000 records  
The 1th record walks through the topology in 1.48584890366 seconds  
The 1000000th record walks through the topology in 35.9245901108 seconds  

---
784370 records  
Spout spend 123.49000001 seconds consuming 1000000 messages  
Spout spend 123.50999999 seconds emitting 1000000 tuples  
Bolt spend 155.505965948 seconds dumping 1000000 records  
The 1th record walks through the topology in 1.57519602776 seconds  
The 1000000th record walks through the topology in 33.5911619663 seconds  

===

3 worker emit_thread 1 split 3 group 6 output:
---
709025 records  
Spout spend 114.710000038 seconds consuming 1000000 messages  
Spout spend 114.720000029 seconds emitting 1000000 tuples  
Bolt spend 193.706103802 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.78900122643 seconds  
The 1000000th record walks through the topology in 82.78510499 seconds  

---
709025 records  
Spout spend 116.49000001 seconds consuming 1000000 messages  
Spout spend 116.519999981 seconds emitting 1000000 tuples  
Bolt spend 191.477756977 seconds dumping 1000000 records  
The 1th record walks through the topology in 13.3878588676 seconds  
The 1000000th record walks through the topology in 88.3756158352 seconds  

---
709025 records  
Spout spend 115.680000067 seconds consuming 1000000 messages  
Spout spend 115.690000057 seconds emitting 1000000 tuples  
Bolt spend 195.906291008 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.33645105362 seconds  
The 1000000th record walks through the topology in 83.5627419949 seconds  

===

3 worker emit_thread 1 split 3 group 9 output:
---
709025 records  
Spout spend 114.190000057 seconds consuming 1000000 messages  
Spout spend 114.200000048 seconds emitting 1000000 tuples  
Bolt spend 157.821233034 seconds dumping 1000000 records  
The 1th record walks through the topology in 6.65663003922 seconds  
The 1000000th record walks through the topology in 50.2878630161 seconds  

---
709025 records  
Spout spend 114.480000019 seconds consuming 1000000 messages  
Spout spend 114.49000001 seconds emitting 1000000 tuples  
Bolt spend 160.637823105 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.64515781403 seconds  
The 1000000th record walks through the topology in 49.8029808998 seconds  

---
stuck @ Split bolt many times (thread not enough?)  

===

3 worker emit_thread 1 split 6 group 6 output:
---
645793 records  
Spout spend 113.78000021 seconds consuming 1000000 messages  
Spout spend 113.7900002 seconds emitting 1000000 tuples  
Bolt spend 177.743953943 seconds dumping 1000000 records  
The 1th record walks through the topology in 6.53059411049 seconds  
The 1000000th record walks through the topology in 70.4945478439 seconds  

---
645793 records  
Spout spend 111.130000114 seconds consuming 1000000 messages  
Spout spend 111.150000095 seconds emitting 1000000 tuples  
Bolt spend 177.60372591 seconds dumping 1000000 records  
The 1th record walks through the topology in 6.64631414413 seconds  
The 1000000th record walks through the topology in 73.1200399399 seconds  

---
645793 records  
Spout spend 114.119999886 seconds consuming 1000000 messages  
Spout spend 114.129999876 seconds emitting 1000000 tuples  
Bolt spend 181.439156055 seconds dumping 1000000 records  
The 1th record walks through the topology in 6.53698897362 seconds  
The 1000000th record walks through the topology in 73.8561451435 seconds  

===

3 worker emit_thread 3 split 3 group 6 output:
---
709593 records  
Spout spend 120.400000095 seconds consuming 1000000 messages  
Spout spend 120.410000086 seconds emitting 1000000 tuples  
Bolt spend 199.53677392 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.58677697182 seconds  
The 1000000th record walks through the topology in 82.7235507965 seconds  

---
717534 records
Spout spend 120.730000019 seconds consuming 1000000 messages  
Spout spend 120.74000001 seconds emitting 1000000 tuples  
Bolt spend 198.961384058 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.37846398354 seconds  
The 1000000th record walks through the topology in 81.6098480225 seconds  

---
709674 records  
Spout spend 120.409999847 seconds consuming 1000000 messages  
Spout spend 120.439999819 seconds emitting 1000000 tuples  
Bolt spend 199.836374044 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.73995089531 seconds  
The 1000000th record walks through the topology in 83.1663250923 seconds  

---
stuck @ Split bolt 1 times (thread not enough?)  

===

3 worker emit_thread 3 split 3 group 9 output:
---
709787 records  
Spout spend 121.799999952 seconds consuming 1000000 messages  
Spout spend 121.829999924 seconds emitting 1000000 tuples  
Bolt spend 159.051470995 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.89870500565 seconds  
The 1000000th record walks through the topology in 41.1501760483 seconds  

---
710070 records  
Spout spend 121.49000001 seconds consuming 1000000 messages  
Spout spend 121.5 seconds emitting 1000000 tuples  
Bolt spend 159.253730059 seconds dumping 1000000 records  
The 1th record walks through the topology in 3.75656604767 seconds  
The 1000000th record walks through the topology in 41.5202960968 seconds  

---
711952 records  
Spout spend 121.159999847 seconds consuming 1000000 messages  
Spout spend 121.159999847 seconds emitting 1000000 tuples  
Bolt spend 159.941496849 seconds dumping 1000000 records  
The 1th record walks through the topology in 5.37320804596 seconds  
The 1000000th record walks through the topology in 44.1547050476 seconds  

---
stuck @ Split bolt 1 times (thread not enough?)

===

3 worker emit_thread 3 split 6 group 6 output:
---
646120 records  
Spout spend 120.960000038 seconds consuming 1000000 messages  
Spout spend 120.970000029 seconds emitting 1000000 tuples  
Bolt spend 188.05143404 seconds dumping 1000000 records  
The 1th record walks through the topology in 7.16098093987 seconds  
The 1000000th record walks through the topology in 74.2524149418 seconds  

---
646114 records
Spout spend 120.549999952 seconds consuming 1000000 messages
Spout spend 120.560000181 seconds emitting 1000000 tuples
Bolt spend 188.576028109 seconds dumping 1000000 records
The 1th record walks through the topology in 7.23381400108 seconds
The 1000000th record walks through the topology in 75.2598421574 seconds  

---
667081 records  
Spout spend 120.200000048 seconds consuming 1000000 messages  
Spout spend 120.210000038 seconds emitting 1000000 tuples  
Bolt spend 188.009760141 seconds dumping 1000000 records  
The 1th record walks through the topology in 10.1889200211 seconds  
The 1000000th record walks through the topology in 77.9986801147 seconds  

===

3 worker emit_thread 3 split 6 group 9 output:
---
647623 records  
Spout spend 121.930000067 seconds consuming 1000000 messages  
Spout spend 121.970000029 seconds emitting 1000000 tuples  
Bolt spend 148.568007946 seconds dumping 1000000 records  
The 1th record walks through the topology in 6.78300619125 seconds  
The 1000000th record walks through the topology in 33.4210140705 seconds  

---
647480 records  
Spout spend 120.660000086 seconds consuming 1000000 messages  
Spout spend 120.670000076 seconds emitting 1000000 tuples  
Bolt spend 151.672669172 seconds dumping 1000000 records  
The 1th record walks through the topology in 6.95689296722 seconds  
The 1000000th record walks through the topology in 37.9695620537 seconds  

---
648759 records  
Spout spend 121.549999952 seconds consuming 1000000 messages  
Spout spend 121.549999952 seconds emitting 1000000 tuples  
Bolt spend 151.277482986 seconds dumping 1000000 records  
The 1th record walks through the topology in 7.17739510536 seconds  
The 1000000th record walks through the topology in 36.9048781395 seconds  

===

3 worker emit_thread 3 split 6 group 12 output:
---
646137 records  
Spout spend 122.900000095 seconds consuming 1000000 messages  
Spout spend 122.910000086 seconds emitting 1000000 tuples  
Bolt spend 138.250850201 seconds dumping 1000000 records  
The 1th record walks through the topology in 6.78896188736 seconds  
The 1000000th record walks through the topology in 22.1398119926 seconds  

---
650712 records  
Spout spend 123.319999933 seconds consuming 1000000 messages  
Spout spend 123.359999895 seconds emitting 1000000 tuples  
Bolt spend 136.419728041 seconds dumping 1000000 records  
The 1th record walks through the topology in 10.1602299213 seconds  
The 1000000th record walks through the topology in 23.2599580288 seconds  

---
652113 records  
Spout spend 121.710000038 seconds consuming 1000000 messages  
Spout spend 121.819999933 seconds emitting 1000000 tuples  
Bolt spend 137.200993061 seconds dumping 1000000 records  
The 1th record walks through the topology in 9.18359088898 seconds  
The 1000000th record walks through the topology in 24.6745839119 seconds  

===