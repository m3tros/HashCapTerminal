import os
import sys
import shlex
import time
import webbrowser
import zlib
import hashlib
import sha3 
import whirlpool
import colorama
import hashbase

from datetime import timedelta
from datetime import datetime
from colorama import Fore
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML

__version__ = 1.1

__help__ = '''All commands
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
    version             Display the current version of the program.'''

__brute__ = '''
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
    brute       --md5           098f6bcd4621d373cade4e832627b4f6    dictionary.txt'''

__cd__ = '''
Command cd
==========

    Command     Description                             
    -------     -----------                          
    cd          Changing the current working directory. 
                                                                                                  
    Usage cd
    ========
    
    Command     Cd options      Description
    -------     ----------      -----------
    cd                          The command without parameters displays the current directory.
    cd          ..              Go back to previous directory.
    cd          /test           Change to another directory.'''

__clear__ = '''
Command clear
=============

    Command     Description                          
    -------     -----------                           
    clear       Clearing the terminal.

    Options clear
    =============
    
    Options                 Description
    -------                 -----------
    -e, --enable, --on      Enabled screen clearing after command input.
    -d, --disable, --off    Disabled screen clearing after command input.

    Usage clear
    ===========
    
    Command     Clear options       Description
    -------     -------------       -----------
    clear                           Clearing the terminal.
    clear       -e                  Enabled screen clearing after command input.
    clear       -d                  Disabled screen clearing after command input.'''

__dir__ = '''
Command dir
===========

    Command     Description                             
    -------     -----------                          
    dir         Displaying directory contents.
                                                                                                 
    Usage dir
    =========

    Command     Dir options     Description
    -------     -----------     -----------
    dir                         Display files and folders in the current directory.
    dir         /test           Display files and folders of a specific directory.'''

__echo__ = '''
Command echo
============

    Command     Description                             
    -------     -----------                          
    echo        Display a line of text.
        
    Options echo
    ============
    
    Options                 Description
    -------                 -----------
    -e, --enable, --on      Enabled command output mode on the screen.
    -d, --disable, --off    Disabled command output mode on the screen.
                                                                                           
    Usage echo
    ==========
        
    Command     Echo options    Description
    -------     ------------    -----------
    echo                        If you do not pass parameters, 
                                then the output will be a new line.
    echo        test            Text output. 
    echo        -e              Enabled command output mode on the screen.
    echo        -d              Disabled command output mode on the screen.'''

__exit__ = '''
Command exit
============

    Command     Description                          
    -------     -----------                           
    exit        Exiting the program.'''

__hfile__ = '''
Command file
============

    Command     Description                             
    -------     -----------                          
    file        Command for working with files.
        
    Options file
    ============
    
    Options             Description
    -------             -----------
    -c, --create        Create file.  
    -r, --remove        Delete a file.
                                                                                           
    Usage file
    ==========

    Command     File options    Description
    -------     ------------    -----------
    file        -c test.txt     The file `test.txt` will be created.      
    file        -r tеst.txt     The file `test.txt` will be removed.'''

__folder__ = '''
Command folder
==============

    Command     Description                             
    -------     -----------                          
    folder      Command for working with folders.
        
    Options folder
    ==============
    
    Options         Description
    -------         -----------
    -c, --create    Create folder.  
    -r, --remove    Delete a folder.
                                                                                           
    Usage folder
    ============

    Command     Folder options      Description
    -------     --------------      -----------
    file        -c test             The folder `test` will be created.      
    file        -r tеst             The folder `test` will be removed.'''

__hash__ = '''
Command hash
============

    Command     Description                             
    -------     -----------                          
    hash        Command for working with a hash function.
        
    Options hash
    ============
    
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
    -a, --all       Hashing a string with all functions. 
                    For the place of a specific function, everything at once.
    -s, --string    Regular string comparisons.       
                                                                
    Usage hash
    ==========

    Command     Hash options                                        Description
    -------     ------------                                        -----------
    hash        --md5 test                                          Hashing string `test` in md5.                         
    hash        --md5 test == 098f6bcd4621d373cade4e832627b4f6      Comparison if after converting the string `test` the 
                                                                    resulting hash will be equal to the parameter, then everything is correct.
    hash        --md5 098f6bcd4621d373cade4e832627b4f6 == test      The same as above, just a different syntax.
    hash        -s test == test                                     Regular string comparisons.'''

