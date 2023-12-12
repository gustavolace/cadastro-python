# Cadastro de Personagens

O sistema de cadastro de personagens em Python é uma aplicação que proporciona uma plataforma para a criação, visualização, atualização e exclusão (CRUD) de personagens fictícios. Além disso, o sistema oferece funcionalidades de cadastro de usuário e login, permitindo que cada usuário tenha seus personagens associados exclusivamente a ele. Independentemente do momento ou local de acesso, os personagens criados por um usuário específico permanecem vinculados à sua conta, garantindo uma experiência consistente e personalizada.

Por favor, leia este README no meu GitHub [gustavolace/cadastro-python](https://github.com/gustavolace/cadastro-python/blob/main/README.md).

## Índice
- [Uso](#uso)
  - [Cadastro](#cadastro)
  - [Lista de personagens](#lista-de-personagens)
  - [Criar personagem](#criar-personagem)
  - [Edição/Exclusão](#ediçãoexclusão)
- [Segurança](#segurança)
  - [Acesso restrito](#acesso-restrito)
  - [Senha criptografada](#senha-criptografada)
- [Créditos](#créditos)

## Uso
Para iniciar o programa de cadastro, abra o arquivo de atalho para executável principal [main.exe](./main.exe)

Ao fazer isso, uma tela de comando será exibida, redirecionando você para o seu navegador principal.

### Cadastro
Clique em ``"Não é um cliente? Cadastrar"``, preencha as informações necessárias e, em seguida, faça login com as credenciais cadastradas.

### Lista de personagens
Nesta seção, serão exibidos os personagens criados. Você pode criar um novo personagem ou desconectar-se.

### Criar Personagem
Aqui, é possível definir atributos para a criação de um personagem. Por padrão, a cor do cabelo é amarela, a cor da pele é bege, e a inteligência e força são definidas como 5.

### Edição/Exclusão
Para editar um personagem, retorne à lista de personagens, clique no personagem desejado, faça as alterações necessárias e atualize.

Para excluir um personagem, clique no ``"x"`` ao lado dele.

## Segurança
O código possui medidas de segurança para impedir acessos não autorizados aos dados dos usuários, incluindo informações dos personagens e senhas.

### Acesso restrito
Cada usuário possui um número de identificação associado. Ao acessar a lista de personagens ou criar um personagem, um número será exibido na barra de endereços. Se um usuário tentar alterar esse número para acessar dados de outros usuários, o programa verificará dinamicamente se ele possui permissão. Caso contrário, será exibida uma mensagem de `"Acesso restrito"`.

### Senha Criptografada
Após o cadastro, a senha é gravada no banco de dados, mas antes de ser armazenada, é criptografada usando a biblioteca ``bcrypt``. Isso torna a senha inacessível para qualquer pessoa, exceto o próprio usuário, que conhece a senha original.

Exemplo de senha criptografada:
``scrypt:32768:8:1$eSpn0VycjQtp2ZQ6$dc9406b42cd899249de6d4fa6f267541690ffa132002da186f863c1af1cf2093dd6e6fc6b255e274059700237278304b5785126b332e9c4736d92082b621ae0``

## Créditos
Código composto por Gustavo Lacerda como projeto da Infinity School.

Confira meus outros projetos!<br>
Entre em contato: [lsbgustavo@gmail.com](mailto:lsbgustavo@gmail.com)


