import os
import sys
import shlex
import time
import webbrowser
import zlib
import hashlib
import sha3
import hashbase
import whirlpool
import datetime
import prompt_toolkit

__version__ = 1.1

COLOR_MESSAGE = '\033[96m'
COLOR_WARNING = '\033[93m'
COLOR_ERROR = '\033[91m'
COLOR_RESET = '\033[39m'

__help__ = '''All Commands
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
Command Brute
=============

    Command     Description                                
    -------     -----------                               
    brute       Brute-force hash function by dictionary.    

    Options Brute
    ============

    Hash            Description (wiki)
    -------         ------------------
    --adler32       https://en.wikipedia.org/wiki/Adler-32
    --blake2b       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --blake2s       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --crc32         https://en.wikipedia.org/wiki/Cyclic_redundancy_check
    --keccak224     https://en.wikipedia.org/wiki/SHA-3 
    --keccak256     https://en.wikipedia.org/wiki/SHA-3
    --keccak384     https://en.wikipedia.org/wiki/SHA-3
    --keccak512     https://en.wikipedia.org/wiki/SHA-3
    --md2           https://en.wikipedia.org/wiki/MD2_(hash_function)
    --md4           https://en.wikipedia.org/wiki/MD4
    --md5           https://en.wikipedia.org/wiki/MD5
    --ripemd128     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd160     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd256     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd320     https://en.wikipedia.org/wiki/RIPEMD
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

    Usage Brute
    ===========

    Command     Options Brute   Hash Target                         Dictionary
    -------     -------------   -----------                         ----------
    brute       --md5           098f6bcd4621d373cade4e832627b4f6    /usr/share/wordlists/rockyou.txt'''

__cd__ = '''
Command Cd
==========

    Command     Description                             
    -------     -----------                          
    cd          Changing the current working directory. 

    Usage Cd
    ========

    Command     Options Cd      Description
    -------     ----------      -----------
    cd                          The command without parameters displays the current directory.
    cd          ..              Go back to previous directory.
    cd          ~/Desktop       Change to another directory.'''

__clear__ = '''
Command Clear
=============

    Command     Description                          
    -------     -----------                           
    clear       Clearing the terminal.

    Options Clear
    =============

    Options                 Description
    -------                 -----------
    -e, --enable, --on      Enabled screen clearing after command input.
    -d, --disable, --off    Disabled screen clearing after command input.

    Usage Clear
    ===========

    Command     Options Clear       Description
    -------     -------------       -----------
    clear                           Clearing the terminal.
    clear       -e                  Enabled screen clearing after command input.
    clear       -d                  Disabled screen clearing after command input.'''

__dir__ = '''
Command Dir
===========

    Command     Description                             
    -------     -----------                          
    dir         Displaying directory contents.

    Usage Dir
    =========

    Command     Options Dir     Description
    -------     -----------     -----------
    dir                         Display files and folders in the current directory.
    dir         ~/Desktop       Display files and folders of a specific directory.'''

__echo__ = '''
Command Echo
============

    Command     Description                             
    -------     -----------                          
    echo        Display a line of text.

    Options Echo
    ============

    Options                 Description
    -------                 -----------
    -e, --enable, --on      Enabled command output mode on the screen.
    -d, --disable, --off    Disabled command output mode on the screen.

    Usage Echo
    ==========

    Command     Echo options    Description
    -------     ------------    -----------
    echo                        If you do not pass parameters, 
                                then the output will be a new line.
    echo        text            Text output. 
    echo        -e              Enabled command output mode on the screen.
    echo        -d              Disabled command output mode on the screen.'''

__exit__ = '''
Command Exit
============

    Command     Description                          
    -------     -----------                           
    exit        Exiting the program.'''

__hfile__ = '''
Command File
============

    Command     Description                             
    -------     -----------                          
    file        Command for working with files.

    Options File
    ============

    Options             Description
    -------             -----------
    -c, --create        Create file.  
    -r, --remove        Delete a file.

    Usage file
    ==========

    Command     Options File    Description
    -------     ------------    -----------
    file        -c file.txt     The file (test.txt) will be created.      
    file        -r file.txt     The file (test.txt) will be removed.'''

