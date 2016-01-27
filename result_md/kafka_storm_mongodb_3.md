environment
---
3 VM(6 core & 16G ram) on Intel(R) Core(TM) i7-4790 CPU @ 3.60GHz (4 core 8 thread)  
Kafka 3 part 3 replica ; pure pykafka client consume performance: 75.5896468163 seconds consuming 1085600 messages   
mongodb 3 shard 1 replica  
total 1085600 records (original file 347MB)  

===

3 worker emit_thread 1 split 1 group 3 output:
---
stuck  @ split

---
787059 records  
Spout spend 116.50999999 seconds consuming 1000000 messages  
Spout spend 116.559999943 seconds emitting 1000000 tuples  
Bolt spend 1158.24936318 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.40558695793 seconds  
The 1000000th record walks through the topology in 1043.14495015 seconds  

---
787059 records  
Spout spend 116.75 seconds consuming 1000000 messages  
Spout spend 116.769999981 seconds emitting 1000000 tuples  
Bolt spend 1154.14342999 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.39341282845 seconds  
The 1000000th record walks through the topology in 1038.78684282 seconds  

---
787059 records  
Spout spend 117.309999943 seconds consuming 1000000 messages  
Spout spend 117.359999895 seconds emitting 1000000 tuples  
Bolt spend 1158.25851417 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.43841290474 seconds  
The 1000000th record walks through the topology in 1042.38692713 seconds  

===

3 worker emit_thread 1 split 1 group 3 output:
---
stuck  @ split  

---
787059 records  
Spout spend 116.829999924 seconds consuming 1000000 messages  
Spout spend 116.889999866 seconds emitting 1000000 tuples  
Bolt spend 391.026594162 seconds dumping 1000000 records.  
The 1th record walks through the topology in 9.94729685783 seconds  
The 1000000th record walks through the topology in 284.143891096 seconds  

---
787059 records  
Spout spend 115.960000038 seconds consuming 1000000 messages  
Spout spend 115.980000019 seconds emitting 1000000 tuples  
Bolt spend 387.30053401 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.44012403488 seconds  
The 1000000th record walks through the topology in 272.780658007 seconds  

===

3 worker emit_thread 1 split 1 group 6 output:
---
787059 records  
Spout spend 120.589999914 seconds consuming 1000000 messages  
Spout spend 120.659999847 seconds emitting 1000000 tuples  
Bolt spend 216.66864109 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.27241897583 seconds  
The 1000000th record walks through the topology in 97.3510601521 seconds  

---
787059 records  
Spout spend 121.49000001 seconds consuming 1000000 messages  
Spout spend 121.50999999 seconds emitting 1000000 tuples  
Bolt spend 216.415550947 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.95349693298 seconds  
The 1000000th record walks through the topology in 96.8790478706 seconds  

---
787059 records  
Spout spend 116.980000019 seconds consuming 1000000 messages  
Spout spend 116.99000001 seconds emitting 1000000 tuples  
Bolt spend 219.541529894 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.35764217377 seconds  
The 1000000th record walks through the topology in 103.919172049 seconds  

===

3 worker emit_thread 1 split 1 group 9 output:
---
787059 records  
Spout spend 124.730000019 seconds consuming 1000000 messages  
Spout spend 124.74000001 seconds emitting 1000000 tuples  
Bolt spend 166.067332029 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.37940406799 seconds  
The 1000000th record walks through the topology in 42.7167360783 seconds  

---
787059 records  
Spout spend 123.379999876 seconds consuming 1000000 messages  
Spout spend 123.419999838 seconds emitting 1000000 tuples  
Bolt spend 166.698433161 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.31641983986 seconds  
The 1000000th record walks through the topology in 44.6348531246 seconds  

---
787059 records  
Spout spend 124.859999895 seconds consuming 1000000 messages  
Spout spend 124.920000076 seconds emitting 1000000 tuples  
Bolt spend 166.202483892 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.24279403687 seconds  
The 1000000th record walks through the topology in 42.5852780342 seconds  

===

