## Part 1: `ipcalc` tool

### 1.1 Networking and Masks
1. **network address of `192.176.38.54/13`**
    ```sh
    ipcal 192.167.38.54/13
    ```
    - **Address:**        `192.167.38.54`          11000000.10100 111.00100110.00110110
    - **Netmask:**        `255.248.0.0 = 13`       11111111.11111 000.00000000.00000000 
    - **Wildcard:**       `0.7.255.255`            00000000.00000 111.11111111.11111111 
    - **Network:**        `192.160.0.0/13`         11000000.10100 000.00000000.00000000
    - **HostMin:**        `192.160.0.1`            11000000.10100 000.00000000.00000001
    - **HostMax:**        `192.167.255.254`        11000000.10100 111.11111111.11111110
    - **Broadcast:**      `192.167.255.255`        11000000.10100 111.11111111.11111111
    - **Hosts/Net:**      `524286`                 Class C

2. **conversion of the mask `255.255.255.0`**
    - **Binary:** `11111111.11111111.11111111.00000000`
    - **Prefix:** `/24` (bu 24 ta 1 bitdan iborat binar shakl)
3. **`/15` to normal and binary**
    - **Normal** `255.254.0.0` 
    - **Binary** `11111111.11111110.00000000.00000000`
4. **`11111111.11111111.11111111.11110000` to normal and prefix**
    - **Normal:** `255.255.255.240`
    - **Prefiks:** `/28` (bu 28 ta 1 bitdan iborat binar shakl)

5. **minimum and maximum host in 12.167.38.4**
    ```sh
    ipcalc 12.167.38.4/8
    ```
    - **Address:** `12.167.38.4` 00001100. 10100111.00100110.00000100
    - **Netmask:** `255.0.0.0 = 8` 11111111. 00000000.00000000.00000000
    - **Wildcard:** `0.255.255.255`00000000. 11111111.11111111.11111111
    - **Network:** `12.0.0.0/8` 00001100. 00000000.00000000.00000000
    - **HostMin:** `12.0.0.1` 00001100. 00000000.00000000.00000001
    - **HostMax:** `12.255.255.254` 00001100. 11111111.11111111.11111110
    - **Broadcast:** `12.255.255.255` 00001100. 11111111.11111111.11111111
    - **Hosts/Net:** `16777214` Class A

6. **`11111111.11111111.00000000.00000000 (/16)`**
    ```sh
    ipcalc 12.167.38.4/16
    ```
    - **Address:** `12.167.38.4` 00001100.10100111. 00100110.00000100
    - **Netmask:** `255.0.0.0 = 16` 11111111.11111111. 00000000.00000000
    - **Wildcard:** `0.0.255.255`00000000.00000000. 11111111.11111111
    - **Network:** `12.167.0.0/16` 00001100.10100111. 00000000.00000000
    - **HostMin:** `12.167.0.1` 00001100.10100111. 00000000.00000001
    - **HostMax:** `12.167.255.254` 00001100.10100111. 11111111.11111110
    - **Broadcast:** `12.167.255.255` 00001100.10100111. 11111111.11111111
    - **Hosts/Net:** `65534` Class A

7. **`255.255.254.0 (/23)`**
    ```sh
    ipcalc 12.167.38.4/23
    ```
    - **Address:** `12.167.38.4` 00001100.10100111.0010011 0.00000100
    - **Netmask:** `255.0.0.0 = 23` 11111111.11111111.1111111 0.00000000
    - **Wildcard:** `0.0.1.255` 00000000.00000000.0000000 1.1111111
    - **Network:** `12.167.38.0/23` 00001100.10100111.0010011 0.00000000
    - **HostMin:** `12.167.38.1` 00001100.10100111.0010011 0.00000001
    - **HostMax:** `12.167.39.254` 00001100.10100111.0010011 1.11111110
    - **Broadcast:** `12.167.39.255` 00001100.10100111.0010011 1.11111111
    - **Hosts/Net:** `510` Class A

8. **minimum and maximum host in 12.167.38.4**
    ```sh
    ipcalc 12.167.38.4/4
    ```
    - **Address:** `12.167.38.4` 0000 1100.10100111.00100110.00000100
    - **Netmask:** `240.0.0.0 = 4` 1111 0000.00000000.00000000.00000000 
    - **Wildcard:** `15.255.255.255`0000 1111.11111111.11111111.11111111
    - **Network:** `0.0.0.0/4` 0000 0000.00000000.00000000.00000000
    - **HostMin:** `0.0.0.1` 0000 0000.00000000.00000000.00000001
    - **HostMax:** `15.255.255.254` 0000 1111.11111111.11111111.11111110
    - **Broadcast:** `15.255.255.255` 0000 1111.11111111.11111111.11111111 
    - **Hosts/Net:** `268435454` Class A, In Part Private Internet    


