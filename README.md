<p align="center"><img src="https://user-images.githubusercontent.com/107058068/178225754-263efd37-04b1-4eb1-b21d-6e7793d62be2.png" alt="HashCapTerminal" width="100px" height="100px"></p>
<h1 align="center">HashCap Terminal</h1>

# Description
HashCap version [Command Line Interpreter | Terminal] program for working with hash functions.<br>
This program is implemented in <a href="https://www.python.org/">Python</a> version <a href="https://www.python.org/downloads/release/python-3104/">3.10.4</a>. The library for getting data from the user is <a href="https://pypi.org/project/prompt-toolkit/">prompt_toolkit</a>.<br>
Hashcap implements the conversion of a string into a hash, iteration of hashes, as well as getting the checksum of files.<br>
<p align="center"><img src="https://user-images.githubusercontent.com/107058068/178722840-caff3c94-832a-4de6-b59b-ba9752dceefc.png" alt="HashCapTerminal"></p>

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
  <td>Unknown parameter.</td>
  <td>The command you entered could not be processed. This means that there is no such command, check the command syntax.</td>
  </tr>
  <tr>
    <td>Not enough permissions to execute the command.</td>
    <td>You do not have sufficient rights to execute the command, increase the rights to execute such commands. Use sudo if you are on linux or run the program as administrator if you are on windows.</td>
  </tr>
</table>

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
## Help
To display help for a specific command, you must add the name of the command after the `help` command.<br>
To display the full program help, use the `-a` or `--all` option, it will display the help of all commands.<br>

> Click on the command you need in the table, the link will take you to its help.

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
    <td>echo</td>
    <td>Display a line of text.</td>
  </tr>
  <tr>
    <td>exit, quit</td>
    <td>Exiting the program.</td>
  </tr>
  <tr>
    <td>file</td>
    <td>Command for working with files.</td>
  </tr>
  <tr>
    <td>folder</td>
    <td>Command for working with folders.</td>
  </tr>
  <tr>
    <td>hash</td>
    <td>Command for working with a hash function.</td>
  </tr>
  <tr>
    <td>help</td>
    <td>Displaying program help.</td>
  </tr>
  <tr>
    <td>history</td>
    <td>Command for working with input history.</td>
  </tr>
  <tr>
    <td>ls</td>
    <td>Displaying directory contents.</td>
  </tr>
  <tr>
    <td>pwd</td>
    <td>Display current working directory.</td>
  </tr>
  <tr>
    <td>read</td>
    <td>Reading files.</td>
  </tr>
  <tr>
    <td>sum</td>
    <td>Display the hash sum of a file.</td>
  </tr>
  <tr>
    <td>system</td>
    <td>Execute an external command in a shell.</td>
  </tr>
  <tr>
    <td>version</td>
    <td>Display the current version of the program.</td>
  </tr>
</table>


## brute
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

