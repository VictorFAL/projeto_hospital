from flask import Flask, request
import csv
import json

app = Flask(__name__)

##### PACIENTES #####
@app.route('/paciente', methods=['GET'])
def pacientes():
    pacientes = listar_csv('db\pacientes.csv')
    return json.dumps(pacientes)

@app.route('/paciente/add', methods=['POST'])
def paciente_add():
    paciente = request.json             # teste
    #paciente = json.loads(request.data)   # codigo do danilo
    nova_linha = [paciente['cpf'], paciente['nome'], paciente['idade'], paciente['bairro'], paciente['comorbidade']]
    with open('db\pacientes.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

@app.route('/paciente/del/<id>', methods=['DELETE'])
def paciente_del(id):
    with open('db\pacientes.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db\pacientes.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            cpf, nome, idade, bairro, comorbidade = item

            if(cpf != id):
                writer.writerow(item)
    
    return {'message': 'OK'}

##### MEDICOS #####

##### ENFERMEIROS #####

##### MEDICAMENTOS #####

##### TECNICOS #####

##### EXAMES #####

##### RECEPCIONISTAS #####

##### TRIAGEM #####

##### CONSULTAS #####



##### LISTAR #####
def listar_csv(arquivo):
    lst = []

    with open(arquivo, 'r', encoding='utf-8') as dados:
        next(dados)     # pula a primeira linha (cabecalho)
        tabela = csv.reader(dados, delimiter=';')

        if('pacientes' in arquivo):
            for linha in tabela:
                paciente = {
                    'cpf': linha[0],
                    'nome': linha[1],
                    'idade': linha[2],
                    'bairro': linha[3],
                    'comorbidade': linha[4]
                }
                lst.append(paciente)
        elif('medicos' in arquivo):
            for linha in tabela:
                medico = {
                    'crm': linha[0],
                    'nome': linha[1],
                    'especialidade': linha[2]
                }
                lst.append(medico)
        elif('enfermeiros' in arquivo):
            for linha in tabela:
                enfermeiro = {
                    'id': linha[0],
                    'nome': linha[1],
                    'ala': linha[2]
                }
                lst.append(enfermeiro)
        elif('medicamentos' in arquivo):
            for linha in tabela:
                medicamento = {
                    'id': linha[0],
                    'nome': linha[1],
                    'tipo': linha[2]
                }
                lst.append(medicamento)
        elif('tecnicos' in arquivo):
            for linha in tabela:
                tecnico = {
                    'id': linha[0],
                    'nome': linha[1],
                    'setor': linha[2]
                }
                lst.append(tecnico)
        elif('exames' in arquivo):
            for linha in tabela:
                exame = {
                    'id': linha[0],
                    'id_paciente': linha[1],
                    'tipo': linha[2]
                }
                lst.append(exame)
        elif('recepcionistas' in arquivo):
            for linha in tabela:
                recepcionista = {
                    'id': linha[0],
                    'nome': linha[1]
                }
                lst.append(recepcionista)
        elif('triagem' in arquivo):
            for linha in tabela:
                triagem = {
                    'id': linha[0],
                    'id_paciente': linha[1],
                    'temperatura': linha[2],
                    'pressao': linha[3]
                }
                lst.append(triagem)
        elif('consultas' in arquivo):
            for linha in tabela:
                consulta = {
                    'id': linha[0],
                    'id_paciente': linha[1],
                    'id_medico': linha[2],
                    'diagnostico': linha[3]
                }
                lst.append(consulta)
    return lst