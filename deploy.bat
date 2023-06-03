REM Apagar todos os arquivos e subdiretorios do diretorio
rmdir /s /q "Y:\PYTHON\CIE_MAT\"

REM Recriar o diretorio apos a exclusão
mkdir "Y:\PYTHON\CIE_MAT\"

echo Todos os arquivos foram apagados de Y:\PYTHON\CIE_MAT\

REM Copiar todos os arquivos .py do diretorio atual e subdiretorios, mantendo a estrutura de diretorios
xcopy /y /q /s /i *.py "Y:\PYTHON\CIE_MAT\"

del Y:\PYTHON\CIE_MAT\boot.py

echo Todos os arquivos .py foram copiados para Y:\PYTHON\CIE_MAT\

