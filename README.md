### **Desafio**
https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/yEPxE/programa-completo-jogo-do-nim

### **Introdução**

Manuel Estandarte atua como monitor na disciplina de Introdução à Produção Textual I na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel identificou a propagação de uma epidemia de COH-PIAH na UPA. Essa enfermidade incomum e altamente contagiosa leva os indivíduos contaminados a produzirem textos involuntariamente similares aos de outros. Diante dessa situação, Manuel, preocupado com a saúde dos alunos, decidiu desenvolver um programa para identificar casos de COH-PIAH, solicitando sua colaboração nesse processo.

### **Detecção de Autoria**

A detecção de autoria baseia-se na análise estatística de diferentes características textuais, permitindo identificar uma "assinatura" única de cada autor. Essa abordagem, útil para detecção de plágio, evidências forenses e diagnóstico de COH-PIAH, utiliza seis traços linguísticos distintos.

### **Traços Linguísticos**

##### Os traços linguísticos considerados são:

- Tamanho Médio de Palavra: Calculado como a média simples do número de caracteres por palavra.
- Relação Type-Token: Obtida pelo número de palavras diferentes dividido pelo total de palavras no texto.
- Razão Hapax Legomana: Representada pelo número de palavras utilizadas uma única vez dividido pelo número total de palavras.
- Tamanho Médio de Sentença: Resulta da média simples do número de caracteres por sentença.
- Complexidade de Sentença: Calculada como a média simples do número de frases por sentença.
- Tamanho Médio de Frase: Obtido pela média simples do número de caracteres por frase.

## **Funcionamento do Programa**

Com base na assinatura conhecida de um portador de COH-PIAH, o programa avalia diversos textos, calculando os valores dos traços linguísticos para compará-los com a assinatura fornecida. A similaridade entre dois textos (A e B) é determinada pela fórmula:

![image](https://github.com/MAGALHAESMARIA/COH_PIAH/assets/159083956/0b7afbb4-0b23-4c27-a460-30b6b169bd92)


Perceba que quanto mais similares A e B forem, menor será **Sab**. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).

O curso forneceu funções de suporte para auxiliar na construção do código.
