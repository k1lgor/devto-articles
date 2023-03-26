---
title: Mastering Text Manipulation with the Cut Command in Linux
published: false
description: Linux commands
tags: 'bash, linux, beginners'
cover_image: null
canonical_url: null
series: "Linux from A to Z"
---

---

### ***Introduction***

When it comes to working with Linux, the command line is a powerful tool that can make your life much easier. While there are many commands available, one that is particularly useful for manipulating text data is `cut`.

### ***The Power of cut***

The `cut` command is used to extract specified sections from each line of a file or input. By default, `cut` extracts every character from the beginning to the end of each line. However, it can be used to extract specific fields, columns or sections of a line based on a delimiter or a character position.

### ***Examples***

For example, suppose we have a file called `data.txt` that contains the following lines of data:

```bash
John,Smith,25,USA
Maria,Garcia,32,Mexico
Ahmed,Khan,45,Pakistan
```

If we want to extract only the first names, we can use the following command:

```bash
cut -d',' -f1 data.txt
```

This tells `cut` to use the comma `,` as the delimiter and extract only the first field of each line, which contains the first name. The output will be:

```bash
John
Maria
Ahmed
```

We can also use `cut` to extract a range of characters from each line. For example, to extract only the first three characters of each line from our `data.txt` file, we can use the following command:

```bash
cut -c1-3 data.txt
```

This will output:

```bash
Joh
Mar
Ahm
```

Another useful feature of `cut` is the ability to extract a specific column from a file that does not use a delimiter. For example, suppose we have a file called `numbers.txt` that contains the following data:

```bash
1234
5678
9101
```

To extract the second column (i.e., the second digit of each number), we can use the following command:

```bash
cut -c2 numbers.txt
```

This will output:

```bash
2
6
1
```

### ***Tips***

Here are some additional tips for using the `cut` command:

* To extract the last field of each line, use the `-f` option with a negative value. For example, to extract the countries from our `data.txt` file, we can use the following command:

```bash
cut -d',' -f4 -s data.txt
```

The `-s` option tells `cut` to suppress lines that do not contain the delimiter.

* To extract a range of characters from each line using a specific delimiter, use the `-d` option followed by the delimiter and the `-c` option followed by the starting and ending character positions. For example, suppose we have a file called `emails.txt` that contains the following data:

```bash
john.smith@example.com
maria.garcia@example.com
ahmed.khan@example.com
```

To extract only the domain names (i.e., the text after the `@` symbol) from each line, we can use the following command:

```bash
cut -d'@' -f2 emails.txt | cut -d'.' -f1
```

This will output:

```bash
example
example
example
```

### ***Conclusion***

With the `cut` command, you can quickly and easily manipulate text data in Linux. Whether you need to extract specific fields from a file, extract a range of characters from each line, or extract a specific column from a file that does not use a delimiter, `cut` is a powerful tool that can save you time and effort. So next time you're working with text data in Linux, be sure to give `cut` a try!

***Thank you for reading*** 🧑‍💻

***Stay tuned for more*** 🚀

✌️ and ***logout***

<a href="https://www.buymeacoffee.com/k1lgor" target="_blank">
<img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" >
</a>
