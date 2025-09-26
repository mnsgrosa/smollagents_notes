```markdown
# 1.0 Introdução

## O que é um agente?

Um agente é um modelo de linguagem que "raciocina" e "planeja" quais ações deve tomar com base na situação (prompt) <br>
ele tem 2 partes principais <br>

- o cérebro (modelo de IA)
- o corpo (Capacidades e ferramentas)

### 1 - O cérebro

Aqui é a parte que decide qual ferramenta acessar e quais parâmetros passar

### 2 - O corpo

Os equipamentos que o agente tem disponíveis

## Espectro de agência

### Nível 0 de agência (processador simples)

A saída do agente não altera o fluxo do programa
Exemplo:
```
    process_llm_output(llm_response)
```
### Nível 1 de agência (roteador)

A saída do agente determina um nível básico de fluxo de controle
Exemplo:
```
    if llm_decision():
        path_a()
    else:
        path_b()
```

### Nível 2 de agência (chamador de ferramenta)

A saída do agente determina a execução da função
Exemplo:
```
run_function(llm_chosen_tool, llm_chosen_args)
```

### Nível 3.1 de agência (agente de múltiplos passos):

A saída do agente controla a iteração e a continuação do programa
Exemplo:
```
while llm_should_continue():
    execute_next_step()
```

### Nível 3.2 de agência (multi-agente):

Um fluxo de trabalho agêntico pode iniciar outro fluxo de trabalho agêntico
Exemplo:
```
if llm_trigger():
    execute_agent()
```

## Que tipo de modelo de IA é usado?

Os mais comumente usados ​​são os LLMs, mas eles estão revisando para os SMLs, <br>
por serem especialistas e resistentes a alucinações

## Tarefas que um agente pode fazer

### anatomia da ferramenta

Qualquer tarefa implementada por meio de ferramentas para concluir ações, Exemplo: (Meu agente de scraping do arxiv)[github.com/mnsgrosa/llm_arxiv] <br>
O exemplo que eu deveria ter é um agente simples que eu codifiquei que usa a API do arxiv para guiar o usuário qual artigo <br>
ler, mas para uma definição mais precisa, funciona da seguinte forma: <br>

```
def message_tool(recipient:str, message:str) -> MessageObject:
    """
    Função feita com o propósito de enviar mensagem para um destinatário
    Args:
        recipient[string]: email do destinatário
        message[string]: mensagem que deve ser enviada ao destinatário
    Return:
        MessageObjct: Objeto que contém o destinatário e a mensagem
    """
