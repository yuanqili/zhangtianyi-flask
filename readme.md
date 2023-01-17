# Simple Flask Server

本项目基于如下教程

- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Database usage

对于一个新项目，首先执行该命令初始化数据库配置

```
flask db init
```

每一次定义新表、修改表结构，都需要执行该命令生成迁移脚本

```
flask db migrate -m "message"
```

最后，执行该命令将迁移脚本应用到数据库中

```
flask db upgrade
```
