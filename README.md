<p align="center"><img src="https://user-images.githubusercontent.com/107058068/178225754-263efd37-04b1-4eb1-b21d-6e7793d62be2.png" alt="MetrosCrypt" width="100px" height="100px"></p>
<h1 align="center">HashCap Terminal</h1>

# Description
HashCap version [Command Line Interpreter | Terminal] program for working with hash functions.<br>
This program is implemented in <a href="https://www.python.org/">Python</a> version <a href="https://www.python.org/downloads/release/python-3104/">3.10.4</a>. The library for getting data from the user is <a href="https://pypi.org/project/prompt-toolkit/">prompt_toolkit</a>.<br>
Hashcap implements the conversion of a string into a hash, iteration of hashes, as well as getting the checksum of files.<br>








# Libraries
<table>
  <tr>
    <th>Library</th>
    <th>Pip</th>
  </tr>
 <tr><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td>pip install hashlib</td></tr>
 <tr><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td>pip install pysha3</td></tr>
 <tr><td><a href="https://pypi.org/project/Whirlpool/">whirlpool</a></td><td>pip install whirlpool</td></tr>
 <tr><td><a href="https://pypi.org/project/colorama/">colorama</a></td><td>pip install colorama</td></tr>
 <tr><td><a href="https://pypi.org/project/prompt-toolkit/">prompt_toolkit</a></td><td>pip install prompt_toolkit</td></tr>
</table>

## Pysha3 platform requirements
Installing this `pysha3` library may cause errors.<br>
Familiarize yourself with the requirements of the library for its work,<br>
it provides the work of such hash functions as: `keccak224`, `keccak256`, `keccak384`, `keccak512`.<br>
Check out the library documentation.<br><br>
Pysha3 requirements:
> Linux (GCC, clang) on X86, X86_64 and ARMv6 (little endian)<br>
> Windows (VS 2008, VS 2010, VS2015) on X86 and X86_64 <br>

# Installation for python3
```bash
git clone https://github.com/John-MetrosSoftware/HashCapTerminal
cd HashCapTerminal
pip3 install -r requirements.txt
python3 HashCapTerminal.py
```

# Terminal input
The propmpt_toolkit bilbiotkea is responsible for entering commands and the prompt function, the session file is located specifically in the place of the program called `.hashcap_terminal_history`, it is also important to note that the backslash is replaced by a slash and the parameters are converted to lower case.
<br><br>
To exit the program, you can press `Ctrl+C`. To stop Brute-force press all the same `Ctrl+C`.

# List of hash functions
<table>
  <tr>
    <th>Name</th>
    <th>Python library</th>
    <th>Wikipedia</th>
  </tr>
 <tr><td><a href="https://docs.python.org/3/library/zlib.html#zlib.adler32">adler32</a></td><td><a href="https://docs.python.org/3/library/zlib.html">zlib</a></td><td><a href="https://en.wikipedia.org/wiki/Adler-32">ADLER32</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html#hashlib.blake2b">blake2b</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/BLAKE_(hash_function)">BLAKE</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html#hashlib.blake2s">blake2s</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/BLAKE_(hash_function)">BLALE</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/zlib.html#zlib.crc32">crc32</a></td><td><a href="https://docs.python.org/3/library/zlib.html">zlib</a></td><td><a href="https://en.wikipedia.org/wiki/Cyclic_redundancy_check">CRC32</a></td></tr>
 <tr><td>keccak224</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td>keccak256</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td>keccak384</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td>keccak512</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">md4</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/MD4">MD4</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">md5</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/MD5">MD5</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">ripemd160</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/RIPEMD">RIPEMD</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha1</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha224</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha256</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha384</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha512</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-224</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-256</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-384</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-512</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">shake128</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">shake256</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td></tr>
 <tr><td>whirlpool</td><td><a href="https://pypi.org/project/Whirlpool/">whirlpool</a></td><td><a href="https://en.wikipedia.org/wiki/Whirlpool_(hash_function)">WHIRLPOOL</a></td></tr>
</table>

> The table of hash functions with which HashCap works is given.<br>
> In the future, the list will expand.

# Usage
## All commands
To display help for a specific command, you must add the name of the command after the `help` command.<br>
To display the full program help, use the `-a` or `--all` option, it will display the help of all commands.<br>

> Click on the command you need in the table, the link will take you to its help.
<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
  </tr>
 <tr><td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal/blob/main/README.md#brute">brute</a></td><td>Brute-force hash function by dictionary.</td></tr>
 <tr><td>cd</td><td>Changing the current working directory.</td></tr>
 <tr><td>clear, clean, cls</td><td>Clearing the terminal.</td></tr>
 <tr><td>dir</td><td>Displaying directory contents.</td></tr>
 <tr><td>echo</td><td>Display a line of text.</td></tr>
 <tr><td>exit, quit</td><td>Exiting the program.</td></tr>
 <tr><td>file</td><td>Command for working with files.</td></tr>
 <tr><td>folder</td><td>Command for working with folders.</td></tr>
 <tr><td>hash</td><td>Command for working with a hash function.</td></tr>
 <tr><td>help</td><td>Displaying program help.</td></tr>
 <tr><td>history</td><td>Command for working with input history.</td></tr>
 <tr><td>ls</td><td>Displaying directory contents.</td></tr>
 <tr><td>pwd</td><td>Display current working directory.</td></tr>
 <tr><td>read</td><td>Reading files.</td></tr>
 <tr><td>sum</td><td>Display the hash sum of a file.</td></tr>
 <tr><td>system</td><td>Execute an external command in a shell.</td></tr>
 <tr><td>version</td><td>Display the current version of the program.</td></tr>