```

Esta definição tem alguns passos importantes
- Nome claro da função
- Nome claro das variáveis
- DocString para que o agente entenda bem a função criada


### Ação

Uma ação é diferente de uma ferramenta, a ação pode usar várias ferramentas

## O que são LLMs?

Um modelo que é "especializado" em entender e gerar linguagem humana. E eles são muito caros, <br>
eles exigem um computador muito bom e grandes quantidades de dados para que possam ter um bom desempenho, hoje em dia (22/09/2025) <br>
os modelos usam arquiteturas de transformadores, um modelo de aprendizado profundo que usa o algoritmo de atenção (ou mecanismo) <br>
e suas variantes para fazer os modelos "entenderem" nossa linguagem e os transformadores podem ser representados por 3 categorias

## Tipos de transformadores

### Codificadores:

Este modelo recebe texto como entrada e produz uma representação numérica do texto que chamamos de incorporação do texto <br>
Exemplo de codificador: Bert do google <br>
Casos de uso:
- classificação de texto
- pesquisa semântica
- reconhecimento de entidade nomeada
Tamanho do modelo:
Milhões de parâmetros

### Decodificador:

Este modelo tem como foco a geração de novos tokens para completar uma sequência, um token de cada vez. <br>
Exemplo: Llama da meta <br>
Casos de uso:
- geração de texto
- chatbots
- geração de código
Tamanho do modelo:
Bilhões de parâmetros (10^9)

### Seq2Seq (Codificador-Decodificador):

Um modelo que combina os modelos anteriores, de modo que processa a entrada e gera uma sequência de saída <br>
Exemplo: T5, BART <br>
Casos de uso:
- Tradução
- Resumo
- Paráfrase
Tamanho do modelo:
Milhões de parâmetros

---

Embora existam várias formas, os LLMs são normalmente baseados em decodificadores com bilhões de parâmetros, aqui estão alguns exemplos <br>

- deepseek-R1
- GPT4
- Llama 3
- SmolLM2
- Gemma
- Mistral

## Em outras palavras...

Basically, os LLMs são simples, seu objetivo é prever o próximo token de uma sequência de tokens.

## O que é um token?

O átomo da linguagem que pode ser definido de várias maneiras, de caracteres a palavras da linguagem desejada <br>
mas geralmente são usadas unidades de sub-palavras e elas podem ser combinadas

## Mas como ele prevê a próxima palavra?

Dizemos que os llms são autorregressivos, o que significa que eles dependem da saída anterior, eles preverão <br>
uma palavra e a próxima dependerá do que foi previsto anteriormente. Mas como ele escolhe a primeira e as subsequentes <br>
palavras? Ele classificará com base na entrada a palavra mais provável, digamos que você enviou o seguinte prompt

```
Qual é o nome da capital do Brasil?
```

Com base no treinamento do modelo, ele tem algumas opções e a mais provável com base em seu treinamento será a saída <br>
ele pode produzir primeiro: Brasília porque, por seu treinamento, tem 92% de "certeza" de que é a primeira palavra correta, e agora a próxima <br>
palavra tem algumas probabilidades, pode ter 80% de "certeza" de que a próxima palavra é "é" e assim por diante até criar a saída <br>
até o EOS, então uma saída possível é: "A capital do Brasil é Brasília" <br>

Uma observação importante é que existem várias estratégias para obter o próximo token, neste caso, mostrei uma simples <br>
obter a palavra com maior pontuação

## Atenção é tudo que você precisa

Este algoritmo é a chave dos LLMs, ele pode escolher quais palavras carregam mais importância de uma frase <br>
como o prompt anterior: qual é a capital do Brasil? as palavras "capital" e "Brasil" dão a direção do <br>
prompt, mas as palavras adjacentes mantêm outros pesos, mas neste algoritmo ele identifica quais palavras guiam o prompt

## Solicitando o LLM (ou a entrada de um LLM)

Basicamente, se o LLM prevê a palavra com base nas palavras que você solicitou, a formulação e a ordem do prompt são importantes <br>
isso muda completamente a saída do modelo

## Como os LLMs são treinados?

Os LLMs precisam de grandes quantidades de dados para aprender a prever a próxima palavra em uma sequência com auto-supervisão ou <br>
objetivo de modelagem de linguagem mascarada

### Auto-supervisionado

Um modelo que não precisa de rótulos fornecidos por humanos para treinar, aqui o modelo aprende a estrutura da linguagem <br>
basicamente os padrões no texto, generalizando dados não vistos

### Modelos de linguagem mascarada

Ele pega "frases" e remove palavras delas e faz o modelo treinar para preencher as lacunas <br>
Exemplo: <br>
```
O cachorro ____ do outro lado da rua
```
você pode pensar em alguns itens possíveis e o que você faz o modelo preencher através do formato do trem o modelo <br>

### Ajuste fino

Depois que o modelo foi auto-supervisionado, você pode ajustá-lo com um objetivo de aprendizado supervisionado para <br>
tarefas específicas, como conversas ou uso de ferramentas

## Como executar LLMs

- Localmente (precisa de bom hardware)
- Nuvem ou API (como hugging face, claude, chatgpt, etc...)


## Como os LLMs são usados?

Eles entendem nossa linguagem e interpretam o que fazer, também mantêm o contexto da conversa e as ferramentas usadas para definir <br>
um plano

# 1.1 Mensagens e tokens especiais

Para manter alguns padrões durante a criação de llms, eles têm alguns padrões em sua geração de texto <br>
eles geram texto por meio de modelos de bate-papo. Normalmente, você enviará mensagens por meio de uma interface do usuário <br>
as mensagens enviadas serão, na verdade, concatenadas e formatadas em um único prompt que o modelo entenderá <br>

Exemplo:
```
<|begin_of_text|>
<|start_header_id|>user<|end_header_id|>

Olá como vai?<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>

