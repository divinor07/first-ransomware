import os


def discover(initial_path):

    extensions = [
        # 'exe', 'jpeg', 'so', 'deb', 'vmlinuz', 'img' # Arquivos do Sistema
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # Imagens
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape', # Audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Videos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', # Microsoft Office
        # OpenOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
        'yml', 'yaml', 'json', 'xml', 'csv', # Dados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso', # Bancos de dados e imagens de discos

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css' # Tecnologias WEB
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # Código fonte C e C++
        'java', 'class', 'jar' # Códigos fonte Java
        'ps', 'bat', 'vb', # Scripts de sistemas windows
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # Scripts de sistemas UNIX
        'go', 'py', 'pyc', 'bf', 'coffee', # Outros tipos de códigos fonte
    ]
    
