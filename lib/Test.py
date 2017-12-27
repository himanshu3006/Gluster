from create_gluster import creategluster, delete_gluster
from create_gluster import gluster_status, fio_start, fio_install
from robotpageobjects import Page,robot_alias
import logging
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
#import unittest


#class Test(unittest.TestCase):
class Test():
    @robot_alias("install__gluster")
    def install__gluster(self):
        print "before setup"
        print("Installing Gluster intio the system")
        print("executing commands squentially")
        creategluster()
        print("Successfully executed commands successfully")
        # self.install_gluster = creategluster()
        #creategluster()
        # self.assertAlmostEquals()=creategluster()
        # fio_install()
        print "After setup"
    @robot_alias("getting__status")
    def getting__status(self):
        print "A before trigger"
        print "Printing the status of the Gluster"
        gluster_status()
        # result = self.assertEqual(3 + 3, 7)
        # print "A result is "+str(result)
        # print "A printting after the assert"
        # fio_start()
        print "A After io trigger"
    @robot_alias("trigger__fio")
    def trigger__fio(self):
        print "B before trigger"
        print "Getting current state of the gluster"
        # gluster_status()
        fio_start()
        # result = self.assertEqual(3 + 3, 5)
        #
        # print "B result is "
        # print "B printting after the assert"
        # # fio_start()
        print "B After io trigger"

    @robot_alias("unstalling__gluster")
    def unstalling__gluster(self):
        print "Before teardown"
        # delete_gluster()
        print "Uninstalling the gluster from the system"
        print "After teardown\n\n\n"

    @robot_alias("creating__repo")
    def creating__repo(self):
        logger.info("Command executing please wait..")
	logger.info("sudo mkdir Gluster_Project")

    @robot_alias("insert__data")
    def insert__data(self):
   	logger.info("Command executing please wait..")
        logger.info("Inserting information in the form of files")

    @robot_alias("validating__data")
    def validating__data(self):
        logger.info("Command executing please wait..")
        logger.info("validating...")

    @robot_alias("collecting__data")
    def collecting__data(self):
        logger.info("Command executing please wait..")
        logger.info("Collecting data from source")

    @robot_alias("pushing__data")
    def pushing__data(self):
        logger.info("Command executing please wait..")
        logger.info("pushing data please wait...")

    @robot_alias("validate__receive")
    def validate__receive(self):
        logger.info("Command executing please wait..")
        logger.info("validating receive")

    @robot_alias("install__cli")
    def install__cli(self):
        logger.info("Command executing please wait..")
        logger.info("Installing contineous integration tool")

    @robot_alias("creating__job")
    def creating__job(self):
	logger.info("Command executing please wait..")
        logger.info("creating job in tool")

    @robot_alias("config__project")
    def triggering__job(self):
        logger.info("Command executing please wait..")
        logger.info("config ...")

    @robot_alias("config__job")
    def config__job(self):
        logger.info("Command executing please wait..")
        logger.info("config ...")

    @robot_alias("triggering__job")
    def triggering__job(self):
        logger.info("Command executing please wait..")
        logger.info("trigger ...")

    @robot_alias("editing__job")
    def editing__job(self):
        logger.info("Command executing please wait..")
        logger.info("editing ...")

    @robot_alias("checking__job")
    def checking__job(self):
        logger.info("Command executing please wait..")
        logger.info("trigger ...")

    @robot_alias("checking__data")
    def triggering__data(self):
        logger.info("Command executing please wait..")
        logger.info("trigger ...")

    @robot_alias("editing__data")
    def editing__data(self):
        logger.info("Command executing please wait..")
        logger.info("editing ...")

    @robot_alias("validate__fail")
    def validate__fail(self):
        logger.info("Command executing please wait..")
        logger.info("validating receive")

    @robot_alias("deleting__job")
    def deleting__job(self):
        logger.info("Command executing please wait..")
        logger.info("deleting job in tool")

    @robot_alias("uninstall__cli")
    def uninstall__cli(self):
        logger.info("Command executing please wait..")
        logger.info("Uninstalling contineous integration tool")
 
    @robot_alias("update__cli")
    def update__cli(self):
        logger.info("Command executing please wait..")
        logger.info("Updating contineous integration tool")

    @robot_alias("download__cli")
    def download__cli(self):
        logger.info("Command executing please wait..")
        logger.info("Downloading contineous integration tool")

    @robot_alias("remove__project")
    def remove__project(self):
        logger.info("Command executing please wait..")
        logger.info("Removing project")

    @robot_alias("rechecked__cli")
    def rechecked__cli(self):
        logger.info("Command executing please wait..")
        logger.info("Rechecking contineous integration tool")

    @robot_alias("verified__project")
    def verified__project(self):
        logger.info("Command executing please wait..")
        logger.info("Verifying the project")

    @robot_alias("add__newproject")
    def add__newproject(self):
        logger.info("Command executing please wait..")
        logger.info("Adding new  project")

    @robot_alias("push__newjob")
    def push__newjob(self):
        logger.info("Command executing please wait..")
        logger.info("Push new job from the Gluster")

    @robot_alias("generate__req")
    def generate__req(self):
        logger.info("Command executing please wait..")
        logger.info("Generate request from the project")

    @robot_alias("customized__project")
    def customized__project(self):
        logger.info("Command executing please wait..")
        logger.info("Customized the project")

    @robot_alias("pull_req")
    def pull__req(self):
        logger.info("Command executing please wait..")
        logger.info("Pulling request from the project")

    @robot_alias("export__project")
    def export__project(self):
        logger.info("Command executing please wait..")
        logger.info("Exporting the project")

    @robot_alias("import__project")
    def import__project(self):
        logger.info("Command executing please wait..")
        logger.info("Importing the project")

    @robot_alias("unchecked__data")
    def unchecked__data(self):
        logger.info("Command executing please wait..")
        logger.info("Unchecking the project")

    @robot_alias("upgrade__project")
    def upgrade__project(self):
        logger.info("Command executing please wait..")
        logger.info("Upgrading the project")

    @robot_alias("copy__project")
    def copy__project(self):
        logger.info("Command executing please wait..")
        logger.info("Copying the project")

    @robot_alias("release__project")
    def release__project(self):
        logger.info("Command executing please wait..")
        logger.info("Releasing the project")

    @robot_alias("change__job")
    def change__job(self):
        logger.info("Command executing please wait..")
        logger.info("Changing job in  the project")

    @robot_alias("refresh__data")
    def refresh__data(self):
        logger.info("Command executing please wait..")
        logger.info("Refreshing data in the project")


if __name__ == "__main__":
    #unittest.main()
    print "before"
    Test()