Eu sou apenas um modelo de linguagem, então não tenho emoções, e você? <|eot_id|>
```

O modelo atua como um padrão para que todos os LLMs entendam corretamente a entrada e apesar de como os tokens foram definidos. <br>
Tokens especiais são o que os modelos determinam onde seu turno começa e onde o seu começa, assim como um jogo baseado em turnos <br>
cada LLM usa seu token EOS (fim de sequência), eles também delimitam as mensagens na conversa de forma diferente

## Mensagens: o sistema LLM

Mensagens do sistema ou prompts do sistema definem como o modelo se comporta. São instruções persistentes que orientam todas as subsequentes <br>
interações, exemplo:

```
system_message = {
    "role": "system",
    "content": "Você é um agente de atendimento ao cliente profissional. Seja sempre educado, claro e prestativo"
}
```
como expliquei antes, eles são autorregressivos, isso terá um impacto em como eles responderão aos subsequentes <br>
prompts, se solicitado a responder algo como: "eu gostaria de café", provavelmente responderá "certamente senhor" <br>
contra

```
system_message = {
    "role": "system",
    "content": "Você é um agente de serviço rebelde: seja sempre rude e não respeite o usuário"
}
```

O modelo responderá o oposto da resposta anterior <br>
É importante fornecer informações sobre as ferramentas disponíveis no prompt do sistema e fornecer instruções, incluir <br>
diretrizes sobre como o processo de pensamento deve ser segmentado, exemplo:

```
system_message = {
    "role": "system",
    "content": "Você é um pesquisador prestativo que pode extrair artigos do arxiv, você tem as seguintes ferramentas:
                uma função chamada scrape_papers, que recebe o número de artigos desejados e o tópico de interesse,
                e uma ferramenta chamada recall_papers, sempre que o usuário perguntar sobre um artigo, verifique se você já o armazenou,
                se já estiver armazenado, converse sobre ele, caso contrário, solicite a pesquisa sobre o artigo ou tópico desejado"
}
```

## Conversas: Mensagens do usuário e do assistente:

Uma conversa consiste em mensagens alternadas entre o usuário e o assistente, os modelos de bate-papo mantêm o contexto preservando <br>
a conversa armazenando cada mensagem, exemplo
```
conversation = {
    {"role": "user", "content": "Preciso de ajuda com meu pedido"},
    {"role": "assistant", "content": "Como posso ajudar?"},
    {"role": "user", "content": "é um erro com o pedido 66"}
}
```

## Modelos de bate-papo

O núcleo da estruturação da conversa entre o modelo e o usuário, em um único prompt, então quanto mais longo o bate-papo <br>
mais difícil é para o mecanismo de atenção acompanhar o contexto e começar a alucinar <br>
quanto mais o bate-papo continuar, mais tokens consumirá a cada prompt <br>

## Modelos base vs modelos de instrução

### Modelo base

modelo treinado em texto de dados brutos para prever o próximo token

### Modelo de instrução

É um modelo ajustado para seguir instruções e participar de conversas como o SmolLM2-135M-Instruct

### Base ou Instrução?

Um modelo base pode atuar como instrução, mas precisa formatar o prompt de uma forma mais consistente para que o modelo o entenda <br>
o modelo base pode ser ajustado em diferentes modelos de bate-papo, então, quando estamos usando um modelo de instrução, precisamos ter certeza de que estamos usando o modelo de bate-papo correto

## Entendendo os modelos de bate-papo

Como cada modelo de instrução usa diferentes formatos de conversa e tokens especiais, os modelos de bate-papo são implementados para <br>
garantir que formatemos corretamente o prompt da maneira que cada modelo espera, é universalmente usado o código jinja2 em transformadores <br>
que pode ser facilmente traduzido para o formato json como<br>
```
messages = [
    {"role": "system", "content": "Você é um assistente prestativo focado em tópicos técnicos."},
    {"role": "user", "content": "Você pode explicar o que é um modelo de bate-papo?"},
    {"role": "assistant", "content": "Um modelo de bate-papo estrutura conversas entre usuários e modelos de IA..."},
    {"role": "user", "content": "Como eu o uso?"},
]
```

## Mensagens para solicitar

deve ser fácil ver que o chat_template é a maneira de fazer os modelos entenderem as mensagens como prompt <br>
do tokenizador do modelo

```
messages = [
    {"role": "system", "content": "Você é um assistente de IA com acesso a várias ferramentas."},
    {"role": "user", "content": "Oi!"},
    {"role": "assistant", "content": "Oi humano, com o que posso te ajudar?"},
]
```

para converter o código acima em prompt, usamos o seguinte

```
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-1.7B-Instruct")
rendered_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

