# parpl
Passive ARP learning tool without sending probes

Learn MACs for IP addresses without sending ARP requests, by simply sniffing ARP frames for their sender IPs and MACs.

Used as an attack aid for a scenario where NAC blocked ARP requests and responses of non-whitelisted devices in network, and the information had to be gathered from broadcasts.


## Note:
Probably won't improve much, this was a quick-and-dirty script written in a hurry.
Beautified it to some extent to provide basic usability.


## Requirements
scapy

```pip install scapy```
or 
```sudo pip install scapy```

## Usage

Clone the repo or download the python script, use with root privileges
```
sudo python3 parpl.py <output base filename>
```


## Outputs:

stdout, also will save into: 
```
<base filename>_raw_results.txt

#for adding and removing static entries
<base filename>_arp_add.sh 
<base filename>_arp_del.sh 
```



## TODO:
1 - Better usability
  - More options
  - Colorization
 
2 - Better stability
 
3 - More testing


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## Disclaimer:

Use at your own discretion.

While this tool alone will not cause any damage, attacking systems/networks without prior mutual consent is illegal. It is the end user’s responsibility to obey all applicable local, state and federal laws. I assume no liability and I am not responsible for any misuse or damage caused by this.
