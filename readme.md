# nunki.co Technical Test

## Theoretical Part
### Basics

> 1.How does a VPN work?

A VPN creates an encrypted connection between your personal computer and the VPN provider, from then it sends your request to the internet so your traffic and any personal information is safe.

> 2.What is a three-way handshake? Where is this protocol used?

A three-way handshake is used by TCP/IP to establish connections between devices.

> 3.What is a SSL certificate?

SSL (Secure Sockets Layer) provides security for communications between a client and a server, it is added to the web server so that web browsers can verify its identity.

> 4.What is a public/private key system? Where is it used?

A public/private key system is used to encrypt and decrypt data, it is used in SSH, SSL, GPG, and blockchain technology.

---
### Cyber-Sec 

> 1.Describe the mechanisms you would put in place (processes, tools, etc.): to check for vulnerabilities in Operating System, virtualization systems, middleware and the network layers both internally and externally.

(I used Google to find some tools, I'd dig in more if I had to use them in a real scenario)

To check for vulnerabilities in the operating system, I would use tools such as the open-source vulnerability scanner OpenVAS. 
This tool can be configured to perform regular scans of our systems and provide reports on any vulnerabilities it identifies. I would also use tools such as Tripwire to monitor changes to the operating system and alert us to any unauthorized changes.

To check for vulnerabilities in the virtualization systems, I would use tools such as Qualys Virtual Scanner Appliance to perform regular scans of our virtual environments. This tool can identify vulnerabilities in the hypervisor and the virtual machines running on it.

To check for vulnerabilities in the middleware and network layers, I would use a network vulnerability scanner such as Nessus. This tool can be configured to scan our network and identify vulnerabilities in the routers, switches, and other network devices.

> 2.How would you check for vulnerabilities at the application level?

I would use tools such as Acunetix to perform regular scans of our web applications. This tool can identify vulnerabilities such as SQL injection and cross-site scripting, as well as provide recommendations for remediation.

> 3.What security policies would you put in place to protect personal workstations (mac, pc’s)

I would put security policies such as requiring strong passwords, enabling two-factor authentication, and regularly patching and updating the operating system and other software. I would also provide training to employees on security best practices and encourage them to report any suspicious activity.

---
### Hacking

> Now imagine you’re a hacker and want to access client data from another start-up. The start-up hosts a password-protected web app at: app.example.com.
What would be your attack plan? You can go into detail for one proposed solution, and only mention others.

I would first try to identify any vulnerabilities in the web app itself. 

I'd use tools such as Burp Suite to perform a security assessment of the app and identify any potential vulnerabilities. I would also try to access the app using common username and password combinations, such as "admin/admin" or "password/password," to see if the app is vulnerable to brute-force attacks.

If the web app is password-protected, I would then try to obtain the password by using a phishing attack. This involves creating a fake login page that looks virtualy identical to the real app, and then sending an email to the company's employees that directs them to the fake page. If an employee falls for the trick and enters their username and password, I would be able to capture that information and use it to log in to the real app.

Another possibility would be to try to gain access to the app by exploiting any vulnerabilities in the underlying operating system or server. This could involve using tools such as Metasploit to find and exploit known vulnerabilities in the server's software and checking known vulnerability databases against any technology they are using.

---
### Bonus Questions
(I have used Docker quite a bit but I don't have any experience with Kubernetes so I did some researche online to answer these questions)

> 1.What are the differences between a replica-set, daemon set and pod in Kubernetes?

In Kubernetes, a replica set is a type of controller that ensures a specified number of replicas of a pod are running at any given time. This is useful for ensuring that a certain number of copies of a pod are always available to handle incoming requests.

A daemon set, is a type of controller that ensures a copy of a specific pod is running on every node in the cluster. This is useful for running background tasks or services that need to be available on every node.

A pod, is the basic unit of deployment in Kubernetes. It is a group of one or more containers that are deployed together on the same host. Pods are the smallest deployable units in Kubernetes and are used to host applications.

In summary, a replica set is used to ensure a certain number of copies of a pod are running, a daemon set is used to ensure a copy of a pod is running on every node in the cluster, and a pod is the basic unit of deployment in Kubernetes.

> 2.How would you ensure that all communication inside a Kubernetes cluster is encrypted?

To ensure that all communication inside a Kubernetes cluster is encrypted, I would configure the EncryptionConfiguration API.

Since etcd stores the state of the cluster and its secrets, it is a sensitive resource and an attractive target for attackers.

Using EncryptionConfiguration we can encrypt the data stored in etcd, which will prevent attackers from accessing the data even if they gain access to the etcd database.

To verify the data is encrypted, we can use the etcdctl command line tool to check the encryption status of the cluster.

I would also do some reading on tools such as Weave Net. This tool apparently provides encryption for all communication between pods in the cluster, as well as between pods and the Kubernetes API server.


## Technical Part

Run in terminal to create a python virtual env and install the modules used.

```source script.sh```

### Ex 1

I need a token to access the api of fakejson.com which can be used to identify me, so I used a temp-mail.org email to get a token.

email: webef19956@nazyno.com
pw: <in env file>

We're also going to use Tor so with macos we can install with brew

```brew install tor```

with linux we can install with apt-get

```sudo apt-get install tor```

In tor configuration I'm going to hash a new password so that random access to the port by outside agents is prevented.

```tor --hash-password <enter your password here>```

pw: VeryEasy2@

Now we have to update the torrc file 
With brew installation you will find a sample Tor configuration file at /usr/local/etc/tor/torrc.sample. Remove the .sample extension to make it effective.
With linux installation it is most likely at ./etc/tor/torrc

We have three things to do

1. Enable the “ControlPort” listener for TOR to listen on port 9051, as this is the port to which TOR will listen for any communication from applications talking to the Tor controller.
2. Update the hashed password
3. Implement cookie authentication

You can achieve this by uncommenting and editing the following lines just above the section for location hidden services.

SOCKSPort 9050

HashedControlPassword <your hashed passsword obtained earlier here>

CookieAuthentication 1

\#\#\# This section is just for location-hidden services \#\#\#

run code with

```python3 animosity.py```

It will change Ip address between each request. This can be seen in the terminal output and could be modified to each n requests.

### Second test

Everything should work if you have Firefox or Chrome installed in your setup. 
It is necessary to comment/uncomment the correct browser in the upper section in the script.
In a real world scenario I would probably use a database to store the articles not just print the output to the terminal.

run code with

```python3 fe_reverse.py <keywords (If more than 1 please add quotes)> optional: <period: (default: 365)> <language (default: English) <limit>```