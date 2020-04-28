

# proxy转发模块的超时设置：
上下文 http server location
### proxy_read_timeout 默认60s
该指令设置与代理服务器的读超时时间。它决定了nginx会等待多长时间来获得请求的响应。
这个时间不是获得整个response的时间，而是两次reading操作的时间。（？？什么是两次reading操作的时间）
* proxy_read_timeout:连接成功后_等候后端服务器响应时间_其实已经进入后端的排队之中等候处理（也可以说是后端服务器处理请求的时间）

### proxy_send_timeout
默认值 60s
说明 这个指定设置了发送请求给upstream服务器的超时时间。超时设置不是为了整个发送期间，而是在两次write操作期间。
如果超时后，upstream没有收到新的数据，nginx会关闭连接。
proxy_send_timeout :后端服务器数据回传时间_就是在规定时间之内后端服务器必须传完所有的数据

### send_timeout
send_timeout 60;
send_timeout 指定客户端的响应超时时间。这个设置不会用于整个转发器，而是在两次客户端读取操作之间。
如果在这段时间内，客户端没有读取任何数据，nginx就会关闭连接。


location / {
            proxy_pass http://127.0.0.1:5000;
			proxy_read_timeout 120;
}


