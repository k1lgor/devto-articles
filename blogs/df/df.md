---
title: Managing Disk Space in Linux with the df Command
published: false
description: Linux commands
tags: 'bash, linux, beginners'
cover_image: null
canonical_url: null
series: "Linux from A to Z"
---

---

### **_Introduction_**

The `df` command is a useful tool for managing disk space on your Linux system. It displays information about the file system disk space usage, including the amount of free space, used space, and the percentage of space used. Here are some examples of using `df` command:

### **_Show disk space usage in human-readable format_**

```bash
df -h
```

### **_Show disk space usage for a specific file system_**

```bash
dh -hT /dev/sda1
```

### **_Show disk space usage for all file systems (including speudo file systems)_**

```bash
df -aTh
```

### **_Show disk space usage for a specific file system and exclude file systems of a certain type_**

```bash
df -hT -x tmpfs /dev/sda1
```

### **_Show disk space usage in bytes for all file systems (including empty file systems)_**

```bash
df -BT
```

### **_Show disk space usage for a specific file system with inode information_**

```bash
df -i /dev/sda1
```

### **_Show disk space usage with a specific output format_**

```bash
df --output=source,fstype,size,used,avail,pcent,target
```

### **_Show disk space usage sorted by a specific column (ascending)_**

```bash
df -hT | sort -k 3
```

### **_Show disk space usage sorted by a specific column (descending)_**

```bash
df -hT | sort -k 3 -r
```

### **_Show disk space usage for all file systems and exclude the header line_**

```bash
df -hT | tail -n +2
```

### **_Tips_**

- Use the `h` option to display disk space usage in human-readable format (e.g., GB, MB)
- Use the `x` option to exclude file systems of a certain type (e.g., tmpfs,devtmpfs)
- Use the `-output` option to customize the output format of the command
- Use the `sort` and `tail` commands to sort and filter the output as needed.

### **_Conclusion_**

In summary, the `df` command is a powerful tool for managing disk space on your Linux system. With the various options available, you can easily view and analyze disk space usage for specific file systems and customize the output format.
Remember to use the available sorting and filtering commands to further manage and analyze the output.

**_Thank you for reading_** 🧑‍💻

**_Stay tuned for more_** 🚀

✌️ and **_logout_**

<a href="https://www.buymeacoffee.com/k1lgor" target="_blank">
<img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" >
</a>
