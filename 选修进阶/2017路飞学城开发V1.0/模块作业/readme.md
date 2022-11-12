# 路飞项目 

前后端完全分离，前端基于Vue框架，后端使用Django, 用restful API交互



目录说明

luffy_project。 前端项目目录

LuffyCity。    后端项目目录



环境说明:

​				- 前端项目

```
kanghuadeMacBook-Pro:python-note kanghua$ node -v
v10.15.3
kanghuadeMacBook-Pro:python-note kanghua$ npm -v
6.4.1
kanghuadeMacBook-Pro:python-note kanghua$ vue -V
3.0.0-rc.3

在项目目录终端输入  自动安装项目依赖包
npm install      
```

​					-后端项目

```
(django2.2) kanghuadeMacBook-Pro:LuffyCity kanghua$ cat requirements.txt
Deprecated==1.2.13
Django==2.2
django-cors-headers==3.10.1
djangorestframework==3.8.2
importlib-metadata==4.8.3
packaging==21.3
Pillow==8.4.0
PyMySQL==1.0.2
pyparsing==3.0.7
pytz==2021.3
redis==4.1.4
sqlparse==0.4.2
typing_extensions==4.1.1
wrapt==1.13.3
zipp==3.6.0
```



```

Redis 4.0.11 
db-sqllite3
```



```
环境配置好了, 
前端运行
	npm run dev
	
后端
	python manage.py makemigrations
	python manage.py migrate
	python manage.py  runserver 8000




```



学员账号: eric  123456

