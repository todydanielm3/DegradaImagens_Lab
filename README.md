# Projeto de Geração de Degradações em Imagens

Este projeto consiste em um script Python que gera diferentes degradações em uma imagem fornecida. As degradações incluem desfoque, brilho, contraste, redimensionamento e muito mais.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python (versão 3.6 ou superior)
- OpenCV (versão 4.5.3 ou superior)
- Matplotlib (versão 3.4.3 ou superior)
- NumPy (versão 1.21.2 ou superior)

## Instalação

1. Clone o repositório do projeto:

```
git clone https://

2. Navegue até o diretório do projeto:

```
cd nome-do-repositorio
```

3. Instale as dependências usando o pip:

```
- Python (versão 3.6 ou superior)
- OpenCV (versão 4.5.3 ou superior)
- Matplotlib (versão 3.4.3 ou superior)
- NumPy (versão 1.21.2 ou superior)

```

## Uso

1. Coloque a imagem que deseja processar no mesmo diretório do script `G_degrad.py` e defina o caminho da imagem na variável `imagem` no código.

2. Abra o arquivo `G_degrad.py` e execute o script Python:

```
python G_degrad.py
```

3. O script irá gerar as imagens degradadas e exibi-las na tela.

4. Os resultados também serão salvos em uma pasta chamada `graficos` no diretório do projeto.

## Personalização

- Você pode personalizar as degradações e as intensidades modificando as variáveis `degradacao` e `intensidades` no arquivo `G_degrad.py`.
- Para adicionar novas degradações, você pode criar métodos adicionais na classe `Degradacoes` no arquivo `gerar_degradacoes.py` e chamá-los no arquivo `G_degrad.py`.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## Agradecimentos

- [OpenCV](https://opencv.org/) pela biblioteca de processamento de imagens.
- [Matplotlib](https://matplotlib.org/) pela biblioteca de visualização de gráficos.
- [NumPy](https://numpy.org/) pela biblioteca de manipulação de arrays.
