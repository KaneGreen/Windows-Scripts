## 清理Windows事件日志

在 Windows 的“事件查看器”中，可以看到“应用程序和服务日志”中“Microsoft”下有大量的日志项目，手动点“清除日志”非常麻烦。这个脚本就能是为了批量清理这些日志。  
至于其他的日志项，你可以手动点“清除日志”——反正数量也不多。

### 依赖
* PowerShell

注意：可以使用 Windows 自带的 PowerShell，也可以使用 [PowerShell Core](https://github.com/PowerShell/PowerShell)。  
但是，如果使用前者，请删除脚本代码中所有的` -NoEmphasis` 参数。
