
# cpu高

```
# tomcat 线程
jstack -F PID > java_thread.txt

# linux 线程
ps -mp PID -o THREAD,tid,time | sort -k2r > linux_thread
```

# 内存高
```
jstat -gcutil PID 2000
jmap -heap PID
# dump内存
jmap -dump:format=b,file=java_memory.hprof PID

```

