import PyPDF2
import re
#abrir o pdf
pdf_file = open('nota.pdf','rb')
dados = PyPDF2.PdfReader(pdf_file)
#usar a primeira pagina
pagina1 = dados.pages[0]
#extrair o texto para dentro da variavel
dados_da_pagina1 = pagina1.extract_text()

#usando o REGEX, seleciono o começo CPF e pego a variavel seguinte
padrao = re.compile(r"CPF\n(.+[0-9.])")
resultado = re.findall(padrao, dados_da_pagina1)
print(resultado)