3 worker emit_thread 1 split 1 group 12 output:
--
stuck  @ split  

---
787059 records  
Spout spend 122.75999999 seconds consuming 1000000 messages  
Spout spend 122.829999924 seconds emitting 1000000 tuples  
Bolt spend 145.05999279 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.30905508995 seconds  
The 1000000th record walks through the topology in 23.6090478897 seconds  

---
787059 records  
Spout spend 124.399999857 seconds consuming 1000000 messages  
Spout spend 124.480000019 seconds emitting 1000000 tuples  
Bolt spend 145.990342855 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.93743395805 seconds  
The 1000000th record walks through the topology in 23.5277769566 seconds  

---
787059 records  
Spout spend 124.269999981 seconds consuming 1000000 messages  
Spout spend 124.279999971 seconds emitting 1000000 tuples  
Bolt spend 145.701582909 seconds dumping 1000000 records.  
The 1th record walks through the topology in 1.2338039875 seconds  
The 1000000th record walks through the topology in 22.6653869152 seconds  

===

3 worker emit_thread 1 split 3 group 12 output:
---
714661 records  
Spout spend 118.25999999 seconds consuming 1000000 messages  
Spout spend 118.46999979 seconds emitting 1000000 tuples  
Bolt spend 136.554130077 seconds dumping 1000000 records.  
The 1th record walks through the topology in 3.35913991928 seconds  
The 1000000th record walks through the topology in 21.6532700062 seconds  

---
714661 records  
Spout spend 117.600000143 seconds consuming 1000000 messages  
Spout spend 117.610000134 seconds emitting 1000000 tuples  
Bolt spend 135.625967979 seconds dumping 1000000 records.  
The 1th record walks through the topology in 3.36970996857 seconds  
The 1000000th record walks through the topology in 21.3956778049 seconds  

---
714661 records  
Spout spend 116.25 seconds consuming 1000000 messages  
Spout spend 116.25 seconds emitting 1000000 tuples  
Bolt spend 135.343389988 seconds dumping 1000000 records.  
The 1th record walks through the topology in 3.5743560791 seconds  
The 1000000th record walks through the topology in 22.667746067 seconds  

===

3 worker emit_thread 1 split 6 group 12 output:
---
650339 records  
Spout spend 117.560000181 seconds consuming 1000000 messages  
Spout spend 117.580000162 seconds emitting 1000000 tuples  
Bolt spend 126.319350958 seconds dumping 1000000 records.  
The 1th record walks through the topology in 6.84160399437 seconds  
The 1000000th record walks through the topology in 15.600954771 seconds  

---
650339 records  
Spout spend 116.409999847 seconds consuming 1000000 messages  
Spout spend 116.460000038 seconds emitting 1000000 tuples  
Bolt spend 126.98576808 seconds dumping 1000000 records.  
The 1th record walks through the topology in 6.7581808567 seconds  
The 1000000th record walks through the topology in 17.3339490891 seconds  

---
650339 records  
Spout spend 120.650000095 seconds consuming 1000000 messages  
Spout spend 120.680000067 seconds emitting 1000000 tuples  
Bolt spend 127.258800983 seconds dumping 1000000 records.  
The 1th record walks through the topology in 6.92383813858 seconds  
The 1000000th record walks through the topology in 13.5326390266 seconds  

===

3 worker emit_thread 1 split 9 group 12 output:
---
609864 records  
Spout spend 116.879999876 seconds consuming 1000000 messages  
Spout spend 116.960000038 seconds emitting 1000000 tuples  
Bolt spend 121.527455091 seconds dumping 1000000 records.  
The 1th record walks through the topology in 10.2342488766 seconds  
The 1000000th record walks through the topology in 14.881704092 seconds  

---
609864 records  
Spout spend 116.960000038 seconds consuming 1000000 messages  
Spout spend 117.060000181 seconds emitting 1000000 tuples  
Bolt spend 120.365499973 seconds dumping 1000000 records.  
The 1th record walks through the topology in 10.1195812225 seconds  
The 1000000th record walks through the topology in 13.5250811577 seconds  

