from flask import Flask, request
from flask_cors import CORS, cross_origin
import csv
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

##### PACIENTES #####
# Listar
@app.route('/pacientes', methods=['GET'])
def pacientes():
    pacientes = listar_csv('db\pacientes.csv')
    return json.dumps(pacientes)

# Adicionar
@app.route('/paciente/add', methods=['POST'])
def paciente_add():
    paciente = request.json             # teste
    #paciente = json.loads(request.data)   # codigo danilo
    nova_linha = [paciente['cpf'], paciente['nome'], paciente['idade'], paciente['bairro'], paciente['comorbidade']]
    with open('db\pacientes.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
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
# Listar
@app.route('/medicos', methods=['GET'])
def medicos():
    medicos = listar_csv('db\medicos.csv')
    return json.dumps(medicos)

# Adicionar
@app.route('/medico/add', methods=['POST'])
def medico_add():
    medico = request.json             # teste
    #medico = json.loads(request.data)   # codigo danilo
    nova_linha = [medico['crm'], medico['nome'], medico['especialidade']]
    with open('db\medicos.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/medico/del/<id>', methods=['DELETE'])
def medico_del(id):
    with open('db\medicos.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db\medicos.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            crm, nome, especialidade = item

            if(crm != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### ENFERMEIROS #####
# Listar
@app.route('/enfermeiros', methods=['GET'])
def enfermeiros():
    enfermeiros = listar_csv('db\enfermeiros.csv')
    return json.dumps(enfermeiros)

# Adicionar
@app.route('/enfermeiro/add', methods=['POST'])
def enfermeiro_add():
    enfermeiro = request.json             # teste
    #enfermeiro = json.loads(request.data)   # codigo danilo
    nova_linha = [enfermeiro['id'], enfermeiro['nome'], enfermeiro['ala']]
    with open('db\enfermeiros.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/enfermeiro/del/<id>', methods=['DELETE'])
def enfermeiro_del(id):
    with open('db\enfermeiros.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db\enfermeiros.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            enf_id, nome, ala = item

            if(enf_id != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### MEDICAMENTOS #####
# Listar
@app.route('/medicamentos', methods=['GET'])
def medicamentos():
    medicamentos = listar_csv('db\medicamentos.csv')
    return json.dumps(medicamentos)

# Adicionar
@app.route('/medicamento/add', methods=['POST'])
def medicamento_add():
    medicamento = request.json             # teste
    #medicamento = json.loads(request.data)   # codigo danilo
    nova_linha = [medicamento['id'], medicamento['nome'], medicamento['tipo']]
    with open('db\medicamentos.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/medicamento/del/<id>', methods=['DELETE'])
def medicamento_del(id):
    with open('db\medicamentos.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db\medicamentos.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            med_id, nome, tipo = item

            if(med_id != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### TECNICOS #####
# Listar
@app.route('/tecnicos', methods=['GET'])
def tecnicos():
    tecnicos = listar_csv('db/tecnicos.csv')
    return json.dumps(tecnicos)

# Adicionar
@app.route('/tecnico/add', methods=['POST'])
def tecnico_add():
    tecnico = request.json             # teste
    #tecnico = json.loads(request.data)   # codigo danilo
    nova_linha = [tecnico['id'], tecnico['nome'], tecnico['setor']]
    with open('db/tecnicos.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/tecnico/del/<id>', methods=['DELETE'])
def tecnico_del(id):
    with open('db/tecnicos.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db/tecnicos.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            tec_id, nome, setor = item

            if(tec_id != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### EXAMES #####
# Listar
@app.route('/exames', methods=['GET'])
def exames():
    exames = listar_csv('db/exames.csv')
    return json.dumps(exames)

# Adicionar
@app.route('/exame/add', methods=['POST'])
def exame_add():
    exame = request.json             # teste
    #exame = json.loads(request.data)   # codigo danilo
    nova_linha = [exame['id'], exame['id_paciente'], exame['tipo']]
    with open('db/exames.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/exame/del/<id>', methods=['DELETE'])
def exame_del(id):
    with open('db/exames.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db/exames.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            exame_id, paciente_id, setor = item

            if(exame_id != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### RECEPCIONISTAS #####
# Listar
@app.route('/recepcionistas', methods=['GET'])
def recepcionistas():
    recepcionistas = listar_csv('db/recepcionistas.csv')
    return json.dumps(recepcionistas)

# Adicionar
@app.route('/recepcionista/add', methods=['POST'])
def recepcionista_add():
    recepcionista = request.json             # teste
    #recepcionista = json.loads(request.data)   # codigo danilo
    nova_linha = [recepcionista['id'], recepcionista['nome'], recepcionista['email']]
    with open('db/recepcionistas.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/recepcionista/del/<id>', methods=['DELETE'])
def recepcionista_del(id):
    with open('db/recepcionistas.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db/recepcionistas.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            rec_id, nome, email = item

            if(rec_id != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### TRIAGEM #####
# Listar
@app.route('/triagem', methods=['GET'])
def triagem():
    triagem = listar_csv('db/triagem.csv')
    return json.dumps(triagem)

# Adicionar
@app.route('/triagem/add', methods=['POST'])
def triagem_add():
    triagem = request.json             # teste
    #triagem = json.loads(request.data)   # codigo danilo
    nova_linha = [triagem['id'], triagem['id_paciente'], triagem['temperatura'], triagem['pressao']]
    with open('db/triagem.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/triagem/del/<id>', methods=['DELETE'])
def triagem_del(id):
    with open('db/triagem.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db/triagem.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            tri_id, id_paciente, temp, pressao = item

            if(tri_id != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### CONSULTAS #####
# Listar
@app.route('/consultas', methods=['GET'])
def consultas():
    consultas = listar_csv('db/consultas.csv')
    return json.dumps(consultas)

# Adicionar
@app.route('/consulta/add', methods=['POST'])
def consulta_add():
    consulta = request.json             # teste
    #consulta = json.loads(request.data)   # codigo danilo
    nova_linha = [consulta['id'], consulta['id_paciente'], consulta['id_medico'], consulta['diagnostico'], consulta['retorno']]
    with open('db/consultas.csv', 'a', encoding='utf-8', newline='') as dados:
        writer = csv.writer(dados, delimiter=';')
        writer.writerow(nova_linha)

    return {'message': 'OK'}

# Deletar
@app.route('/consulta/del/<id>', methods=['DELETE'])
def consulta_del(id):
    with open('db/consultas.csv', 'r', encoding='utf-8') as planilha:
        reader = csv.reader(planilha, delimiter=';')
        dados = list(reader)
    
    with open('db/consultas.csv', 'w', encoding='utf-8', newline='') as planilha:
        writer = csv.writer(planilha, delimiter=';')

        for item in dados:
            cons_id, id_paciente, id_medico, diag, retorno = item

            if(cons_id != id):
                writer.writerow(item)
    
    return {'message': 'OK'}


##### FUNCOES #####
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
                    'nome': linha[1],
                    'email': linha[2]
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
                    'diagnostico': linha[3],
                    'retorno': linha[4]
                }
                lst.append(consulta)
    return lst