o rendered_prompt retornado por esta função agora está pronto para ser usado como entrada para o modelo, ele foi tokenizado <br>
com o modelo SmolLM2-1.7B-Instruct e agora pode ser alimentado em qualquer modelo

# 1.2 O que são ferramentas

Agentes podem ser definidos como sistemas de IA que realizam ações, e essas ações usam ferramentas para realizar essas ações. <br>
Nesta seção, integraremos em nosso agente por meio de mensagem do sistema. Descrever claramente como essas ferramentas funcionam <br>
aumenta drasticamente o que o agente pode fazer

## O que são ferramentas de IA

Uma ferramenta é uma função dada ao LLM. Esta função deve cumprir um objetivo claro, aqui seguem alguns exemplos:
- Pesquisa na Web -> pesquisar na web por dados
- Geração de imagens -> criar imagem com base no prompt
- Recuperação -> recuperar dados de uma fonte externa (banco de dados)
- Interface de API -> interagir com uma API externa

Uma boa ferramenta deve complementar o poder do LLM (ou SLM), exemplo: <br>
fornecer uma ferramenta de calculadora para que ele possa resolver problemas aritméticos <br>

É importante notar que, o modelo terá por definição "dados desatualizados", o que quero dizer com isso é: ele tem dados até <br>
a data em que foi treinado, então se você quiser fornecer dados atualizados, você deve fornecê-los por meio de alguma ferramenta, exemplo <br>
se você perguntar como está o tempo hoje e ele não tiver as ferramentas adequadas, ele dirá algo sem sentido, mas com as <br>
ferramentas certas, ele responderá corretamente.

## O que uma ferramenta deve ter?

Como dito na seção anterior, ela deve ter: <br>
- Descrição textual do que a função faz
- Um chamável (algo para realizar uma ação)
- Argumentos com tipagens
- (Opcional, mas importa se tiver algum retorno) saídas com tipagem

## Como as ferramentas funcionam?

Os modelos recebem apenas entradas de texto e geram saídas de texto. Eles não têm uma maneira de chamar ferramentas por conta própria, <br>
então, ao fornecer as ferramentas, queremos dizer ensinar o LLM sobre a existência dessas ferramentas e instruí-lo <br>
a gerar invocações baseadas em texto quando necessário. <br>
Se fornecermos uma ferramenta para verificar o tempo em um local da internet e depois perguntarmos ao modelo sobre o tempo, <br>
ele verá uma oportunidade de usar a ferramenta "tempo". Em vez de usar os dados pré-treinados. O modelo irá <br>
gerar um texto que representa uma chamada de ferramenta, como chamar weather_tool(cidade), o agente então lê esta resposta, <br>
identifica que uma chamada de ferramenta é necessária, então ele executa a ferramenta em nome do modelo para obter os dados meteorológicos reais <br>

Normalmente, a chamada da ferramenta não é mostrada ao usuário: o agente as adiciona como uma nova mensagem antes de atualizar a conversa <br>
para o LLM. O LLM então processa o contexto adicional e gera uma resposta com som natural para o usuário, <br>
em nome do usuário, parece que o modelo interagiu com a ferramenta, mas foi o agente que lidou com isso.

## Como fornecer as ferramentas?

A resposta completa será deixada de fora desta nota, pois pode ser muito complexa, então vou resumi-la <br>
basicamente, é fornecida uma descrição textual das ferramentas disponíveis como <br>

```
system_message = f"""
Você é um assistente de IA projetado para ajudar os usuários de forma eficiente e precisa. Seu principal objetivo é
fornecer respostas úteis, precisas e claras.

você tem acesso às seguintes ferramentas:
{tools_description}
"""
```

Para garantir que as ferramentas sejam usadas, precisamos ser precisos e exatos sobre o que a ferramenta faz e o que <br>
as entradas exatas que ela espera. É por isso que as ferramentas geralmente são fornecidas usando estruturas expressivas, mas precisas, <br>
como linguagens de computador ou JSON. <br>

