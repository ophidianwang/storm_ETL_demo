environment
---
3 VM(2 core & 16G ram) on Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (4 core 8 thread)  
Kafka 3 part 3 replica ; pure pykafka client consume performance: 75.5896468163 seconds consuming 1085600 messages  
mongodb 3 shard 1 replica  
total 1085600 records (original file 347MB)  

===

3 worker no_emit_thread 1 split 1 group 6 output:
---
761720 records  
Spout spend 183.5 seconds consuming 1000000 messages    
Bolt spend 311.341186047 seconds dumping 1000000 records  
The 1th record walks through the topology in 11.4836730957 seconds  
The 1000000th record walks through the topology in 139.324859142 seconds  

===

3 worker no_emit_thread 3 split 1 group 6 output:
---
780403 records  
Spout spend 216.159999847 seconds consuming 1000000 messages  
Bolt spend 311.73939085 seconds dumping 1000000 records  
The 1th record walks through the topology in 14.202409029 seconds  
The 1000000th record walks through the topology in 109.781800032 seconds  

===

3 worker no_emit_thread 6 split 1 group 6 output:
---
769839 records  
Spout spend 211.950000048 seconds consuming 1000000 messages  
Bolt spend 321.58140111 seconds dumping 1000000 records  
The 1th record walks through the topology in 7.8164019585 seconds  
The 1000000th record walks through the topology in 117.44780302 seconds  

===

6 worker no_emit_thread 6 split 1 group 6 output:
---
763080 records  
Spout spend 233.650000095 seconds consuming 1000000 messages    
Bolt spend 364.19163394 seconds dumping 1000000 records  
The 1th record walks through the topology in 7.7955591679 seconds  
The 1000000th record walks through the topology in 138.337193012 seconds  

===

3 worker no_emit_thread 1 split 3 group 6 output:
---
683537 records
Spout spend 184.410000086 seconds consuming 1000000 messages    
Bolt spend 301.542105198 seconds dumping 1000000 records  
The 1th record walks through the topology in 9.9622209072 seconds  
The 1000000th record walks through the topology in 127.094326019 seconds  

===

3 worker no_emit_thread 3 split 3 group 6 output:
---
692999 records  
Spout spend 262.920000076 seconds consuming 1000000 messages    
Bolt spend 328.571909904 seconds dumping 1000000 records  
The 1th record walks through the topology in 9.5790441036 seconds  
The 1000000th record walks through the topology in 75.2309539318 seconds  

===

3 worker no_emit_thread 3 split 6 group 6 output:
---
623327 records  
Spout spend 260.519999981 seconds consuming 1000000 messages  
Bolt spend 305.347239971 seconds dumping 1000000 records  
The 1th record walks through the topology in 11.2063760757 seconds  
The 1000000th record walks through the topology in 56.033616066 seconds  

===

3 worker emit_thread 1 split 1 group 6 output:
---
Spout spend 125.630000114 seconds consuming 1000000 messages  
Spout spend 125.650000095 seconds emitting 1000000 tuples  

---
stuck @ Split bolt 3 times  (often)  

===

3 worker emit_thread 1 split 3 group 6 output:
---
683537 records  
Spout spend 132.270000219 seconds consuming 1000000 messages  
Spout spend 132.350000143 seconds emitting 1000000 tuples  
Bolt spend 410.024453878 seconds dumping 1000000 records  
The 1th record walks through the topology in 9.9584171772 seconds  
The 1000000th record walks through the topology in 287.712870836 seconds  

---
stuck @ Split bolt 1 times  (seldom, and will finish jos after a while)  

===

3 worker emit_thread 1 split 6 group 6 output:
---
623120 records  
Spout spend 128.579999924 seconds consuming 1000000 messages  
Spout spend 128.579999924 seconds emitting 1000000 tuples  
Bolt spend 271.754601955 seconds dumping 1000000 records  
The 1th record walks through the topology in 9.2969079018 seconds  
The 1000000th record walks through the topology in 152.471509933 seconds  

---
623075 records  
Spout spend 178.130000114 seconds consuming 1000000 messages  
Spout spend 178.180000067 seconds emitting 1000000 tuples  
Bolt spend 296.51628089 seconds dumping 1000000 records  
The 1th record walks through the topology in 10.0786471367 seconds  
The 1000000th record walks through the topology in 128.464927912 seconds  

---
623075 records
Spout spend 134.900000095 seconds consuming 1000000 messages
Spout spend 134.920000076 seconds emitting 1000000 tuples
Bolt spend 282.678925991 seconds dumping 1000000 records
The 1th record walks through the topology in 10.1083900928 seconds
The 1000000th record walks through the topology in 157.887315989 seconds

---
648329 records  
Spout spend 137.019999981 seconds consuming 1000000 messages  
Spout spend 137.029999971 seconds emitting 1000000 tuples  
Bolt spend 299.633217096 seconds dumping 1000000 records  
The 1th record walks through the topology in 19.8444778919 seconds  
The 1000000th record walks through the topology in 182.457695007 seconds  

---
stuck @ Split/Group bolt 2 times  

---

===

3 worker emit_thread 3 split 3 group 6 output:
---
626736 records  
Spout spend 192.230000019 seconds consuming 1000000 messages  
Spout spend 192.24000001 seconds emitting 1000000 tuples  
Bolt spend 281.229850054 seconds dumping 1000000 records  
The 1th record walks through the topology in 13.1629669666 seconds  
The 1000000th record walks through the topology in 102.162817001 seconds  

---
exception @ spout many times  (often) (about thread)  

===

3 worker emit_thread 3 split 6 group 6 output:
---
645980 records  
Spout spend 167.620000124 seconds consuming 1000000 messages  
Spout spend 167.630000114 seconds emitting 1000000 tuples  
Bolt spend 273.025521994 seconds dumping 1000000 records  
The 1th record walks through the topology in 9.6930260658 seconds  
The 1000000th record walks through the topology in 115.098547935 seconds  

---
682394 records  
Spout spend 154.330000162 seconds consuming 1000000 messages  
Spout spend 154.360000134 seconds emitting 1000000 tuples  
Bolt spend 276.000237942 seconds dumping 1000000 records  
The 1th record walks through the topology in 11.627956152 seconds  
The 1000000th record walks through the topology in 133.298193932 seconds  

---
636594 records  
Spout spend 178.760000229 seconds consuming 1000000 messages  
Spout spend 178.770000219 seconds emitting 1000000 tuples  
Bolt spend 270.807075977 seconds dumping 1000000 records  
The 1th record walks through the topology in 14.7744090557 seconds  
The 1000000th record walks through the topology in 106.821484804 seconds  

===

3 worker emit_thread 3 split 6 group 12 output:
---
stuck @ Split bolt many times  (often)  
thread not enough maybe  