__hhelp__ = '''
Command help
============

    Command     Description                             
    -------     -----------                          
    help        Displaying program help.
        
    Options help
    ============
    
    Options             Description
    -------             -----------
    -a, --all           Complete help for the program.                                
    -g, --github        Open the program repository.
    
    Usage help
    ==========
    
    Command     Help options        Description
    -------     ------------        -----------
    help                            Brief display of the list of program commands.
    help        -a                  Full display of the list of program commands.
    help        -g                  Viewing the program repository.
    help        hash                Display help for a specific command.'''

__history__ = '''
Command history
===============

    Command     Description                             
    -------     -----------                          
    history     Command for working with input history.
        
    Options history
    ===============
    
    Options                 Description
    -------                 -----------
    -c, --clear             Clearing the history file.
    -s, --clear-session     Clearing the history file and session.   
    
    Usage history
    =============
    
    Command     History options     Description
    -------     ---------------     -----------
    history                         Display input history.
    history     -c                  The history file will be cleared. (.hashcap_terminal_history).
    history     -s                  The history file and session will be cleared.'''

__ls__ = '''
Command ls
==========

    Command     Description                             
    -------     -----------                          
    ls          Displaying directory contents.
        
    Options ls
    ==========
    
    Options             Description
    -------             -----------
    -f, --file          Display only files.
    -d, --directory     Display only folders.

    Usage ls
    ========
    
    Command     Ls options      Description
    -------     ----------      -----------
    ls                          Display files and folders in the current directory.
    ls          /test -f        Display only files.
    ls          /test -d        Display only folders.'''

__pwd__ = f'''
Command pwd
===========

    Command     Description                          
    -------     -----------                           
    pwd         Display current working directory.   

    Usage pwd
    =========

    Command     Example     
    -------     -------
    pwd         {Fore.BLUE}[*]{Fore.WHITE} You are in directory: {os.getcwd()}'''

__read__ = '''
Command read
============

    Command     Description                             
    -------     -----------                          
    read        Reading files.
        
    Options read
    ============
    
    Options         Description
    -------         -----------
    -e, --encoding  File opening encoding.
    
    Usage read
    ==========

    Command     Read options        Description
    -------     ------------        -----------
    read        test.txt            The file `test.txt` will be read. (default: UTF-8).
    read        test.txt -e=UTF-8   The `test.txt` file will be read with only the specified encoding.'''

__sum__ = '''
Command sum
===========

    Command         Description                             
    -------         -----------                          
    sum             Display the hash sum of a file.
        
    Options sum
    ===========
    
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
    -a, --all       Hashing a string with all functions. 
                    For the place of a specific function, everything at once.

    Usage sum
    =========

    Command     Sum options                                         Description
    -------     -----------                                         -----------
    sum         --md5 test.txt                                      Display the hash sum of the file.
    sum         --md5 test.txt == d8e8fca2dc0f896fd7cb4cb0031ba249  Compare sum hashes.
    sum         --md5 d8e8fca2dc0f896fd7cb4cb0031ba249 == test.txt  Compare sum hashes.'''

__system__ = '''
Command system
==============

    Command     Description                             
    -------     -----------                          
    system      Execute an external command in a shell.

    Usage system
    ============

    Command     System options      Description
    -------     --------------      -----------                          
    system      echo Hello, world!  The external `echo` command will be executed.'''

__hversion__ = '''
Command version
===============

    Command     Description                          
    -------     -----------                           
    version     Display the current version of the program.'''

class Display:
    '''
    The class responsible for working with displaying messages on the screen has 3 types in total:
     * Regular message
     * Error message
     * Message warning
    And also for displaying the version, shutting down and clearing the terminal.
    '''

    def message(text, start='', end='\n'):
        print(f'{start}{Fore.BLUE}[i]{Fore.WHITE} {text}', end=end)
    
    def warning(text, start='', end='\n'):
        print(f'{start}{Fore.YELLOW}[w]{Fore.WHITE} {text}', end=end)
        
    def error(text, start='', end='\n'):
        print(f'{start}{Fore.RED}[e]{Fore.WHITE} {text}', end=end)
    
    def version_program():
        Display.message(f'Metros HashCap Terminal (version {__version__}).')

    def exit_program():
        Display.message('Metros HashCap Terminal Completion of work...', start='\n')
        sys.exit()  
        
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


