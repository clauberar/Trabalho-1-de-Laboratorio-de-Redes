# TRABALHO 1 DE LABORATÓRIO DE REDES

Esse trabalho foi desenvolvido na disciplina de Laboratório de Redes ministrada pelo Professor Alexandre Pereira do Carmo. Tem como objetivo desenvolver 3 programas rodando em Máquinas Virtuais:

**1º Programa:** Criar matrizes com valores inteiros aleatórios. 

**2º Programa:** Calcular a Inversa e o Determinante.

**3º Programa:** Exibir os resultados do segundo programa.

## PRÉ-REQUISITOS

Certifique-se de ter o Python3 instalado em sua máquina.Você pode ver a versão do seu Python executando:

>python --version

Com a versão atualizada, precisa-se instalar algumas bibliotecas utilizadas ao decorrer dos programas. Caso não tenha instaladas, basta executar:

>pip install numpy

>pip install pickle

>pip install socket

A sincronização do tempo das máquinas virtuais precisam ser realizadas, para isso o seguinte passo precisa ser seguido. Mostrar a sincronização
TESTANDO OS PROGRAMAS

>**NOTA:** Como esse trabalho foi desenvolvido para fins didáticos, algumas informações devem ser inseridas no código, como por exemplo o IPs e portas de algumas máquinas.
 
### PROGRAMA 1
No primeiro programa, devemos colocar na variável Host o  IP da máquina que está rodando o segundo programa.
Figura do local para inserir o IP 

Feito isso, o programa 1 irá se conectar através do protocolo TCP com o programa 2. Na tela do console, duas informações serão pedidas: o tamanho da matriz quadrada que vai ser criada e a quantidade de matrizes. 
Figura com as perguntas

>**Ex:**  Se a escolha for uma matriz 10x10 e quantidade de matrizes for 1, a seguinte resposta irá aparecer na tela do mesmo programa.
Figura com a matriz

Com essas informações a matriz vai ser criada de forma aleatória e um tempo de início vai ser armazenado em uma variável, a matriz junto com o tempo vai ser destinada ao programa 2. Ainda no programa 1, uma pergunta para verificar o desejo de querer enviar mais matrizes vai ser exibida, sendo a opção S para enviar novas matrizes ou N para não enviar e fechar o programa.
 
### PROGRAMA 2
Assim como no primeiro programa, devemos colocar na variável o HostProx o  IP da máquina que está rodando o terceiro programa. Dessa forma o programa vai conseguir receber através do socket e enviar os resultados para o terceiro programa.
Figura do local para inserir o IP 

Neste programa não vai ter intervenção do usuário na interface, somente na mudança do valor da variável HostProx por motivo do desenvolvimento didático do trabalho.
Essa aplicação tem como objetivo receber a matriz, calcular a sua inversa e o seu determinante e encaminhar para uma terceira aplicação junto com o tempo inicial da criação da matriz.
 
### PROGRAMA  3
Alterações realizadas no programa 1 e 2 não vão ser necessárias nesta aplicação, pois somente vai  receber pacotes e não encaminhar. Após o recebimento dos pacotes, a Inversa, o Determinante e o Tempo vão ser exibidos na tela. O tempo de todo processo, desde a criação da matriz até a exibição, vai ser uma subtração do tempo gravado no momento da exibição pelo o Tempo da criação. Para que o tempo resultante seja autêntico, a sincronização dos tempos da máquina como citado anteriormente tem que ser realizada.
Figura do resultado

## CONSIDERAÇÕES
Esse programa foi realizado com todos os conhecimentos adquiridos na disciplina de Redes e com instruções de programas recebidos ao longo de toda a formação acadêmica. 
