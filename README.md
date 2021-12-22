# Projeto Hospital

- Paciente
	- cpf
	- nome
	- idade
	- bairro
	- comorbidade (diabetes, alergia, etc)

- Medico
	- CRM
	- nome
	- especialidade

- Enfermeiro
	- id
	- nome
	- ala (UTI, pronto-socorro, etc)

- Medicamento
	- id
	- nome
	- tipo (analgesico, anti-inflama, etc)

- Tecnico
	- id
	- nome
	- setor

- Exame
	- id
	- id_paciente
	- tipo (sangue, fezes, tumografia, etc)

- Recepcionista
	- id
	- nome

- Triagem
	- id
	- id_paciente
	- temp
	- pressao

- Consultas
	- id
	- id_paciente
	- id_medico
	- diagnostico