</table>

### Terminal 
```
Usage: help [<command> or <option>]

All commands
============

    Command             Description
    -------             -----------
    brute               Brute-force hash function by dictionary.
    cd                  Changing the current working directory.
    clear, clean, cls   Clearing the terminal.
    dir                 Displaying directory contents.
    echo                Display a line of text.
    exit, quit          Exiting the program.
    file                Command for working with files.
    folder              Command for working with folders.
    hash                Command for working with a hash function.
    help                Displaying program help.
    history             Command for working with input history.
    ls                  Displaying directory contents.
    pwd                 Display current working directory.
    read                Reading files.
    sum                 Display the hash sum of a file.
    system              Execute an external command in a shell.
    version             Display the current version of the program.

[*] Use the `help` command to display help for a specific command.
```

## brute
The `brute` command is responsible for brute force hash of the function by dictionary.
<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
  </tr>
 <tr><td>brute</td><td>Brute-force hash function by dictionary.</td></tr>
</table>
<table>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
 <tr><td>--adler32</td><td>https://en.wikipedia.org/wiki/Adler-32</td></tr>
 <tr><td>--blake2b</td><td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td></tr>
 <tr><td>--blake2s</td><td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td></tr>
 <tr><td>--crc32</td><td>https://en.wikipedia.org/wiki/Cyclic_redundancy_check</td></tr>
 <tr><td>--keccak224</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--keccak256</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--keccak384</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--keccak512</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--md4</td><td>https://en.wikipedia.org/wiki/MD4</td></tr>
 <tr><td>--md5</td><td>https://en.wikipedia.org/wiki/MD5</td></tr>
 <tr><td>--ripemd160</td><td>https://en.wikipedia.org/wiki/RIPEMD</td></tr>
 <tr><td>--sha1</td><td>https://en.wikipedia.org/wiki/SHA-1</td></tr>
 <tr><td>--sha224</td><td>https://en.wikipedia.org/wiki/SHA-1</td></tr>
 <tr><td>--sha256</td><td>https://en.wikipedia.org/wiki/SHA-1</td></tr>
 <tr><td>--sha384</td><td>https://en.wikipedia.org/wiki/SHA-1</td></tr>
 <tr><td>--sha512</td><td>https://en.wikipedia.org/wiki/SHA-1</td></tr>
 <tr><td>--sha3-224</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--sha3-256</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--sha3-384</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--sha3-512</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--shake128</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--shake256</td><td>https://en.wikipedia.org/wiki/SHA-3</td></tr>
 <tr><td>--whirlpool</td><td>https://en.wikipedia.org/wiki/Whirlpool_(hash_function)</td></tr>
</table>

<table>
  <tr>
    <th>Command</th>
    <th>Brute options</th>
    <th>Hash target</th>
    <th>Dictionary</th>
  </tr>
 <tr><td>brute</td><td>--md5</td><td>098f6bcd4621d373cade4e832627b4f6</td><td>dictionary.txt</td></tr>
</table>
### Terminal 
```
Usage:  brute <hash_option> <hash_target> <dictionary>

Command brute
=============
    Command     Description                                
    -------     -----------                               
    brute       Brute-force hash function by dictionary.    
        
Options brute 
=============
    
    Options         Description
    -------         -----------
    --adler32       https://en.wikipedia.org/wiki/Adler-32
    --blake2b       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --blake2s       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --crc32         https://en.wikipedia.org/wiki/Cyclic_redundancy_check
    --keccak224     https://en.wikipedia.org/wiki/SHA-3 
    --keccak256     https://en.wikipedia.org/wiki/SHA-3
    --keccak384     https://en.wikipedia.org/wiki/SHA-3
    --keccak512     https://en.wikipedia.org/wiki/SHA-3
    --md4           https://en.wikipedia.org/wiki/MD4
    --md5           https://en.wikipedia.org/wiki/MD5
    --ripemd160     https://en.wikipedia.org/wiki/RIPEMD
    --sha1          https://en.wikipedia.org/wiki/SHA-1
    --sha224        https://en.wikipedia.org/wiki/SHA-1
    --sha256        https://en.wikipedia.org/wiki/SHA-1
    --sha384        https://en.wikipedia.org/wiki/SHA-1
    --sha512        https://en.wikipedia.org/wiki/SHA-1
    --sha3-224      https://en.wikipedia.org/wiki/SHA-3
    --sha3-256      https://en.wikipedia.org/wiki/SHA-3
    --sha3-384      https://en.wikipedia.org/wiki/SHA-3
    --sha3-512      https://en.wikipedia.org/wiki/SHA-3
    --shake128      https://en.wikipedia.org/wiki/SHA-3
    --shake256      https://en.wikipedia.org/wiki/SHA-3
    --whirlpool     https://en.wikipedia.org/wiki/Whirlpool_(hash_function)
    
Usage brute
===========
    Command     Brute options   Hash target                         Dictionary
    -------     -------------   -----------                         ----------
    brute       --md5           098f6bcd4621d373cade4e832627b4f6    dictionary.txt
```
