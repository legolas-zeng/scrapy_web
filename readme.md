
版本：
- [x] python3.7
- [x] mysql5.7
- [x] django2.2.4

#### database

##### 1、article_soure
    存储文章

##### 2、django
    web后台


#### web server

##### 1、customer
web服务后台权限控制

权限类型：
类型 | 字段|注释
---|---|---
ID | id|与django数据库的user表id唯一关联
分组|is_group|权限组，目前还没有做
超级用户 | is_superuser|django后台管理员，通过id与user表关联
管理员 | is_staff|普通管理员，通过id与user表关联
会员|is_vip_type|普通账户
激活|is_active|默认激活，通过id与user表关联

会员：

会员类型 | is_vip_type
---|---
充值会员 | 2
非会员 | 0(默认)
管理员会员 | 1(默认)


##### 2、newsweb
web服务文章展示页
- [x] 文章列表展示
- [x] 文章详情展示
- [x] 翻译
- [x] 文章下载
- [x] vip批量下载
- [ ] vip翻译
- [ ] 翻译批量下载


##### 3、search
文章搜索功能
- [x] 标题
- [x] 日期
- [x] 来源















