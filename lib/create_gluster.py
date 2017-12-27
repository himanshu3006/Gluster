import subprocess
from robot.api import logger
import time
#import pexpect
import logging
def creategluster():
    gluster_creation= ["cd",
                     "sudo apt-get install -y lsb-release",
                     "sudo apt-get install -y apt-transport-https",
                     "wget -O - http://download.gluster.org/pub/gluster/glusterfs/LATEST/rsa.pub | sudo apt-key add -",
                     "echo deb https://download.gluster.org/pub/gluster/glusterfs/LATEST/Debian/$(lsb_release -sc)/apt $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/gluster.list",
                     "sudo apt-get install -y software-properties-common",
                       # sudo apt autoremove
                     "sudo add-apt-repository ppa:gluster/glusterfs-3.8",
                     "sudo apt-get update",
                     "sudo apt-get install -y glusterfs-server",
                     "sudo service glusterfs-server start"]
    # GlusterFS components use DNS for name resolutions, so configure either DNS or set up a hosts entry.
    # If you do not have a DNS on your environment, modify / etc / hosts file and update it accordingly.

    #Before proceeding to the installation, we need to configure GlusterFS repository on both storage nodes.
    # Follow the instruction to add the repository to your system.

    #Install support package for https transactions

    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                        )
    for i in range(len(gluster_creation)):
        try:
            # subprocess.Popen('cd',shell=True, stdout=subprocess.PIPE)
            proc=subprocess.Popen([gluster_creation[i]], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
           # child = pexpect.spawn(gluster_creation[i])
           # child.expect('Password:')
            #child.sendline('ivtree123')
            #child.sendline('Helloivtree')
            if(gluster_creation[i]==7):
		proc.stdin.write('ivtree123\n')
		proc.stdin.flush()
	    #print "before wait"
            proc.wait()
            #print "after wait"
            #logging.debug("%s"%gluster_creation[i]+" is Executed successfully\n")
            
	    output = proc.stdout.read()
            #logging.debug("process read" + output+"\n")
	    logger.info(gluster_creation[i]+" command executed  result is: "+output+"\n")

        except  subprocess.CalledProcessError as e:
            print "Called Process Error while  executing command %s"+gluster_creation[i]

    print "successfully created gluster"

def gluster_status():
    try:

        logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                            )
        proc=subprocess.Popen(['sudo service glusterfs-server status'], shell=True, stdout=subprocess.PIPE)
        #print "before wait"
        proc.wait()
        #print "after wait"
        output = proc.stdout.read()
        #logging.debug("process read" + output+"\n")
        #logging.debug("sudo service glusterfs-server status is Executed successfully\n")
	logger.info("Gluster status command executed  result is: "+output+"\n")
	#if(output==" ")
	#	logger.info("Gluster status commans=d fail")
	#	raise AssertionError("Test Failed")

    except subprocess.CalledProcessError as e:
        print "Called Process Error while executing command"
        logger.info("status of gluster command fail")
	raise AssertionError("Test Failed")

def delete_gluster():
    gluster_deletion = ["cd",
                        "sudo apt-get --yes remove -y lsb-release",
                        "sudo apt-get --yes remove -y apt-transport-https",
                        "wget -O - http://download.gluster.org/pub/gluster/glusterfs/LATEST/rsa.pub | sudo apt-key remove -",
                        "sudo apt autoremove"
                        "sudo apt-get --yes remove -y glusterfs-server"]
    for i in range(len(gluster_deletion)):
        try:
            logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
            proc=subprocess.Popen([gluster_deletion[i]], shell=True, stdout=subprocess.PIPE)
            #print "before wait"
            proc.wait()
            #print "after wait"
            output=proc.stdout.read()
            #logging.debug("process output "+str(i)+" is "+output+"\n")
	    logger.info("gluster deleted command executed  result is: "+output+"\n")

        except subprocess.CalledProcessError as e:
            print "Called Process Error while executing command"
    #Deleting gluster info
    p1=subprocess.Popen(['sudo rm -rf /etc/apt/sources.list.d/gluster.list'], shell=True, stdout=subprocess.PIPE)
    p1.wait()
    # Removing locks
    p2=subprocess.Popen(['sudo rm /var/lib/dpkg/lock'],shell=True, stdout=subprocess.PIPE)
    p2.wait()

def fio_start():
    try:
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s', )
	logger.info("fio jobs are triggred and started please wait it will take more time..")

        proc=subprocess.Popen(['fio --name=randwrite --ioengine=libaio --iodepth=1 --rw=randwrite --bs=4k --direct=0 --size=512M --numjobs=8 --runtime=240 --group_reporting'], shell=True, stdout=subprocess.PIPE)
        #print "before wait"
        proc.wait()
        #print "after wait"
        logging.debug("fio jobs started\n")
        output = proc.stdout.read()
        #logging.debug("process output is " + output+"\n")
	logger.info("fio jobs command executed thanks for wait result is: "+output+"\n")
    except subprocess.CalledProcessError as e:
        print "Called Process Error while executing command"

def fio_install():
    try:
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s', )
        proc=subprocess.Popen(['apt-get --yes install fio'], shell=True, stdout=subprocess.PIPE)
        #print "before wait"
        proc.wait()
        #print "after wait"
        #logging.debug("fio successfully installed\n")
	logger.info("fio successfully installed\n")
        output = proc.stdout.read()
        #logging.debug("process output is " + output+"\n")
	logger.info("Result of fio install command is: "+output+"\n")

    except subprocess.CalledProcessError as e:
        print "Called Process Error while executing command"

def add_storage():
    std=["cd",
         "sudo fdisk /dev/sdb",
         "n",
         "p",
         "1"
         "\n",
         "\n",
         "p",
         "w",
         "sudo mkfs.ext4 /dev/sdb1",
         "sudo mkdir -p /data/gluster2",
         "sudo mount /dev/sdb1 /data/gluster2",
         "echo "+"/dev/sdb1 /data/gluster2 ext4 defaults 0 0"+" | sudo tee --append /etc/fstab"]
    for i in range(len(std)):
        try:
            logging.basicConfig(level=logging.DEBUG,
                            format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
            proc=subprocess.Popen([std[i]], shell=True, stdout=subprocess.PIPE)
            #print "before wait"
            proc.wait()
            #print "after wait"
            output=proc.stdout.read()
            #logging.debug("process output "+str(i)+" is "+output+"\n")
	    logger.info("successfully added storage\n")

        except subprocess.CalledProcessError as e:
            print "Called Process Error while executing command"





def clone_create():
    proc = subprocess.Popen(['ch'], shell=True, stdout=subprocess.PIPE)
    # child = pexpect.spawn()
    # child.expect('Password:')
    # child.sendline('ivtree123')


if __name__ == '__main__':

    print "programing start"
    # pinging()
    # creategluster()
    # gluster_status()
    # delete_gluster()
    # fio_install()
    # fio_start()
    # add_storage()
    #add_storage()

