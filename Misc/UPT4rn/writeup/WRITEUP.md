### [Name]：

```
UPT4rn
```

### [Author]

```
1cePeak@Nepnep
```

### [Description]：

```
No One Know Upload than T4rn:)
```

### [Key Point]：
```bash
1. Traffic Upload Analysis
2. zlib data decrypt
```

### [Flag]:
`MOCSCTF{No_oNe_kn0W_UP1O@d_2l18_d@TA_Th4N_T4Rn}`

### [Writeup]：

First, upon analyzing the traffic, it was discovered that there was a large amount of junk traffic.

![image-20230213134643273](img/image-20230213134643273.png)

After filtering, it was found that T4rn had uploaded 47 valid data to the directory /tmp/upload/(\d){1}. 

![image-20230213134818501](img/image-20230213134818501.png)

By tracing the TCP stream and analyzing the data, we finally determined that the traffic was encrypted with zlib.compress. The uploaded content can be decrypted by calling zlib.decompress in sequence according to the number of the uploaded data.

![image-20230213135129465](img/image-20230213135129465.png)

![image-20230213135244350](img/image-20230213135244350.png)

![image-20230213135401024](img/image-20230213135401024.png)

![image-20230213135418856](img/image-20230213135418856.png)

Then, we will flagged:
`MOCSCTF{No_oNe_kn0W_UP1O@d_2l18_d@TA_Th4N_T4Rn}`