### 1.2 localhost
1. **localhostdagi ilovaga kirish mumkin bo'lgan IP manzillar:**
    - **194.34.23.100:** (localhost emas) 
    - **127.0.0.2:** (localhost) 
    - **127.1.0.1:** (localhost) 
    - **128.0.0.1:** (localhost emas)


### 1.3 Network ranges and segments

1. **Public IPs:**
    - 134.43.0.2
    - 172.0.2.1
    - 192.172.0.1
    - 172.68.0.2
    - 192.169.168.1

2. **Private IPs:**
    - 10.0.0.45
    - 192.168.4.2
    - 172.20.250.4
    - 172.16.255.255
    - 10.10.10.10

3. **IP addresses are possible for `10.10.0.0/18` network:**
    - `10.10.0.2`
    - `10.10.10.10`
    

## Part 2: Static routing between two machines
1. **`ip` command**
    ```sh
    ip a
    ```
    - screenshot ![ws1](photos/ws1_new.png)
    - screenshot ![ws2](photos/ws2_new.png)

2.  **Added `192.168.100.10/16` and `172.24.116.8/12`**
    ```sh
    sudo nano /etc/netplan/00-installer-config.yaml
    ```
    - screenshots ![ws2.1](photos/ws3.1.png)
    - screenshots ![ws2.2](photos/ws3.2.png)
3.  **`netplan apply` restarted the network service**
    ```sh
    sudo netplan apply
    ```
    - screenshots ![ws3.1](photos/ws2.1.png)
    - screenshots ![ws3.2](photos/ws2.2.png)
    
### 2.1 Adding a static route manually
1. **`ip r add` command**
    ```sh
    sudo ip r add 172.16.0.0/12 via 192.168.100.1 dev enp0s8
    ping 172.24.116.8
    ```
    - screenshots ![ws](photos/ws1.5.png)
    ```sh
    sudo ip r add 192.168.0.0/16 via 172.24.116.1 dev enp0s9
    ping 192.168.100.10
    ```
    - screenshots ![ws](photos/ws2.5.png)    


### 2.2 Adding a static route with saving
1. **Statik marshrut qo'shish**
    - from ws1 to ws2:
    ```sh
    sudo ip route add 172.24.116.0/24 dev enp0s9
    ```
    - screenshots ![yaml](photos/ws3.1.png)
    ```sh
    ping 172.24.116.8
    ```
    - screenshot ![ping_ws1](photos/ws4.1.png) 
    
    - from ws2 to ws1:
    ```sh
    sudo ip route add 192.168.100.0/24 dev enp0s8
    ```
    - screenshots ![yaml](photos/ws3.2.png)
    ```sh
    ping 192.168.100.10
    ```    
    - screenshot ![ping_ws2](photos/ws4.2.png)
    

## Part 3: iperf3 utility
### **3.1 Connection speed**

1. **8 Mbps to MB/s (Megabits per second to Megabytes per second):**
    - ***1 byte = 8 bits***
    - 8 Mbps ÷ 8 = 1 MB/s
    - `Answer`: 8 Mbps = 1 MB/s

2. **100 MB/s to Kbps (Megabytes per second to Kilobits per second):**
    - ***1 byte = 8 bits and 1 MB = 1024 * 1024 bytes***
    - 100 MB/s * 8 * 1024 = 819,200 Kbps
    - `Answer:` 100 MB/s = 819,200 Kbps

3. **1 Gbps to Mbps (Gigabits per second to Megabits per second):**
    - ***1 Gbps = 1000 Mbps***
    - `Answer:` 1 Gbps = 1000 Mbps

### **3.2 iperf3 utility**
    ```sh
    sudo apt update
    sudo apt install iperf3
    ```
1. **`ws1` da server ishga tushirish**
    ```sh
    iperf -s
    ```
    - `ws2` clientni ishga tushirish
    ```sh
    iperf3 -c 192.168.100.10
    ```
    - screenshot: ![ws2_iperf3](photos/ws2_i.png)

2. **`ws2` da server ishga tushirish**
    ```sh
    iperf -s
    ```
    - `ws1` clientni ishga tushirish
    ```sh
    iperf3 -c 172.24.116.8
    ```
    - screenshot: ![ws1_iperf3](photos/ws1_i.png)
    





