import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações iniciais
apps = ['iFood', '99Food', 'Keeta']
categorias = ['Pizza', 'Hamburguer', 'Japonesa', 'Brasileira', 'Doces']
bairros = ['Centro', 'Campestre', 'Jardim', 'Bangu', 'Casa Branca'] # Santo André

dados = []

# Gerando 1000 registros de pedidos simulados em 2026
for i in range(1000):
    data_pedido = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 120))
    app = random.choices(apps, weights=[55, 30, 15])[0] # iFood liderando a simulação
    categoria = random.choice(categorias)
    valor = round(random.uniform(30.0, 150.0), 2)
    bairro = random.choice(bairros)
    
    dados.append([data_pedido, app, categoria, valor, bairro])

# Criando o DataFrame
df = pd.DataFrame(dados, columns=['Data', 'Aplicativo', 'Categoria', 'Valor_Pedido', 'Bairro'])

# Salvando em CSV para usarmos no Power BI depois
df.to_csv('pedidos_delivery_2026.csv', index=False, encoding='utf-8-sig')

print("Arquivo 'pedidos_delivery_2026.csv' gerado com sucesso!")