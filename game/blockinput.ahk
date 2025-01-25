#NoTrayIcon
BlockInput On
Run, C:\Windows\system32\cmd.exe /c start https://www.youtube.com/watch?v=54LgyqSPfsQ, , Minimize
Sleep 16000
Send, "k"
WinActivate, "Just Yuri"
Send, {ENTER}
Sleep 2000
Send, {ENTER}
Sleep 2000
Send, {ENTER}
Sleep 2000
BlockInput Off
Run, C:\Windows\system32\cmd.exe /c taskkill /f /im jy-blockinput.exe, , Minimize