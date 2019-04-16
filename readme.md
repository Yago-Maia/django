# Informações Gerais

O **GitLAB Community Edition (CE)** é uma plataforma de desenvolvimento de software de ponta a ponta com controle de versão integrado, rastreamento de problemas, revisão de código, CI / CD e muito mais.

O **Git** é um sistema de controle de versão distribuído e o **GitLAB** é um sistema de gerenciamento web de projetos e repositórios **Git**.

O **GitLAB** pode hospedar projetos e repositórios **Git** online semelhante ao que acontece com o **GitHub**.

No **Grupo São Marcos** ele está instalado em servidor local para armazenamento privado dos códigos a serem versionados pelo **Git**.

Abaixo uma breve explicação das funcionalidades básicas do Git.

## Instalando o Git Client

Acesse a pagina https://git-scm.com/downloads, e faça o download do executável, apos o download um duplo click do executável para iniciar a instalação, siga as instruções para finalizar a instalação.

## Configurações no prompt de comando

Abra um prompt de comando do git(git-bash) e execute os comandos abaixo;

### Git - Configurações Globais

```bash
git config --global user.name "{Nome Sobrenome}"

git config --global user.email "{e-mail cadastrado no git}"

git config --global http.sslverify false
```

## Criando um novo repositório

Crie uma nova pasta, abra-a e execute o comando

```bash
git init
```

## Obtendo projeto de um repositório

Crie uma cópia de trabalho em um repositório local executando o comando

```bash
git clone /caminho/para/o/repositório
```

quando usar um servidor remoto, seu comando será

```bash
git clone usuario@servidor:/caminho/para/o/repositório
```

## Como funciona o Fluxo de Trabalho com o Git

Seus repositórios locais consistem em três "árvores" mantidas pelo git. A primeira delas é sua **Working Directory** que contém os arquivos vigentes. A segunda **Index** que funciona como uma área temporária e finalmente a **Head** que aponta para o último commit (confirmação) que você fez. Quando achar que já está pronto para enviar pro servidor as alterações feitas locais, basta efetuar o commit (confirmação) para o branch(ramo) desejado.

### Adicionar & confirmar

Você pode propor mudanças (adiçona-las ao **Index** ) usando

```bash
git add <arquivo>
```

Ou para inserir todos os arquivo de uma pasta

```bash
git add *
```

Este é o primeiro passo no fluxo de trabalho básico do git. Para realmente confirmar estas mudanças (isto é, fazer um commit), use

```bash
git commit -m "comentários das alterações"
```

Agora  arquivo  é enviado para o **HEAD**, mas ainda não para o repositório remoto.

### Enviando alterações

Suas alterações agora estáo no **HEAD** da sua cópia de trabalho local. Para enviar estas alterações ao seu repositório remoto, execute

```bash
git push origin master
```

Altere _master_ para qualquer ramo(_branch_) desejado, enviando suas alterações para ele.

Se você não clonou um repositório existente e quer conectar seu repositório a um servidor remoto, você deve adicioná-lo com

```bash
git remote add origin <servidor>
```

Agora você é capaz de enviar suas alterações para o servidor remoto selecionado.

### Ramificando

Branches("ramos") são utilizado para desenvolver funcionalidades isoladas umas das outras. O branch master é o branch "padrão" quando você cria um repositório. Use outros branches para desenvolver e mescle-os (merge) ao branch master após a conclusão.

Crie um novo branch chamado "funcionalidades_x" e selecione-o usando

```bash
git checkout -b funcionalidade_x
```

retorne para o master usando

```bash
git checkout master
```

e remova o branch da seguinte forma

```bash
git branch -d funcionalidade_x
```

um branch não está disponível a outros a menos que você envie o brnach para seu repositório remoto.

```bash
git push origin <funcionalidade_x>
```

### Atualizar & Mesclar

Para atualizar seu repositório local com a mais nova versão, execute

```bash
git pull
```

na sua pasta de trabalho para obter e fazer merge (mesclar) alterações remotas.
para fazer merge de um outro branch ao seu branch ativo (ex. master), use

```bash
git merge <branch>
```

em ambos os casos o git tenta fazer o merge das alterações automaticamente. Infelizmente, isto nem sempre é possível e resulta em conflitos. Você é responsável por fazer o merge estes conflitos manualmente editando os arquivos exibidos pelo git. Depois de alterar, você precisa marcá-los como merged com

```bash
git add <arquivo>
```

antes de fazer o merge das alterações, você pode também pré-visualizá-as usando

```bash
git diff <branch origin> <branch destino>
```

### Rotulando

É recomendado criar rótulos para releases de software. Este é um conhecido conceito, que também existe no SVN. Você pode criar um novo rótulo chamado _1.0.0_ executando o comando

```bash
git tag 1.0.0 1b2e1d63ff
```

o 1b2e1d63ff representa os 10 primeiros caracteres do id de commit que você quer referenciar com seu rótulo. você pode obter o id de commit com

```bash
git log
```

você pode também usar menos caracteres do id de commit, ele somente precisa ser único.

### Sobrescrever alterações locais

No caso de você ter feito algo errado (que seguramente nunca acontece ;)) você pode sobrescrever as alterações locais usando o comando

```bash
git checkout -- <arquivo>
```

isso substitui as alterações na usa árvore de trabalho com o conteúdo mais recente ho HEAD. Alterações já adicionadas ao index, bem como novos arquivos serão mantidos.
Se ao invés disso você deseja remover todas as alterações e commits locais, recupere o histórico mais recente do servidor e aponte para seu branch master local desta forma

```bash
git fetch origin

git reset --hard origin/master
```

## Abaixo exemplos de utilização do prompt de comando para os projetos hospedados em nosso **GitLAB**

### Git - Configurações Globais

```bash
git config --global user.name "{Nome Sobrenome}"

git config --global user.email "{e-mail cadastrado no git}"

git config --global http.sslverify false
```

### Git - Para servidores que não estão com SSL valido

```bash
git config --global http.sslverify false
```

### Git - Incluir arquivo no projeto 

```bash
cd {projeto}

git add {Nome do arquivo}

git commit -m "Informe observação relacionada ao commit do arquivo"

git push -u origin master
```

### Git - Projeto existente na maquina local mas não está no Git

```bash
cd existing_folder

git init

git remote add origin https://git.smarcos.com.br/{grupo}/{projeto}.git

ou git remote add origin https://git.smarcos.com.br/{projeto}.git

git add .

git commit -m "Informe observação relacionada ao commit do arquivo"

git push -u https://git.smarcos.com.br/{projeto}.git master
```

### Git - Projeto já existe no repositorio Git (abrir um novo branch)

```bash
cd existing_repo

git remote rename origin old-origin

git remote add origin https://git.smarcos.com.br/{grupo}/{projeto}.git

ou git remote add origin https://git.smarcos.com.br/{projeto}.git

git push -u origin --all

git push -u origin --tags
```
