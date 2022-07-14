<p align="center"><img src="https://user-images.githubusercontent.com/107058068/178225754-263efd37-04b1-4eb1-b21d-6e7793d62be2.png" alt="HashCapTerminal" width="100px" height="100px"></p>
<h1 align="center">HashCap Terminal</h1>

# Description
HashCap version [Command Line Interpreter | Terminal] program for working with hash functions.<br>
This program is implemented in <a href="https://www.python.org/">Python</a> version <a href="https://www.python.org/downloads/release/python-3104/">3.10.4</a>. The library for getting data from the user is <a href="https://pypi.org/project/prompt-toolkit/">prompt_toolkit</a>.<br>
Hashcap implements the conversion of a string into a hash, iteration of hashes, as well as getting the checksum of files.<br>
<p align="center">

![image](https://user-images.githubusercontent.com/107058068/179056663-b1c47324-cdba-4af0-80b4-45e78698c777.png)

> Current version: 1.0

# Libraries
<table>
  <tr>
    <th>Library</th>
    <th>Pip</th>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td>pip install hashlib</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/pysha3">pysha3</a></td>
    <td>pip install pysha3</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/Whirlpool/">whirlpool</a></td>
    <td>pip install whirlpool</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/colorama/">colorama</a></td>
    <td>pip install colorama</td>
  </tr>
  <tr>
    <td><a href="https://pypi.org/project/prompt-toolkit/">prompt_toolkit</a></td>
    <td>pip install prompt_toolkit</td>
  </tr>
</table>

> In case of problems with the installation, read the official documentation here there are all links. You can remove the libraries that are responsible for hashing from the code in case of problems, the most important is hashlib.

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

# Terminal messages
<table>
  <tr>
    <th colspan="2">Terminal messages</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <td>[i] - info</td>
  <td>Regular message. Information about something.</td>
  </tr>
  <tr>
    <td>[w] - warning</td>
    <td>A warning is usually used when deleting a file. Notification of dangerous actions.</td>
  </tr>
  <tr>
    <td>[e] - error</td>
    <td>An error has occurred, there should be a description of the error next to it.</td>
  </tr>
</table>

# Terminal input
The <a href="https://pypi.org/project/prompt-toolkit/">propmpt_toolkit</a> library is responsible for entering commands and the prompt function, the session file is located specifically in the place of the program called `.hashcap_terminal_history`, it is also important to note that the backslash is replaced by a slash and the parameters are converted to lower case.
<br><br>
To exit the program, you can press `Ctrl+C`. To stop Brute-force press all the same `Ctrl+C`.
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <td>Command not found.</td>
  <td>The command you entered could not be processed. This means that there is no such command, check the command syntax.</td>
  </tr>
  <tr>
    <td>Not enough permissions to execute the command.</td>
    <td>You do not have sufficient rights to execute the command, increase the rights to execute such commands. Use sudo if you are on linux or run the program as administrator if you are on windows.</td>
  </tr>
</table>

# Terminal mistakes
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <td>Unknown error.</td>
  <td>If you get this message, then there should be an error message nearby, look for an answer on the Internet or create a question in the repository and describe the problem in more detail.</td>
  </tr>
</table>

> The program does not handle such errors.

# List of hash functions
<table>
  <tr>
    <th>Name</th>
    <th>Python library</th>
    <th>Wikipedia</th>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/zlib.html#zlib.adler32">adler32</a></td>
    <td><a href="https://docs.python.org/3/library/zlib.html">zlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/Adler-32">ADLER32</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html#hashlib.blake2b">blake2b</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/BLAKE_(hash_function)">BLAKE</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html#hashlib.blake2s">blake2s</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/BLAKE_(hash_function)">BLALE</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/zlib.html#zlib.crc32">crc32</a></td>
    <td><a href="https://docs.python.org/3/library/zlib.html">zlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/Cyclic_redundancy_check">CRC32</a></td>
  </tr>
  <tr>
    <td>keccak224</td>
    <td><a href="https://pypi.org/project/pysha3">pysha3</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td>keccak256</td>
    <td><a href="https://pypi.org/project/pysha3">pysha3</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td>keccak384</td>
    <td><a href="https://pypi.org/project/pysha3">pysha3</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td>keccak512</td>
    <td><a href="https://pypi.org/project/pysha3">pysha3</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">md4</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/MD4">MD4</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">md5</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/MD5">MD5</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">ripemd160</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/RIPEMD">RIPEMD</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha1</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha224</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha256</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha384</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha512</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha3-224</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha3-256</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha3-384</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">sha3-512</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">shake128</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td><a href="https://docs.python.org/3/library/hashlib.html">shake256</a></td>
    <td><a href="https://pypi.org/project/hashlib/">hashlib</a></td>
    <td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td>
  </tr>
  <tr>
    <td>whirlpool</td>
    <td><a href="https://pypi.org/project/Whirlpool/">whirlpool</a></td>
    <td><a href="https://en.wikipedia.org/wiki/Whirlpool_(hash_function)">WHIRLPOOL</a></td>
  </tr>
</table>

> The table of hash functions with which HashCap works is given.<br>
> In the future, the list will expand.

# Usage
## All commands
To display help for a specific command, you must add the name of the command after the `help` command.<br>
To display the full program help, use the `-a` or `--all` option, it will display the help of all commands.<br>
<table>
  <tr>
    <th colspan="2">All commands</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#brute">brute</a></td>
    <td>Brute-force hash function by dictionary.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#cd">cd</a></td>
    <td>Changing the current working directory.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#clear">clear, clean, cls</a></td>
    <td>Clearing the terminal.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#dir">dir</a></td>
    <td>Displaying directory contents.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#echo">echo</a></td>
    <td>Display a line of text.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#exit">exit, quit</a></td>
    <td>Exiting the program.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#file--folder">file</a></td>
    <td>Command for working with files.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#file--folder">folder</a></td>
    <td>Command for working with folders.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#hash">hash</a></td>
    <td>Command for working with a hash function.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#help">help</a></td>
    <td>Displaying program help.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#history">history</a></td>
    <td>Command for working with input history.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#ls">ls</a></td>
    <td>Displaying directory contents.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#pwd">pwd</a></td>
    <td>Display current working directory.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#read">read</a></td>
    <td>Reading files.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#sum">sum</a></td>
    <td>Display the hash sum of a file.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#system">system</a></td>
    <td>Execute an external command in a shell.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/John-MetrosSoftware/HashCapTerminal#version">version</a></td>
    <td>Display the current version of the program.</td>
  </tr>
</table>

> Click on the command you need in the table, the link will take you to its help.

## brute
![image](https://user-images.githubusercontent.com/107058068/179058770-80537b3b-fdcf-4c3b-a890-150c6d42a120.png)

<table>
  <tr>
    <th colspan="2">Command brute</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>brute</td>
    <td>Brute-force hash function by dictionary.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options brute</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>--adler32</td>
    <td>https://en.wikipedia.org/wiki/Adler-32</td>
  </tr>
  <tr>
    <td>--blake2b</td>
    <td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td>
  </tr>
  <tr>
    <td>--blake2s</td>
    <td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td>
  </tr>
  <tr>
    <td>--crc32</td>
    <td>https://en.wikipedia.org/wiki/Cyclic_redundancy_check</td>
  </tr>
  <tr>
    <td>--keccak224</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak384</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak512</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--md4</td>
    <td>https://en.wikipedia.org/wiki/MD4</td>
  </tr>
  <tr>
    <td>--md5</td>
    <td>https://en.wikipedia.org/wiki/MD5</td>
  </tr>
  <tr>
    <td>--ripemd160</td>
    <td>https://en.wikipedia.org/wiki/RIPEMD</td>
  </tr>
  <tr>
    <td>--sha1</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha224</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha256</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha384</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha512</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha3-224</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-384</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-512</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--shake128</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--shake256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--whirlpool</td>
    <td>https://en.wikipedia.org/wiki/Whirlpool_(hash_function)</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="4">Usage brute</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Brute options</th>
    <th>Hash target</th>
    <th>Dictionary</th>
  </tr>
  <tr>
    <td>brute</td>
    <td>--md5</td>
    <td>098f6bcd4621d373cade4e832627b4f6</td>
    <td>dictionary.txt</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <td>There are not enough parameters to execute the command `brute`.</td>
  <td>There are not enough parameters for the command to work. Check the spelling syntax.</td>
  </tr>
  <td>There must be an exact parameter here. The `--all` option is not applicable here.</td>
  <td>You cannot use the `--all` option, or `-a` for short. This parameter is responsible for the use of all hash functions in the bruforce command, you need a specific hash function. </td>
  </tr>
  <td>An error occurred while opening the dictionary file.</td>
  <td>Apparently there was an error opening the dictionary file. The file is opened with `latin-1` encoding in `r` mode.</td>
  </tr>
  <td>Nothing was found.</td>
  <td>No results. Try with a different dictionary.</td>
  </tr>
  <td>Could not find dictionary file.</td>
  <td>Check the existence of the dictionary and the syntax for writing the command.</td>
  </tr>
</table>

## cd
<table>
  <tr>
    <th colspan="2">Command cd</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>cd</td>
    <td>Changing the current working directory.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage cd</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Cd options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>cd</td>
    <td></td>
    <td>The command without parameters displays the current directory.</td>
  </tr>
  <tr>
    <td>cd</td>
    <td>..</td>
    <td>Go back to previous directory.</td>
  </tr>
  <tr>
    <td>cd</td>
    <td>/test</td>
    <td>Change to another directory.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <td>Could not find directory.</td>
  <td>Failed to change directory. Check the existence of the directory and the syntax for writing the command.</td>
  </tr>
</table>

## clear
<table>
  <tr>
    <th colspan="2">Command clear</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>clear</td>
    <td>Clearing the terminal.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options clear</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-e, --enable, --on</td>
    <td>Enabled screen clearing after command input.</td>
  </tr>
  <tr>
    <td>-d, --disable, --off</td>
    <td>Disabled screen clearing after command input.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage clear</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Clear options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>clear</td>
    <td></td>
    <td>The command without parameters displays the current directory.</td>
  </tr>
  <tr>
    <td>clear</td>
    <td>-e</td>
    <td>Enabled screen clearing after command input.</td>
  </tr>
  <tr>
    <td>clear</td>
    <td>-d</td>
    <td>Disabled screen clearing after command input.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <td>Unknown parameter.</td>
  <td>Apparently you specified an incorrect parameter to execute the command, view the list of available parameters. Pay attention to the command syntax.</td>
  </tr>
</table>

> clear or clean or cls are called by the same command. Syntactic sugar, nothing more.

## dir
<table>
  <tr>
    <th colspan="2">Command dir</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>dir</td>
    <td>Displaying directory contents.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage dir</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Dir options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>dir</td>
    <td></td>
    <td>Display files and folders in the current directory.</td>
  </tr>
  <tr>
    <td>dir</td>
    <td>/test</td>
    <td>Display files and folders of a specific directory.</td>
  </tr>
</table>

## echo
<table>
  <tr>
    <th colspan="2">Command echo</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>echo</td>
    <td>Displaying directory contents.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options echo</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-e, --enable, --on</td>
    <td>Enabled command output mode on the screen.</td>
  </tr>
  <tr>
    <td>-d, --disable, --off</td>
    <td>Disabled command output mode on the screen.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage echo</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Echo options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>echo</td>
    <td></td>
    <td>If you do not pass parameters, then the output will be a new line.</td>
  </tr>
  <tr>
    <td>echo</td>
    <td>test</td>
    <td>Text output.</td>
  </tr>
  <tr>
    <td>echo</td>
    <td>-e</td>
    <td>Enabled command output mode on the screen.</td>
  </tr>
  <tr>
    <td>echo</td>
    <td>-d</td>
    <td>Disabled command output mode on the screen.</td>
  </tr>
</table>

## exit
<table>
  <tr>
    <th colspan="2">Command exit</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>exit</td>
    <td>Exiting the program.</td>
  </tr>
</table>

## file | folder
<table>
  <tr>
    <th colspan="2">Command file | folder</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>file | folder</td>
    <td>Command for working with files | folders.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options file | folder</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-c, --create</td>
    <td>Create file | folder.</td>
  </tr>
  <tr>
    <td>-r, --remove</td>
    <td>Delete a file | folder.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage file | folder</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>File | folder options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>file | folder</td>
    <td>-c test.txt | -c test</td>
    <td>The file `test.txt` | folder `test` will be created.</td>
  </tr>
  <tr>
    <td>file | folder</td>
    <td>-r tеst.txt | test</td>
    <td>The file `test.txt` | folder `test` will be removed.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Unknown parameter.</td>
    <td>Could not find the parameter to execute the command, please note the syntax of writing.</td>
  </tr>
  <tr>
    <td>You did not enter a file | folder name.</td>
    <td>Apparently you did not specify the file | folder name, pay attention to the syntax for writing the command.</td>
  </tr>
  <tr>
    <td>Failed to create file | folder.</td>
    <td>For some reason, the file | folder could not be created.</td>
  </tr>
  <tr>
    <td>Failed to delete file | folder.</td>
    <td>Apparently for some reason it was not possible to delete the file | folder.</td>
  </tr>
  <tr>
    <td>There are not enough parameters to execute the command `file` | `folder`.</td>
    <td>Apparently you didn't specify any parameters. This command will not work without parameters.</td>
  </tr>
  <tr>
    <td>Could not find file | folder.</td>
    <td>The file | folder could not be found to delete. Check its existence, most likely it has already been deleted or simply moved. Also check the command syntax.</td>
  </tr>
</table>

> Commands such as file or folder are combined into one help because they work the same `almost` but the errors are the same `only handled by the program`. I just didn't want to write the same text twice.

## hash
![image](https://user-images.githubusercontent.com/107058068/179059858-c8c5cf37-cae1-4ea4-a8d0-8b419a1a8e73.png)

<table>
  <tr>
    <th colspan="2">Command hash</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>hash</td>
    <td>Command for working with a hash function.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options hash</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>--adler32</td>
    <td>https://en.wikipedia.org/wiki/Adler-32</td>
  </tr>
  <tr>
    <td>--blake2b</td>
    <td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td>
  </tr>
  <tr>
    <td>--blake2s</td>
    <td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td>
  </tr>
  <tr>
    <td>--crc32</td>
    <td>https://en.wikipedia.org/wiki/Cyclic_redundancy_check</td>
  </tr>
  <tr>
    <td>--keccak224</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak384</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak512</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--md4</td>
    <td>https://en.wikipedia.org/wiki/MD4</td>
  </tr>
  <tr>
    <td>--md5</td>
    <td>https://en.wikipedia.org/wiki/MD5</td>
  </tr>
  <tr>
    <td>--ripemd160</td>
    <td>https://en.wikipedia.org/wiki/RIPEMD</td>
  </tr>
  <tr>
    <td>--sha1</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha224</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha256</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha384</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha512</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha3-224</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-384</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-512</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--shake128</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--shake256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--whirlpool</td>
    <td>https://en.wikipedia.org/wiki/Whirlpool_(hash_function)</td>
  </tr>
  <tr>
    <td>-a, --all</td>
    <td>Hashing a string with all functions. For the place of a specific function, everything at once.</td>
  </tr>
  <tr>
    <td>-s, --string</td>
    <td>Regular string comparisons.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage hash</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Hash options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>hash</td>
    <td>--md5 test</td>
    <td>Hashing string `test` in md5.</td>
  </tr>
  <tr>
    <td>hash</td>
    <td>--md5 test == 098f6bcd4621d373cade4e832627b4f6</td>
    <td>Comparison if after converting the string `test` the resulting hash will be equal to the parameter, then everything is correct.</td>
  </tr>
  <tr>
    <td>hash</td>
    <td>--md5 098f6bcd4621d373cade4e832627b4f6 == test</td>
    <td>The same as above, just a different syntax.</td>
  </tr>
  <tr>
    <td>hash</td>
    <td>-s test == test</td>
    <td>Regular string comparisons.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Does not equal.</td>
    <td>This reads that when comparing the parameters are not equal to each other.</td>
  </tr>
  <tr>
    <td>There are not enough parameters to execute the command `hash`.</td>
    <td>Apparently you didn't specify any parameters. This command will not work without parameters.</td>
  </tr>
  <tr>
    <td>Could not find hash.</td>
    <td>Apparently you have specified a hash function that is not in the program, check the syntax for writing the command.</td>
  </tr>
</table>

## Help
<table>
  <tr>
    <th colspan="2">Command help</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>help</td>
    <td>Displaying program help.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options echo</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-a, --all</td>
    <td>Complete help for the program.</td>
  </tr>
  <tr>
    <td>-g, --github</td>
    <td></td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage help</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Help options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>help</td>
    <td></td>
    <td>Brief display of the list of program commands.</td>
  </tr>
  <tr>
    <td>help</td>
    <td>-a</td>
    <td>Full display of the list of program commands.</td>
  </tr>
  <tr>
    <td>help</td>
    <td>-g</td>
    <td>Viewing the program repository.</td>
  </tr>
  <tr>
    <td>help</td>
    <td>hash</td>
    <td>Display help for a specific command.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Can't find help for command</td>
    <td>There is no help for the command you entered, pay attention to the syntax of writing.</td>
  </tr>
  </tr>
</table>

## history
<table>
  <tr>
    <th colspan="2">Command history</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>history</td>
    <td>Command for working with input history.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options history</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-c, --clear</td>
    <td>Clearing the history file.</td>
  </tr>
  <tr>
    <td>-s, --clear-session </td>
    <td>Clearing the history file and session.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage history</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>History options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>history</td>
    <td></td>
    <td>Display input history.</td>
  </tr>
  <tr>
    <td>history</td>
    <td>-c</td>
    <td>The history file will be cleared. (.hashcap_terminal_history).</td>
  </tr>
  <tr>
    <td>history</td>
    <td>-s</td>
    <td>The history file and session will be cleared.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Unknown parameter.</td>
    <td>Apparently you entered an unknown parameter, pay attention to the syntax for writing the command.</td>
  </tr>
</table>

## ls
<table>
  <tr>
    <th colspan="2">Command ls</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>ls</td>
    <td>Displaying directory contents.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options ls</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-f, --file</td>
    <td>Display only files.</td>
  </tr>
  <tr>
    <td>-d, --directory</td>
    <td>Display only folders.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage ls</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Ls options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>ls</td>
    <td></td>
    <td>Display files and folders in the current directory.</td>
  </tr>
  <tr>
    <td>ls</td>
    <td>/test -f</td>
    <td>Display only files.</td>
  </tr>
  <tr>
    <td>ls</td>
    <td>/test -d</td>
    <td>Display only folders.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Could not find directory</td>
    <td>Could not find directory to display content. Check the syntax for writing the command and for the existence of the directory.</td>
  </tr>
</table>

## pwd
<table>
  <tr>
    <th colspan="3">Usage pwd</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>pwd</td>
    <td>Display current working directory.</td>
  </tr>
</table>

## read
<table>
  <tr>
    <th colspan="2">Command read</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>read</td>
    <td>Reading files.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options read</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>-e, --encoding</td>
    <td>File opening encoding.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage read</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Read options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>read</td>
    <td>test.txt</td>
    <td>The file `test.txt` will be read. (default: UTF-8).</td>
  </tr>
  <tr>
    <td>read</td>
    <td>test.txt -e=UTF-8</td>
    <td>The `test.txt` file will be read with only the specified encoding.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>There are not enough parameters to execute the command `read`.</td>
    <td>Apparently you didn't specify any parameters. This command will not work without parameters.</td>
  </tr>
  <tr>
    <td>Could not find the file.</td>
    <td>Could not find a file to display it. Check the syntax for writing and existing the file.</td>
  </tr>
  <tr>
    <td>Unknown encoding.</td>
    <td>Failed to find the encoding, you specified the wrong encoding or the file cannot be opened with this encoding. (errors != ignore).</td>
  </tr>
</table>

## sum
![image](https://user-images.githubusercontent.com/107058068/179059304-182e2282-1943-46b6-9153-e506cd3ca681.png)

<table>
  <tr>
    <th colspan="2">Command sum</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>sum</td>
    <td>Display the hash sum of a file.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options sum</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
  <tr>
    <td>--adler32</td>
    <td>https://en.wikipedia.org/wiki/Adler-32</td>
  </tr>
  <tr>
    <td>--blake2b</td>
    <td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td>
  </tr>
  <tr>
    <td>--blake2s</td>
    <td>https://en.wikipedia.org/wiki/BLAKE_(hash_function)</td>
  </tr>
  <tr>
    <td>--crc32</td>
    <td>https://en.wikipedia.org/wiki/Cyclic_redundancy_check</td>
  </tr>
  <tr>
    <td>--keccak224</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak384</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--keccak512</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--md4</td>
    <td>https://en.wikipedia.org/wiki/MD4</td>
  </tr>
  <tr>
    <td>--md5</td>
    <td>https://en.wikipedia.org/wiki/MD5</td>
  </tr>
  <tr>
    <td>--ripemd160</td>
    <td>https://en.wikipedia.org/wiki/RIPEMD</td>
  </tr>
  <tr>
    <td>--sha1</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha224</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha256</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha384</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha512</td>
    <td>https://en.wikipedia.org/wiki/SHA-1</td>
  </tr>
  <tr>
    <td>--sha3-224</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-384</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--sha3-512</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--shake128</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--shake256</td>
    <td>https://en.wikipedia.org/wiki/SHA-3</td>
  </tr>
  <tr>
    <td>--whirlpool</td>
    <td>https://en.wikipedia.org/wiki/Whirlpool_(hash_function)</td>
  </tr>
  <tr>
    <td>-a, --all</td>
    <td>Hashing a string with all functions. For the place of a specific function, everything at once.</td>
  </tr>
</table>
</tr>
</table>
<table>
  <tr>
    <th colspan="3">Usage sum</th>
  </tr>
  <tr>
    <th>Command</th>
    <th>Sum options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>sum</td>
    <td>--md5 test.txt</td>
    <td>Display the hash sum of the file.</td>
  </tr>
  <tr>
    <td>sum</td>
    <td>--md5 test.txt == d8e8fca2dc0f896fd7cb4cb0031ba249</td>
    <td>Compare sum hashes.</td>
  </tr>
  <tr>
    <td>sum</td>
    <td>--md5 d8e8fca2dc0f896fd7cb4cb0031ba249 == test.txt</td>
    <td>Compare sum hashes.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Mistakes</th>
  </tr>
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Does not equal.</td>
    <td>This reads that when comparing the parameters are not equal to each other.</td>
  </tr>
  <tr>
    <td>Could not find the file.</td>
    <td>Could not find a file in order to display its sum, check the syntax for writing a command and the existence of a file.</td>
  </tr>
  <tr>
    <td>There are not enough parameters to execute the command `sum`.</td>
    <td>Apparently you didn't specify any parameters. This command will not work without parameters.</td>
  </tr>
</table>

## system
<table>
  <tr>
    <th colspan="2">Command system</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>system</td>
    <td>Execute an external command in a shell.</td>
  </tr>
</table>
<table>
  <tr>
    <th colspan="2">Options system</th>
  </tr>
  <tr>
    <th>Options</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>echo Hello, world!</td>
    <td>The external `echo` command will be executed.</td>
  </tr>
</table>

## version
<table>
  <tr>
    <th colspan="2">Command version</th>
  </tr>
  <tr>
    <th>Command</th>
    <th colspan="2">Description</th>
  </tr>
  <tr>
    <td>version</td>
    <td>Display the current version of the program.</td>
  </tr>
</table>

## Compilation
There are a lot of compilers for python, but I will use <a href="https://pypi.org/project/pyinstaller/">pyinstaller</a>.
```
pyinstaller -F HashCapTerminal.py
```
After compilation, one executable file will appear in the dist folder. In order to change the icon, add the parameter `--icon=ICON_NAME`.

## From developer
Please report all problems / errors so that they can be fixed in time, I think there are enough of them.
