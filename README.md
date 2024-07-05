Adapter Pattern for User Types

Este repositório apresenta uma implementação do padrão Adapter em Python, aplicado ao cenário de diferentes tipos de usuários em um sistema.

LINK PARA SLIDES COM EXPLICAÇÃO TEÓRICA E OUTROS EXEMPLOS DE CÓDIGOS: https://www.canva.com/design/DAGFWM6FTDQ/weGYtgWpExRL-lImj2tp7Q/edit?utm_content=DAGFWM6FTDQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Funcionalidades:

- Interface IUser: Define o comportamento esperado de todos os tipos de usuários.
  - `login(username: str, password: str) -> None`: Método para realizar o login do usuário.
  - `get_permissions() -> list`: Método para obter as permissões do usuário.

- Classe Administrator: Implementação concreta para o tipo de usuário Administrador.
  - `login(username: str, password: str) -> None`: Lógica de login para administrador.
  - `get_permissions() -> list`: Retorna as permissões específicas para administrador.

- Classe Volunteer: Implementação concreta para o tipo de usuário Voluntário.
  - `login(username: str, password: str) -> None`: Lógica de login para voluntário.
  - `get_permissions() -> list`: Retorna as permissões específicas para voluntário.

- Classe Beneficiary: Implementação concreta para o tipo de usuário Beneficiário.
  - `login(username: str, password: str) -> None`: Lógica de login para beneficiário.
  - `get_permissions() -> list`: Retorna as permissões específicas para beneficiário.

- Classe BeneficiaryAdapter: Adaptador para o usuário Beneficiário que remove permissões de cadastro.
  - `__init__(beneficiary: Beneficiary)`: Inicializa o adaptador com um beneficiário existente.
  - `login(username: str, password: str) -> None`: Encaminha o login para o beneficiário adaptado.
  - `get_permissions() -> list`: Modifica as permissões retornadas pelo beneficiário adaptado, removendo as permissões de cadastro.

- Função user_login: Realiza o login de um usuário e obtém suas permissões.
  - `user_login(user: IUser, username: str, password: str) -> None`: Função para efetuar o login e imprimir as permissões do usuário.

Como usar:

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
   
2. Navegue até o diretório do projeto:
   ```
   cd nome-do-repositorio
   ```
   
3. Execute o arquivo principal para ver o padrão Adapter em ação:
   ```
   python main.py
   ```
