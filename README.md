## Description
A doubly linked list.

#### Functionality
- [x] `.append()`
- [x] `.display()`
- [x] `.length()`
- [x] `.get()`
- [x] `.delete()`
- [x] `.count()`
- [x] `.pop()`
- [x] `>=, <=, <, >, ==`
- [ ] `.__repr__()`
- [ ] `.__str__()`
- [x] `.__getitem()`
- [ ] `.__len__()` 

#### Usage
```py
ll = LinkedList()
ll.append(2)
ll.display()

ll.pop()
ll.append(1)
ll.append(27)
ll.display()

ll.count(1)
ll.length()
ll.get(1)

ll.change(1, 9)
ll.display()
```
```hs
> [2]
> [1, 27]
> 1
> 2
> 27
> [1, 9]
```

