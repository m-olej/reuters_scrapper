# Usage

> Po pierwsz dziękuję bardzo za pomoc ! <3

## Sklonuj repo

```sh
git clone https://github.com/m-olej/reuters_scrapper.git
```

## Stwórz venva

```sh
python -m venv .venv
```

## aktywuj venva

Linux

```sh
source .venv/bin/activate
```

Windows

```
.venv/Scripts/Activate.ps1
```

## Zainstaluj zależności

```sh
pip install -r requirements.txt
playwright install
```

# Scrapowanie:

> (ich strona się aktualizuje dosyć często można pare razy dziennie, ale lepiej nie za często, bo będzie dużo duplikatów)

póki działa za pomocą skryptu

```sh
python pywright.py
```

przestanie działać:
otwórz reuters.com w przeglądarce

Włączyć dev tools

```
ctrl + shift + j (chrome)
LUB
ctrl + shift + c (firefox)
```

w inspektorze prawy przycisk -> edit as HTML

ctrl + a (zaznacz wszystko) i skopiuj do pliku .html w folderze html

## po uzbieraniu plików .html

```sh
python scrapper.py
```

powinno wyprintować zebrane artykuły i ich ilość

końcowo skopiuj zawartość pliku do "Beka_z_reuters" na drivie CyberOdpornych z opcjonalnum podpisem

Każdemu kto przekopiuje i się podpiszę stawiam napój własnego wyboru !

Dziękuję jeszcze raz <3
