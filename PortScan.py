import socket
import datetime

target = input("Enter a host to scan: ")

f = open(target, "w")
f.write(">> Port scan of " + str(target) + " <<\n\n")

print("-" * 60)
print("Now scanning ports 1 - 1025 on the target host.")
print("Please wait while the results of your scan are collected.")
print("This may take several minutes.")
print("-" * 60)

start_time = datetime.datetime.now()
f.write("Time scan started: " + str(start_time) + "\n\n")

def pscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.close()
        return True
    except ConnectionRefusedError:
        f.write("Port " + str(x) + " - Host refused connection.\n")
    except TimeoutError:
        print("Host did not respond.")
        f.write("Connection timed out. \nHost is not available.\n")
        print("The scan is ending early.")
        print("Please try again or pick a different host to scan.")
        end_time = datetime.datetime.now()
        f.write("\nTime scan ended: " + str(end_time) + "\n")
        total_time = end_time - start_time
        print("-" * 60)
        print("Time elapsed: " + str(total_time))
        f.write("Duration of scan: " + str(total_time) + "\n")
        print("-" * 60)
        print("The full results of your scan have been collected in a")
        print("file named '" + target + "' for review.")
        f.close()
        exit()
    except OSError[WindowsError(10065)]:
        f.write("Host unreachable.")
    except socket.gaierror:
        f.write("Connection Reset Error")
    except socket.error:
        f.write("Hostname could not be resolved.")

for x in range(1, 1026):
    if pscan(x):
        result = ">> Port " + str(x) + " is OPEN.\n"
        f.write(result)
        print('Port',x,'is open')

end_time = datetime.datetime.now()
f.write("\nTime scan ended: " + str(end_time) + "\n")
total_time = end_time - start_time
print("-" * 60)
print("Time elapsed: " + str(total_time))
f.write("Duration of scan: " + str(total_time) +"\n")
f.close()

print("-" * 60)
print("The full results of your scan have been collected in a")
print("file named '" + target + "' for review.")


#program that should test the given host and it should generate a list of
#all TCP Open ports within range of 1 to 1025. Use only standard Python’s “socket” library.
#1. On execution of program system should prompt “Enter a host to scan”. User will provide a host name
#2. System should look for all the ports between the range of 1 to 1025
#3. If the Ports is open it should create a file and add an entry for port number
#4. In case of any exception for instance “host is not available”, “host name could not be resolved” or due to any other error you need to write that exception into same file
#5. You also need to record starting and ending date and time at the beginning and ending of file accordingly. It should also show the total time it took in port scanning process