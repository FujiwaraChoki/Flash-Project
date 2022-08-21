# Flash-Project
This Project is all about malware (malicious software). In this repository you'll find everything from Keyloggers, up to Reverse Shells.
All is written and made by me, an individual (Sami Hindi).

# How to run
To run this All-Purpose Hacking-Tool, you must have python 3 or above installed, if you don't have python 3 or above installed on your machine,
<a href="https://www.python.org/downloads/">download the most recent version of python</a> from their official website.

# Documentation (Outdated)
<h3><b>flashconsole</b></h3>
The "flashconsole" is used to work with Reverse Shells.
A Reverse Shell is when you get the victim computer to install malicious code or software on their system. When that file is run, you will have a fully interactive shell, where you can do all kidns of things.
Here are all the commands of the <b>flashconsole</b>:
<ul>
  <li><b>flashrs <--create/--listen> < OPTIONS ></b></li>
    <ul>
      <li>--create  -  This will switch to creating mode, meaning it will create a backdoor file.</li>
      <ul>
        <li>First Positional Argument -> TARGET_HOST  -  Target Host specifies the hostname or IP the backdoor will send a connection to. This will only work if you and the victim are in the same network, except if you have Port-Forwarding enabled in your Router-Settings for that specific Port, or have setup an SSH-Tunnel (I recommend NGROK).</li>
        <li>Second Positional Argument -> TARGET_PORT  -  Target Port specifies the port on which it will be sending the connection to the target host with
      </ul>
      <li>--listen  -  Using --listen will switch to listening mode, which means the backdoor is installed on the victim's machine, but not run yet.
        <ul>
          <li>First Positional Argument -> LISTENING_HOST  -  This is the Bind-Address basically, it is usually localhost, which is set as the default.</li>
          <li>Second Positional Argument -> PORT  -  Exactly what it says, this will specify the port you're using to connect to the vitim's machine.</li>
        </ul>
    </ul>
    <li><b>flashddos --start < OPTIONS ></b></li>
    <ul>
      <li>Type  -  Specifies the type of Attack that will be sent. There are currently two available Attacks:</li>
      <ul>
        <li>-b  -  A basic DDoS Attack with Threading</li>
        <ul>
          <li>First Positional Argument -> Target  -  Specifies the target which the attack will be sent to</li>
          <li>Second Positional Argument -> Proxy File Location  -  When running a DDoS Attack, proxies are inevitable if you do not want to get caught. So this argument specifies the location the proxy file. It should be stored in a combo, like this for example: <b>192.168.300.1:8080</b></li>
          <li>Third Positional Argument -> Threads  -  This specifies the amount of Threads you want your Attack to run with, the recommended amount is 500 - 1000.</li>
        </ul>
        <li>-s  -  A Synflood Attack without Threading, since already powerful without</li>
        <ul>
          <li>First Positional Argument -> Target  -  Specifies the target which the attack will be sent to</li>
          <li>Second Positional Argument -> Proxy File Location  -  When running a DDoS Attack, proxies are inevitable if you do not want to get caught. So this argument specifies the location the proxy file. It should be stored in a combo, like this for example: <b>192.168.300.1:8080</b></li>
        </ul>
      </ul>
    </ul>
</ul>

# License
This Repository and all of it's contents are licensed under GNU General Public License V3.0

# Feedback
I would appreciate Feedback, since this Project was created a couple weeks ago. For Feedback, please write an E-Mail to sami@samihindi.com.

Thanks and have fun using it!

<i>Educational Purposes only</i>
