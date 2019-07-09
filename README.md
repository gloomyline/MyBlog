# MyBlog
My personal blog, a general cms(content management system), share with anyone.

## 踩坑记
### 一、 python-dotenv 管理环境变量
1. Flask的自动发现程序实例机制规则：如果安装了python-dotenv，那么在使用flask run或其他命令时会使用它自动从.flaskenv文件
和.env文件中加载环境变量。

  > 注意：当安装了python-dotenv时，Flask在加载环境变量的优先级是：手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量。

2. 我们在项目根目录下分别创建两个文件：.env和.flaskenv。.flaskenv用来存储和Flask相关的公开环境变量，比如FLASK_APP；而.env用
来存储包含敏感信息的环境变量

### 二、服务器启动选项
1. 使服务器外部可见

    Web服务器默认是对外不可见的，可以在run命令后添加--host选项将主机地址设为0.0.0.0使其对外可见：
    ```
    flask run--host=0.0.0.0
    ```
    这会让服务器监听所有外部请求，所以你的程序只能被局域网内的其他用户通过你的个人计算机的内网IP（私有地址）访问。

2. 改变默认端口号

    Flask提供的默认端口号是5000，可以在启动时传入参数来改变它：
    ```
    flask run-port=8888
    ```
    执行flask run命令时的host和port选项也可以通过环境变量FLASK_RUN_HOST和FLASK_RUN_PORT设置。事实上，Flask内置的命令都
    可以使用这种模式定义默认选项值，即`“FLASK_<COMMAND>_<OPTION>”`。

### 三、 设置运行环境
1. 根据运行环境的不同，Flask程序、扩展以及其他程序会改变相应的行为和设置。

    为了区分程序运行环境，Flask提供了一个FLASK_ENV环境变量用来设置环境，默认为production（生产）。在开发时，将其设置为development（开发）,这会开启所有支持开发的特性。为了方便管理，我们将把环境变量`FLASK_ENV`写入`.flaskenv`文件中。
    ```
    FLASK_ENV=develoment
    ```

### 四、Flask中的HTTP请求
1. `request`对象
2. `response`对象

### 五、Flask中的 template engine `Jinjia2`

### 六、Flask中的Forms
