# Git Guide/Standard

This details my own git standard so that I don't forget.

# Commit Message Format
All git commits should conform to the following template to ensure that they are easy to understand. While this can be forced by adding a .gitmessage file however I like short and sweet so hand typed single line is the way to go.

Template:
```
[bfix,add,cleanup,update]: <description>
```

Where:

| --- | --- |
| bfix | A bug fix |
| add | New Feature |
| cleanup | Code cleanup |
| update | Update to existing features |

Examples:

```
bfix: GUI not clearing
```

```
update: README
```
