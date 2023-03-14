# If using PowerShell that comes with Windows, please remove all '-NoEmphasis' in the code below
$entries = wevtutil.exe enum-logs | Select-String -Pattern '^Microsoft-' -CaseSensitive -NoEmphasis
foreach($line in $entries) {
    if( wevtutil.exe get-log $line | Select-String -Pattern '^enabled: true' -CaseSensitive -NoEmphasis ) {
        Write-Output "Try to clean: $line"
        wevtutil.exe clear-log $line
    }
}
