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
--> Ao ser executado, o cliente deverá informar ao servidor que ele está on-line, informando o nome do HOST do cliente, seu IP e usuário logado (obter o usuário do computador):

#### ON-LINE – Registro do Agente no Servidor
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
--> Deverá ser implementado um comando na aplicação servidora para solicitar aos agentes informações do hardware onde estão sendo executados (CPU, memória, disco, Sistema Operacional, ...).

#### INFO-HARDWARE – Obter Informações do Hardware e Sistema Operacional
##### Requisição (Servidor - Cliente)
'INFO-HARDWARE\n'
##### Resposta (Cliente - Servidor)
200 OK <CPU> <MEMÓRIA_TOTAL> <MEMÓRIA_LIVRE> <DISCO_TOTAL> <DISCO_LIVRE> <SISTEMA_OPERACIONAL>\n
###### Se houver erro na obtenção dos dados:
500 INTERNAL_ERROR\n

--> Deverá ser implementado um comando na aplicação servidora para solicitar aos agentes a lista de programas instalados no computador.

#### LISTA-PROGRAMAS – Listar Programas Instalados
##### Requisição (Servidor - Cliente)
LISTA-PROGRAMAS\n
##### Resposta (Cliente - Servidor)
200 OK <APP1> <APP2> <APP3> ...\n
###### Se não houver aplicativos instalados:
204 NO_CONTENT\n
###### Se houver erro na obtenção dos dados:
500 INTERNAL_ERROR\n

--> Deverá ser implementado um comando na aplicação servidora para solicitar aos agentes o histórico de navegação.

#### HISTORICO – Obter Histórico de Navegação
##### Requisição (Servidor - Cliente)
HISTORICO\n
##### Resposta (Cliente - Servidor)
200 OK <URL1> <DATA1> <URL2> <DATA2> ...\n
###### Se não houver histórico disponível:
204 NO_CONTENT\n
###### Se houver erro na obtenção dos dados:
500 INTERNAL_ERROR\n

--> Deverá ser implementado um comando na aplicação servidora para solicitar aos agentes informações detalhadas do usuário que está logado (podem incluir dados como o diretório inicial (home directory), identificador de usuário (UID), grupo principal, grupo(s) secundário(s), shell padrão, entre outros).

#### INFO-USUARIO – Obter Informações do Usuário Logado
##### Requisição (Servidor - Cliente)
INFO-USUARIO\n
##### Resposta (Cliente - Servidor)
200 OK <USUÁRIO> <UID> <GRUPO> <GRUPOS_SECUNDÁRIOS> <HOME> <SHELL>\n
######Se houver erro na obtenção dos dados:
500 INTERNAL_ERROR\n

--> Deverá ser implementado um comando na aplicação servidora que liste os agentes que estão on-line trazendo informações como: IP, nome do HOST, usuário logado e o tempo que está que o agente está on-line.

#### LISTA-AGENTES – Listar Agentes Conectados
##### Requisição (Servidor - Cliente)
LISTA-AGENTES\n
##### Resposta (Cliente - Servidor)
###### Se houver agentes conectados:
200 OK <NOMEHOST1> <IPV4_1> <USUÁRIO1> <TEMPO1> <NOMEHOST2> <IPV4_2> <USUÁRIO2> <TEMPO2> ...\n
###### Se não houver agentes online:
204 NO_CONTENT\n

--> Servidor encerra conexão
#### Requisição
QUIT\n
#### Resposta
200 OK BYE\n

### Tratamento de Erros
| Código | Significado | Ação do Cliente |
|--------|-------------|-----------------|
|200 OK	 |Operação bem-sucedida|Prosseguir com a resposta|
|204 NO_CONTENT|Nenhum dado disponível|Exibir "Nenhum dado encontrado."|
|400 BAD_REQUEST|Requisição malformada|Exibir "Erro: Comando inválido."|
|404 NOT_FOUND|Dados não encontrados|Exibir "Erro: Informação não encontrada."|
|409 ALREADY_LOGGED_IN|Agente já registrado|Exibir "Erro: O agente já está conectado."|
|500 INTERNAL_ERROR|Erro interno no cliente ou servidor|Exibir "Erro: Falha ao processar a solicitação."|

## Licença
Este projeto está licenciado sob a MIT License.

## Contribuições
Sinta-se à vontade para abrir Issues e enviar Pull Requests!

## Contato
* Email: ahls.n3t@gmail.com
* GitHub: @ahlsouza







