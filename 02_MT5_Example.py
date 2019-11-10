# - Link oficial do exemplo:
# - https://www.mql5.com/pt/docs/integration/python_metatrader5/mt5copyticksfrom_py
# - MT5CopyTicksFrom(
# -    symbol,       // nome do símbolo
# -    from,         // data a partir da qual os ticks são solicitados
# -    count,        // número de ticks solicitados
# -    flags         // combinação de sinalizadores que definem o tipo de ticks solicitados
# -    )

from MetaTrader5 import *
from pytz import timezone
from datetime import datetime, timedelta
import pandas as pd

# - Passso - 01
# - Inicializando a conexão co MT5 e buscando os dados do ativo.
def inicializa(Ativo, Ano,Mes,Dia,QtdeBar):
    utc_tz = timezone('America/Recife') #timezone("UTC")
    try:
        MT5Initialize()
        MT5WaitForTerminal()
        
        utc_from = datetime(Ano, Mes, Dia, tzinfo=utc_tz)
        # - MT5_COPY_TICKS_ALL ...: todos os ticks
        # - MT5_COPY_TICKS_INFO ..: ticks contendo alterações de preços Bid e/ou Ask
        # - MT5_COPY_TICKS_TRADE .: ticks contendo alterações do preço Last e/ou do volume (Volume)
        ticksAtivo = MT5CopyTicksFrom(Ativo, utc_from, QtdeBar, MT5_COPY_TICKS_TRADE)
        
        MT5Shutdown()
        return ticksAtivo
    except Exception as e:
        raise e

# - Passso - 02
def prepareData(Ativo, Ano,Mes,Dia, QtdeBar):  
    try:
        ticksAtivo = inicializa(Ativo,Ano,Mes,Dia, QtdeBar)
        df = pd.DataFrame(data=list(ticksAtivo), 
                  columns=['time', 'bid', 'ask', 'last', 'volume', 'flags'])

        # - Eliminando a coluna flags
        df.drop('flags', axis=1, inplace=True)
        # - Somente formatando a data para que Dataframe entenda a coluna como um objeto de datetime.
        df['time'] = pd.to_datetime(df.time, format='%Y-%m-%d %H:%M:%S')
        # - Ajustando o horario UTC.
        df['time'] += timedelta(hours=3)
        # - Ordenando os dados do mais novo para o mais antigo.
        #df.sort_index(ascending=False, inplace=True)        
 
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
# - Quantidade de ticks solicitados.
# - Pega 3000 ticks a partir da data solicitada. 
_QtdeBar = 3000

# - DataFrame do Pandas para armazenar os dados do MT5 - _Df_Ativo
# - Buscando os dados do MT5
_Df_Ativo = prepareData(_Ativo, _Ano,_Mes, _Dia, _QtdeBar)

# - Imprimindo na tela os 10 primeiros registros.
print(_Df_Ativo.head(10))