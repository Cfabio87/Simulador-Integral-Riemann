# Simulador-Integral-Riemann

Aplicação interativa desenvolvida em Python para visualização das somas de Riemann, convergência do erro e interpretação geométrica da integral definida.

## Descrição

Este projeto consiste em uma aplicação interativa desenvolvida em Python para auxiliar no ensino e na aprendizagem do conceito de Integral Definida por meio da visualização das Somas de Riemann.

A ferramenta permite comparar as aproximações obtidas pelos métodos da Soma de Riemann à Esquerda, à Direita e do Ponto Médio, possibilitando a análise gráfica da convergência dessas aproximações para o valor real da integral.

Por meio da manipulação dos parâmetros da aplicação, os usuários podem explorar diferentes funções, intervalos de integração e números de subdivisões, observando em tempo real a relação entre os retângulos utilizados na aproximação, a área sob a curva e o erro associado a cada método.

## Funcionalidades

* Seleção interativa de funções matemáticas.
* Definição dos limites de integração (a) e (b).
* Controle do número de subdivisões do intervalo.
* Visualização simultânea de:
  * Soma de Riemann à Esquerda;
  * Soma de Riemann à Direita;
  * Soma de Riemann pelo Ponto Médio.
* Cálculo do valor exato da integral utilizando integração numérica.
* Exibição do erro de aproximação para cada método.
* Gráfico de convergência do erro conforme o número de subdivisões aumenta.
* Visualização da área sob a curva e dos retângulos utilizados nas aproximações.

## Funções Disponíveis

Atualmente a aplicação permite explorar as seguintes funções:

* (f(x)=x^2)
* (f(x)=\sin(x))
* (f(x)=\sqrt{x})
* (f(x)=\frac{1}{x})
* (f(x)=e^{-x^2})
* (f(x)=x^3-4x)

Novas funções podem ser facilmente adicionadas ao código.

## Objetivos Educacionais

A ferramenta foi desenvolvida com o objetivo de:

* Facilitar a compreensão do conceito de Integral Definida;
* Relacionar as representações algébrica, gráfica e geométrica das funções;
* Demonstrar o funcionamento das Somas de Riemann;
* Evidenciar a convergência das aproximações para o valor da integral;
* Auxiliar o ensino de Cálculo Diferencial e Integral por meio de recursos computacionais interativos.

## Tecnologias Utilizadas

* Python
* NumPy
* Matplotlib
* SciPy
* ipywidgets

## Como Executar

1. Instale as dependências necessárias:
pip install numpy matplotlib scipy ipywidgets

2. Execute o código em um ambiente compatível com widgets interativos, como:

* Jupyter Notebook
* Jupyter Lab
* Google Colab

3. Utilize os controles para:

* Selecionar a função;
* Definir os limites de integração;
* Alterar o número de retângulos utilizados na aproximação.

## Aplicações

Este projeto pode ser utilizado em disciplinas de:

* Cálculo Diferencial e Integral;
* Matemática Aplicada;
* Métodos Numéricos;
* Formação de Professores de Matemática;
* Tecnologias Digitais no Ensino de Matemática.

## Autor

Carlos Fábio de Oliveira Mendes

Projeto desenvolvido com fins educacionais e acadêmicos para o ensino de Integrais Definidas e Somas de Riemann.

Projeto desenvolvido com fins educacionais e acadêmicos para o ensino de Integrais Definidas e Somas de Riemann.
