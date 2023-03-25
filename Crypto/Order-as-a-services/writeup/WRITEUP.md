1. bruteforce the encode list, there is only subsitute cipher.
2. decode the cipher with the encode list.
3. 
```python
Order_id = str(urandom(32).hex())
system(f"mkdir /tmp/{Order_id}")
system(f"cp /flag.txt /tmp/{Order_id}/{decoded_Order}.txt")
system(f"rm -f /tmp/{Order_id}/*.txt")
return f"Your Order ID is : {Order_id}"
```
rm -f /tmp/{Order_id}/*.txt will delete all the files in the directory, so we can't use the Order_id to read the flag.
but rm -rf would delete the directory and hidden files :D
4. make a file that name star with dot, and the content is the flag.