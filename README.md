# TeamBang9
## 안녕하세요 TeamBang9 입니다. 

<details>
<summary>### Dependencies</summary>

```
* docker >= 19.03.12
* kubernetes >= 1.22.4
* Nvidia GPU Driver >= 440.82


### 설치 및 테스트 완료 OS
* Linux
    * CentOS == 7.8.2003
    * Oracle Linux == 8.5

## Install Guide
```shell
sudo systemctl stop firewalld
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=disabled$/' /etc/selinux/config
sudo sed -i 's/^SELINUX=permissive/SELINUX=disabled$/' /etc/selinux/config
sudo swapoff -a
sudo sed -ri '/\sswap\s/s/^#?/#/' /etc/fstab
```
</details>
