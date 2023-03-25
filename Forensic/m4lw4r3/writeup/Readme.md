# Writeup

Question: Be aware of downloading m4lw4r3 from internet!!!

Attachment: https://drive.google.com/file/d/1vFZeRPt9si8mCb3IdkAm4QBmDnNYT_eB/view?usp=share_link

## Solution
1. Install volatility3

```
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
pip3 install -r requirements.txt
sudo pip3 install capstone
sudo python3 setup.py install
python3 vol.py -h
```

2. Analyse the memory dump

```
python3 vol.py -f ~/Downloads/memory.dmp windows.pstree.PsTree

*** 8252        1892    powershell.exe  0x8d8dfe721080  22      -       1       False   2023-02-09 14:47:31.000000      N/A
```
```
python3 vol.py -f ~/Downloads/memory.dmp windows.cmdline.CmdLine

7364    notepad.exe     "C:\Windows\system32\NOTEPAD.EXE" C:\Users\IEUser\Downloads\temp.txt
```

```
python3 vol.py -f ~/Downloads/memory.dmp -o ~/Downloads/procdump  windows.memmap.Memmap --pid 1892 --dump
```

```
strings ~/Downloads/procdump/pid.1892.dmp | grep temp.txt 

Invoke-WebRequest -Uri "https://drive.google.com/uc?export=download&id=1xNiCXAxUt9Gw5U0Whu-SEPzjv3KPb68P" -OutFile "C:\Users\IEUser\Downloads\temp.txt"

Get-Content C:\Users\IEUser\Downloads\temp.txt

```

3. Download the flag from google drive
https://drive.google.com/uc?export=download&id=1xNiCXAxUt9Gw5U0Whu-SEPzjv3KPb68P

> MOCSCTF{malicous_powershell_command}