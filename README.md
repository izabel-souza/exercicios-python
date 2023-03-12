<h1>Python Exercises during vacation</h1>

<div>
  <p>
      Avaliação 1: Você ficou encarregado de criar um programa para validar o número de um novo documento da sua empresa. Como é um documento sensível, algumas regras foram criadas para que seja mais difícil alguém criar um número falso.

  Regras:

  - Regra 1: O número do documento deve ter 5 dígitos no total. Exemplo: 23265. Neste exemplo, o primeiro dígito é o 2, o segundo é o 3, o terceiro é o 2 e assim por diante.
  - Regra 2: O segundo dígito elevado a 4 deve ser divisível por 3. A mesma regra deve valer para o quarto dígito.
  - Regra 3: O terceiro dígito não pode ser 0 nem 1.
  - Regra 4: A soma do terceiro com o último dígito deve ser maior que 3.
  - Regra 5: O primeiro dígito deve necessariamente ser 2, 5 ou 9.

  Seu programa deverá receber como entrada três números de documento, sendo um número por linha. Como saída, para cada número, o programa deverá exibir True caso o respectivo número seja válido de acordo com as regras acima, ou False caso contrário.
  </p>
</div>

<div></div>

<div>
  <p>Avaliação 2: Construa um programa para simular um personagem andando em uma sala escura. O programa recebe como entrada comandos direcionais para o personagem andar. Somente os comandos na tabela abaixo são aceitos pelo programa. Se um comando inválido for dado como entrada, o programa deve exibir a mensagem “E” e terminar.

Entrada	Ação
D	Personagem anda para a direita.
E	Personagem anda para a esquerda.
C	Personagem anda para cima.
B	Personagem anda para baixo.
O programa deve se basear no seguinte mapa visto de cima:

  <div><p>INÍCIO	  O	       O	       X</p></div>
  <div><p>X	      PORTA3	   O	     PORTA 1</p></div>
  <div><p>X	        X	    PORTA 2	    X</p></div>
 
No mapa acima, o personagem começa no piso “INÍCIO”. Os pisos marcados com “O” são pisos onde o personagem pode passar. Os pisos marcados com “X” são pisos onde o personagem não pode passar. Se o personagem chegar em um piso com “X”, deverá ser exibida a mensagem correspondente da tabela abaixo e o programa deverá terminar. Leve em consideração as ações da tabela e os resultados de cada ação ao fazer o seu programa. O programa deve esperar uma entrada caso o piso onde se encontra o personagem seja o INÍCIO ou um piso marcado com “O”.

Lembrem-se que as mensagens de saída do programa devem estar exatamente iguais à tabela e exemplos abaixo. Se você usar x ao invés de X, seu programa não estará correto.

Ação

Ação	Resultado
Andar para um piso marcado com "X"	Exibir a mensagem "X" e terminar o programa.
Andar de volta para o piso onde acabou de passar.	Exibir a mensagem "V" e terminar o programa.
Chegar no piso PORTA 3.	Exibir a mensagem "P3" e terminar o programa.
Chegar no piso PORTA 2.	Exibir a mensagem "P2" e terminar o programa.
Chegar no piso PORTA 1.	Exibir a mensagem "P1" e terminar o programa.
Inserir um comando desconhecido.	Exibir a mensagem "E" e terminar o programa.</p>
</div>

<div></div>

<div>
  <p>
    Avaliação 3: Você foi contratado pela empresa SpaceX para construir um programa que simula o resultado do lançamento de um foguete.
 
- O programa deve receber como entrada:
    - A distância esperada (inteiro) que o foguete deve chegar em km (distância alvo), em relação ao solo.
    - A quantidade de combustível (inteiro) disponível inicialmente, em kg.
- O programa deve exibir como saída:
    - A cada km percorrido com sucesso, deve exibir o total de kms percorridos até o momento e a quantidade atual de combustível disponível. Essas informações são separadas por um espaço. Os valores deverão ser exibidos como inteiros (sem casa decimal). Use a função (int) para transformá-los. Exemplo: se em um dado momento o foguete percorreu 50km e ainda tem 30kg de combustível, deve imprimir: 50 30.
 

Você deve considerar no programa que o foguete irá percorrer 1 km por vez (iteração). O programa deve terminar no momento que o foguete chegar até a distância esperada ou quando a quantidade de combustível disponível não for suficiente para percorrer o próximo kilômetro.



 A cada iteração do programa, você deve calcular quanto de combustível ainda resta subtraindo o consumo de combustível da quantidade de combustível atual. Use as regras abaixo para calcular o consumo de combustível a cada iteração.
 
Consumo de combustível
 
O consumo de combustível depende distância atual do foguete em relação ao solo e da distância alvo.
 

Para calcular o consumo, usaremos duas etapas:
 

- A primeira etapa, que iremos chamar de soma_pares, é a soma dos números inteiros pares menores que a distância atual, mais um.
- A segunda etapa é a divisão da distância alvo por soma_pares.
  </p>
</div>

<div></div
  
<div>
  <p>
    Desenvolva um programa que receba duas entradas. A primeira é um parágrafo de um texto. A segunda é uma lista de palavras.

Entradas:
- um texto (sem quebra de linhas).
- uma lista de palavras separadas por espaço.

 

Um detalhe importante é que tanto o texto como a lista de palavras recebidos como entrada não possuem espaços em branco. Cada espaço em branco foi substituído por um caractere underscore "_". Sua primeira tarefa é substituir todos os caracteres underscores por espaços em branco no texto e na lista de palavras.

Depois, seu programa deve retirar os caracteres de pontuação (ponto, vírgula e ponto e vírgula) do texto. Feito isso, deverá processá-lo e exibir algumas estatísticas sobre o texto processado, conforme lista de saídas abaixo:

Saídas:
- Quantidade de palavras no texto. Considere que qualquer conjunto de caracteres separados por espaço é uma palavra. A única exceção é quando o texto possui uma única palavra. Nesse caso não existe espaço.
- Para cada palavra da lista de palavras, exibir a palavra e a quantidade de vezes que ela aparece no texto. 
  </p>
</div>

