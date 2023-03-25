# Writeup

使用volatility工具對vmem文件進行解析，一個Str0nger文件，下載後可以發現兩個txt文件

分別得到guitargirl.txt和hint.txt

hint.txt在顏文字解密後可以知道是提醒另外一個txt文件中的base64字符串缺少圖片前綴

guitargirl.txt的base64字符串加上前綴後轉換出图片，使用010editor或者別的工具可以看到flag

```
volatility -f babyvm.vmem imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/root/Downloads/babyvm.vmem)
                      PAE type : PAE
                           DTB : 0xb4f000L
                          KDBG : 0x80546ae0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2022-11-21 10:47:14 UTC+0000
     Image local date and time : 2022-11-21 18:47:14 +0800


volatility -f babyvm.vmem --profile WinXPSP2x86 filescan | grep Str
Volatility Foundation Volatility Framework 2.6
0x0000000005df7818      1      0 R--r-- \Device\HarddiskVolume1\Program Files\Str0nge.rar

volatility -f babyvm.vmem --profile WinXPSP2x86 dumpfiles -Q 0x0000000005df7818 --name file -D ~/Downloads/
Volatility Foundation Volatility Framework 2.6
DataSectionObject 0x05df7818   None   \Device\HarddiskVolume1\Program Files\Str0nge.rar

```

```
hexdump -C cbimage.png | grep MOCS
0004c200  5a 37 64 bb 6a ad ad 8f  ff d9 4d 4f 43 53 43 54  |Z7d.j.....MOCSCT|

hexdump -C cbimage.png | grep 0004c2
00004c20  fc bf bd ba ab 9d 98 f9  71 87 20 65 48 e4 8e 84  |........q. eH...|
0004c200  5a 37 64 bb 6a ad ad 8f  ff d9 4d 4f 43 53 43 54  |Z7d.j.....MOCSCT|
0004c210  46 7b 67 75 31 74 61 72  5f 67 31 72 6c 5f 53 30  |F{gu1tar_g1rl_S0|
0004c220  5f 63 30 6f 6c 21 21 7d  1a                       |_c0ol!!}.|
0004c229
```