__folder__ = '''
Command Folder
==============

    Command     Description                             
    -------     -----------                          
    folder      Command for working with folders.

    Options Folder
    ==============

    Options         Description
    -------         -----------
    -c, --create    Create folder.  
    -r, --remove    Delete a folder.

    Usage Folder
    ============

    Command     Options Folder  Description
    -------     --------------  -----------
    file        -c folder       The folder [folder] will be created.      
    file        -r folder       The folder [test] will be removed.'''

__hash__ = '''
Command Hash
============

    Command     Description                             
    -------     -----------                          
    hash        Command for working with a hash function.

    Options Hash
    ============

    Hash            Description (wiki)
    -------         ------------------
    --adler32       https://en.wikipedia.org/wiki/Adler-32
    --blake2b       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --blake2s       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --crc32         https://en.wikipedia.org/wiki/Cyclic_redundancy_check
    --keccak224     https://en.wikipedia.org/wiki/SHA-3 
    --keccak256     https://en.wikipedia.org/wiki/SHA-3
    --keccak384     https://en.wikipedia.org/wiki/SHA-3
    --keccak512     https://en.wikipedia.org/wiki/SHA-3
    --md2           https://en.wikipedia.org/wiki/MD2_(hash_function)
    --md4           https://en.wikipedia.org/wiki/MD4
    --md5           https://en.wikipedia.org/wiki/MD5
    --ripemd128     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd160     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd256     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd320     https://en.wikipedia.org/wiki/RIPEMD
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
    
    Options         Description 
    -------         -----------
    -a, --all       Hashing a string with all functions. 
                    For the place of a specific function, everything at once.
    -s, --string    Regular string comparisons.       

    Usage Hash
    ==========

    Command     Options Hash                                        Description
    -------     ------------                                        -----------
    hash        --md5 text                                          Hashing string (test) in md5.                         
    hash        --md5 text == 098f6bcd4621d373cade4e832627b4f6      Comparison if after converting the string (test) the 
                                                                    resulting hash will be equal to the parameter, 
                                                                    then everything is correct.
    hash        --md5 098f6bcd4621d373cade4e832627b4f6 == text      The same as above, just a different syntax.
    hash        -s text == text                                     Regular string comparisons.'''

__all_command__ = '''
Command Help
============

    Command     Description                             
    -------     -----------                          
    help        Displaying program help.

    Options Help
    ============

    Options             Description
    -------             -----------
    -a, --all           Complete help for the program.                                
    -g, --github        Open the program repository.

    Usage Help
    ==========

    Command     Options Help    Description
    -------     ------------    -----------
    help                        Brief display of the list of program commands.
    help        -a              Full display of the list of program commands.
    help        -g              Viewing the program repository.
    help        hash            Display help for a specific command.'''

__history__ = '''
Command History
===============

    Command     Description                             
    -------     -----------                          
    history     Command for working with input history.

    Options History
    ===============

    Options                 Description
    -------                 -----------
    -c, --clear             Clearing the history file.
    -s, --clear-session     Clearing the history file and session.   

    Usage History
    =============

    Command     Options History     Description
    -------     ---------------     -----------
    history                         Display input history.
    history     -c                  The history file will be cleared. (.file_history).
    history     -s                  The history file and session will be cleared.'''

__ls__ = '''
Command Ls
==========

    Command     Description                             
    -------     -----------                          
    ls          Displaying directory contents.

    Options Ls
    ==========

    Options             Description
    -------             -----------
    -f, --file          Display only files.
    -d, --directory     Display only folders.

    Usage Ls
    ========

    Command     Options Ls      Description
    -------     ----------      -----------
    ls                          Display files and folders in the current directory.
    ls          ~/Desktop -f    Display only files.
    ls          ~/Desktop -d    Display only folders.'''

__pwd__ = f'''
Command Pwd
===========

    Command     Description                          
    -------     -----------                           
    pwd         Display current working directory.   

    Usage Pwd
    =========

    Command     Example     
    -------     -------
    pwd         {COLOR_MESSAGE}[*]{COLOR_RESET} You are in directory: {os.getcwd()}'''

__read__ = '''
Command Read
============

    Command     Description                             
    -------     -----------                          
    read        Reading files.

    Options Read
    ============

    Options         Description
    -------         -----------
    -e, --encoding  File opening encoding.

    Usage Read
    ==========

    Command     Options Read            Description
    -------     ------------            -----------
    read        test_file.txt           The file (test.txt) will be read. (default: UTF-8).
    read        test_file.txt -e=UTF-8  The (test.txt) file will be read with only the specified encoding.'''

__sum__ = '''
Command Sum
===========

    Command         Description                             
    -------         -----------                          
    sum             Display the hash sum of a file.

    Options Sum
    ===========
    
    Hash            Description (wiki)
    -------         ------------------
    --adler32       https://en.wikipedia.org/wiki/Adler-32
    --blake2b       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --blake2s       https://en.wikipedia.org/wiki/BLAKE_(hash_function)
    --crc32         https://en.wikipedia.org/wiki/Cyclic_redundancy_check
    --keccak224     https://en.wikipedia.org/wiki/SHA-3 
    --keccak256     https://en.wikipedia.org/wiki/SHA-3
    --keccak384     https://en.wikipedia.org/wiki/SHA-3
    --keccak512     https://en.wikipedia.org/wiki/SHA-3
    --md2           https://en.wikipedia.org/wiki/MD2_(hash_function)
    --md4           https://en.wikipedia.org/wiki/MD4
    --md5           https://en.wikipedia.org/wiki/MD5
    --ripemd128     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd160     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd256     https://en.wikipedia.org/wiki/RIPEMD
    --ripemd320     https://en.wikipedia.org/wiki/RIPEMD
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

    Options         Description
    -------         -----------
    -a, --all       Hashing a string with all functions. 
                    For the place of a specific function, everything at once.

    Usage Sum
    =========

    Command     Options Sum                                             Description
    -------     -----------                                             -----------
    sum         --md5 test_file.txt                                     Display the hash sum of the file.
    sum         --md5 test_file.txt == d8e8fca2dc0f896fd7cb4cb0031ba249 Compare sum hashes.
    sum         --md5 d8e8fca2dc0f896fd7cb4cb0031ba249 == test_file.txt Compare sum hashes.'''

__system__ = '''
Command System
==============

    Command     Description                             
    -------     -----------                          
    system      Execute an external command in a shell.

    Usage System
    ============

    Command     Options System      Description
    -------     --------------      -----------                          
    system      echo Hello, World!  The external (echo) command will be executed.'''

__help_version__ = '''
Command Version
===============

    Command     Description                          
    -------     -----------                           
    version     Display the current version of the program.'''


def message(text, start='', end='\n'):
    print(f'{start}{COLOR_MESSAGE}[i]{COLOR_RESET} {text}', end=end)


def warning(text, start='', end='\n'):
    print(f'{start}{COLOR_WARNING}[w]{COLOR_RESET} {text}', end=end)


def error(text, start='', end='\n'):
    print(f'{start}{COLOR_ERROR}[e]{COLOR_RESET} {text}', end=end)


def exit_program():
    message('Metros HashCap Terminal Completion of work...', start='\n')
    sys.exit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


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


def hash_whirlpool(string):
    return whirlpool.new(string).hexdigest()


