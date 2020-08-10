import config
import pyodbc
from sqlserverconexoes.configurar import DATABASE_CONFIG
# Return the sql connection
def getConnection():
#initialize the connection to the database
  connection = pyodbc.connect(
    #'DRIVER={SQL Server};SERVER=OPUSQUALE-WIN\DATA;DATABASE=Opusquale;UID=sa;PWD=Opus@2018', check_same_thread=False)
   'DRIVER={'+config.DATABASE_CONFIG["Driver"]+'} ;'
   'SERVER='+DATABASE_CONFIG["Server"]+';'
   'DATABASE='+DATABASE_CONFIG["Database"]+';'
   'UID='+DATABASE_CONFIG["UID"]+';'
   'PWD='+DATABASE_CONFIG["Password"]+';', check_same_thread=False)

  cursor = connection.cursor()
  return cursor
  #pass
  #cursor.close()



class bancodedados():
    connection = pyodbc.connect(
    #'DRIVER={SQL Server};SERVER=OPUSQUALE-WIN\DATA;DATABASE=Opusquale;UID=sa;PWD=Opus@2018', check_same_thread=False)
   'DRIVER={'+config.DATABASE_CONFIG["Driver"]+'} ;'
   'SERVER='+DATABASE_CONFIG["Server"]+';'
   'DATABASE='+DATABASE_CONFIG["Database"]+';'
   'UID='+DATABASE_CONFIG["UID"]+';'
   'PWD='+DATABASE_CONFIG["Password"]+';', check_same_thread=False)

    #cursor = connection.cursor()
    #try:
        # create_table_request_list = [
    #    cursor.execute('CREATE TABLE jogos(jogoid text UNIQUE NOT NULL DEFAULT 0 ,nome TEXT NOT NULL,url TEXT,emailnintendo TEXT NOT NULL,emailsenha TEXT NOT NULL,idacesso TEXT NOT NULL,idsenha TEXT NOT NULL )')
    #    cursor.execute('CREATE TABLE alugados(idcliente text,nomecliente text, idjogo int,nomejogo text,dataaluguel text Not Null, datadevolucao text NOT NULL )')
    #    cursor.execute('CREATE TABLE clientes(id text UNIQUE NOT NULL DEFAULT 0 ,email text UNIQUE NOT NULL,nome TEXT NOT NULL,telefone TEXT NOT NULL  )')

    #except:
    #    pass
    #connection.close()

def inserir(tabela,row):
        connection = bancodedados.connection
        #sqlite3.connect('t3.sqlite', check_same_thread=False)
        cursor = connection.cursor()
        """Retrieve an entity's unique ID from the database, given its associated text.
        If the row is not already present, it is inserted.
        The entity can either be a sentence or a word."""

        values = '?'
        for i in range(len(row) -1):
            values = values + ',?'
            pass
        cursor.execute("INSERT INTO " + tabela + " VALUES (" +values + ")" ,row)
        connection.commit()
        connection.close()

def selecionar(tabela,valor,coluna):
    linhas=[]
    connection = bancodedados.connection
    cursor2 = connection.cursor()
    if valor ==-1:
        cursor2.execute("SELECT  * FROM " + tabela )
        row = cursor2.fetchone()
        linhas.append(row)
        while row:
            row = cursor2.fetchone()
            #print(row)
            linhas.append(row)
            pass
    else:
        try:
            texto = 'select* from ' + tabela + ' where ' + coluna + ' like"' + valor + '%"'
            cursor2.execute(texto)
            row = cursor2.fetchone()

        except:
            try:
                cursor2.execute("SELECT  * FROM " + tabela + " where " + coluna + " = {}".format(int(valor)))
                row = cursor2.fetchone()
            except:
                row=None
            pass
        pass
        linhas.append(row)
    pass
    connection.close()
    return linhas
pass



def selecionarmultiplo(tabela,valor,coluna):
   # print(valor)
    linhas=[]
    connection = bancodedados.connection
    cursor2 = connection.cursor()
    try:
        texto = 'select * from ' + tabela + ' where strftime("%s",' + coluna + ') between strftime("%s","' + valor[
        0] + '") and strftime("%s","' + valor[1] + '")'
        #print(texto)
        cursor2.execute(texto)
        row = cursor2.fetchone()
    except:
        try:
            cursor2.execute("SELECT  * FROM " + tabela + " where " + coluna + " between {} and {}".format(int(valor[0]),int(valor[1])))
            row = cursor2.fetchone()
        except:
            row = None
        pass
    pass
    while row:
        # print(row)
        linhas.append(row)
        row = cursor2.fetchone()
        pass
    return linhas
    pass

def atualizar(tabela,setcampo,setvalor,wherecampo,wherevalor):
    connection = bancodedados.connection
    cursor2 = connection.cursor()
    #print("update " + tabela + " set " + coluna[0] + "='" + valor[0] + "' where "+coluna[1]+"='"+valor[1]+"'")
    cursor2.execute("update " + tabela + " set " + setcampo + "='" + setvalor + "' where "+wherecampo+"='"+wherevalor+"'")
    connection.commit()
    connection.close()

def excluir(tabela,row,coluna):
    connection = bancodedados.connection
    cursor2 = connection.cursor()
    #print("DELETE FROM "+ tabela+ " where "+coluna+" = "+row)
    cursor2.execute ("DELETE FROM "+ tabela+ " where "+coluna+" = '"+row+"'")
    connection.commit()
    connection.close()
