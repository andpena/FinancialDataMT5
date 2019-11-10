# - Link oficial do exemplo:
# - https://www.mql5.com/pt/docs/integration/python_metatrader5/mt5copyratesfrom_py
# - MT5CopyRatesFrom(
# -    symbol,       // nome do símbolo
# -    timeframe,    // período gráfico
# -    from,         // data de abertura da barra inicial
# -    count         // número de barras
# -    )

from MetaTrader5 import *
from pytz import timezone
from datetime import datetime, timedelta
import pandas as pd

# - Passso - 01
# - Inicializando a conexão co MT5 e buscando os dados do ativo.
def inicializa(Ativo, Ano,Mes,Dia,QtdeBar,TimeFrame):
    utc_tz = timezone("America/Recife") #timezone("UTC")
    try:
        MT5Initialize()
        MT5WaitForTerminal()
        
        utc_from = datetime(Ano, Mes, Dia, tzinfo=utc_tz)
        
        ticksAtivo =  MT5CopyRatesFrom(Ativo, TimeFrame, utc_from, QtdeBar)
        
        MT5Shutdown()
        return ticksAtivo
    except Exception as e:
        raise e

# - Passso - 02
def prepareData(Ativo, Ano,Mes,Dia, QtdeBar, TimeFrame):  
    try:
        ticksAtivo = inicializa(Ativo,Ano,Mes,Dia, QtdeBar, TimeFrame)
        df = pd.DataFrame(data=list(ticksAtivo), 
                  columns=['date', 'open', 'high','low', 'close','tick_volume', 'spread', 'real_volume'])

        # - Somente formatando a data para que Dataframe entenda a coluna como um objeto de datetime.
        df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d %H:%M:%S')  
        # - Ajustando o horario UTC.
        df['date'] += timedelta(hours=3)
        # - Ordenando os dados do mais novo para o mais antigo.
        df.sort_index(ascending=False, inplace=True)        
 
    except Exception as e:
        raise e
    df.symbol = Ativo
    return df

# - Ativo
_Ativo = "MGLU3"

# - Data inicio da busca dos dados historicos
_Ano = 2019
_Mes = 11
_Dia = 8  
# - Quantidade de barras solicitadas.
# - Pega 30 barras fechadas para traz da data solicitada. 
_QtdeBar = 30

# - Tempo grafico - M1, M5, M15, M30, H1, D1 etc...
# - Timeframe diario.
_TimeFrame = MT5_TIMEFRAME_D1

# - DataFrame do Pandas para armazenar os dados do MT5 - _Df_Ativo
# - Buscando os dados do MT5
_Df_Ativo = prepareData(_Ativo, _Ano,_Mes, _Dia, _QtdeBar, _TimeFrame)

# - Imprimindo na tela os 10 primeiros registros.
print(_Df_Ativo.head(10))
