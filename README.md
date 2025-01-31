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
