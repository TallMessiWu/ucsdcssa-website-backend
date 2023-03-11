# UCSD CSSA官网后端

[官网入口](https://www.ucsdcssa.com/)

[API入口](https://api.ucsdcssa.com/)

[前端GitHub仓库](https://github.com/TallMessiWu/ucsdcssa-website-vue)

[后端GitHub仓库](https://github.com/TallMessiWu/ucsdcssa-website-backend)

## 目录

- [代码样式](#代码样式)
- [项目运行要求](#项目运行要求)
    - [classified.py文件](#classifiedpy-文件)
    - [courses-qr-codes文件夹](#courses-qr-codes-文件夹)
    - [departments-group-photos文件夹](#departments-group-photos-文件夹)
    - [members-photos文件夹](#members-photos-文件夹)
- [更新说明](#更新说明)
    - [更新课友群](#更新课友群)
    - [更新部门信息](#更新部门信息)
    - [更新文章信息](#更新文章信息)
    - [网站更新指南](#网站更新指南)
- [API接口](#API接口)
    - [课友群相关接口](#课友群相关接口)
    - [文章相关接口](#文章相关接口)
    - [部门信息相关接口](#部门信息相关接口)
    - [用户相关接口](#用户相关接口)

## 代码样式

1. 代码缩进使用4个空格。
2. 多个单词组成的变量名使用下划线分割，如`user_name`。
3. 文件名尽量也使用下划线命名法，如`article_blueprint.py`。
4. 代码段落直接应该用空行隔开。

## 代码提交要求

1. 代码提交前需要先在本地运行一遍，确保没有报错。
2. 每次提交都应使用`gitmoji`，即一个表情加更新的内容概述。
3. 表情的挑选需要依照[gitmoji官网](https://gitmoji.dev/)。选择最符合每次提交内容的表情，例如 “:rocket:
   部署了课友群功能。”，并注意句子应以句号结尾。建议多次小量的提交代码更改，尽量避免一次更新过多代码。

## 项目运行要求

在克隆项目后，需要在项目根目录下创建`classified.py`文件。里面所需要建立的变量请看[classified.py文件](#classifiedpy-文件)
部分内容。

需要安装requirements.txt中的所有依赖。

需要确保MySQL数据库已经安装并且已经启动。同时需要建立了名为`ucsdcssa_website`的数据库。

需要确保Redis数据库已经安装并且已经启动。

同时需要在assets文件夹中创建`courses-qr-codes`文件夹。并在文件夹中放入所有课程的二维码图片。
图片命名与格式要求请看[courses-qr-codes文件夹](#courses-qr-codes-文件夹)部分内容。

需要确保所有图片都为`.jpg`(后缀必须是小写)。同时`assets`文件夹中需要有生成的`courses_grouped.json`和`department.json`文件。
有两种方式确保这些：

1. 根据自己的系统，运行`utils`文件夹中的`format_courses_and_department.bat`或`format_courses_and_department.sh`文件。
   并查看`assets`文件夹中是否有生成的`courses_grouped.json`和`department.json`文件。

2. 手动查看并修改所有图片的后缀为`.jpg`，然后手动运行`utils`文件夹中的`get_courses_grouped_json.py`文件来生成`assets`
   文件夹中关于课程分组的`courses_grouped.json`文件。
   还需要运行同一文件夹下的`get_department_json.py`文件来生成`assets`文件夹中关于部门信息的`department.json`文件。

需要运行flask服务器后，在终端中`cd`到项目根目录并运行`flask db init`、`flask db migrate`、`flask db upgrade`命令来初始化数据库。
如果中间有报错，如过报错提示的是需要安装依赖则安装依赖。如果报错的是其他，可尝试删除`migrations`
文件夹与数据库中的`alembic_version`表。
然后再重新跑上方的三个命令。

### 图片格式要求

图片格式要求为`.jpg`。三个字母必须全部小写，因此`.JPG`文件必须改为`.jpg`。`.jpeg`或其他格式也是不行的。
图片最好进行压缩以方便快速加载，可以使用[这个网站](https://imagecompressor.com/)进行压缩。

### `classified.py`文件

需要在`classified.py`文件中写入下方代码并根据更换为相应的值：

```python
DB_PASSWORD = "更换为你的MySQL数据库密码"

MAIL_USERNAME = "更换为你发送验证码的邮箱"
MAIL_PASSWORD = "更换为发送验证码邮箱的邮箱密码，有些邮箱网站可能需要手动生成应用专用密码，可以网上自行搜索一下步骤"
MAIL_DEFAULT_SENDER = '更换为你发送验证码的邮箱'

BACKEND_ADDRESS = "更换为后端地址，例如如果在本地跑，就写'http://127.0.0.1:{flask服务端口号}'。如果在服务器跑就写'https://api.ucsd.com'。"

"""
获取微信公众号文章

参考文章：https://www.mianshigee.com/note/detail/38130ncd/

COOKIE: 从浏览器里复制过来的cookie
TOKEN: 从浏览器里复制过来的token
"""
COOKIE = "跟着上方注释的教程走，这里更换为你网络请求的cookie"
TOKEN = "跟着上方注释的教程走，这里更换为你网络请求的token"

```

### `courses-qr-codes`文件夹

所有图片的命名格式为`{专业简写} {课程号}.jpg`。例如`CSE 12.jpg`。

文件名中间的空格是必须的，且其必须是英文空格，不能是中文空格。

### `departments-group-photos`文件夹

所有图片的命名格式为`{部门名}合照.jpg`。例如`主席团合照.jpg`、`开发部合照.jpg`。

文件名中不能有空格。

### `members-photos`文件夹

所有图片的命名格式为`{部门名}-{姓名}-{职位}.jpg`。例如`开发部-张三-部长.jpg`、`主席团-李四-主席.jpg`。

文件名中不能有空格。

职位是用来排序的。排序顺序为`主席`、`副主席`、`秘书`、`开发部部长`、`人事部部长`、`外联部部长`、`文体部部长`、`新媒体部部长`、`宣传部部长`、
`学术部部长`、`部长`、`成员`。如果有其他职位例如`设计组组长`，则其会被排序在`部长`与`部员`之间。

部长的照片需要出现两次。以开发部部长为例，需要有`主席团-张三-开发部部长.jpg`和`开发部-张三-部长.jpg`两张图片。

下方为错误命名的例子：

1. `开发部-张三-开发部部长.jpg`，这里的`开发部部长`是错误的，应该是`部长`。因为前面开头的部门已经指向了开发部。
2. `外联部-李四-外联部部员.jpg`，这里的`外联部部员`是错误的，应该是`部员`。因为前面开头的部门已经指向了外联部。
3. `主席团 - 王五 - 主席.jpg`，这里的错误的原因是文件名有空格。
4. `主席团 赵六 主席.jpg`，这里的错误的原因是需要用`-`而不是空格进行连接。文件名中是不能有空格的。

## 更新信息

### 更新课友群

把`courses-qr-codes`文件夹中的图片全部删除，然后重新放入新的图片。
删除`courses_grouped.json`(其实不删也行，会自动覆盖。删除是为了确保真的生成了新的文件)。

然后像[项目运行要求](#项目运行要求)中的部分一样，有两种方法更新：

1. 根据系统，运行`utils`文件夹中的`format_courses_and_department.bat`或`format_courses_and_department.sh`文件。
2. 手动查看并修改所有图片的后缀为`.jpg`，然后手动运行`utils`文件夹中的`get_courses_grouped_json.py`文件来生成`assets`
   文件夹中关于课程分组的`courses_grouped.json`文件。

运行完后，需要查看在`assets`文件夹是否已经生成了`courses_grouped.json`文件。

### 更新部门信息

把`departments-group-photos`文件夹中的图片全部删除，然后重新放入新的图片。

把`members-photos`文件夹中的图片全部删除，然后重新放入新的图片。

如果需要，修改`assets`文件夹中的`departments_description.json`文件。其中每个部门的`recruit`字段是`HTML`代码。
可以使用[这个网站](https://onlinehtmleditor.dev/)编辑文本，然后直接生成`HTML`代码并复制进来。
如果有成立了新部门，照着其他部门照着写就行了。

确保上方都更新好之后，删除原有的`department.json`文件然后有两种方法生成新的`department.json`文件：

1. 根据系统，运行`utils`文件夹中的`format_courses_and_department.bat`或`format_courses_and_department.sh`文件。
2. 手动查看并修改所有图片的后缀为`.jpg`，然后手动运行`utils`文件夹中的`get_department_json.py`文件来生成`assets`
   文件夹中关于部门信息的`department.json`文件。

运行完后，需要查看在`assets`文件夹是否已经生成了`department.json`文件。

### 更新文章信息

如果需要更新服务器的文章，则首先需要根据[这个教程](https://www.mianshigee.com/note/detail/38130ncd/)，
设置好`classified.py`的`COOKIE`和`TOKEN`字段。

然后用浏览器或软件`Postman`访问`{flask地址}/crawl-articles/{要爬的文章数量}`即可。例如:

- 如果需要在服务器上爬取100篇文章，则访问`https://api.ucsdcssa.com/crawl-articles/100`
- 如果需要在本地爬取50篇文章，则访问`http://127.0.0.1:{你的端口号}/crawl-articles/50`
  ，例如`http://127.0.0.1:667/crawl-articles/50`

然后自己去MySQL数据库中查看是否已经爬取成功。

每条文章的所有字段除了`headline_index`和`categories`外，都是非空的。

`headline_index`决定了文章是否出现在头条的位置，如果为`NULL`则不会出现在头条的位置。如果不为`NULL`
，则会根据值的大小来决定文章在头条的位置。值越小，文章越靠前。

`categories`决定文章的类别。默认为`NULL`，所以文章只会出现在`全部`中。如果想增加类别，则需要在`categories`中添加类别名。类别名之间用空格分隔。

例如`categories`为`CSSA原创`，则文章会出现在`CSSA原创`和`全部`中。如果`categories`为`CSSA原创 学术干货`
，则文章会出现在`CSSA原创`、`学术干货`和`全部`中。

类别的可选值在[前端代码](https://github.com/TallMessiWu/ucsdcssa-website-vue)中的`src/staticVariables.js`文件。
目前的可选值为：`CSSA原创`、`活动推文`、`学术干货`、`新生必读`、`生活周边`、`政策要闻`、`独家赞助`、`其他`。

- 这里要注意`全部`不是一个可选值，而是在前端代码中用来布局的。

### 网站更新指南

1. 首先确保更改都已经发布到`GitHub`上。
2. 打开网站的宝塔面板，在左侧侧边栏中选中“网站”页面，并在上方选中“其他项目”。
3. 找到项目`ucsdcssa_website_backend`并点击服务状态列的`运行中▶`以停止项目，确保其状态变成`||未启动`。
4. 在左侧侧边栏中找到“文件”页面并打开。然后打开网站目录：`/www/wwwroot/ucsdcssa-website-backend`。
5. 点击上方的终端，并在终端中运行`git pull`按回车，然后根据提示输入相关用户名与密码或口令。
6. `git`抓取成功后，在左侧侧边栏中选中“网站”页面，并在上方选中“其他项目”。
7. 找到项目`ucsdcssa_website_backend`并点击服务状态列的`||未启动`以启动项目，确保其状态变成`运行中▶`。

## API接口

文档顺序是根据代码中的顺序来的。

### 课友群相关接口

- `GET /courses`：获取所有按照首字母分组的课程信息。
    - 请求参数（需要在headers中）
        - id：`string`类型，用于验证身份，必填。
        - token：`string`类型，用于验证身份，必填。
    - 返回值
        - `JSON`格式的课程信息。


- `GET /courses/{course_name}/{id}/{token}`：获取指定课程的二维码。
    - 请求参数（需要直接放在请求路径中）
        - course_name：`string`类型，课程名，必填。
        - id：`string`类型，用于验证身份，必填。
        - token：`string`类型，用于验证身份，必填。
    - 返回值
        - 指定课程的二维码图片。
    - 示例
        - `GET /courses/CSE 12/VdaMSEHtjc3dxUPBCcrnG3/FuOgozzNXUOXOhaOXBKo`
        - `GET /courses/CSE%2012/VdaMSEHtjc3dxUPBCcrnG3/FuOgozzNXUOXOhaOXBKo`
            - 这里的`%20`是空格的`URL`编码，不过无论用`URL`编码还是直接用空格都是支持的。


- `GET /assistants/{id}`: 获取指定小助手的二维码。
    - 请求参数（需要直接放在请求路径中）
        - id：`int`类型，小助手的id，必填。
            - 如需要访问小助手1的二维码，则id为1。如需要访问小助手2的二维码，则id为2。
    - 示例
        - `GET /assistants/1`
    - 返回值
        - 指定小助手的二维码图片。

### 文章相关接口

- `GET /crawl-articles/{num}`：爬取指定数量的文章到数据库。
    - 请求参数（需要直接放在请求路径中）
        - num：`int`类型，要爬取的文章数量，必填。
    - 返回值：成功后会返回"文章获取成功"。


- `GET /articles/{offset_num}/{category}`：获取指定类别的文章。
    - 请求参数（需要直接放在请求路径中）
        - offset_num：`int`类型，偏移量，必填。
            - 例如：如果offset_num为0，则返回第1篇文章到第10篇文章。
            - 如果offset_num为10，则返回第11篇文章到第20篇文章。
            - 如果offset_num为20，则返回第21篇文章到第30篇文章。
            - 以此类推。
        - category：`string`类型，文章类别，必填。
            - 可选值为`全部`、`CSSA原创`、`活动推文`、`学术干货`、`新生必读`、`生活周边`、`政策要闻`、`独家赞助`、`其他`。
            - 如果为`全部`，则返回所有类别的文章。
    - 返回值
        - `JSON`格式的文章信息。


- `GET /headlines`：获取头条文章。
    - 返回值
        - `JSON`格式的头条文章信息。

### 部门信息相关接口

- `GET /department/{department_name}`: 获取指定部门的信息。
    - 请求参数（需要直接放在请求路径中）
        - department_name：`string`类型，部门名。
    - 返回值
        - `JSON`格式的部门信息。


- `GET /member/{department_name}/{member_name}`: 获取指定部门的指定成员的照片。
    - 请求参数（需要直接放在请求路径中）
        - department_name：`string`类型，部门名。
        - member_name：`string`类型，成员名。
    - 返回值
        - 指定部员的照片。


- `GET /group-photo/{department_name}`: 获取指定部门的部门合照。
    - 请求参数（需要直接放在请求路径中）
        - department_name：`string`类型，部门名。
    - 返回值
        - 指定部门的部门合照。

### 用户相关接口

- `POST /register`: 注册用户。
    - 请求参数（需要在form中）
        - email：`string`类型，邮箱，必填。
        - username：`string`类型，用户名，必填。
        - password：`string`类型，密码，必填。
        - captcha：`string`类型，验证码，必填。
    - 返回值
        - id：`string`类型，用户唯一标识。
        - token：`string`类型，此次登录的token。


- `POST /catpcha`: 获取验证码。
    - 请求参数（需要在form中）
        - email：`string`类型，邮箱，必填。
        - purpose：`string`类型，验证码用途，必填。
            - 可选值为`注册`、`重置密码`。
    - 返回值
        - 如果成功则无返回值。

- `POST /login`: 登录。
    - 请求参数（需要在form中）
        - email：`string`类型，邮箱，必填。
        - password：`string`类型，密码，必填。
    - 返回值
        - id：`string`类型，用户唯一标识。
        - token：`string`类型，此次登录的token。


- `PUT /reset-password`: 重置密码。
    - 请求参数（需要在form中）
        - email：`string`类型，邮箱，必填。
        - password：`string`类型，新密码，必填。
        - captcha：`string`类型，验证码，必填。
    - 返回值
        - 如果成功则无返回值。

- `GET /users/{id}`: 获取指定用户的信息。
    - 请求参数（需要直接放在请求路径中）
        - id：`string`类型，用户唯一标识，必填。
    - 请求参数（需要在headers中）
        - token：`string`类型，登录后产生的token，必填。
    - 返回值
        - `JSON`格式的用户信息。


- `DELETE /users/{id}`: 删除指定用户。
    - 请求参数（需要直接放在请求路径中）
        - id：`string`类型，用户唯一标识，必填。
    - 请求参数（需要在headers中）
        - token：`string`类型，登录后产生的token，必填。
    - 返回值
        - 如果成功则无返回值。

- `PUT /users/{id}`: 更新指定用户的信息除邮箱和密码外的信息。
    - 请求参数（需要直接放在请求路径中）
        - id：`string`类型，用户唯一标识，必填。
    - 请求参数（需要在headers中）
        - token：`string`类型，登录后产生的token，必填。
    - 请求参数（需要在form中）
        - username：`string`类型，用户名，选填。
        - real_name：`string`类型，真实姓名，选填。
        - avatar：`string`类型，头像，选填。
            - 为图片的base64编码。
        - purchased: `bool`类型，是否购买了CSSA卡，选填。
        - card_number: `string`类型，CSSA卡号，选填。
    - 返回值
        - 如果成功则无返回值。
