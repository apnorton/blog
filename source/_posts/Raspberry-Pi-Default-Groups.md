title: Raspberry Pi Default Groups
date: 2017-11-25 13:54:28
tags:
  - computer-science 
  - general-computing
  - hardware
categories:
  - electronics
  - raspberry-pi
---


In setting up my Raspberry Pi for a home fileshare, I noticed the `pi` user is a part of several default groups.  These are:

```
pi adm dialout cdrom sudo audio video plugdev games users input netdev gpio i2c spi
```

(I'm using the 2017-09-07 image of Raspbian Stretch Lite.)

This looked like a lot of groups to me!  To make sure my new user only has the minimum permissions needed, let's look at the what each group is and why it's there.

<!-- more -->

## Group Descriptions

| Name | Notes |
| :- | :- |
| pi | User-specific group.  A group is automatically created for each new user; you can ignore this. |
| adm | Allows access to log files in `/var/log` and using `xconsole` |
| dialout | Allows access to serial ports/modem reconfiguration, etc. |
| cdrom | Uncreatively, this group enables access to optical drives. |
| sudo | Enables `sudo` access for the user. |
| audio | Allows access to audio devices like microphones and soundcards |
| video | Allows graphics card/webcam access. |
| plugdev | Enables access to external storage devices |
| games | I'm unsure of this.  No files belong to this group by default, and I cannot find references to it online. |
| users | Appears to be a Pi-specific group enabling access to `/opt/vc/src/hello_pi/` directory and contained files. |
| input | Appears to give access to the `/dev/input/mice` folder and nothing else. |
| netdev | Enables access to network interfaces |
| gpio | Pi-specific group for GPIO pin access. |
| i2c | Similar to the above, but for I2C access. Generated after installing `i2c-tools`. |
| spi | Similar to the above, but for the SPI bus. | 

So, based on my application (and future use of the Pi), I'm not adding the `cdrom`, `games`, and `users` groups to my new user.

## Helpful Resources
The above descriptions were sourced based on the following:

  - [SystemGroups - Debian Wiki][systemgroups]
  - [Privileges - Ubuntu Wiki][privileges]
  - Molloy, Derek.  *Exploring Raspberry Pi: Interfacing to the Real World with Embedded Linux.* [Page 270][page270]. 
  - [I2C group discussion on Raspberry Pi forums][i2cdiscussion] 

[systemgroups]:https://wiki.debian.org/SystemGroups
[i2cdiscussion]:https://www.raspberrypi.org/forums/viewtopic.php?p=158107#p158107
[privileges]:https://wiki.ubuntu.com/Security/Privileges 
[page270]: https://books.google.com/books?id=ro0gCwAAQBAJ&pg=PA270&lpg=PA270&source=bl&ots=0T50hVUvy5&sig=6n_Hi0U2rCyu7pvx5LUqXJfDhbE&hl=en&sa=X&ved=0ahUKEwjG6qGorNrXAhUNRN8KHcndBDQQ6AEISTAE#v=onepage&q&f=false

