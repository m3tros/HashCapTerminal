<p align="center"><img src="https://user-images.githubusercontent.com/107058068/178225754-263efd37-04b1-4eb1-b21d-6e7793d62be2.png" alt="MetrosCrypt" width="100px" height="100px"></p>
<h1 align="center">HashCap Terminal</h1>

# Description
HashCap version [Command Line Interpreter | Terminal] program for working with hash functions.<br>
This program is implemented in <a href="https://www.python.org/">Python</a> version <a href="https://www.python.org/downloads/release/python-3104/">3.10.4</a>. The library for getting data from the user is <a href="https://pypi.org/project/prompt-toolkit/0.5/">prompt_toolkit</a>.<br>
Hashcap implements the conversion of a string into a hash, iteration of hashes, as well as getting the checksum of files.<br>

# List of hash functions

<table>
  <tr>
    <th>Name</th>
    <th>Python library</th>
    <th>Wiki</th>
    <th>Example</th>
  </tr>

 <tr><td><a href="https://docs.python.org/3/library/zlib.html#zlib.adler32">adler32</a></td><td><a href="https://docs.python.org/3/library/zlib.html">zlib</a></td><td><a href="https://en.wikipedia.org/wiki/Adler-32">ADLER32</a></td><td>73204161</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html#hashlib.blake2b">blake2b</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/BLAKE_(hash_function)">BLAKE</a></td><td>a71079d42853dea26e453004338670a53814b78137ffbed07603a41d76a483aa9bc33b582f77d30a65e6f29a896c0411f38312e1d66e0bf16386c86a89bea572</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html#hashlib.blake2s">blake2s</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/BLAKE_(hash_function)">BLALE</a></td><td>f308fc02ce9172ad02a7d75800ecfc027109bc67987ea32aba9b8dcc7b10150e</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/zlib.html#zlib.crc32">crc32</a></td><td><a href="https://docs.python.org/3/library/zlib.html">zlib</a></td><td><a href="https://en.wikipedia.org/wiki/Cyclic_redundancy_check">CRC32</a></td><td>3632233996</td></tr>
 <tr><td>keccak224</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>3be30a9ff64f34a5861116c5198987ad780165f8366e67aff4760b5e</td></tr>
 <tr><td>keccak256</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>9c22ff5f21f0b81b113e63f7db6da94fedef11b2119b4088b89664fb9a3cb658</td></tr>
 <tr><td>keccak384</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>53d0ba137307d4c2f9b6674c83edbd58b70c0f4340133ed0adc6fba1d2478a6a03b7788229e775d2de8ae8c0759d0527</td></tr>
 <tr><td>keccak512</td><td><a href="https://pypi.org/project/pysha3">pysha3</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>1e2e9fc2002b002d75198b7503210c05a1baac4560916a3c6d93bcce3a50d7f00fd395bf1647b9abb8d1afcc9c76c289b0c9383ba386a956da4b38934417789e</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">md4</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/MD4">MD4</a></td><td>db346d691d7acc4dc2625db19f9e3f52</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">md5</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/MD5">MD5</a></td><td>098f6bcd4621d373cade4e832627b4f6</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">ripemd160</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/RIPEMD">RIPEMD</a></td><td>5e52fee47e6b070565f74372468cdc699de89107</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha1</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td><td>a94a8fe5ccb19ba61c4c0873d391e987982fbbd3</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha224</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td><td>90a3ed9e32b2aaf4c61c410eb925426119e1a9dc53d4286ade99a809</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha256</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td><td>9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha384</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td><td>768412320f7b0aa5812fce428dc4706b3cae50e02a64caa16a782249bfe8efc4b7ef1ccb126255d196047dfedf17a0a9</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha512</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-1">SHA1</a></td><td>ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-224</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>3797bf0afbbfca4a7bbba7602a2b552746876517a7f9b7ce2db0ae7b</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-256</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-384</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>e516dabb23b6e30026863543282780a3ae0dccf05551cf0295178d7ff0f1b41eecb9db3ff219007c4e097260d58621bd</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">sha3-512</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>9ece086e9bac491fac5c1d1046ca11d737b92a2b2ebd93f005d7b710110c0a678288166e7fbe796883a4f2e9b3ca9f484f521d0ce464345cc1aec96779149c14</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">shake128</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>d3b0aa9cd8b7255622cebc631e867d4093d6f6010191a53973c45fec9b07c774</td></tr>
 <tr><td><a href="https://docs.python.org/3/library/hashlib.html">shake256</a></td><td><a href="https://pypi.org/project/hashlib/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/SHA-3">SHA3</a></td><td>b54ff7255705a71ee2925e4a3e30e41aed489a579d5595e0df13e32e1e4dd202</td></tr>
 <tr><td>whirlpool</td><td><a href="https://pypi.org/project/Whirlpool/">hashlib</a></td><td><a href="https://en.wikipedia.org/wiki/Whirlpool_(hash_function)">SHA3</a></td><td>b913d5bbb8e461c2c5961cbe0edcdadfd29f068225ceb37da6defcf89849368f8c6c2eb6a4c4ac75775d032a0ecfdfe8550573062b653fe92fc7b8fb3b7be8d6</td></tr>
 

</table>
