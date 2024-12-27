# Hisobot

## Part 1: OS o'rnatish

1. **Ubuntu 20.04 Server LTS VirtualBox orqali o'rnatildi. **
2. **Ubuntu versiyasi `cat /etc/issue` komandasi yordamida tekshirildi.**
    - Skrinshot: ![Part 1](part_1.png)


## Part 2: Foydalanuvchi yaratish

1. **O'rnatish jarayonida yaratilgan foydalanuvchidan tashqari yana bir foydalanuvchi yaratildi.**
    - sudo adduser user_1
    - sudo usermod -aG adm user_1
    - Foydalanuvchi `adm` guruhiga qo'shildi.
    - Skrinshot: ![adm ga qo'shildi](part_2.1.png)

2. **Yangi foydalanuvchi `cat /etc/passwd` komandasining natijasida ko'rsatilgan.**
    - Skrinshot: ![Natija](part_2.png)


## Part 3: Tarmoq sozlamalarini o'rnatish

1. **Mashina nomi `user-1` deb o'rnatildi.**
    - sudo hostnamectl set-hostname user_1
    - Skrinshot: ![Mashina nomi o'zgartirildi](part_3.1.png)

2. **Vaqt zonasi joriy joylashuvingizga mos ravishda sozlandi.**
    - sudo timedatectl set-timezone Asia/Tashkent
    - Skrinshot: ![Vaqt zonasi sozlash](part_3.2.png)

3. **Tarmoq interfeyslari nomlari konsol komandasidan chiqarildi.**
    - ip link
    - Skrinshot: ![Tarmoq interfeyslari nomlari](part_3.3.png)

4. **`lo` interfeysining mavjudligi tushuntirildi.**

    `lo` interfeysi - bu "loopback" interfeysi bo'lib, bu interfeys tarmoq qurilmasining o'zi bilan aloqa qilish uchun mo'ljallangan.

5. **Tarmoq qurilmasining ip manzili DHCP serverdan konsol komandasi yordamida olindi.**
    - ip addr
    - Skrinshot: ![DHCP serverdan ip manzili](part_3.5.png)

6. **DHCP dekodlandi.**

    DHCP (Dynamic Host Configuration Protocol) - bu tarmoq qurilmalariga avtomatik ravishda IP manzillar va boshqa tarmoq sozlamalarini taqdim etish uchun ishlatiladigan protokol.

7. **Shlyuzning tashqi ip manzili (ip) va ichki ip manzili (gw) aniqlandi va ko'rsatildi.**
    - ip route
    - curl ifconfig.me
    - Skrinshot: ![Shlyuz ip manzillari](part_3.6.png)

8. **Statik (DHCP serverdan olinmagan) ip, gw, dns sozlamalari o'rnatildi.**
    - sudo nano /etc/netplan/01-netcfg.yaml
    - sudo netplan apply
    - Skrinshot: ![Statik tarmoq sozlamalari](part_3.7.png)

9. **1.1.1.1 va ya.ru masofaviy hostlari muvaffaqiyatli ping qilindi va komanda natijasi hisobotga qo'shildi. Komanda natijasida "0% packet loss" iborasi ko'rsatilgan.**
    - ping -c 4 1.1.1.1
    - ping -c 4 ya.ru
    - Skrinshot: ![Ping natijasi](part_3.8.png)


## Part 4: OS yangilash

1. **Tizim paketlari eng so'nggi versiyaga yangilandi.**
    - sudo apt update
    - sudo apt install -y
    - sudo apt dist-upgrade -y
    - sudo apt autoremove -y
    - sudo apt update
    - Skrinshot: ![sudo apt update && sudo apt upgrade -y](part_4.png)
  

## Part 5: Sudo komandasi ishlatilishi

1. **Part 2 da yaratilgan foydalanuvchi orqali OS hostname o'zgartirildi.**
      ```sh
      sudo usermod -aG sudo user_1
      sudo hostnamectl set-hostname xamid
      hostnamectl
      ```
    - Skrinshot: ![Hostname o'zgartirilgan](part_5.png)


