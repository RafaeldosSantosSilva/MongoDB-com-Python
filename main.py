from pymongo import MongoClient

#mongodb+srv://<db_username>:<db_password>@cluster0.kx5fg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
conection_string = "mongodb+srv://RafaelSilva:159357@cluster0.kx5fg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(conection_string)

db = client['escola']
collection = db['alunos']


def inserir(nome:str, idade:int, curso: str,nota:float):
    aluno = {
        "nome": nome,
        "idade":idade,
        "curso":curso,
        "nota":nota
    }

    resultado = collection.insert_one(aluno)
    print (f"Aluno cadastrado: {resultado.inserted_id}")


def listar():
    resultados = collection.find()
    for aluno in resultados:
        print(aluno)
        print()


def buscar_curso(curso: str):
    filtro = {
        "$or":[
            {"curso": curso}, {"curso": curso.capitalize()}
        ]
    }

    resultado = collection.find(filtro)
    for alunos in resultado:
        print(alunos)
        print()



def editar(nome: str, idade: int, curso: str, nota:float):
    filtro = {"nome":"Julia"}
    novo_valor = {
        "$set":{
            "nome":nome,
            "idade":idade,
            "curso":curso,
            "nota":nota
        }
    }
    resultado = collection.update_one(filtro, novo_valor)
    



def deletar(nome:str):
    filtro= {
        "nome":nome
    }
    collection.delete_one(filtro)
    print("Deletado com sucesso")


#deletar("Lais")

#editar("Samyra",25,"Python",8)
#buscar_curso("python")
#listar()
#inserir("Carlos",25,"Python",9)
