observe:
===

1. shutdown/break...etc a supervisor host: the storm cluster will automatic re-balance workers/tasks after seconds specified in storm.yaml (nimbus.supervisor.timeout.secs, default:60)  

2. running topology can be re-balanced by web-ui or command line (manually)  

3. though not documented, storm.emit([tuple_content], id=message_id) is possible (Storm's reliability API)

4. don't use time-wasting loop in spout.nextTuple(); otherwise storm-petrel won't be able to call spout.ack/spout.fail, that will break the topology pipeline!!! (VERY IMPORTANT)
===

problem:
===

1. storm is a single master(nimbus) cluster, how to manage fault-tolerance?  
    reference: http://hortonworks.com/blog/fault-tolerant-nimbus-in-apache-storm/  
    survey twitter-heron next?
 

===