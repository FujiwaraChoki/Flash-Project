# Flash-Project
This Project is all about malware (malicious software). In this repository you'll find everything from Keyloggers, up to Reverse Shells.
All is written and made by me, an individual (Sami Hindi).

# How to run
To run this Key/Mouse-Logger, you must have python 3 or above installed, if you don't have python 3 or above installed on your machine,
<a href="https://www.python.org/downloads/">download the most recent version of python</a> from their official website.

# Docs
<h3><b>flashconsole</b></h3>
The "flashconsole" is used to work with Reverse Shells.
A Reverse Shell is when you get the victim computer to install malicious code or software on their system. When that file is run, you will have a fully interactive shell, where you can do all kidns of things.
Here are all the commands of the <b>flashconsole</b>:
<ul>
  <li>flashrs <--create/--listen> <TARGET_HOST> <LISTENING_HOST> <PORT></li>
    <ul>
      <li>--create  -  This will switch to creating mode, meaning it will create a backdoor file.</li>
      <li>--listen  -  Using --listen will switch to listening mode, which means the backdoor is installed on the victim's machine, but not run yet.
        <ul>
          <li>TARGET_HOST  -  TARGET_HOST specifies the hostname or IP the backdoor will send a connection to. This will only work if you and the victim are in the same network, except if you have Port-Forwarding enabled in your Router-Settings for that specific Port, or have setup an SSH-Tunnel (I recommend NGROK).</li>
          <li>LISTENING_HOST  -  This is the Bind-Address basically, it is usually localhost, which is set as the default.</li>
          <li>PORT  -  Exactly what it says, this will specify the port you're using to connect to the vitim's machine.
        </ul>
    </ul>
</ul>

# License
This Repository and all of it's contents are licensed under GNU General Public License V3.0

# Feedback
I would appreciate Feedback, since this Project was created a couple weeks ago. For Feedback, please write an E-Mail to <a href="mailto::fujiwarachoki@zohomail.eu>fujiwarachoki@zohomail.eu</a>

Thanks and have fun using it!

<i>Educational Purposes only</i>
