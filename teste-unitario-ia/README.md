# Atividade 2: Uso de IA para geração de cenários de teste

## Estrutura
- `calculadora.py`: funções da calculadora (copiadas da atividade anterior).
- `test_calculadora_ia.py`: testes unitários planejados com apoio de IA.

## Função escolhida
`potencia(a, b)`

## Prompt utilizado

Primeiro prompt (cenários):
```text
Atue como um professor de Teste de Software.

Tenho a seguinte função Python:

def potencia(a, b):
    return a ** b

Quero criar testes unitários usando unittest.

Liste pelo menos 6 cenários de teste para essa função.

Para cada cenário, informe:
- nome do cenário;
- entrada;
- resultado esperado;
- tipo do cenário: caso normal, caso de borda ou caso de erro.

Não gere código ainda.
```

Segundo prompt (código):
```text
Agora transforme os cenários anteriores em testes unitários usando Python e unittest.

Considere que a função potencia(a, b) já foi importada no arquivo de teste.

Gere apenas o método de teste que deve ser colocado dentro da classe TestCalculadora.
Use nome de método iniciando com test_.
```

## Cenários sugeridos pela IA

| ID | Cenário | Entrada | Resultado esperado | Tipo |
| :--- | :--- | :--- | :--- | :--- |
| T01 | Potência de base positiva e expoente positivo | `potencia(2, 3)` | `8` | normal |
| T02 | Qualquer número elevado a zero | `potencia(5, 0)` | `1` | borda |
| T03 | Base positiva elevada a 1 | `potencia(7, 1)` | `7` | borda |
| T04 | Base 0 elevada a um número positivo | `potencia(0, 5)` | `0` | borda |
| T05 | Base negativa elevada a expoente par | `potencia(-2, 2)` | `4` | normal |
| T06 | Base negativa elevada a expoente ímpar | `potencia(-2, 3)` | `-8` | normal |
| T07 | Expoente negativo | `potencia(2, -1)` | `0.5` | borda |

## Análise dos cenários

Todos os cenários sugeridos pela IA foram aceitos. Eles cobrem casos normais, casos de borda (expoente zero, expoente um, base zero e expoente negativo) e nenhum erro/exceção, já que a função `potencia` não levanta exceções para esses valores. Nenhum cenário foi removido ou alterado, pois todos faziam sentido e os resultados esperados estavam corretos.

## Código final dos testes

```python
# test_calculadora_ia.py
import unittest
from calculadora import potencia


class TestCalculadora(unittest.TestCase):

    def test_potencia_com_varios_casos(self):
        casos = [
            (2, 3, 8),
            (5, 0, 1),
            (7, 1, 7),
            (0, 5, 0),
            (-2, 2, 4),
            (-2, 3, -8),
            (2, -1, 0.5),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(potencia(a, b), esperado)


if __name__ == "__main__":
    unittest.main()
```

## Resultado da execução

Comando:
```bash
python -m unittest discover
```

Saída obtida:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```