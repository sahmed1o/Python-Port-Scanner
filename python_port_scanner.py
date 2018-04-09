import socket
from threading import Thread

print('==========================================')
print('   ÛÛÛÛÛÛÛÛÛ   ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛ    ')
print('  ÛÛÛ°°°°°ÛÛÛ ÛÛÛ°°°°°ÛÛÛ°°ÛÛÛ')
print(' ÛÛÛ     °°° °ÛÛÛ    °°°  °ÛÛÛ       ')
print('°ÛÛÛ         °°ÛÛÛÛÛÛÛÛÛ  °ÛÛÛ       ')
print('°ÛÛÛ          °°°°°°°°ÛÛÛ °ÛÛÛ       ')
print('°°ÛÛÛ     ÛÛÛ ÛÛÛ    °ÛÛÛ °ÛÛÛ      Û')
print(' °°ÛÛÛÛÛÛÛÛÛ °°ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛÛÛÛÛÛÛ')
print('  °°°°°°°°°   °°°°°°°°°  °°°°°°°°°°°')
print('==========================================')

# check what type of port it is
def check_port_type(port, is_open):
    # is_open is a flag that checks whether the port is opened or closed
    if(is_open == 'o'):
        port_status = "  OPEN     "
    else:
        port_status = "  CLOSED   "

    # designation for ports. These are the ports most often attacked, others can be included here as well.
    if(port == 25):
        print('%4s' % port, port_status + "SMTP (Simple Mail Transfer Protocol)")
    elif (port == 21):
        print('%4s' % port, port_status + "FTP (File Transfer Protocol)")
    elif (port == 22):
        print('%4s' % port, port_status + "SSH (Secure Shell)")
    elif (port == 23):
        print('%4s' % port, port_status + "Telnet")
    elif (port == 53):
        print('%4s' % port, port_status + "DNS (Domain Name System)")
    elif (port == 80):
        print('%4s' % port, port_status + "Hypertext Transfer Protocol (HTTP)")
    elif (port == 443):
        print('%4s' % port, port_status + "HTTP (Hypertext Transport Protocol) and HTTPS (HTTP over SSL)")
    elif (port == 110):
        print('%4s' % port, port_status + "POP3 (Post Office Protocol version 3)")
    elif (port == 119):
        print('%4s' % port, port_status + "Network News Transfer Protocol (NNTP)")
    elif (port == 135):
        print('%4s' % port, port_status + "Windows RPC")
    elif (port == 137) or (port == 138) or (port == 139):
        print('%4s' % port, port_status + "Windows NetBIOS over TCP/IP")
    elif (port == 143):
        print('%4s' % port, port_status + "Internet Message Access Protocol (IMAP)")
    elif (port == 465):
        print('%4s' % port, port_status + "URL Rendezvous Directory for SSM (Cisco protocol)")
    elif (port == 1433) or (port == 1434):
        print('%4s' % port, port_status + "Microsoft SQL Server")
    else:
        print('%4s' % port, port_status + "Unknown")
        pass


# port scan function, checks if port is open by connecting to it,
# if connection is established, set appropriate flag 'o'
# show_clport_opt is a flag to indicate wether the user wishes to show closed ports
def pScan(port, ip_target, show_clport_opt):
    try:
        # create a socket and connect to port, socket.SOCK_STREAM makes tcp connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con = s.connect_ex((ip_target, port))
        # if connection is estabilished (con==0), then port is open, else closed
        if con == 0:
            check_port_type(port, 'o')
        else:
            # if user inputted 'y' (yes) to show closed port, then check port type and print it
            if(show_clport_opt == 'y'):
                check_port_type(port, 'c')
        # port scan complete, close connection
        con.close()
    except:
        pass


# this function is outputted after scan is done
def final_message():
    print('==========================================')
    print("Done Scanning.")


# This function is used to speed up the process of portscanning by splitting the scan into multiple threads.
# Since the we scan all the ports on a seperate thread at once, the process is alot faster.
# ip_target is the target we the program is scanning, while show_clport_opt is the flag for users to decide
# if they want to see closed ports.
def start_scan(ip_target, show_clport_opt,  min_port, max_port):
    # scan ports 1 to 500.
    # Create a separate thread to scan each port. Each thread scans an assigned port.
    """If you get a "RuntimeError: can't start new thread", then you are running to many threads, consider
        lowering the min and max."""
    min_p = int(min_port)
    max_p = int(max_port)
    for x in range(min_p, max_p):
        t = Thread(target=pScan, args=(x, ip_target, show_clport_opt))
        num_thrd.append(t)

    # Tell all threads to start scanning
    for i in range(0, len(num_thrd)):
        num_thrd[i].start()

    # Lock the code. Final message is printed after all threads are finished scanning.
    for i in range(0, len(num_thrd)):
        num_thrd[i].join()

    # All threads finished, print final message to indicate the program is done scanning.
    final_message()


# starting function, this is the start of the program. it prints a message and then asks for input.
# The inputs are the target the program will scan, and whether the user wants to see closed ports.
# After the inputs are typed in, the function passes these inputs into another function and starts the port scanning.
def program_start():
    print('Running Port Scanner...')
    ip_target = input("Target Link/IP: ")
    show_clport_opt = input("Show Closed ports? (y/n) ")
    min_port = input("Pick Min Range of Port: ")
    max_port = input("Pick Max Range of Port: ")
    print('----------------------------------------')
    print('PORT | STATE |  SERVICE')
    print('----------------------------------------')
    start_scan(ip_target, show_clport_opt, min_port, max_port)


# An array thread is used to simultaneously scan all ports at once
num_thrd = []

# This function call starts the program
program_start()

# Press any key to quit the program...
input("Press any key to quit the program...")
