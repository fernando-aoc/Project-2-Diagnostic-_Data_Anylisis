#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados Diagnóstica: Verificando o porquê do alto cancelamento de serviço de internet 

# ##### # Importando módulos

# In[1]:


import pandas as pd
import plotly.express as px


# ## Passo I: Importando a base de dados

# In[2]:


dados = pd.read_csv('dados/internet_service_churn.csv')
dados.head()


# ## Passo II: Tratando e entendendo a base de dados 

# In[3]:


dados.shape


# In[4]:


dados.info()


# In[5]:


dados.isnull().sum()


# In[6]:


selecao = (dados['bill_avg'] == 0)
x = dados[selecao]
x['bill_avg'].value_counts()


# In[7]:


dados = dados[dados.bill_avg != 0]


# In[8]:


dados.drop(['reamining_contract', 'id'], axis = 1, inplace = True)
dados.head()


# In[9]:


novos_nomes = {'is_tv_subscriber': 'assinante_tv', 'is_movie_package_subscriber': 'assinante_pacote_filmes', 'subscription_age': 'tempo de assinatura', 'bill_avg': 'valor_conta', 'service_failure_count': 'falhas_de_serviço', 'download_avg':'mps_download', 'upload_avg': 'mps_upload', 'download_over_limit': 'downlaod_acima_limite', 'churn': 'cancelamento'}


# In[10]:


dados.rename(columns = novos_nomes, inplace=True)
dados.head()


# In[11]:


assinante_tv = {0: 'Não', 1: 'Sim'}
assinante_pacote_filmes = {0: 'Não', 1: 'Sim'}
falhas_de_serviço = {0: 'Não', 1: 'Sim'}
downlaod_acima_limite = {0: 'Não', 1: 'Sim'}
cancelamento = {0: 'Não', 1: 'Sim'}


# In[12]:


dados.assinante_tv = dados.assinante_tv.map(assinante_tv)
dados.assinante_pacote_filmes = dados.assinante_pacote_filmes.map(assinante_pacote_filmes)
dados.falhas_de_serviço = dados.falhas_de_serviço.map(falhas_de_serviço)
dados.downlaod_acima_limite = dados.downlaod_acima_limite.map(downlaod_acima_limite)
dados.cancelamento = dados.cancelamento.map(cancelamento)


# In[13]:


dados.head()


# ## Passo III: Analisando e visualizando os dados

# In[14]:


print(dados["cancelamento"].value_counts())
print(dados["cancelamento"].value_counts(normalize=True).map("{:.1%}".format))


# In[15]:


for coluna in dados.columns: 
        grafico = px.histogram(dados, x=coluna, color="cancelamento", text_auto=True)
        grafico.show()


# ## Passo IV: Conclusão

# #### I: O cancelamento é proporcionalmente muito maior com os assinantes que não tem TV assinada também (podemos oferecer incentivos para assinarem TV);
# #### II: O cancelamento é proporcionalmente muito maior com os assinantes que não tem pacote de filmes assinados também (podemos oferecer incentivos para assinarem o pacoted e filmes);
# #### III: O cancelamento é muito maior proporcionalemnte nos primeiros meses (podemos oferecer incentivos para assinarem por um período mais longo);
# #### IV: Há um alto cancelamento relacionado a altas taxas de mps para download e mps para upload, indicando um problema de conexão generalizado na rede.

# In[ ]:




