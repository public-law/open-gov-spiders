"""
This type stub file was generated by pyright.
"""

import sys

'''
Tika Python module provides Python API client to Aapche Tika Server.

**Example usage**::

    import tika
    from tika import parser
    parsed = parser.from_file('/path/to/file')
    print(parsed["metadata"])
    print(parsed["content"])

Visit https://github.com/chrismattmann/tika-python to learn more about it.

**Detect IANA MIME Type**::

    from tika import detector
    print(detector.from_file('/path/to/file'))

**Detect Language**::

    from tika import language
    print(language.from_file('/path/to/file'))

**Use Tika Translate**::

   from tika import translate
   print(translate.from_file('/path/to/file', 'srcLang', 'destLang')
   # Use auto Language detection feature
   print(translate.from_file('/path/to/file', 'destLang')

***Tika-Python Configuration***
You can now use custom configuration files. See https://tika.apache.org/1.18/configuring.html
for details on writing configuration files. Configuration is set the first time the server is started.
To use a configuration file with a parser, or detector:
    parsed = parser.from_file('/path/to/file', config_path='/path/to/configfile')
or:
    detected = detector.from_file('/path/to/file', config_path='/path/to/configfile')
or:
    detected = detector.from_buffer('some buffered content', config_path='/path/to/configfile')

'''
USAGE = ...
unicode_string = ...
binary_string = ...
def make_content_disposition_header(fn):
    ...

if sys.version_info[0] < 3:
    ...
log_path = ...
log_file = ...
logFormatter = ...
log = ...
fileHandler = ...
consoleHandler = ...
Windows = ...
TikaVersion = ...
TikaJarPath = ...
TikaFilesPath = ...
TikaServerLogFilePath = ...
TikaServerJar = ...
ServerHost = ...
Port = ...
ServerEndpoint = ...
Translator = ...
TikaClientOnly = ...
TikaServerClasspath = ...
TikaStartupSleep = ...
TikaStartupMaxRetry = ...
TikaJava = ...
TikaJavaArgs = ...
Verbose = ...
EncodeUtf8 = ...
csvOutput = ...
TikaServerProcess = ...
class TikaException(Exception):
    ...


def echo2(*s): # -> None:
    ...

def warn(*s): # -> None:
    ...

def die(*s):
    ...

def runCommand(cmd, option, urlOrPaths, port, outDir=..., serverHost=..., tikaServerJar=..., verbose=..., encode=...): # -> list[Unknown] | list[tuple[Unknown, Unknown]]:
    '''
    Run the Tika command by calling the Tika server and return results in JSON format (or plain text).
    :param cmd: a command from set ``{'parse', 'detect', 'language', 'translate', 'config'}``
    :param option:
    :param urlOrPaths:
    :param port:
    :param outDir:
    :param serverHost:
    :param tikaServerJar:
    :param verbose:
    :param encode:
    :return: response for the command, usually a ``dict``
    '''
    ...

def getPaths(urlOrPaths): # -> list[Unknown]:
    '''
    Determines if the given URL in urlOrPaths is a URL or a file or directory. If it's
    a directory, it walks the directory and then finds all file paths in it, and ads them
    too. If it's a file, it adds it to the paths. If it's a URL it just adds it to the path.
    :param urlOrPaths: the url or path to be scanned
    :return: ``list`` of paths
    '''
    ...

def parseAndSave(option, urlOrPaths, outDir=..., serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., metaExtension=..., services=...): # -> list[Unknown]:
    '''
    Parse the objects and write extracted metadata and/or text in JSON format to matching
    filename with an extension of '_meta.json'.
    :param option:
    :param urlOrPaths:
    :param outDir:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param metaExtension:
    :param services:
    :return:
    '''
    ...

def parse(option, urlOrPaths, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=..., rawResponse=...): # -> list[tuple[Unknown, Unknown]]:
    '''
    Parse the objects and return extracted metadata and/or text in JSON format.
    :param option:
    :param urlOrPaths:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def parse1(option, urlOrPath, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=..., rawResponse=..., headers=..., config_path=..., requestOptions=...): # -> tuple[Unknown, Unknown]:
    '''
    Parse the object and return extracted metadata and/or text in JSON format.
    :param option:
    :param urlOrPath:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :param rawResponse:
    :param headers:
    :return:
    '''
    ...

def detectLang(option, urlOrPaths, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=...): # -> list[tuple[Unknown, Unknown]]:
    '''
    Detect the language of the provided stream and return its 2 character code as text/plain.
    :param option:
    :param urlOrPaths:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def detectLang1(option, urlOrPath, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=..., requestOptions=...): # -> tuple[Unknown, Unknown]:
    '''
    Detect the language of the provided stream and return its 2 character code as text/plain.
    :param option:
    :param urlOrPath:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def doTranslate(option, urlOrPaths, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=...): # -> list[tuple[Unknown, Unknown]]:
    '''
    Translate the file from source language to destination language.
    :param option:
    :param urlOrPaths:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def doTranslate1(option, urlOrPath, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=..., requestOptions=...): # -> tuple[Unknown, Unknown]:
    '''

    :param option:
    :param urlOrPath:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def detectType(option, urlOrPaths, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=...): # -> list[tuple[Unknown, Unknown]]:
    '''
    Detect the MIME/media type of the stream and return it in text/plain.
    :param option:
    :param urlOrPaths:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def detectType1(option, urlOrPath, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=..., config_path=..., requestOptions=...): # -> tuple[Unknown, Unknown]:
    '''
    Detect the MIME/media type of the stream and return it in text/plain.
    :param option:
    :param urlOrPath:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def getConfig(option, serverEndpoint=..., verbose=..., tikaServerJar=..., responseMimeType=..., services=..., requestOptions=...): # -> tuple[Unknown, Unknown]:
    '''
    Get the configuration of the Tika Server (parsers, detectors, etc.) and return it in JSON format.
    :param option:
    :param serverEndpoint:
    :param verbose:
    :param tikaServerJar:
    :param responseMimeType:
    :param services:
    :return:
    '''
    ...

def callServer(verb, serverEndpoint, service, data, headers, verbose=..., tikaServerJar=..., httpVerbs=..., classpath=..., rawResponse=..., config_path=..., requestOptions=...): # -> tuple[Unknown, Unknown]:
    '''
    Call the Tika Server, do some error checking, and return the response.
    :param verb:
    :param serverEndpoint:
    :param service:
    :param data:
    :param headers:
    :param verbose:
    :param tikaServerJar:
    :param httpVerbs:
    :param classpath:
    :return:
    '''
    ...

def checkTikaServer(scheme=..., serverHost=..., port=..., tikaServerJar=..., classpath=..., config_path=...): # -> str:
    '''
    Check that tika-server is running.  If not, download JAR file and start it up.
    :param scheme: e.g. http or https
    :param serverHost:
    :param port:
    :param tikaServerJar:
    :param classpath:
    :return:
    '''
    ...

def checkJarSig(tikaServerJar, jarPath): # -> bool:
    '''
    Checks the signature of Jar
    :param tikaServerJar:
    :param jarPath:
    :return: ``True`` if the signature of the jar matches
    '''
    ...

def startServer(tikaServerJar, java_path=..., java_args=..., serverHost=..., port=..., classpath=..., config_path=...): # -> bool:
    '''
    Starts Tika Server
    :param tikaServerJar: path to tika server jar
    :param serverHost: the host interface address to be used for binding the service
    :param port: the host port to be used for binding the service
    :param classpath: Class path value to pass to JVM
    :return: None
    '''
    ...

def killServer(): # -> None:
    '''
    Kills the tika server started by the current execution instance
    '''
    ...

def toFilename(url): # -> str:
    '''
    gets url and returns filename
    '''
    ...

def getRemoteFile(urlOrPath, destPath): # -> tuple[Unknown, Literal['binary']] | tuple[Unknown, Literal['local']] | tuple[Unknown, Literal['remote']]:
    '''
    Fetches URL to local path or just returns absolute path.
    :param urlOrPath: resource locator, generally URL or path
    :param destPath: path to store the resource, usually a path on file system
    :return: tuple having (path, 'local'/'remote'/'binary')
    '''
    ...

def getRemoteJar(urlOrPath, destPath): # -> tuple[Unknown, Literal['local']] | tuple[Unknown, Literal['remote']]:
    '''
    Fetches URL to local path or just return absolute path.
    :param urlOrPath: remote resource locator
    :param destPath: Path to store the resource, usually a path on file system
    :return: tuple having (path, 'local'/'remote')
    '''
    ...

def checkPortIsOpen(remoteServerHost=..., port=...): # -> bool:
    '''
    Checks if the specified port is open
    :param remoteServerHost: the host address
    :param port: port which needs to be checked
    :return: ``True`` if port is open, ``False`` otherwise
    '''
    ...

def main(argv=...): # -> list[Unknown] | list[tuple[Unknown, Unknown]]:
    """Run Tika from command line according to USAGE."""
    ...

if __name__ == '__main__':
    resp = ...
