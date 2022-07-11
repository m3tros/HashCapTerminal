<p align="center"><img src="https://user-images.githubusercontent.com/107058068/178225754-263efd37-04b1-4eb1-b21d-6e7793d62be2.png" alt="MetrosCrypt" width="100px" height="100px"></p>
<h1 align="center">HashCap Terminal</h1>

# Description
HashCap version [Command Line Interpreter | Terminal] program for working with hash functions.<br>
This program is implemented in <a href="https://www.python.org/">Python</a> version <a href="https://www.python.org/downloads/release/python-3104/">3.10.4</a>. The library for getting data from the user is <a href="https://pypi.org/project/prompt-toolkit/">prompt_toolkit</a>.<br>
Hashcap implements the conversion of a string into a hash, iteration of hashes, as well as getting the checksum of files.<br>








# Installation for python3
<table>
  <tr>
    <th>Library</th>
  </tr>
 <tr><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td></tr>
 <tr><td><a href="https://pypi.org/project/pysha3">pysha3</a></td></tr>
 <tr><td><a href="https://pypi.org/project/Whirlpool/">whirlpool</a></td></tr>
 <tr><td><a href="https://pypi.org/project/colorama/">colorama</a></td></tr>
 <tr><td><a href="https://pypi.org/project/prompt-toolkit/">prompt_toolkit</a></td></tr>
</table>

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
