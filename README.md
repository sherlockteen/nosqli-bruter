# NoSQL Injection Brute Forcer

Red Team Tool для автоматизированного подбора пароля через NoSQL Injection (MongoDB-style `$regex` payloads).

## Установка

```bash
git clone https://github.com/sherlockteen/nosqli-bruter
cd nosqli-bruter
pip3 install -r requirements.txt --break-system-packages
python3 setup.py install
