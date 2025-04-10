# raspberrypi_tailscale_statusd
Check the status of tailscale connection on a led of a raspberry pi

`Green LED on ` - tailscale is online \
`Green LED off` - tailscale is offline (not connected/error...)

# Requirements:

- python installed
- tailscale set-up with magic DNS and `raspberrypi` set as the hostname
- check with `tailscale status`
  ```
  > tailscale status
    {IPv4}  raspberrypi          egirlcatnip@ linux   -
            ^hostname                                 ^not "offline"
  ```
  
- `tailscale_statusd` marked as executable (`chmod +x tailscale_statusd`)
- `tailscale_statusd` in path
- `tailscale_statusd.service` in `/etc/systemd/system/{here}` 

# Setup
- `sudo tailscale up` 
- `sudo systemctl daemon-reload`
- `sudo systemctl enable tailscale_statusd`
- `sudo systemctl start tailscale_statusd`
- `sudo systemctl status tailscale_statusd` (check status)
- - should be `Active: active (running)`



![image](https://github.com/user-attachments/assets/6e478f8a-d05f-4487-b4b6-beeccc7391de)

![image](https://github.com/user-attachments/assets/5d51c696-629d-4f0f-9e77-75b5bfde0a20)
