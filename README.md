# <center>人工智能检查文章错字</center><br>

首先你得先安装python3以上的版本，并且可以使用pip自动安装所需要的库。其次要去百度api申请差错别字的应用，并且获取相应id和key（不会可百度）。<br>

###### 安装方法<br>

```shell
git clone https://github.com/Franklyn1987/checkerror.git
cd root #将命令行切换至所在目录
python setup.py install
```

###### 使用方法一<br>

* 进入Python模式<br>

  ```python
  	import checkerror as c
  	c.doc() #函数用法说明
  	c.checkerror("D:\demo.docx")#开始执行检查错误	
  	
  ```

###### 使用方法二<br>

```shell
cd root #切换至checkerror的所在目录，利用chacuo.py
python chacuo.py "D:\demo.docx"

```

###### 使用方法三<br>

自己修改注册表，添加鼠标右键选项。其中,'查错别添加邮件.reg'需要针对个人电脑安装情况进行修改：<br>

1. ‘@=’后面的'chacuo.bat'所在路径,注意‘ %1’(空格%1)不能少
2. 'chacuo'替换成你想要鼠标右键中显示的名称
3. '"icon"='后面的路径是你自己想要的图标所在路径