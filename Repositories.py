from conexao import Conexao
class Repositories():


    def list_imovel(self):
        cx = Conexao()

        sql = """ SELECT * FROM imovel"""

        resul = cx.select(sql)

        return resul

    def list_imobiliaria(self):
        cx = Conexao()

        sql = """ SELECT * FROM imobiliaria"""

        resul = cx.select(sql)

        return resul

    def register_imobiliaria_rep(self, param):
        cx = Conexao()

        sql = f"""insert into imobiliaria (nome, endereco) 
                  values ('{param["NOME"]}', '{param["ENDERECO"]}') """

        cx.executa(sql, param)

        return 'Imobiliaria cadastrada com sucesso.'

    def register_imovel_rep(self, param):
        cx = Conexao()

        sql = f"""insert into imovel (nome, endereco,descricao,status, caracteristicas, tipo,
                              finalidade,imobiliaria)
                  values (  '{param["NOME"]}', '{param["ENDERECO"]}', 
                            '{param["DESCRICAO"]}', '{param["STATUS"]}', '{param["CARACTERISTICA"]}', 
                            '{param["TIPO"]}', '{param["FINALIDADE"]}', '{param["IMOBILIARIA"]}') """

        cx.executa(sql, param)

        return 'Imobiliaria cadastrada com sucesso.'

    def edit_imobiliaria_rep(self, param):
        cx = Conexao()

        sql = f"""UPDATE IMOBILIARIA SET 
                  NOME = '{param["NOME"]}',
                  ENDERECO = '{param["ENDERECO"]}'
                   WHERE NOME = '{param["IMOBILIARIA_ALTERAR"]}'"""

        cx.executa(sql, param)

        return 'Imobiliaria alterada com sucesso.'

    def edit_imovel_rep(self, param):
        cx = Conexao()

        sql = f"""UPDATE IMOVEL SET 
                  NOME = '{param["NOME"]}', 
                  ENDERECO = '{param["ENDERECO"]}',
                  DESCRICAO = '{param["DESCRICAO"]}',
                  STATUS = '{param["STATUS"]}',
                  TIPO = '{param["TIPO"]}',
                  FINALIDADE = '{param["FINALIDADE"]}',
                  IMOBILIARIA = '{param["IMOBILIARIA"]}',
                  CARACTERISTICAS = '{param["CARACTERISTICAS"]}'
                  WHERE NOME = '{param["IMOVEL_ALTERAR"]}'
                  """

        cx.executa(sql, param)

        return 'Imobiliaria alterada com sucesso.'

    def delete_imobiliaria_rep(self, param):
        cx = Conexao()

        sql = f"""DELETE FROM IMOBILIARIA WHERE NOME = '{param["IMOBILIARIA_DELETAR"]}' """

        cx.executa(sql, param)

        return 'Imobiliaria deletada com sucesso.'

    def delete_imovel_rep(self, param):
        cx = Conexao()

        sql = f"""DELETE FROM IMOVEL WHERE NOME = '{param["IMOVEL_DELETAR"]}' """

        cx.executa(sql, param)

        return 'Imovel deletada com sucesso.'
