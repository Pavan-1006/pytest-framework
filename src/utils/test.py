import telenetlib

tn=telenetlib.Telnet("192.168.0.1",23)

tn.write(b"Hello\n")



