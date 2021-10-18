# Aplicando get em uma API simples

Esse repositório faz uso de método get para extrair dados de uma [API](https://www.alphavantage.co/documentation/).

<h2>Requirements</h2>
Para inicializar crie sua [API Key totalmente gratuita](https://www.alphavantage.co/support/#api-key) pela própria plataforma da API. 


Após a criação da API, faça a alteração da mesma no arquivo `.env-example`, juntamente do BASE_URL, que deve ser `https://www.alphavantage.co/query`
para a realização de consultas. Ao término da operação altere o nome do arquivo para `.env` 

Como último requisito de preparação, para quem for apenas fazer uso, é necesário realizar um `pip install requirements.txt` no terminal do seu Sistema.
O mesmo irá instalar os pacotes necessários para a utilização da API. Caso seja de uso para estudo, faça uso do `pip install requirements-dev.txt` 
ele irá instalar os pacotes necessários para o desenvolvimento e aprimoramento do programa.

<h2>Execution</h2>
No terminal é necessário acessar o diretório do projeto dentro do seu computador e importar a classe StockTimeSeries do arquivo main. Para isso digite `from main import StockTimeSeries`
Depois disso já podemos instanciar a classe, atribuindo-a para alguma variável. Por exemplo:

`var = StockTimeSeries()`

Com a classe instanciada já podemos fazer uso de seus métodos com o objeto `var`, dentre os métodos temos consultas no modo `intraday`, `daily`,
`weekly` e `monthly`. Cada um desses métodos possui parâmetros específicos, sugiro consultar a [documentação da API](https://www.alphavantage.co/documentation/) para a aplicação dos GETs de forma
correta, sem gerar algum tipo de erro.

