## V2EX ##
几个针对[V2EX](https://v2ex.com)写的小脚本~

## v2ex_daily.py ##
无任何非标准库依赖, 获取v2ex每日登录奖励.

### 如何使用 ###
之前[V2EX](https://v2ex.com)验证登录用的Cookie是`auth`, 每次登录后`auth`的值都是相同的, 你需要做的就是把这个值赋给脚本中的变量`V2EX_COOKIE`. 

不过最新的v2ex验证Cookie已经更为`A2`, 不过之前的`auth`还是可以使用的, 而且我们可以从`A2`中得到`auth`的值. 典型`A2`的格式是这样的:

> 2|1:0|10:1415406915|2:A2|56:xxxxxx|uuuuuu

我们关注的是`56:xxxxxx`, 前面的`56`表示后面的`xxxxxx`长度, 而后面的`xxxxxx`是**之前Cookie`auth`值的`Base64`编码值**, 解码这个值并赋给脚本中的变量`V2EX_COOKIE`就可以了!

最后, 添加定时任务, 每天执行脚本~~

## v2ex_avatar.py ##
获取v2ex某个注册用户的头像（前提是该用户上传了自定义头像）。方法来自 [有什么办法能弄到v2ex里面所有用户的头像图片](https://www.v2ex.com/t/95092).