---
609864 records  
Spout spend 116.539999962 seconds consuming 1000000 messages  
Spout spend 116.630000114 seconds emitting 1000000 tuples  
Bolt spend 122.059859991 seconds dumping 1000000 records.  
The 1th record walks through the topology in 10.0183050632 seconds  
The 1000000th record walks through the topology in 15.5381650925 seconds  

===

3 worker emit_thread 1 split 12 group 12 output:
---
573034 records  
Spout spend 118.710000038 seconds consuming 1000000 messages  
Spout spend 118.720000029 seconds emitting 1000000 tuples  
Bolt spend 118.969332933 seconds dumping 1000000 records.  
The 1th record walks through the topology in 13.3921880722 seconds  
The 1000000th record walks through the topology in 13.6515209675 seconds  

---
573034 records  
Spout spend 118.0400002 seconds consuming 1000000 messages  
Spout spend 118.050000191 seconds emitting 1000000 tuples  
Bolt spend 116.826158047 seconds dumping 1000000 records.  
The 1th record walks through the topology in 14.5526931286 seconds  
The 1000000th record walks through the topology in 13.338850975 seconds  

---
573034 records  
Spout spend 117.7099998 seconds consuming 1000000 messages  
Spout spend 117.71999979 seconds emitting 1000000 tuples  
Bolt spend 117.887727976 seconds dumping 1000000 records.  
The 1th record walks through the topology in 13.1581709385 seconds  
The 1000000th record walks through the topology in 13.3358991146 seconds  

===

3 worker emit_thread 3 split 6 group 12 output:
---
650624 records  
Spout spend 122.019999981 seconds consuming 1000000 messages  
Spout spend 122.069999933 seconds emitting 1000000 tuples  
Bolt spend 127.694338083 seconds dumping 1000000 records.  
The 1th record walks through the topology in 7.11964297295 seconds  
The 1000000th record walks through the topology in 12.7939810753 seconds  

---
655980 records
Spout spend 123.630000114 seconds consuming 1000000 messages  
Spout spend 123.670000076 seconds emitting 1000000 tuples  
Bolt spend 127.551127911 seconds dumping 1000000 records.  
The 1th record walks through the topology in 10.7111101151 seconds  
The 1000000th record walks through the topology in 14.6322379112 seconds  

---
650599 records  
Spout spend 120.980000019 seconds consuming 1000000 messages  
Spout spend 121.0 seconds emitting 1000000 tuples  
Bolt spend 128.679519892 seconds dumping 1000000 records.  
The 1th record walks through the topology in 6.74270510674 seconds  
The 1000000th record walks through the topology in 14.4422249794 seconds  

===

3 worker emit_thread 6 split 6 group 12 output:
---
stuck  @ split 2 times 

---
651398 records  
Spout spend 122.609999895 seconds consuming 1000000 messages  
Spout spend 122.679999828 seconds emitting 1000000 tuples  
Bolt spend 136.59360218 seconds dumping 1000000 records.  
The 1th record walks through the topology in 7.09122681618 seconds  
The 1000000th record walks through the topology in 21.0748291016 seconds  

---
650538 records  
Spout spend 122.75 seconds consuming 1000000 messages  
Spout spend 122.7900002 seconds emitting 1000000 tuples  
Bolt spend 132.533104897 seconds dumping 1000000 records.  
The 1th record walks through the topology in 6.88691115379 seconds  
The 1000000th record walks through the topology in 16.6700160503 seconds  

---
650495 records  
Spout spend 121.99000001 seconds consuming 1000000 messages  
Spout spend 121.99000001 seconds emitting 1000000 tuples  
Bolt spend 132.000051975 seconds dumping 1000000 records.  
The 1th record walks through the topology in 7.2488758564 seconds  
The 1000000th record walks through the topology in 17.2589278221 seconds  

===

3 worker emit_thread 9 split 6 group 12 output:
---
iostat: N/A

---
stuck  @ split 4 times 

===

3 worker emit_thread 12 split 6 group 12 output:
---
iostat: N/A

---
stuck  @ split 4 times 

===