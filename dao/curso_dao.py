from dao.db_config import get_connection 


class CursoDAO: 

    sqlSelect = 'SELECT c.id, c.nome_curso, p.disciplina, p.nome FROM curso c LEFT JOIN turma t ON t.curso_id = c.id LEFT JOIN professor p ON t.professor_id = p.id order by id desc'


    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista
    
     
    def salvar(self, id, nome_curso):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute('UPDATE curso SET nome_curso = %s WHERE id = %s', (nome_curso, id))
            else:
                cursor.execute('INSERT INTO curso (nome_curso) VALUES (%s)', (nome_curso,))
            
            conn.commit() 
            return {"status": "ok"}
        except Exception as e:
            conn.rollback() 
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()