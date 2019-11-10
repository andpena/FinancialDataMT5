# FinancialDataMT5
Exemplos de integração com Metatrader 5

## Dados financeiros Históricos
A ideia aqui é ser bem simples, somente mostrar como é possivel buscar as informações da plataforma MetaTrader5.(Ai cada um que use sua imaginação)

### 01_MT5_Example - Busca dados históricos de um ativo
Arquivo inicia a coleta da informações OHLC (Open,High,Low,Close e volume ) de um timeframe(Tempo Grafico) da sua escolha em um determinado periodo: python 01_MT5_Example.py


### 02_MT5_Example - Busca os ticks históricos de um ativo (Informaçoes do Times & Trades ou Times and Sales)
Arquivo inicia a coleta da informações do Times & Trades: python 02_MT5_Example.py



#### Observação: É necessário que o MetaTrader5 esteja aberto e conectado a corretora. (Sei que parece óbvio, mas é bom lembrar)

Video do programa rodando (Também não sei gravar video, mas vai esse mesmo):
https://youtu.be/mceSoc96Y9M

### Bibliotecas necessárias para os exemplos
	* Instalando bibliotecas
		* python -m pip install MetaTrader5
		* python -m pip install pytz
		* python -m pip install pandas
###### Talvez seja necessário instalar o pacote da microsoft runtime c++. Quem já tem Visual Studio na máquina não precisa instalar.
###### https://www.microsoft.com/pt-br/download/details.aspx?id=48145

###### Link de onde foram tirados os exemplos.
###### https://www.mql5.com/pt/docs/integration/python_metatrader5

Não sou especialista em Python, então não reparem no código. 
