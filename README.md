# servert

## Logging

You can use servert.log to create cool logging

```
import servert
servert.log('hello world')
# [2022-4-2 14:48:20] hello world
```
Heres the full command:
`log(message,error=False,detailedtime=True)`

When set to True error changes the color of the text to red 

When detailed time is False it prints `[14:48:20] text` instead of `[2022-4-2 14:48:20] text`
## Server

not added yet however its simple to replicate what the package will do in the future;

```
while True:
  l=str(input("> "))
  if l.startswith("echo"):
    # if text == 'echo' get text after echo and print via servert.log()
    servert.log(l.split("echo")[1])
 ```