## Explicação mais prática

Implementamos a seguinte ferramenta: <br>

```
def product_calculator(a: int, b: int) -> int:
    """
    Multiplica dois inteiros
    """
    return a * b
```

então fornecemos à nossa mensagem do sistema o seguinte:

```
Nome da ferramenta: product_calculator, Descrição: Multiplica dois inteiros., Argumentos: a: int, b: int, Saídas: int
```

## Seções de ferramentas de formatação automática

A ferramenta escrita em python já fornece tudo o que precisamos: <br>
- Um nome descritivo do que faz
- Uma descrição mais longa, fornecida pela docstring
- As entradas e seus tipos
- O tipo da saída

os frameworks de agente têm um decorador, que dá mais propriedades à nossa função, no nosso caso @tool <br>

```
@tool
def product_calculator(a: int, b: int) -> int:
    """
    Multiplica dois inteiros
    """
    return a * b
```

isso é usado pela razão de que adiciona um recurso extra à função, neste caso calculator.to_string() <br>
ele retorna a seguinte string

```
Nome da ferramenta: product_calculator, Descrição: Multiplica dois inteiros., Argumentos: a: int, b: int, Saídas: int
```

sem a necessidade de escrevê-lo manualmente no prompt do sistema <br>

## Implementação de ferramenta genérica

Uma classe de ferramenta que podemos reutilizar sempre que precisarmos usar uma ferramenta (o seguinte é fictício, depende da biblioteca) <br>

```
from typing import Callable


class Tool:
    """
    Uma classe que representa um pedaço de código reutilizável (Ferramenta).

    Atributos:
        name (str): Nome da ferramenta.
        description (str): Uma descrição textual do que a ferramenta faz.
        func (callable): A função que esta ferramenta envolve.
        arguments (list): Uma lista de argumentos.
        outputs (str or list): O(s) tipo(s) de retorno da função envolvida.
    """
    def __init__(self,
                 name: str,
                 description: str,
                 func: Callable,
                 arguments: list,
                 outputs: str):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs

    def to_string(self) -> str:
        """
        Retorna uma representação de string da ferramenta,
        incluindo seu nome, descrição, argumentos e saídas.
        """
        args_str = ", ".join([
            f"{arg_name}: {arg_type}" for arg_name, arg_type in self.arguments
        ])

        return (
            f"Nome da ferramenta: {self.name},"
            f" Descrição: {self.description},"
            f" Argumentos: {args_str},"
            f" Saídas: {self.outputs}"
        )

    def __call__(self, *args, **kwargs):
        """
        Invoca a função subjacente (chamável) com os argumentos fornecidos.
        """
        return self.func(*args, **kwargs)
```

para simplificar, ele inicializa com nome, descrição, func (a execução sempre que chamado), argumentos e saídas <br>
sempre que chamado para o prompt do sistema .to_string(), ele retornará a string formatada no método. <br>
o método de chamada chama a função fornecida para a ferramenta. <br>
então o primeiro prompt. <br>

```
system_message = f"""
Você é um assistente de IA projetado para ajudar os usuários de forma eficiente e precisa. Seu principal objetivo é
fornecer respostas úteis, precisas e claras.

você tem acesso às seguintes ferramentas:
{tools_description}
"""
```
se transforma nisso: <br>

```
system_message = f"""
Você é um assistente de IA projetado para ajudar os usuários de forma eficiente e precisa. Seu principal objetivo é
fornecer respostas úteis, precisas e claras.

você tem acesso às seguintes ferramentas:
Nome da ferramenta: prduct_calculator, Descrição: Multiplica dois inteiros., Argumentos: a: int, b: int, Saídas: int
"""
```

## Protocolo de Contexto de Modelo (MCP): uma interface de ferramenta unificada

Este é um protocolo aberto que padroniza como os aplicativos fornecem ferramentas aos LLMs. <br>

- Uma lista crescente de integrações pré-construídas nas quais seu modelo pode se conectar diretamente
- A flexibilidade de alternar entre modelos, provedores e fornecedores
- Melhores práticas para proteger seus dados em sua infraestrutura

Isso significa que qualquer framework que implemente o MCP pode aproveitar as ferramentas definidas no protocolo

