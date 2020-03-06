                                                 Avaliação Técnica
-----------------------------------------------------------------------------------------------------------------
Descrição:
O projeto tem por finalidade retornar o tempo no momento, através da API da climatempo das seguintes cidades:
São Paulo
Santos
Salvador
Rio de Janeiro
São Carlos
Maceió
Todos os dados são salvos em uma tabela, desenvolvida por meio do módulo SQLite.
-----------------------------------------------------------------------------------------------------------------
Arquivos:
No site sqlite.org, na aba de downloads, deve-se fazer o download do sqlite-tools e sqlite-dll.
Posteriormente, é preciso extrair os arquivos sqlite3.def, sqlite3.dll e sqlite3.exe. Neste caso, estes 
arquivos foram alocados em C:.
-----------------------------------------------------------------------------------------------------------------
Detalhes:
Como há um limite por minuto para as requisições, uma parte do procedimento foi omitida. No site da API, há uma
url para requisição e obtenção da id de cada cidade. Um exemplo para a cidade de são paulo é:
req = requests.get('http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=b22460a8b91ac5f1d48f5b7029891b53')
Desta forma, foram obtidos os dados necessários (id das cidades) para as requisições do tempo no momento.

Deve ser criado um ambiente virtual e instaladas as dependências listadas em requirements.txt.
O código principal, chamado 'requisicoes', tem um while destinado a, caso ocorra um erro na busca dos dados,
repita o procedimento dentro de 60 segundos. Este while é auxiliado por dois if e um else, que estão presentes
para cada requisição ao longo do código. Imediatamente antes da requisição, há um if que verifica se houve sucesso
na requisição. Caso não, há a requisição, depois a verificação de sucesso. Se houve sucesso, aquele dado é 
guardado em uma linha da tabela. Se não houve sucesso, haverá a verificação após 60 segundos.

No código chamado 'banco_dados', é criada uma tabela chamada 'clima', e, posteriormente, existe uma função para
inserir dados de um dicionário nela. Há também uma função para consulta, que está presente na última linha do 
código principal, que retorna os dados salvos na tabela quando o código é executado. 