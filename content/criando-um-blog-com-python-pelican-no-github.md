Title: Criando um blog com Python, Pelican, Github Pages e domínio personalizado
Date: 2017-08-27 16:30
Category: Python
Tags: python, pelican, github, hospedagem, domínio, tutorial
Authors: Felipe N Souza
Summary: Como criar um blog utilizando Python + Pelican e hospedar no Github Pages utilizando domínio personalizado.

Fala galera!

<p>Nesse post vamos mostrar como preparar o ambiente e criar um blog utilizando Python e Pelican. Depois utilizaremos o Github Pages para hospedar gratuitamente e configurar um domínio personalizado.</p>

### Preparando o ambiente

<p>Para preparar o ambiente recomendo fortemente a utilização do virtualenv e virtualenv-wrapper. O virtualenv cria ambientes virtuais que isolam os pacotes python instalados do restante do seu S.O. e o virtualenv-wrapper facilita a utilização do virtualenv. Se tiver problemas para isso recomendo fortemente o post sobre organização de ambiente Python do Henrique Bastos (Link no fim do post)</p>
<p>Com o virtualenv e virtualenv-wrapper instalados e configurados utilizaremos o comando abaixo para criar o ambiente virtual e o diretório no qual vamos trabalhar. Para utilizarmos o guthub pages é importante que o nome do projeto seja seu nome de usuário do github .github.io</p>

```bash
$ mkproject username-do-github.github.io
```
<p>Após isso você terá o ambiente virtual criado em seu diretório de ambientes virtuais, a pasta do projeto criada dentro do seu diretório de projetos, já estará com o venv ativo e dentro da pasta do projeto. (Massa neh!) Quando precisar ativar o ambiente basta rodar:</p>

```bash
$ workon username-do-github.github.io
```
E para desativá-lo:
```bash
$ deactivate
```
Para listar todos os seus ambientes virtuais basta rodar:
```bash
$ workon
```

### Primeiros passos com Pelican

<p>Com o venv ativo vamos instalar o Pelican e o markdown com o pip</p>
```bash
$ pip install pelican markdown
```
Para gerar o projeto pelo pelican basta rodar
```bash
$ pelican-quickstart

Welcome to pelican-quickstart v3.7.1.
This script will help you create a new Pelican-based website.
Please answer the following questions so this script can generate the files
needed by Pelican.

Using project associated with current virtual environment.Will save to:
/caminho/para/seus/projetos/username-do-github.github.io

#as opções em letras maísculas são os padrões

> What will be the title of this web site? # O título do seu site
> Who will be the author of this web site? # O nome do autor (provavelmente o seu)
> What will be the default language of this web site? [pt] #Idioma
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) # Deseja especificar a URL 
> What is your URL prefix? (see above example; no trailing slash) #sua url personalizada
> Do you want to enable article pagination? (Y/n) y   #Paginação nos posts                     
> How many articles per page do you want? [10]        #Quantos posts por página                          
> What is your time zone? [Europe/Paris] America/Sao_Paulo     #Fuso horário                              
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y #Altamente recomendado, pois faclita a geração do site estático
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y # Recarregamento automático do server em desenvolvimento
> Do you want to upload your website using FTP? (y/N) n                                                      
> Do you want to upload your website using SSH? (y/N) n                                                      
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n                                                       
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y   #Github
> Is this your personal page (username.github.io)? (y/N) y                                                                                              
Done. Your new project is available at /caminho/para/seus/projetos/username-do-github.github.io
```

### Versionando o blog com git e hospedando no Github Pages

<p>Após isso a estrutura do projeto estará pronta e é hora de começar a trabalhar com git. Para isso criaremos no github um repositório com o mesmo nome do projeto, ou seja, username-do-github.github.io. No diretório local precisamos iniciar o versionamento com git e adicionar o repositório do github como repositório remoto.</p>
```bash
$ git init
$ git remote add origin git@github.com:username-do-github/username-do-github.github.io.git
```

<p>Organizaremos o projeto em duas branchs:<br>
- master<br>
- pelican<br>
Na branch pelican ficarão os arquivos e códigos que irão gerar o site estático e na branch master apenas os arquivos estáticos gerados. Para isso crie um nova branch chamada pelican, adicione as alterações, faça o primeiro commit e suba para o repositório remoto</p>
```bash
$ git checkout -b pelican
$ git add .
$ git commit -m 'iniciando branch pelican'
$ git push origin pelican
```
<p>Para publicar o conteúdo estático na branch master utilizaremos o ghp-import, para instalá-lo basta utilizar o pip</p>
```bash
pip install ghp-import
```
<p>Para gerar os estáticos e enviar direto para o github basta utilizar o make</p>
```bash
make github
```

### Configurando o domínio personalizado

<p>Para adicionar o domínio personalizado o primeiro passo é adicionar o endereço de sua URL nos settings do repositório no github. Em seguida precisamos criar um arquivo chamado CNAME contendo o domínio na raiz do projeto. Para isso você deve adicionar o seguinte trecho ao seu pelicanconf.py</p>
```python
STATIC_PATHS = ['extras/CNAME']
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
}
```
<p>Isso fará com que o CNAME seja criado no momento da geração dos arquivos estáticos.</p>

### Criando e publicando novos posts

<p>Para criar novos posts você deverá criar um novo arquivo markdown na pasta content com o conteúdo do post seguindo a seguinte estrutura</p>
```bash
Title: Meu primeiro post
Date: 2017-08-27 15:30
Modified: 2017-08-27 19:30
Category: Python
Tags: pelican, publishing
Slug: meu-super-post
Authors: Seu Nome
Summary: Descrição resumida do post

Conteúdo do post!
```
<p>
 Em seguida add os arquivos alterados ao git, faça commit e suba as alterações para o repositório remoto primeiro para a branch pelican e depois utilizando o make para a branch master.</p>
```bash
$ git add . 
$ git commit -m 'first post' 
$ git push origin pelican 
$ make github
```
<p>Pronto! Seu site foi gerado com Python utilizando o Pelican, está hospedado gratuitamente no Github Pages e utilizando um domínio personalizado. Você ainda pode personalizar seu site utilizando os temas e plugins disponíveis [no repositório do pelican no github](https://github.com/getpelican)</p>

<p>Dúvidas, comentários ou sugestões são muito bem vindas!<br><br>
Até</p>

*Fonte:*<br>
[Guia para organização de ambiente Python - Henrique Bastos](https://medium.com/welcome-to-the-django/guia-definitivo-para-organizar-meu-ambiente-python-a16e2479b753)<br>
[Documentação Pelican](http://docs.getpelican.com/en/stable/)<br>
[Criando sites estáticos com Pelican Framework](http://pythonclub.com.br/criando-sites-estaticos-com-pelican.html)<br>
[Github Pages com Pelican e Travis-CI](http://pythonclub.com.br/github-pages-com-pelican-e-travis-ci.html)<br>
[Using a custom domain with github pages](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)