def all_hash(string):
    return [f'adler32    : {adler32(string)}',
            f'blake2b    : {blake2b(string)}',
            f'blake2s    : {blake2s(string)}',
            f'crc32      : {crc32(string)}',
            f'keccak224  : {keccak224(string)}',
            f'keccak256  : {keccak256(string)}',
            f'keccak384  : {keccak384(string)}',
            f'keccak512  : {keccak512(string)}',
            f'md2        : {md2(string)}',
            f'md4        : {md4(string)}',
            f'md5        : {md5(string)}',
            f'ripemd128  : {ripemd128(string)}',
            f'ripemd160  : {ripemd160(string)}',
            f'ripemd256  : {ripemd256(string)}',
            f'ripemd320  : {ripemd320(string)}',
            f'sha1       : {sha1(string)}',
            f'sha224     : {sha224(string)}',
            f'sha256     : {sha256(string)}',
            f'sha384     : {sha384(string)}',
            f'sha512     : {sha512(string)}',
            f'sha3-224   : {sha3_224(string)}',
            f'sha3-256   : {sha3_256(string)}',
            f'sha3-384   : {sha3_384(string)}',
            f'sha3-512   : {sha3_512(string)}',
            f'shake128   : {shake128(string)}',
            f'shake256   : {shake256(string)}',
            f'whirlpool  : {hash_whirlpool(string)}']


def get_hash(target_hash, string):
    if target_hash == '--adler32':
        return adler32(string)
    elif target_hash == '--blake2b':
        return blake2b(string)
    elif target_hash == '--blake2s':
        return blake2s(string)
    elif target_hash == '--crc32':
        return crc32(string)
    elif target_hash == '--keccak224':
        return keccak224(string)
    elif target_hash == '--keccak256':
        return keccak256(string)
    elif target_hash == '--keccak384':
        return keccak384(string)
    elif target_hash == '--keccak512':
        return keccak512(string)
    elif target_hash == '--md2':
        return md2(string)
    elif target_hash == '--md4':
        return md4(string)
    elif target_hash == '--md5':
        return md5(string)
    elif target_hash == '--ripemd128':
        return ripemd128(string)
    elif target_hash == '--ripemd160':
        return ripemd160(string)
    elif target_hash == '--ripemd256':
        return ripemd256(string)
    elif target_hash == '--ripemd320':
        return ripemd320(string)
    elif target_hash == '--sha1':
        return sha1(string)
    elif target_hash == '--sha224':
        return sha224(string)
    elif target_hash == '--sha256':
        return sha256(string)
    elif target_hash == '--sha384':
        return sha384(string)
    elif target_hash == '--sha512':
        return sha512(string)
    elif target_hash == '--sha3-224':
        return sha3_224(string)
    elif target_hash == '--sha3-256':
        return sha3_256(string)
    elif target_hash == '--sha3-384':
        return sha3_384(string)
    elif target_hash == '--sha3-512':
        return sha3_512(string)
    elif target_hash == '--shake128':
        return shake128(string)
    elif target_hash == '--shake256':
        return shake256(string)
    elif target_hash == '--whirlpool':
        return hash_whirlpool(string)
    elif target_hash == '--all' or target_hash == '-a':
        for i in all_hash(string):
            message(i)
        return False
    else:
        error('Could not find target_hash: {}'.format(target_hash.replace('--', '')))
        return False


def action_check(type_hash, target_hash, string):
    def file_as_bytes(file):
        with file:
            return file.read()

    if type_hash == 'sum':
        string = file_as_bytes(open(string, 'rb'))
    elif type_hash == 'hash' or type_hash == 'brute':
        string = string.encode('UTF-8')
    return get_hash(target_hash, string)


def command_ls_file(ls_directory_file):
    for file in os.listdir(ls_directory_file):
        if os.path.isfile(os.path.abspath(f'{ls_directory_file}/{file}')):
            print(file)


def command_ls_folder(ls_directory_folder):
    for folder in os.listdir(ls_directory_folder):
        if os.path.isdir(os.path.abspath(f'{ls_directory_folder}/{folder}')):
            print(f'{COLOR_MESSAGE}{folder}{COLOR_RESET}')


