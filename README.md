基于 Tornado 的示例程序

安装第三方库命令

```
pip install pyyaml sqlalchemy mysql-connector
```

设置配置文件

```
cp app.example.yaml cp app.yaml
```

启动程序命令

```
python app.py
````

启动成功后，访问地址 http://localhost:8000

测试

coverage run tests/test.py