class Hash:
    '''
    The class responsible for working with hash functions. 
    With it, you can convert strings to a hash, 
    get the hash sum of a file, and for brute force.
    '''
    
    def adler32(string):
        return zlib.adler32(string)
        
    def blake2b(string):
        return hashlib.blake2b(string).hexdigest()
    
    def blake2s(string):
        return hashlib.blake2s(string).hexdigest()
    
    def crc32(string):
        return zlib.crc32(string)
    
    def keccak224(string):
        return sha3.keccak_224(string).hexdigest()
    
    def keccak256(string):
        return sha3.keccak_256(string).hexdigest()
    
    def keccak384(string):
        return sha3.keccak_384(string).hexdigest()
    
    def keccak512(string):
        return sha3.keccak_512(string).hexdigest()
    
    def md2(string):
        return hashbase.MD2().generate_hash(string.decode())

    def md4(string):
        return hashlib.new('md4', string).hexdigest()

    def md5(string):
        return hashlib.md5(string).hexdigest()
    
    def ripemd128(string):
        return hashbase.RIPEMD128().generate_hash(string.decode())
    
    def ripemd160(string):
        return hashlib.new('ripemd160', string).hexdigest()
    
    def ripemd256(string):
        return hashbase.RIPEMD256().generate_hash(string.decode())
    
    def ripemd320(string):
        return hashbase.RIPEMD320().generate_hash(string.decode())

    def sha1(string):
        return hashlib.sha1(string).hexdigest()
    
    def sha224(string):
        return hashlib.sha224(string).hexdigest()
    
    def sha256(string):
        return hashlib.sha256(string).hexdigest()
    
    def sha384(string):
        return hashlib.sha384(string).hexdigest()
    
    def sha512(string):
        return hashlib.sha512(string).hexdigest()
   
    def sha3_224(string):
        return hashlib.sha3_224(string).hexdigest()
    
    def sha3_256(string):
        return hashlib.sha3_256(string).hexdigest()
    
    def sha3_384(string):
        return hashlib.sha3_384(string).hexdigest()
    
    def sha3_512(string):
        return hashlib.sha3_512(string).hexdigest()
    
    def shake128(string):
        return hashlib.shake_128(string).hexdigest(32)
    
    def shake256(string):
        return hashlib.shake_256(string).hexdigest(32)
    
    def whirlpool(string):
        return whirlpool.new(string).hexdigest()
    
    def all(string):
        return [f'adler32    ➜ {Hash.adler32(string)}',
                f'blake2b    ➜ {Hash.blake2b(string)}',
                f'blake2s    ➜ {Hash.blake2s(string)}',
                f'crc32      ➜ {Hash.crc32(string)}',
                f'keccak224  ➜ {Hash.keccak224(string)}',
                f'keccak256  ➜ {Hash.keccak256(string)}',
                f'keccak384  ➜ {Hash.keccak384(string)}',
                f'keccak512  ➜ {Hash.keccak512(string)}',
                f'md2        ➜ {Hash.md2(string)}',
                f'md4        ➜ {Hash.md4(string)}',
                f'md5        ➜ {Hash.md5(string)}',
                f'ripemd128  ➜ {Hash.ripemd128(string)}',
                f'ripemd160  ➜ {Hash.ripemd160(string)}',
                f'ripemd256  ➜ {Hash.ripemd256(string)}',
                f'ripemd320  ➜ {Hash.ripemd320(string)}',
                f'sha1       ➜ {Hash.sha1(string)}',
                f'sha224     ➜ {Hash.sha224(string)}',
                f'sha256     ➜ {Hash.sha256(string)}',
                f'sha384     ➜ {Hash.sha384(string)}',
                f'sha512     ➜ {Hash.sha512(string)}',
                f'sha3-224   ➜ {Hash.sha3_224(string)}',
                f'sha3-256   ➜ {Hash.sha3_256(string)}',
                f'sha3-384   ➜ {Hash.sha3_384(string)}',
                f'sha3-512   ➜ {Hash.sha3_512(string)}',
                f'shake128   ➜ {Hash.shake128(string)}',
                f'shake256   ➜ {Hash.shake256(string)}',
                f'whirlpool  ➜ {Hash.whirlpool(string)}']
    
    def action_check(type, hash, string):
        def file_as_bytes(file):
            with file:
                return file.read()
        if type == 'sum':
            string = file_as_bytes(open(string, 'rb')) 
        elif type == 'hash':
            string = string.encode('UTF-8')
        return Hash.get_hash(hash, string)
        
    def get_hash(hash, string):
        if hash == '--adler32':
            return Hash.adler32(string)
        elif hash == '--blake2b':
            return Hash.blake2b(string)
        elif hash == '--blake2s':
            return Hash.blake2s(string)
        elif hash == '--crc32':
            return Hash.crc32(string)
        elif hash == '--keccak224':
            return Hash.keccak224(string)
        elif hash == '--keccak256':
            return Hash.keccak256(string)
        elif hash == '--keccak384':
            return Hash.keccak384(string)
        elif hash == '--keccak512':
            return Hash.keccak512(string)
        elif hash == '--md2':
            return Hash.md2(string)
        elif hash == '--md4':
            return Hash.md4(string)
        elif hash == '--md5':
            return Hash.md5(string)
        elif hash == '--ripemd128':
            return Hash.ripemd128(string)
        elif hash == '--ripemd160':
            return Hash.ripemd160(string)
        elif hash == '--ripemd256':
            return Hash.ripemd256(string)
        elif hash == '--ripemd320':
            return Hash.ripemd320(string)
        elif hash == '--sha1':
            return Hash.sha1(string)
        elif hash == '--sha224':
            return Hash.sha224(string)
        elif hash == '--sha256':
            return Hash.sha256(string)
        elif hash == '--sha384':
            return Hash.sha384(string)
        elif hash == '--sha512':
            return Hash.sha512(string)
        elif hash == '--sha3-224':
            return Hash.sha3_224(string)
        elif hash == '--sha3-256':
            return Hash.sha3_256(string)
        elif hash == '--sha3-384':
            return Hash.sha3_384(string)
        elif hash == '--sha3-512':
            return Hash.sha3_512(string)
        elif hash == '--shake128':
            return Hash.shake128(string)
        elif hash == '--shake256':
            return Hash.shake256(string)
        elif hash == '--whirlpool':
            return Hash.whirlpool(string)
        elif hash == '--all' or hash == '-a':
            for i in Hash.all(string):
                Display.message(i)
            return False
        else:
            Display.error('Could not find hash: {}'.format(hash.replace('--', '')))
            return False
        

