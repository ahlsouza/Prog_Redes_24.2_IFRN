# Monitoramento Remoto de Agentes
Este projeto implementa um sistema de monitoramento remoto onde um servidor central gerencia agentes (clientes) conectados à rede. O servidor pode solicitar informações sobre o hardware, software e atividade do usuário dos dispositivos conectados.

## Funcionalidades
* Registro automático dos agentes no servidor
* Listagem de agentes online com detalhes como IP, hostname e tempo de conexão
* Coleta de informações do sistema (CPU, memória, disco, SO)
* Listagem de programas instalados
* Histórico de navegação do usuário
* Informações detalhadas do usuário logado

### Arquitetura do Projeto
O sistema segue um modelo Cliente-Servidor com comunicação via TCP.

#### Servidor:
* Gerencia os agentes conectados
* Envia comandos para coletar informações
* Mantém um histórico dos agentes ativos

#### Cliente (Agente):
* Envia automaticamente informações ao conectar-se
* Responde às solicitações do servidor
* Retorna dados do sistema operacional, programas instalados e usuário

### Características de operação
* A conexão entre o cliente e o servidor será através de um socket (UDP ou TCP);
* A aplicação cliente (agente) deverá executar as seguintes operações:
i. O cliente deverá ser executado em segundo plano, ou seja, ao ser executado no terminal ele é carregado na memória e libera o terminal para o usuário;
ii. Caso o servidor não esteja on-line, o cliente deverá ficar rodando em segundo plano testando a cada tempo pré-determinado se o servidor voltou a ficar on-line;
iii. Uma vez que o agente esteja na memória, ele não deve permitir que uma segunda instância dele seja carregado na memória;
iv. Deverá haver uma forma para o próprio agente se remover da memória;
v. Enquanto estiver na memória o agente deverá responder a requisições oriundas do servidor.

* A aplicação servidora deverá executar as seguintes operações:
i. O servidor deverá permitir conexão oriunda de vários clientes (agentes) simultaneamente;
ii. Deverá haver um mecanismo no servidor para ele gerenciar as conexões ativas e detectar quando um cliente ficar off-line;
iii. O servidor deverá ser executado em segundo plano, ou seja, ao ser executado no terminal ele é carregado na memória e libera o terminal para o usuário;
iv. Uma vez que o servidor esteja na memória, ele não deve permitir que uma segunda instância dele seja carregado na memória;
v. Deverá haver uma forma para o próprio servidor se remover da memória;

## Protocolo
### A aplicação cliente (agente)        
Ao ser executado, o cliente deverá informar ao servidor que ele está on-line, informando o nome do HOST do cliente, seu IP e usuário logado (obter o usuário do computador):

#### LOGIN – Registro do Agente no Servidor
##### Requisição (Cliente - Servidor)
'ON-LINE <NOMEHOST> <IPV4> <USUÁRIO>\n'
##### Resposta (Servidor → Cliente)
###### Se o agente for registrado com sucesso:
'200 OK\n'
###### Se houver erro no formato da mensagem:
'400 BAD_REQUEST\n'
###### Se o agente já estiver registrado:
'409 ALREADY_LOGGED_IN\n'

### A aplicação servidora
Deverá ser implementado um comando na aplicação servidora para solicitar aos agentes informações do hardware onde estão sendo executados (CPU, memória, disco, Sistema Operacional, ...).

#### LISTAGENTS – Listar Agentes Conectados
##### Requisição (Servidor - Cliente)
'LISTAGENTS\n'
##### Resposta (Cliente - Servidor)
###### Se houver agentes conectados:
'200 OK <MAQUINA1> <IPV4_1> <USUÁRIO1> <TEMPO1> <MAQUINA2> <IPV4_2> <USUÁRIO2> <TEMPO2> ...\n'
###### Se não houver agentes online:
'204 NO_CONTENT\n'








