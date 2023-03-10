<h1>Python Exercises during vacation</h1>



<p>Avaliação 1: Você ficou encarregado de criar um programa para validar o número de um novo documento da sua empresa. Como é um documento sensível, algumas regras foram criadas para que seja mais difícil alguém criar um número falso.

Regras:

- Regra 1: O número do documento deve ter 5 dígitos no total. Exemplo: 23265. Neste exemplo, o primeiro dígito é o 2, o segundo é o 3, o terceiro é o 2 e assim por diante.
- Regra 2: O segundo dígito elevado a 4 deve ser divisível por 3. A mesma regra deve valer para o quarto dígito.
- Regra 3: O terceiro dígito não pode ser 0 nem 1.
- Regra 4: A soma do terceiro com o último dígito deve ser maior que 3.
- Regra 5: O primeiro dígito deve necessariamente ser 2, 5 ou 9.

Seu programa deverá receber como entrada três números de documento, sendo um número por linha. Como saída, para cada número, o programa deverá exibir True caso o respectivo número seja válido de acordo com as regras acima, ou False caso contrário.</p>



<p>Avaliação 3: Você foi contratado pela empresa SpaceX para construir um programa que simula o resultado do lançamento de um foguete.
 
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
- A segunda etapa é a divisão da distância alvo por soma_pares.</p>


<p></p>
