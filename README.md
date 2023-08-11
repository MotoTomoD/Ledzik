#Ledzik

#####Autorzy: Karol Łukasik, Tomasz Danis


###Opis projektu:

Projekt ma za zadanie sterowanie diodą podłączoną do RPi, poprzez wciskanie przycisku na innym RPi. Wciśnięcie przycisku powoduje przesłanie do serwera informacji o tym, że dioda powinna się włączyć/wyłączyć. Dane przesyłane są przez kabel Ethernet. Komunikacja zachodzi przy wykorzystaniu framework'a gRPC. Klient wykorzystuje do konfiguracji plik konfiguracyjny yaml.

###Konfiguracja programu:

#### 1. Środowisko wirtualne python

Utworzenie wirtualnego środowiska python
>python -m venv nazwakatalogu

Aktywowanie utworzonego środowiska

>source ./nazwakatalogu/bin/activate

pobranie wymaganych modułów
>pip install -r requirements.txt

#### 2. Wprowadzenie **adresu serwera** ipv4 oraz **portu** w pliku konfiguracyjnym config.yaml



#### 3. Instalacja oraz konfigurowanie **supervisor** w celu automatycznego włączania klienta na raspberry pi

W pliku **`start.sh`** należy ****zmienić ścieżke** do katalogu wirtualnego środowiska** na taką jak ustalono wcześniej **i wybrać plik który ma się automatycznie uruchamiać** (serwer lub klient)

Plik konfiguracyjny w katalogu /etc/supervisor/conf.d/ należy skonfigurować tak żeby uruchamiał **`start.sh`, ustawiał użytkownika i uruchamiał autostart**. Przykładowa konfiguracja:
>[program:LedSwitch_server]
command=/home/pi/Ledzik/start.sh
directory=/home/pi/Ledzik/
startsecs = 0
autostart=true
autorestart=true
stderr_logfile=test.err.log
stdout_logfile=test.out.log
user=pi

___ 
Całą konfigurację należy przeprowadzić na obydwu urządzeniach - dla serwera i dla klienta.

Do **serwera** należy podłączyć **diodę** do **GPIO16**
Do **klienta** należy podłączyć **przycisk** do **GPIO4**


###Wykorzystane narzędzia i ich przeznaczenie:
Visual Studio Code - tworzenie programów potrzebnych do funkcjonowania programu
GRPC - komunikacja pomiędzy dwoma oddzielnymi programami - serwerem i klientem
Pydantic YAML - konfiguracja pomiędzy plikami
SSH - połączenie raspberry 
Supervisor - automatyczne włączenie programu w pythonie na Raspberry Pi

###Wykorzystane materiały:
Raspberry Pi 4B - wykorzystane jako klient
Raspberry Pi 3B+ - wykorzystane jako serwer
kabel Ethernet-Ethernet - wykorzystane do podłączenia Raspberry Pi z PC
Płytka stykowa - wykorzystana do podłączenia guzika i diody z rezystorem
Guzik, rezystor 100 Ω, kable męsko-żeńskie, dioda

###Kod źródłowy: https://github.com/MotoTomoD/Ledzik.git



 




