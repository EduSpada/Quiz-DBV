
# QUIZ DBV

QUIZ DBV é um aplicativo desktop desenvolvido para auxiliar Clubes de Desbravadores trabalhar as classes regulares e avançadas com seus membros de uma forma mais interativa. Podendo ser configurado com as perguntas específicas de cada classe ou manter a configuração criada por nós!


## Autores

- [@Eduardo Rodrigo Spada](https://github.com/EduSpada)


## Licença

[MIT](https://github.com/EduSpada/Quiz-DBV/blob/main/LICENSE)

Desenvolvido por:

Eduardo Rodrigo Spada
Ano: 2023

Aberto para uso ou modificações, com a 
única premissa de manter os créditos do 
desenvolvedor original estampado no 
aplicativo e código.




![Logo](https://s.educacaoadventista.org.br/escola/conteudos/7A9uWK04hAx0KxmjIsanJJNOZPtn26hQezwgB3e4.jpeg)


## Instalação

Basta clonar ou baixar este repositório e executar o arquivo "Quiz DBV.exe"

Para alterar, incluir ou excluir as perguntas será necessário alterar o arquivo "quest.json" seguindo o padrão JSON do arquivo.

O arquivo "quest.json" possue as seguintes chaves "ami", "com", "pes", "pio", "exc" e "gui" representando respectivamente as classes regulares.

Dentro de cada chave temos as preguntas em chaves numéricas iniciando em "0", novas perguntas devem seguir a sequencia numérica e quando preguntas forem excluídas é obrigatório ajustar a chave das perguntas seguintes.

Cada pregunta deve ter as chaves "quest" representando a pergunta e "resp" representando a resposta.

Exemplo do arquivo "quest.json":

```json
{
    "ami": 
        {
            "0":
                {
                    "quest": "Qual é o Voto do Desbravador?",
                    "resp": " Pela graça de Deus, serei puro, bondoso e leal; guardarei a lei do Desbravador, serei servo de Deus e amigo de todos."
                },
            "1":
                {
                    "quest": "Recite a Lei do Desbravador:",
                    "resp": "A lei do Desbravador ordena-me: Observar a devoção matinal; Cumprir fielmente a parte que me corresponde; Cuidar de meu corpo; Manter a consciência limpa; Ser cortês e obediente; Andar com reverência na casa de Deus; Ter sempre um cântico no coração; Ir aonde Deus mandar"
                }
        },
    "com": 
        {
            "0":
                {
                    "quest": "Qual é o voto do Desbravador?",
                    "resp": "Pela graça de Deus, serei puro, bondoso e leal, guardarei a lei dos Desbravadores, serei um servo de Deus e amigo de todos."
                },
            "1":
                {
                    "quest": "Qual é o nome do livro de leitura do ano?",
                    "resp": "Um desafio atrás do outro."
                }
        }
}
```
    
## Contribuindo

A aplicação foi desenvolvida utilizando o Python na versão 3.7.9 e só deve ser modificado com essa distribuição do SDK para evitar bugs.

Para modificar crie uma virtual env e instale as dependências contidas no arquivo "requirements.txt"