class Main:

    """
    The main class of the program in it receives and processes the entered commands by the user.
    The (prompt toolkit) library is used to get the parameters.

    terminal_while - Variable responsible for the program loop in which the processing takes place.
    terminal_cleaning - Variable responsible for clearing the screen after a parameter entered by the user.
    terminal_session - Current terminal session.
    terminal_text - Input text. It can be hidden with the (echo) command.
    terminal_tmp_text - Variable containing input text. Needed to restore after hiding with the (echo) command.

    In the (__init__) function, the loop starts in which the init_input function works.
    In the (init_input) function, parameters are received from the user,
    if the command is not equal to emptiness, then the (input_validation) command processing function will be called.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_line = ''
        self.input_line_split = []
        self.terminal_while = True
        self.terminal_cleaning = False
        self.current_path = os.path.split(os.path.abspath(__file__))[0]
        self.file_history = os.path.abspath(f'{self.current_path}/.hashcap_history')
        self.terminal_session = prompt_toolkit.PromptSession(
            history=prompt_toolkit.history.FileHistory(self.file_history))
        self.terminal_text = prompt_toolkit.HTML(f'\n┌──(HashCapTerminal)-[<b>{os.getcwd()}</b>] \n└─$ ')
        self.terminal_tmp_text = self.terminal_text
        self.brute = False
        while self.terminal_while:
            self.init_input()

    def init_input(self):
        try:
            self.input_line = self.terminal_session.prompt(self.terminal_text.format(os.getcwd()))
        except KeyboardInterrupt:
            exit_program()
        except EOFError:
            exit_program()
        if self.terminal_cleaning:
            clear()
        if self.input_line.replace(' ', '') != '':
            self.input_line_split = shlex.split(self.input_line.replace('\\', '/'))
            try:
                self.input_validation()
            except PermissionError:
                error(f'Not enough permissions to execute the command: {self.input_line}')
            except UnboundLocalError:
                pass

    def input_validation(self):
        if self.input_line_split[0].lower() == 'brute':
            self.command_brute()
        elif self.input_line_split[0].lower() == 'cd':
            self.command_cd()
        elif self.input_line_split[0].lower() == 'clear' or self.input_line_split[0].lower() == 'clean' or \
                self.input_line_split[0].lower() == 'cls':
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
        elif self.input_line_split[0].lower() == 'help' or self.input_line_split[0].lower() == '?':
            self.command_help()
        elif self.input_line_split[0].lower() == 'history':
            self.command_history()
        elif self.input_line_split[0].lower() == 'ls':
            self.command_ls()
        elif self.input_line_split[0].lower() == 'pwd':
            message(f'You are in directory: {os.getcwd()}')
        elif self.input_line_split[0].lower() == 'read':
            self.command_read()
        elif self.input_line_split[0].lower() == 'sum':
            self.command_sum()
        elif self.input_line_split[0].lower() == 'system' or self.input_line_split[0].lower() == '$':
            self.command_system()
        elif self.input_line_split[0].lower() == 'version':
            message(f'Metros HashCap Terminal (version {__version__}).')
        else:
            error(f'Command not found: {self.input_line}')

    def command_brute(self):
        time_start_brute_force = time.monotonic()
        try:
            self.command_brute_start()
        except IndexError:
            error('There are not enough parameters to execute the command.')
            return
        except KeyboardInterrupt:
            message('Completion of brute force...', start='\n')
            return
        message('Runtime: {}'.format(datetime.timedelta(seconds=time.monotonic() - time_start_brute_force)),
                start='\n')

    def command_brute_start(self):
        brute_dictionary = ''
        line = 0
        try:
            if self.input_line_split[1].lower() == '--all' or self.input_line_split[1].lower() == '-a':
                error('There must be an exact parameter here. The (--all) option is not applicable here.')
                return
        except IndexError:
            pass
        if os.path.isfile(self.input_line_split[3]):
            try:
                brute_dictionary = open(self.input_line_split[3], 'r', encoding='latin-1')
            except Exception as error_open_file:
                error('An error occurred while opening the dictionary file ({}): {}'.format(self.input_line_split[3],
                                                                                            error_open_file))
            message('Hash type\t\t : {}'.format(self.input_line_split[1].replace('--', '').lower()))
            message(f'Hash target\t\t : {self.input_line_split[2]}')
            message(f'Path dictionary\t : {self.input_line_split[3]}')
            message(
                'Start date and time\t : {}\n'.format(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')))
            for i in brute_dictionary:
                line += 1
                i = i.rstrip()
                if self.input_line_split[2] == action_check('brute',
                                                            target_hash=self.input_line_split[1].lower(),
                                                            string=i):
                    message(f'{self.input_line_split[2]}:{i}')
                    message('Result {}: {}'.format(self.input_line_split[1].replace('--', '').lower(), i))
                    self.brute = True
                    break
                else:
                    sys.stdout.write(f'{COLOR_MESSAGE}[i]{COLOR_RESET} Processed combinations: {line}\r')
                    sys.stdout.flush()
            if not self.brute:
                error('Nothing was found.', start='\n\n')
        elif not os.path.isfile(self.input_line_split[3]):
            error(f'Could not find dictionary file: {self.input_line_split[3]}', start='\n')

    def command_cd(self):
        try:
            if os.path.isdir(self.input_line_split[1]):
                os.chdir(self.input_line_split[1])
                if self.terminal_text != '':
                    self.terminal_text = self.terminal_tmp_text.format(os.getcwd())
            else:
                error(f'Could not find directory: {self.input_line_split[1]}')
        except IndexError:
            message(f'You are in directory: {os.getcwd()}')

    def command_clear(self):
        try:
            if self.input_line_split[1].lower() == '--enable' or self.input_line_split[1].lower() == '--on' or \
                    self.input_line_split[1].lower() == '-e':
                self.terminal_cleaning = True
                message('Enabled screen clearing after command input.')
            elif self.input_line_split[1].lower() == '--disable' or self.input_line_split[1].lower() == '--off' or \
                    self.input_line_split[1].lower() == '-d':
                self.terminal_cleaning = False
                message('Disabled screen clearing after command input.')
            else:
                error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            clear()

    def command_dir(self):
        dir_directory = ''
        try:
            if self.input_line_split[1].lower() != 'dir':
                dir_directory = os.path.abspath(self.input_line_split[1])
        except IndexError:
            dir_directory = os.getcwd()
        print(' '.join(os.listdir(dir_directory)))

    def command_echo(self):
        try:
            if self.input_line_split[1].lower() == '--enable' or self.input_line_split[1].lower() == '--on' or \
                    self.input_line_split[1].lower() == '-e':
                self.terminal_text = self.terminal_tmp_text
                message('Enabled command output mode on the screen.')
            elif self.input_line_split[1].lower() == '--disable' or self.input_line_split[1].lower() == '--off' or \
                    self.input_line_split[1].lower() == '-d':
                self.terminal_text = ''
                message('Disabled command output mode on the screen.')
            else:
                del self.input_line_split[0]
                print(' '.join(self.input_line_split))
        except IndexError:
            print()

    def command_file(self):
        try:
            if self.input_line_split[1].lower() == '--create' or self.input_line_split[1].lower() == '-c':
                try:
                    with open(self.input_line_split[2], 'w') as create_file:
                        create_file.write('')
                    if os.path.isfile(self.input_line_split[2]):
                        message(f'The file has been successfully created: {self.input_line_split[2]}')
                    elif not os.path.isfile(self.input_line_split[2]):
                        error(f'Failed to create file: {self.input_line_split[2]}')
                except IndexError:
                    error('You did not enter a file name.')
                except IsADirectoryError:
                    pass
            elif self.input_line_split[1].lower() == '--remove' or self.input_line_split[1].lower() == '-r':
                try:
                    if not os.path.isfile(self.input_line_split[2]):
                        error(f'Could not find file: {self.input_line_split[2]}')
                    elif os.path.isfile(self.input_line_split[2]):
                        os.remove(self.input_line_split[2])
                        if not os.path.isfile(self.input_line_split[2]):
                            warning(f'The file has been successfully deleted: {self.input_line_split[2]}')
                        elif os.path.isfile(self.input_line_split[2]):
                            error(f'Failed to delete file: {self.input_line_split[2]}')
                except IndexError:
                    error('You did not enter a file name.')
            else:
                error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            error('There are not enough parameters to execute the command.')

    def command_folder(self):
        try:
            if self.input_line_split[1].lower() == '--create' or self.input_line_split[1].lower() == '-c':
                try:
                    os.mkdir(self.input_line_split[2])
                    if os.path.isdir(self.input_line_split[2]):
                        message(f'The folder has been successfully created: {self.input_line_split[2]}')
                    elif not os.path.isdir(self.input_line_split[2]):
                        error(f'Failed to create folder: {self.input_line_split[2]}')
                except IndexError:
                    error('You did not enter a folder name.')
                except FileExistsError:
                    pass
            elif self.input_line_split[1].lower() == '--remove' or self.input_line_split[1].lower() == '-r':
                try:
                    if os.path.isdir(self.input_line_split[2]):
                        os.rmdir(self.input_line_split[2])
                        if not os.path.isfile(self.input_line_split[2]):
                            warning(f'The folder has been successfully deleted: {self.input_line_split[2]}')
                        elif os.path.isdir(self.input_line_split[2]):
                            error(f'Failed to delete folder: {self.input_line_split[2]}')
                    elif not os.path.isdir(self.input_line_split[2]):
                        error(f'Could not find folder: {self.input_line_split[2]}')
                except IndexError:
                    error('You did not enter a folder name.')
            else:
                error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            error('There are not enough parameters to execute the command.')

    def command_hash(self):
        try:
            if self.input_line_split[3] == '==':
                if self.input_line_split[1] == '--string' or self.input_line_split[1] == '-s':
                    string_1 = self.input_line_split[2]
                    string_2 = self.input_line_split[4]
                else:
                    string_1 = action_check('hash', self.input_line_split[1].lower(), self.input_line_split[2])
                    string_2 = action_check('hash', self.input_line_split[1].lower(), self.input_line_split[4])
                if string_1 == self.input_line_split[4]:
                    message('Equals.')
                elif self.input_line_split[2] == string_2:
                    message('Equals.')
                else:
                    warning('Does not equal.')
                return
        except IndexError:
            pass
        try:
            if action_check('hash', self.input_line_split[1].lower(), self.input_line_split[2]):
                message(action_check('hash', self.input_line_split[1].lower(), self.input_line_split[2]))
        except IndexError:
            error('There are not enough parameters to execute the command.')
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
                          __all_command__,
                          __history__,
                          __ls__,
                          __pwd__,
                          __read__,
                          __sum__,
                          __system__,
                          __help_version__]:
                    print(i)
                message('Learn more: https://github.com/John-MetrosSoftware/HashCapTerminal', start='\n')
            elif self.input_line_split[1].lower() == '-g' or self.input_line_split[1].lower() == '--github':
                webbrowser.open_new('https://github.com/John-MetrosSoftware/HashCapTerminal')
            elif self.input_line_split[1].lower() == 'brute':
                print(__brute__)
            elif self.input_line_split[1].lower() == 'cd':
                print(__cd__)
            elif self.input_line_split[1].lower() == 'clear' or self.input_line_split[1].lower() == 'clean' or \
                    self.input_line_split[1].lower() == 'cls':
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
                print(__all_command__)
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
                print(__help_version__)
            else:
                del self.input_line_split[0]
                error('Can\'t find help for command: {}'.format(' '.join(self.input_line_split)))
        except IndexError:
            print(__help__)
            message('Use the `help` command to display help for a specific command.', start='\n')

    def command_history(self):
        if not os.path.isfile(self.file_history):
            with open(self.file_history, 'w') as history_file:
                history_file.write('')
        try:
            if self.input_line_split[1].lower() == '--clear' or self.input_line_split[1].lower() == '-c':
                self.command_history_remove_history_file()
            elif self.input_line_split[1].lower() == '--clear-session' or self.input_line_split[1].lower() == '-s':
                self.terminal_session = prompt_toolkit.PromptSession(
                    history=prompt_toolkit.history.FileHistory(self.file_history))
                self.command_history_remove_history_file()
                message('The history has been completely cleared.')
            else:
                error(f'Unknown parameter: {self.input_line_split[1]}')
        except IndexError:
            print(open(self.file_history).read())

    def command_history_remove_history_file(self):
        os.remove(self.file_history)
        if not os.path.isfile(self.file_history):
            message('The history file has been cleared.')
        elif os.path.isfile(self.file_history):
            error('The history file has not been cleared.')

    def command_ls(self):
        ls_directory = ''
        try:
            if self.input_line_split[1].lower() != 'ls':
                ls_directory = os.path.abspath(self.input_line_split[1])
        except IndexError:
            ls_directory = os.getcwd()
        try:
            if self.input_line_split[1].lower() == '--directory' or self.input_line_split[1].lower() == '-d':
                command_ls_folder(os.getcwd())
            elif self.input_line_split[1].lower() == '--file' or self.input_line_split[1].lower() == '-f':
                command_ls_file(os.getcwd())
            elif self.input_line_split[2].lower() == '--directory' or self.input_line_split[2].lower() == '-d':
                command_ls_folder(ls_directory)
            elif self.input_line_split[2].lower() == '--file' or self.input_line_split[2].lower() == '-f':
                command_ls_file(ls_directory)
        except FileNotFoundError:
            error(f'Could not find directory: {ls_directory}')
        except IndexError:
            try:
                command_ls_file(ls_directory)
                command_ls_folder(ls_directory)
            except FileNotFoundError:
                error(f'Could not find directory: {ls_directory}')

    def command_read(self):
        encoding = ''
        try:
            split_encoding = shlex.split(self.input_line_split[2].lower().replace('=', ' '))
            if split_encoding[0] == '--encoding' or split_encoding[0] == '-e':
                encoding = split_encoding[1]
        except IndexError:
            encoding = 'UTF-8'
        try:
            print(open(self.input_line_split[1], encoding=encoding).read())
            message(f'Read file: {self.input_line_split[1]} {encoding}')
        except IndexError:
            error('There are not enough parameters to execute the command.')
            return
        except FileNotFoundError:
            error(f'Could not find the file: {self.input_line_split[1]}')
        except LookupError:
            error(f'Unknown encoding: {encoding}')
        except IsADirectoryError:
            pass

    def command_sum(self):
        try:
            if self.input_line_split[3] == '==':
                try:
                    if os.path.isfile(self.input_line_split[2]):
                        string_1 = action_check('sum', self.input_line_split[1].lower(), self.input_line_split[2])
                        if string_1 == self.input_line_split[4]:
                            message('Equals.')
                        else:
                            warning('Does not equal.')
                    elif not os.path.isfile(self.input_line_split[2]):
                        string_2 = action_check('sum', self.input_line_split[1].lower(), self.input_line_split[4])
                        if self.input_line_split[2] == string_2:
                            message('Equals.')
                        else:
                            warning('Does not equal.')
                except FileNotFoundError:
                    if not os.path.isfile(self.input_line_split[2]) and not os.path.isfile(self.input_line_split[4]):
                        error('Could not find file. ')
                return
        except IndexError:
            pass
        try:
            if os.path.isfile(self.input_line_split[2]):
                function_return_hash = action_check('sum',
                                                    self.input_line_split[1].lower(),
                                                    self.input_line_split[2])
                if function_return_hash:
                    message(function_return_hash)
            elif not os.path.isfile(self.input_line_split[2]):
                error(f'Could not find file: {self.input_line_split[2]}')
        except IndexError:
            error('There are not enough parameters to execute the command.')
            return

    def command_system(self):
        try:
            if self.input_line_split[1]:
                del self.input_line_split[0]
                os.system(' '.join(self.input_line_split))
        except IndexError:
            os.system(prompt_toolkit.prompt('Enter command > '))


def Boot():
    message(f'Metros HashCap Terminal (version {__version__}).')
    Main()
    exit_program()


if __name__ == '__main__':
    try:
        Boot()
    except Exception as unknown_error:
        error(f'Unknown error: {unknown_error}')
    sys.exit()
