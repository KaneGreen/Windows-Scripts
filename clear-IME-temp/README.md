## 清理中文输入法临时文件

Windows 10 及以后版本操作系自带的中文输入法会在 `%AppData%\Microsoft\InputMethod\Chs\` 目录下创建一些临时文件，但不会自动清理。时间长了会导致启动输入法时卡住。  
将这个脚本加入到开机自启动中（在运行中输入 `shell:Common Startup` 并执行），可以在每次开机时清理这些文件。

### 依赖
* Windows 命令提示符
