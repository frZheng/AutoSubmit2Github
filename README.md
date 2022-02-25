# AutoSubmit2Github



设置后sshkey和第一次命令行提交后,使用submitCode.py每日多次自动提交当前目录下的`java`文件夹的所有代码.

实现原理是运行`submit.bat`模拟键盘输入密码实现自动提交代码到github.



# 详细教程

注意:只支持window操作系统, 其他操作系统还没有测试.

python环境.3.7, 根据require.txt 安装即可, 命令`pip install -r requirement.txt`

1. github 创建项目

2. win操作系统生成公钥,将公钥放到github上的sshkey里
3. 修改代码`submit.bat`里面第一行代码`cd java`, 转移到你要上传代码的路径, 如果切换盘符注意要在代码加入`盘符\:`.
4. 修改代码`submitCode.py`里面124行代码`password = ""`, `""`设置为你的密码.
5.  测试上传. 在`submitCode.py`里面138行代码打开注释.
6. 在当前命令行运行cmd,  cmd里运行`python submitCode.py`,然后到github查看是否上传成功.