class Main:
    '''
    The main class of the program in it receives and processes the entered commands by the user.
    The `prompt toolkit` library is used to get the parameters. For output, the `Display` class with the `colorama` library.

    terminal_while - Variable responsible for the program loop in which the processing takes place.
    terminal_cleaning - Variable responsible for clearing the screen after a parameter entered by the user.
    terminal_session - Current terminal session.
    terminal_text - Input text. It can be hidden with the `echo` command.
    terminal_tmp_text - Variable containing input text. Needed to restore after hiding with the `echo` command.

    In the `__init__` function, the loop starts in which the init_input function works.
    In the `init_input` function, parameters are received from the user, 
    if the command is not equal to emptiness, then the `input_validation` command processing function will be called.
    '''
    
    terminal_while = True
    terminal_cleaning = False
    current_path = os.path.split(os.path.abspath(__file__))[0]
    terminal_prompt_history = os.path.abspath(f'{current_path}/.hashcap_history')
    terminal_session = PromptSession(history=FileHistory(terminal_prompt_history))
    terminal_text = HTML('''\n[<font color="#008000">HashCapTerminal</font>] (<b>{}</b>) \n$ ''')
    terminal_tmp_text = terminal_text
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        while self.terminal_while == True:
            self.init_input()
    
    def init_input(self):
        try:
            self.input_line = self.terminal_session.prompt(self.terminal_text.format(os.getcwd()))
        except KeyboardInterrupt:
            self.command_exit()
        except EOFError:
            self.command_exit()
        if self.terminal_cleaning == True:
            Display.clear()
        if self.input_line.replace(' ', '') != '':            
            self.input_line_split = shlex.split(self.input_line.replace('\\', '/'))
            try:
                self.input_validation()
            except PermissionError:
                Display.error(f'Not enough permissions to execute the command: {self.input_line}')
            except UnboundLocalError:
                pass
    
    def input_validation(self):
        if self.input_line_split[0].lower() == 'brute':
            self.command_brute()
        elif self.input_line_split[0].lower() == 'cd':
            self.command_cd()
        elif self.input_line_split[0].lower() == 'clear' or self.input_line_split[0].lower() == 'clean' or self.input_line_split[0].lower() == 'cls':
            self.command_clear()
        elif self.input_line_split[0].lower() == 'dir':
            self.command_dir()
        elif self.input_line_split[0].lower() == 'echo':
            self.command_echo()
        elif self.input_line_split[0].lower() == 'exit' or self.input_line_split[0].lower() == 'quit':
            self.terminal_while = False
        elif self.input_line_split[0].lower() == 'file':
            self.command_file()
        elif self.input_line_split[0].lower() == 'folder':
            self.command_folder()
        elif self.input_line_split[0].lower() == 'hash':
            self.command_hash()
        elif self.input_line_split[0].lower() == 'help':
            self.command_help()
        elif self.input_line_split[0].lower() == 'history':
            self.command_history()
        elif self.input_line_split[0].lower() == 'ls':
            self.command_ls()
        elif self.input_line_split[0].lower() == 'pwd':
            self.command_pwd()
        elif self.input_line_split[0].lower() == 'read':
            self.command_read()
        elif self.input_line_split[0].lower() == 'sum':
            self.command_sum()
        elif self.input_line_split[0].lower() == 'system':
            self.command_system()
        elif self.input_line_split[0].lower() == 'version':
            Display.version_program()
        else:
            Display.error(f'Command not found: {self.input_line}')
    
    def command_brute(self):        
        self.brute = False
        time_start_brute_force = time.monotonic()
        Display.message('Hash type\t\t : {}'.format(self.input_line_split[1].replace('--', '').lower()))
        Display.message(f'Hash target\t\t : {self.input_line_split[2]}')
        try:
            self.command_brute_start()
        except IndexError:
            Display.error('There are not enough parameters to execute the command `brute`.')
            return
        except KeyboardInterrupt:
            Display.message('Completion of brute force...', start='\n')
            return
        Display.message('Runtime: {}'.format(timedelta(seconds=time.monotonic() - time_start_brute_force)), start='\n')

    def command_brute_start(self):
        line = 0
        try:
            if self.input_line_split[1].lower() == '--all' or self.input_line_split[1].lower() == '-a':
                Display.error('There must be an exact parameter here. The `--all` option is not applicable here.')
                return
        except IndexError:
            pass
        if os.path.isfile(self.input_line_split[3]) == True:                
            try:
                dictionary = open(self.input_line_split[3], 'r', encoding='latin-1')
            except Exception as error_open_file:
                Display.error(f'An error occurred while opening the dictionary file ({self.input_line_split[3]}): {error_open_file}')
            Display.message(f'Path dictionary\t : {self.input_line_split[3]}')
            Display.message('Start date and time\t : {}\n'.format(datetime.now().strftime('%d.%m.%Y %H:%M:%S')))
            for i in dictionary: 
                line += 1
                i = i.rstrip()
                hash = Hash.action_check('hash', self.input_line_split[1].lower(), i)
                if self.input_line_split[2] == hash:
                    Display.message(f'{self.input_line_split[2]}:{i}')
                    Display.message('Result {}: {}'.format(self.input_line_split[1].replace('--', '').lower(), i))
                    self.brute = True
                    break
                else:
                    sys.stdout.write(f'{Fore.BLUE}[i]{Fore.WHITE} Processed combinations: {line}\r')
                    sys.stdout.flush()
            if self.brute == False:
                Display.error('Nothing was found.', start='\n\n')
        elif os.path.isfile(self.input_line_split[3]) == False:
            Display.error(f'Could not find dictionary file: {self.input_line_split[3]}', start='\n')
    
    def command_cd(self):
        try:
            if os.path.isdir(self.input_line_split[1]) == True:
                os.chdir(self.input_line_split[1])
                if self.terminal_text != '':
                    self.terminal_text = self.terminal_tmp_text.format(os.getcwd())
            else:
                Display.error(f'Could not find directory: {self.input_line_split[1]}')
        except IndexError:
            self.command_pwd()
     
    def command_clear(self):
        try:
            if self.input_line_split[1].lower() == '--enable' or self.input_line_split[1].lower() == '--on' or self.input_line_split[1].lower() == '-e':
                self.terminal_cleaning = True
                Display.message('Enabled screen clearing after command input.')
            elif self.input_line_split[1].lower() == '--disable' or self.input_line_split[1].lower() == '--off' or self.input_line_split[1].lower() == '-d':
                self.terminal_cleaning = False
                Display.message('Disabled screen clearing after command input.')
            else:
                Display.error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            Display.clear()
    
    def command_dir(self):
        try:
            if self.input_line_split[1].lower() != 'dir':
                directory = os.path.abspath(self.input_line_split[1])  
        except IndexError:
            directory = os.getcwd()
        print(' '.join(os.listdir(directory)))

    def command_echo(self):
        try:
            if self.input_line_split[1].lower() == '--enable' or self.input_line_split[1].lower() == '--on' or self.input_line_split[1].lower() == '-e':
                self.terminal_text = self.terminal_tmp_text
                Display.message('Enabled command output mode on the screen.')
            elif self.input_line_split[1].lower() == '--disable' or self.input_line_split[1].lower() == '--off' or self.input_line_split[1].lower() == '-d':
                self.terminal_text = ''
                Display.message('Disabled command output mode on the screen.')
            else:
                del self.input_line_split[0]
                print(' '.join(self.input_line_split))
        except IndexError:
            print()
    
    def command_exit(self): 
        Display.exit_program()

    def command_file(self):
        try:
            if self.input_line_split[1].lower() == '--create' or self.input_line_split[1].lower() == '-c':
                try:
                    with open(self.input_line_split[2], 'w') as create_file:
                        create_file.write('')
                    if os.path.isfile(self.input_line_split[2]) == True:
                        Display.message(f'The file has been successfully created: {self.input_line_split[2]}')
                    elif os.path.isfile(self.input_line_split[2]) == False:
                        Display.message(f'Failed to create file: {self.input_line_split[2]}')
                except IndexError:
                    Display.error('You did not enter a file name.')
                except IsADirectoryError:
                    pass
            elif self.input_line_split[1].lower() == '--remove' or self.input_line_split[1].lower() == '-r':
                try:
                    if os.path.isfile(self.input_line_split[2]) == False:
                        Display.error(f'Could not find file: {self.input_line_split[2]}')
                    elif os.path.isfile(self.input_line_split[2]) == True:
                        os.remove(self.input_line_split[2])
                        if os.path.isfile(self.input_line_split[2]) == False:
                            Display.warning(f'The file has been successfully deleted: {self.input_line_split[2]}')
                        elif os.path.isfile(self.input_line_split[2]) == True:
                            Display.error(f'Failed to delete file: {self.input_line_split[2]}')
                except IndexError:
                    Display.error('You did not enter a file name.')
            else:
                Display.error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            Display.error('There are not enough parameters to execute the command `file`.')
                
    def command_folder(self):
        try:
            if self.input_line_split[1].lower() == '--create' or self.input_line_split[1].lower() == '-c':
                try:
                    os.mkdir(self.input_line_split[2])
                    if os.path.isdir(self.input_line_split[2]) == True:
                        Display.message(f'The folder has been successfully created: {self.input_line_split[2]}')
                    elif os.path.isdir(self.input_line_split[2]) == False:
                        Display.error(f'Failed to create folder: {self.input_line_split[2]}')
                except IndexError:
                    Display.error('You did not enter a folder name.')
                except FileExistsError:
                    pass
            elif self.input_line_split[1].lower() == '--remove' or self.input_line_split[1].lower() == '-r':
                try:
                    if os.path.isdir(self.input_line_split[2]) == True:
                        os.rmdir(self.input_line_split[2])
                        if os.path.isfile(self.input_line_split[2]) == False:
                            Display.warning(f'The folder has been successfully deleted: {self.input_line_split[2]}')
                        elif os.path.isdir(self.input_line_split[2]) == True:
                            Display.error(f'Failed to delete folder: {self.input_line_split[2]}')
                    elif os.path.isdir(self.input_line_split[2]) == False: 
                        Display.error(f'Could not find folder: {self.input_line_split[2]}')
                except IndexError:
                    Display.error('You did not enter a folder name.')
            else:
                Display.error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            Display.error('There are not enough parameters to execute the command `folder`.')
    
    def command_hash(self):
        try:
            if self.input_line_split[3] == '==':
                if self.input_line_split[1] == '--string' or self.input_line_split[1] == '-s':
                    string_1 = self.input_line_split[2]
                    string_2 = self.input_line_split[4]
                else:
                    string_1 = Hash.action_check('hash', self.input_line_split[1].lower(), self.input_line_split[2])
                    string_2 = Hash.action_check('hash', self.input_line_split[1].lower(), self.input_line_split[4])
                if string_1 == self.input_line_split[4]:
                    Display.message('Equals.')
                elif self.input_line_split[2] == string_2:
                    Display.message('Equals.')
                else:
                    Display.warning('Does not equal.')
                return
        except IndexError:
            pass
        try:
            function_return_hash = Hash.action_check('hash', self.input_line_split[1].lower(), self.input_line_split[2])
            if function_return_hash != False:
                Display.message(function_return_hash)
        except IndexError:
            Display.error('There are not enough parameters to execute the command `hash`.')
            return

    def command_help(self):
        try:
            if self.input_line_split[1].lower() == '-a' or self.input_line_split[1].lower() == '--all':
                for i in [__help__,
                          __brute__,
                          __cd__,
                          __clear__,
                          __dir__,
                          __echo__,
                          __exit__,
                          __hfile__,
                          __folder__,
                          __hash__,
                          __hhelp__,
                          __history__,
                          __ls__,
                          __pwd__,
                          __read__,
                          __sum__,
                          __system__,
                          __hversion__]:
                    print(i)
                Display.message('Learn more: https://github.com/John-MetrosSoftware/HashCapTerminal', start='\n')
            elif self.input_line_split[1].lower() == '-g' or self.input_line_split[1].lower() == '--github':
                webbrowser.open_new('https://github.com/John-MetrosSoftware/HashCapTerminal')
            elif self.input_line_split[1].lower() == 'brute':
                print(__brute__)
            elif self.input_line_split[1].lower() == 'cd':
                print(__cd__)
            elif self.input_line_split[1].lower() == 'clear' or self.input_line_split[1].lower() == 'clean' or self.input_line_split[1].lower() == 'cls' :
                print(__clear__)
            elif self.input_line_split[1].lower() == 'dir':
                print(__dir__)
            elif self.input_line_split[1].lower() == 'echo':
                print(__echo__)
            elif self.input_line_split[1].lower() == 'exit' or self.input_line_split[1].lower() == 'quit':
                print(__exit__)
            elif self.input_line_split[1].lower() == 'file':
                print(__hfile__)
            elif self.input_line_split[1].lower() == 'folder':
                print(__folder__)
            elif self.input_line_split[1].lower() == 'hash':
                print(__hash__)
            elif self.input_line_split[1].lower() == 'help':
                print(__hhelp__)
            elif self.input_line_split[1].lower() == 'history':
                print(__history__)
            elif self.input_line_split[1].lower() == 'ls':
                print(__ls__)
            elif self.input_line_split[1].lower() == 'pwd':
                print(__pwd__)
            elif self.input_line_split[1].lower() == 'read':
                print(__read__)
            elif self.input_line_split[1].lower() == 'sum':
                print(__sum__)
            elif self.input_line_split[1].lower() == 'system':
                print(__system__)
            elif self.input_line_split[1].lower() == 'version':
                print(__hversion__)
            else:
                del self.input_line_split[0]
                Display.error('Can\'t find help for command: {}'.format(' '.join(self.input_line_split)))
        except IndexError:
            print(__help__)
            Display.message('Use the `help` command to display help for a specific command.', start='\n')

    def command_history(self):
        if os.path.isfile(self.terminal_prompt_history) == False:
            with open(self.terminal_prompt_history, 'w') as history_file:
                history_file.write('')
        try:
            if self.input_line_split[1].lower() == '--clear' or self.input_line_split[1].lower() == '-c':
                self.command_history_remove_history_file()
            elif self.input_line_split[1].lower() == '--clear-session' or self.input_line_split[1].lower() == '-s':
                self.terminal_session = PromptSession(history=FileHistory(self.terminal_prompt_history))
                self.command_history_remove_history_file()
                Display.message('The history has been completely cleared.')
            else:
                Display.error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            print(open(self.terminal_prompt_history).read())          
    
    def command_history_remove_history_file(self):
        os.remove(self.terminal_prompt_history)
        if os.path.isfile(self.terminal_prompt_history) == False:
            Display.message('The history file has been cleared.')
        elif os.path.isfile(self.terminal_prompt_history) == True:
            Display.error('The history file has not been cleared.')

    def command_ls(self):
        try:
            if self.input_line_split[1].lower() != 'ls':
                directory = os.path.abspath(self.input_line_split[1])
        except IndexError:
            directory = os.getcwd()
        try:
            if self.input_line_split[1].lower() == '--directory' or self.input_line_split[1].lower() == '-d':
                self.command_ls_folder(os.getcwd())
            elif self.input_line_split[1].lower() == '--file' or self.input_line_split[1].lower() == '-f':
                self.command_ls_file(os.getcwd())           
            elif self.input_line_split[2].lower() == '--directory' or self.input_line_split[2].lower() == '-d':
                self.command_ls_folder(directory)
            elif self.input_line_split[2].lower() == '--file' or self.input_line_split[2].lower() == '-f':
                self.command_ls_file(directory)
        except FileNotFoundError:
            Display.error(f'Could not find directory: {directory}')
        except IndexError:
            try:        
                self.command_ls_file(directory)
                self.command_ls_folder(directory)
            except FileNotFoundError:
                Display.error(f'Could not find directory: {directory}')
            
    def command_ls_folder(self, directory):
        for folder in os.listdir(directory):
            if os.path.isdir(os.path.abspath(f'{directory}/{folder}')):
                print(f'{Fore.BLUE}{folder}{Fore.WHITE}')
                
    def command_ls_file(self, directory):
        for file in os.listdir(directory):    
            if os.path.isfile(os.path.abspath(f'{directory}/{file}')):
                print(file)
    
    def command_pwd(self):
        Display.message(f'You are in directory: {os.getcwd()}')
                                  
    def command_read(self):
        try:
            split_encoding = shlex.split(self.input_line_split[2].lower().replace('=', ' '))
            if split_encoding[0] == '--encoding' or split_encoding[0] == '-e':
                encoding = split_encoding[1]
        except IndexError:
            encoding = 'UTF-8'
        try:
            print(open(self.input_line_split[1], encoding=encoding).read())
            Display.message(f'Read file: {self.input_line_split[1]} {encoding}')
        except IndexError:
            Display.error('There are not enough parameters to execute the command `read`.')
            return
        except FileNotFoundError:
            Display.error(f'Could not find the file: {self.input_line_split[1]}')
        except LookupError:
            Display.error(f'Unknown encoding: {encoding}')  
        except IsADirectoryError:
            pass
           
    def command_sum(self):
        try:
            if self.input_line_split[3] == '==':
                try:
                    if os.path.isfile(self.input_line_split[2]) == True:
                        string_1 = Hash.action_check('sum', self.input_line_split[1].lower(), self.input_line_split[2])
                        if string_1 == self.input_line_split[4]:
                            Display.message('Equals.')
                        else:
                            Display.warning('Does not equal.')
                    elif os.path.isfile(self.input_line_split[2]) == False:
                        string_2 = Hash.action_check('sum', self.input_line_split[1].lower(), self.input_line_split[4])
                        if self.input_line_split[2] == string_2:
                            Display.message('Equals.')
                        else:
                            Display.warning('Does not equal.')
                except FileNotFoundError :
                    if os.path.isfile(self.input_line_split[2]) == False and os.path.isfile(self.input_line_split[4]) == False:
                        Display.error('Could not find file. ')
                return
        except IndexError:
            pass     
        try:
            if os.path.isfile(self.input_line_split[2]) == True:
                function_return_hash = Hash.action_check('sum', self.input_line_split[1].lower(), self.input_line_split[2])
                if function_return_hash != False:
                    Display.message(function_return_hash)
            elif os.path.isfile(self.input_line_split[2]) == False:
                Display.error(f'Could not find file: {self.input_line_split[2]}')
        except IndexError:
            Display.error('There are not enough parameters to execute the command `sum`.')
            return
            
    def command_system(self):
        try:
            self.input_line_split[1]
            del self.input_line_split[0]
            os.system(' '.join(self.input_line_split))
        except IndexError:
            os.system(prompt('Enter command > '))
    

class Boot:
    '''
    This class is responsible for the program launch point; 
    the colorama library is initialized in it - this is necessary if you have windows problems here. 
    As well as displaying the version and after the completion of the work, displaying the successful closure.
    '''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__colorama__()
        self.__main__()
    
    def __colorama__(self):
        Display.clear()
        colorama.init()
        
    def __main__(self):
        Display.version_program()
        Main()
        Display.display_exit_program()

if __name__ == '__main__':
    try:
        Boot()
    except Exception as unknown_error:
        Display.error(f'Unknown error: {unknown_error}')
    sys.exit()
