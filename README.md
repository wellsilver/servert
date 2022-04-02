# servert

## Logging

You can use servert.log to create cool logging

```
import servert
servert.log('hello world')
# [2022-4-2 14:48:20] hello world
```

## Server

not added yet however its simple to replicate what the package will do in the future;

```
while True:
  l=str(input("> "))
  if l.startswith("echo"):
    # if text == 'echo' get text after echo and print via servert.log()
    servert.log(l.split("echo")[1])
 ```
