from sqlserverconexoes.db_connection import inserir, selecionar, excluir, atualizar

#lista de valores a serem inseridos na tabela
# tabela ´´e a tabela a ser inseridos os dados

lista=['nome','numerotelefone','numerocep']
tabela = 'nometabela'
inserir(tabela, lista)

#linha é o valor a ser procurado e cmpo é a coluna em que o valor deve estar
#se a linha estiver como -1, entao um selct * será chamado
campo = 'id'
linha ='1'
selecionar(tabela, linha, str(campo))

#linha é o valor a ser procurado e cmpo é a coluna em que o valor deve estar
#se a linha estiver como -1, entao um selct * será chamado

campo = 'id'
linha ='1'
excluir(tabela,lista,campo)

#setcampo o campo a ser alterado
#setvalor o valor a ser alterado
#wherecampo o campo de referencia
#wherevalor o valor de referencia do wherecampo
setcampo = 'telefone'
setvalor = '33230123'
wherecampo = 'id'
wherevalor = '2'
atualizar(tabela,setcampo,setvalor,wherecampo,wherevalor)