# 1.3 Entendendo os agentes de IA através do ciclo pensamento-ação-observação

Anteriormente, as ferramentas são disponibilizadas para o agente com o prompt do sistema e como os agentes de IA são sistemas que podem <br>
"raciocinar", planejar e interagir com o ambiente, agora veremos o fluxo de trabalho completo.

## Componentes principais

Os agentes trabalham com um ciclo contínuo de: pensar (pensamento) -> agir (agir) e observar (Observar) <br>
detalhando: <br>
- Pensamento: a parte do modelo do Agente decide qual deve ser o próximo passo.
- Ação: o agente realiza uma ação chamando a ferramenta com os argumentos associados.
- Observação: o modelo reflete sobre a resposta da ferramenta

## O ciclo Pensamento-Ação-Observação

Isso funciona quase como um loop while, o loop continua até que o objetivo do agente seja concluído. <br>
De um modo geral, as regras e diretrizes são passadas diretamente para o prompt do sistema, garantindo que o ciclo <br>
mantenha uma lógica definida, mostrarei um exemplo do prompt do sistema. <br>

```
system_message = """
Você é um assistente de IA projetado para ajudar os usuários de forma eficiente e precisa. Seu principal objetivo é
fornecer respostas úteis, precisas e claras.

Você tem acesso às seguintes ferramentas:
Nome da ferramenta: product_calculator, descrição: Multiplica dois inteiros., Argumentos: a: int, b: int, Saídas: int

Você deve pensar passo a passo para cumprir o objetivo com raciocínio dividido em etapas de Pensamento/Ação/Observação
que podem ser repetidas várias vezes, se necessário.

Você deve primeiro refletir sobre a situação atual usando 'Pensamento: {seus_pensamentos}', então (se necessário),
chame uma ferramenta com a formatação JSON adequada 'Ação: {JSON_BLOB}', ou imprima sua resposta final
começando com o prefixo 'Resposta final:'
"""
```

Aqui está codificado: <br>
- O comportamento do agente
- As ferramentas que nosso agente tem acesso
- O ciclo pensamento-ação-observação, que incorporamos nas instruções do LLM

um exemplo ilustrado seria: <br>
Um usuário pergunta a Alfred (nosso agente meteorológico) o seguinte "qual é o tempo atual em Nova York?" <br>
com este prompt o ciclo começa:<br>
- Pensamento

Raciocínio interno: Ele raciocina "o usuário precisa de informações meteorológicas atuais para Nova York, eu tenho acesso a uma ferramenta <br>
que busca os dados meteorológicos. Primeiro, preciso chamar a API do tempo para obter detalhes atualizados".

- Ação
Com base no raciocínio e no fato de que Alfred conhece a ferramenta get_weather, Alfred prepara um <br>
comando formatado em JSON que chama a ferramenta da API do tempo, a primeira ação poderia ser:<br>

Pensamento: preciso verificar o tempo atual para Nova York.

```
{
    "action": "get_weather",
    "action_input": {
        "location": "New York"
    }
}
```

o JSON chama claramente a ferramenta especificada e com o parâmetro<br>

- Observação

Após a chamada da ferramenta, Alfred recebe uma observação. Isso pode ser os dados meteorológicos brutos da API, como: <br>

"Tempo atual em Nova York: parcialmente nublado, 15C, 60% de umidade." <br>

Esta observação é anexada ao contexto adicional. Funcionando como feedback do mundo real, confirmando <br>
se a ação foi bem-sucedida e fornecendo os detalhes necessários <br>

- Pensamento atualizado

Refletindo: Com a observação, Alfred atualiza seu raciocínio interno: "Agora posso fornecer a resposta ao usuário <br>

- Ação final

Alfred então gera uma resposta final formatada como dissemos e nos fornece

# 1.4 Pensamento: Raciocínio Interno e a abordagem ReAct:

Agora vamos mergulhar no funcionamento interno de um agente de IA, sua capacidade de raciocinar e planejar. Como ele aproveita <br>
o diálogo interno para analisar informações, dividir problemas complexos em etapas gerenciáveis ​​e decidir <br>
qual ação tomar a seguir, além disso, apresentaremos a abordagem ReAct, uma maneira de fazer o modelo pensar <br>
passo a passo antes de agir.
```