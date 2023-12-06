# API de Reservas de Hotéis

Esta é uma API em Python construída com o framework Flask para gerenciar reservas de hotéis em várias cidades. A API permite criar, atualizar, listar e excluir reservas de hotéis, bem como obter informações sobre hotéis em uma cidade específica.

## Requisitos

- Python 3.6 ou superior
- Banco de dados SQLite
- Pacotes Python listados em `requirements.txt` (você pode instalá-los usando `pip install -r requirements.txt`)

## Configuração

1. Crie um ambiente virtual (recomendado):

```bash
python3 -m venv venv
```

2. Ativar a venv

```bash
source venv/bin/activate
```

3. Instale as dependências usando o pip:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python3 webapp/impl/app.py
```

A API estará disponível em `http://localhost:5000`.

## Endpoints da API

- `GET /hoteis/<cidade>`: Obtém todos os hotéis em uma cidade específica.
- `POST /reservas`: Cria uma nova reserva.
- `PATCH /reservas/<id>`: Atualiza uma reserva existente.
- `DELETE /reservas/<id>`: Exclui uma reserva.
- `GET /reservas`: Obtém todas as reservas.
- `GET /reservas/<id>`: Obtém uma reserva específica.

# Como Importar e Utilizar uma Coleção no Postman

O Postman é uma poderosa ferramenta de desenvolvimento de APIs que permite aos desenvolvedores criar, testar e documentar APIs de forma eficiente. Neste guia, você aprenderá como importar uma coleção no Postman e como utilizá-la para testar APIs.

## Pré-requisitos

Antes de começar, certifique-se de que você tenha o [Postman](https://www.postman.com/downloads/) instalado no seu computador.

## Importando uma Coleção

1. Abra o Postman:
   - Após a instalação, abra o aplicativo Postman.

2. Importe uma Coleção:
   - No lado esquerdo da interface, você verá uma guia chamada "Coleções" no painel de navegação. Clique nela para abrir as coleções existentes.
   - No canto superior direito, clique no botão "Importar" para abrir a janela de importação.

3. Selecione o arquivo da Coleção:
   - Clique no botão "Escolher arquivo" e selecione o arquivo WebApp.postman_collection.json que está na raiz do projeto.
   - Clique em "Continuar".

4. Confirme a Importação:
   - O Postman analisará a coleção e exibirá informações sobre o que será importado. Verifique se as informações estão corretas e clique em "Importar".

5. Acesse a Coleção Importada:
   - A coleção importada agora estará disponível na guia "Coleções" do Postman. Você pode expandir a coleção para ver todas as solicitações e detalhes relacionados a ela.

## Utilizando a Coleção

Agora que você importou com sucesso a coleção, você pode começar a utilizá-la para testar as APIs. Siga estes passos básicos:

1. Selecione uma Solicitação:
   - No painel de navegação à esquerda, clique na coleção que você importou.
   - Escolha uma solicitação específica dentro da coleção.

2. Execute a Solicitação:
   - Clique no botão "Enviar" para executar a solicitação. O Postman fará a solicitação à API com base nas configurações especificadas.

3. Analise a Resposta:
   - A resposta da solicitação será exibida na parte inferior da interface, mostrando o status da resposta, o corpo da resposta e outras informações relevantes.

4. Repita ou Edite:
   - Você pode repetir a solicitação quantas vezes quiser ou editar os parâmetros, cabeçalhos e corpo da solicitação conforme necessário.

## Exemplos de Uso utilizando o Postman

Aqui estão alguns exemplos de como usar os endpoints da API:

### Obtendo Hotéis em uma Cidade Específica

```
GET /hoteis/saoPaulo
```

### Criando uma Nova Reserva

```
POST /reservas

{
  "cidade": "saoPaulo",
  "hotel": "Hotel A",
  "quarto": "simples",
  "data": "2023-11-10"
}
```

### Atualizando uma Reserva Existente

```
PATCH /reservas/idDaReserva

{
  "data": "2023-11-15"
}
```

### Excluindo uma Reserva

```
DELETE /reservas/idDaReserva
```

### Obtendo Todas as Reservas

```
GET /reservas
```

### Obtendo uma Reserva Específica

```
GET /reservas/idDaReserva
```

5. Para visualizar o banco e manipula-lo
   baixe a extensão no VsCode:
[sqlite-editor](https://marketplace.visualstudio.com/items?itemName=yy0931.vscode-sqlite3-edito)

6. O arquivo do banco está localizado

```
instance/db.sqlite
```

Utilizando a extensão, consegue manipular o banco por completo.
