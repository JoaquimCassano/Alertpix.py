<div align="center">
<img src="https://i.imgur.com/ir3vFwk.png" width=100px>
<br>
<h1>Alertpix.py</h1>

![OS](https://img.shields.io/badge/OS-linux%20%7C%20windows-blue??style=flat&logo=Linux&logoColor=b0c0c0&labelColor=363D44)
<br>
<i>Uma biblioteca python para facilitar o uso da API do AlertPix</i>
<br>

<h1>Instalação</h1>

Instale usando o pip:
```
pip install alertpix
```

<h1>Exemplos</h1>

<h2>Criar um pagamento </h2>
```python
import alertpix, time

pagamento = alertpix.Charge(link="apenasumnerdd", amount=100, comment="teste", username="fulano")

pagamento.create()
print("BrCode para o pagamento: ", pagamento.brcode.code)

while True:
    time.sleep(1)
    if pagamento.check():
        print("Pagamento concluído")
        break
    else:
        print("Aguardando pagamento...")
  ```
