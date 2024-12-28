# DO1_Linux

## Part 1: OS o'rnatish

1. **Ubuntu versiyasi `cat /etc/issue` komandasi yordamida tekshirildi.**
    ```sh
    cat /etc/issue
    ```
    - Skrinshot: ![Part 1](part_1.png)


## Part 2: Foydalanuvchi yaratish

1. **O'rnatish jarayonida yaratilgan foydalanuvchidan tashqari yana bir foydalanuvchi yaratildi.**
    ```sh
    sudo adduser user_1
    sudo usermod -aG adm user_1
    ```
    - Skrinshot: ![adm ga qo'shildi](part_2.1.png)

2. **Yangi foydalanuvchi `cat /etc/passwd` komandasining natijasida ko'rsatilgan.**
    ```sh
    cat /etc/passwd
    ```
    - Skrinshot: ![Natija](part_2.png)


## Part 3: Tarmoq sozlamalarini o'rnatish

1. **Mashina nomi `user-1` deb o'rnatildi.**
    ```sh
    sudo hostnamectl set-hostname user_1
    ```
    - Skrinshot: ![Mashina nomi o'zgartirildi](part_3.1.png)

2. **Vaqt zonasi joriy joylashuvingizga mos ravishda sozlandi.**
    ```sh
    sudo timedatectl set-timezone Asia/Tashkent
    ```
    - Skrinshot: ![Vaqt zonasi sozlash](part_3.2.png)

3. **Tarmoq interfeyslari nomlari konsol komandasidan chiqarildi.**
    ```sh
    ip link
    ```
    - Skrinshot: ![Tarmoq interfeyslari nomlari](part_3.3.png)

4. **`lo` interfeysining mavjudligi tushuntirildi.**

    `lo` interfeysi - bu "loopback" interfeysi bo'lib, bu interfeys tarmoq qurilmasining o'zi bilan aloqa qilish uchun mo'ljallangan.

5. **Tarmoq qurilmasining ip manzili DHCP serverdan konsol komandasi yordamida olindi.**
    ```sh
    ip addr
    ```
    - Skrinshot: ![DHCP serverdan ip manzili](part_3.5.png)

6. **DHCP dekodlandi.**

    DHCP (Dynamic Host Configuration Protocol) - bu tarmoq qurilmalariga avtomatik ravishda IP manzillar va boshqa tarmoq sozlamalarini taqdim etish uchun ishlatiladigan protokol.

7. **Shlyuzning tashqi ip manzili (ip) va ichki ip manzili (gw) aniqlandi va ko'rsatildi.**
    ```sh
    ip route
    curl ifconfig.me
    ```
    - Skrinshot: ![Shlyuz ip manzillari](part_3.6.png)

8. **Statik (DHCP serverdan olinmagan) ip, gw, dns sozlamalari o'rnatildi.**
    ```sh
    sudo nano /etc/netplan/01-netcfg.yaml
    sudo netplan apply
    ```
    - Skrinshot: ![Statik tarmoq sozlamalari](part_3.7.png)

9. **1.1.1.1 va ya.ru masofaviy hostlari muvaffaqiyatli ping qilindi va komanda natijasi hisobotga qo'shildi. Komanda natijasida "0% packet loss" iborasi ko'rsatilgan.**
    ```sh
    ping -c 4 1.1.1.1
    ping -c 4 ya.ru
    ```
    - Skrinshot: ![Ping natijasi](part_3.8.png)


## Part 4: OS yangilash

1. **Tizim paketlari eng so'nggi versiyaga yangilandi.**
    ```sh
    sudo apt update
    sudo apt install -y
    sudo apt dist-upgrade -y
    sudo apt autoremove -y
    sudo apt update
    ```
    - Skrinshot: ![sudo apt update && sudo apt upgrade -y](part_4.png)
  

## Part 5: Sudo komandasi ishlatilishi

1. **Part 2 da yaratilgan foydalanuvchi orqali OS hostname o'zgartirildi.**
    ```sh
    sudo usermod -aG sudo user_1
    sudo hostnamectl set-hostname xamid
    hostnamectl
    ```
    - Skrinshot: ![Hostname o'zgartirilgan](part_5.png)


## Part 6: Vaqt xizmatini o'rnatish va sozlash

1. **Avtomatik vaqt sinxronizatsiyasi xizmati o'rnatildi va sozlandi.**
    ```sh
    sudo apt update
    sudo apt istall systemd-timesynd -y

    sudo systemctl enable systemd-timesyncd
    sudo systemctl start systemd-timesyncd

    sudo systemctl status systemd-timesyncd
    ```

2. **Hozirgi joylashuvingiz bo'yicha vaqt zonasi vaqti chiqarildi.**
    ```sh
    sudo timedatectl set-timezone Asia/Tashkent
    timedatectl
    ```
    - Skrinshot: ![Vaqt zonasi vaqti](part_6.png)

3. **`timedatectl show` komandasi natijasi.**
    ```sh
    timedatectl show
    ```
    - Skrinshot: ![timedatectl show](part_6.1.png)


## Part 7: 

## Matn muharrirlarini o'rnatish va ishlatish

1. **VIM, NANO, va MCEDIT matn muharrirlari o'rnatildi.**
    ```sh
    sudo apt update
    sudo apt install vim nano joe -y
    ```

2. **Har bir muharrirda test_X.txt fayli yaratildi va nik kiritildi, keyin fayl saqlandi.**
    - VIM muharririda fayl:
      - Komanda: vim test_emperora.txt
      - Insert rejimiga o'tish: i
      - Nickname yozish: emperora
      - Command rejimiga qaytish: Esc
      - Faylni saqlash va chiqish: :wq
    - Skrinshot: ![emperora fayli](part_7.1_vim.png)

    - NANO muharririda fayl:
      - Komanda: nano test_emperora.txt
      - Matnni yozish: emperora
      - Saqlash va chiqish: Ctrl+O, Enter, Ctrl+X
    - Skrinshot: ![emperora fayli](part_7.4_nano.png)

    - MCEDIT muharririda fayl:
      - Komanda: mcedit test_empeora.txt
      - Matnni yozish: emperora
      - Saqlash va chiqish: F2, F10
    - Skrinshot: ![emperora fayli](part_7.7_mcedit.png)

3. **Har bir muharrirda faylni tahrirlash va "21 School 21" qatoriga almashtirish, keyin faylni saqlamasdan chiqish amalga oshirildi.**
    - VIM muharririda fayl:
      - Komanda: vim test_emperora.txt
      - Insert rejimiga o'tish: i
      - Matnni o'zgartirish: emperora dan 21 School 21 ga o'zgartirish.
      - Command rejimiga qaytish: Esc
      - Saqlamasdan chiqish: :q!
    - Skrinshot: ![emperora fayli](part_7.2_vim.png)

    - NANO muharririda fayl:
      - Komanda: nano test_emperora.txt
      - Matnni o'zgartirish: emperora dan 21 School 21 ga o'zgartirish.
      - Saqlamasdan chiqish: Ctrl+X, N
    - Skrinshot: ![emperora tahrirlangan](part_7.6_nano.png)

    - MCEDIT muharririda fayl:
      - Komanda: mcedit test_emperora.txt
      - Matnni o'zgartirish: emperora dan 21 School 21 ga o'zgartirish.
      - Saqlamasdan chiqish: F10, N
      - O'zgartirilgan matn: 21 School 21
    - Skrinshot: ![emperora tahrirlangan](part_7.8_mcedit.png)

4. **Har bir muharrirda fayl ichidagi so'zlarni qidirish va almashtirish funksiyalari o'rganildi va amalga oshirildi.**
    - VIM muharririda qidirish va almashtirish:
      - Komanda: vim test_emperora.txt
      - Qidirish rejimi: /emperora
      - Almashtirish: :%s/emperora/xamidullaxon/g
      - Screenshot:
      - Qidirilgan so'z: emperora
      - Almashtirilgan so'z: xamidullaxon
    - Skrinshot: ![VIM so'z almashtirish](part_7.3_vim.png)

    - NANO muharririda qidirish va almashtirish:
      - Komanda: nano test_emperora.txt
      - Qidirish: Ctrl+W, your_nickname
      - Almashtirish: Ctrl+\, emperora, enter, xamidullaxon
      - Qidirilgan so'z: emperora
      - Almashtirilgan so'z: xamidullaxon
    - Skrinshot: ![NANO so'z almashtirish](part_7.5_nano.png)

    - MCEDIT muharririda qidirish va almashtirish:
      - Komanda: mcedit test_emperora.txt
      - Qidirish: F7, emperora, Enter
      - Almashtirish: F4, emperora, xamidullaxon, Enter
      - Qidirilgan so'z: emperora
      - Almashtirilgan so'z: xamidullaxon
    - Skrinshot: ![MCEDIT so'z almashtirish](part_7.9_mcedit.png)



