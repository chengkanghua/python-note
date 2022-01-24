# WEB环境部署与上线流程

## 环境搭建

### 部署规范

- 服务器部署规范
- 软件部署规范
- 测试
- 上线

### 服务器环境搭建

- nginx

	- nginx管理

		- nginx介绍
		- nginx安装，启动
		- nginx相关目录及配置文件详解
		- nginx默认网站

			- 访问控制
			- 日志管理
			- 仿盗链

		- nginx虚拟主机
		- 反向代理
		- URL重写
		- nginx下载限速

	- nginx

		- 长连接
		- 压缩
		- 客户端缓存
		- 并发数

	- nginx负载均衡

		- 集群介绍
		- 使用nginx分发器构建一个web服务器
		- nginx分发算法

			- 轮询
			- 基于权重的轮询
			- 基于开发语言
			- 基于浏览器
			- 基于源ip

		- 构建高可用nginx集群
		- rs故障检测机制

	- nginx缓存

- nginx+uwsgi+python+mysql+django

	- python
	- mysql的安装管理
	- python业务集成部署，发布一个python开发的web

### 业务环境快速升级部署

- saltstack

	- saltstack介绍
	- saltstack自动化部署
	- 业务环境更新案例

## 代码管理

### 持续集成

- 持续集成介绍
- 认识devops

### 持续交付-源码管理

- git

	- git介绍
	- git安装与配置
	- git仓库初始化
	- git基础命令
	- git分支
	- git标签

- gitlab

	- gitlab介绍
	- gitlab安装
	- gitlab服务与系统设置
	- gitlab仓库管理
	- gitlab备份与恢复

- github

	- github的使用

### 持续部署

- jenkins介绍
- jenkins安装与初始化
- jenkins目录介绍
- jenkins创建freestyle-job
- jenkins获取gitlab源码
- jenkins部署html网站
- jenkins部署脚本编写
- jenkins配置gitlab自动触发构建
- jenkins配置jenkins返回构建状态到gitlab
- maven配置
- jenkins创建maven job
- jenkins pipeline介绍
- jenkins pipeline示例

## 案例

### 按照上线流程完成一次上线

