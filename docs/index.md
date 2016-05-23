#Welcome to the jolla wiki!



`Jolla` 是一个写于Python2.7的高速API server

`Jolla` 基于gevent的pywsgi，而gevent基于一个用C写的库 `libev`，在`monkey.patch`后能有非常良好的并发效率，很适合作并发服务器

这里是gevent所有的特性（来自gevent的文档）：

* 基于libev的高速的event loop(epoll on Linux,kqueue on freeBSD)
* 轻量执行的 `greenlet`
* 还能更好的使用Python标准库的API（被gevent猴子补丁后）
* Cooperative sockets with SSL support.
* DNS queries performed through threadpool or c-ares.
* Monkey patching utility to get 3rd party modules to become cooperative.

以上这些特性，都被 `Jolla` 继承了

`Jolla`也拥有以下独特的特性

* 自己的精简好用的路由系统
* 简单快速的json response
* 简单而且简短的项目结构
* 自己的错误处理方式

当我在写`Jolla`时，想写的是一个高性能的 API server，它能让使用者以简短而简短的规则去完成server 的工作，能让他们把她们的计算过程也好运算也好，快速的发到浏览器或移动端，所以我把 `Jolla`写的尽可能简单。


希望你们喜欢，喜欢的话可以点个star哦＝ ＝＋
