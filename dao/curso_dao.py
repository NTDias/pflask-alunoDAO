from dao.db_config import get_connection 


class CursoDAO: 

    sqlSelect = 'SELECT c.id, c.nome_curso, p.disciplina, p.nome FROM turma t JOIN curso c ON t.curso_id = c.id JOIN professor p ON t.professor_id = p.id'


    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista