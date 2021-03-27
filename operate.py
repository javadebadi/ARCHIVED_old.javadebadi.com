# A code to have command line tools to install, clean, build, and run 
# both frontend (Django) and backend (Angular) projects together
# Date: Mar 28, 2021
# Author: Javad Ebadi
import os
import sys
import shutil
from multiprocessing import Process

# get the kind of build
if len(sys.argv) < 2:
    raise ValueError("an argument must be given for operate.py")
elif len(sys.argv) >= 2:
    OPERATION_KIND = sys.argv[1]
    if len(sys.argv) == 2:
        OPERATION_ARG = None
    elif len(sys.argv) == 3:
        OPERATION_ARG = sys.argv[2]
       
# top directory
ROOT_PATH = os.getcwd()
# Frontend directory
FRONTEND_PATH = os.path.join(ROOT_PATH, "frontend")
# path for directory where js files after build will be placed there
DIST_PATH = os.path.join(FRONTEND_PATH, "dist")
# backend directory
BACKEND_PATH = os.path.join(ROOT_PATH, "backend")



class Operate:

    def __init__(self, operation_kind, operation_arg):
        self.operation_kind = operation_kind
        self.operation_arg = operation_arg
        if self.operation_kind not in ["build", "run", "all", "clean", "install"]:
            raise ValueError(f"the given argument {self.operation_kind} is not valid")
        if self.operation_arg not in [None, "-A", "--all", "-F",
                                    "--frontend", "-B", "--backend"]:
            raise ValueError(f"the given argument {self.operation_arg} is not valid")

    def _runProcesses(self, func1, func2):
        """a function to run processes simultaneously"""
        p1 = Process(target=func1)
        p1.start()
        p2 = Process(target=func2)
        p2.start()
        p1.join()
        p2.join()


    # clean project ----------------------------------------------------
    def _cleanFrontend(self):
        os.chdir(FRONTEND_PATH)
        if os.path.isdir(DIST_PATH):
            shutil.rmtree(DIST_PATH)

    def _cleanBackend(self):
        os.chdir(BACKEND_PATH)
        # get list of all directories inside backend directory
        # such that all of them is a __pycache__ directory
        # dirs_list = [x[0] for x in os.walk(BACKEND_PATH) if (('.venv' not in x[0]) and x[0].endswith('__pycache__'))]
        dirs_list = [x[0] for x in os.walk(BACKEND_PATH) if x[0].endswith('__pycache__')]
        for dir_path in dirs_list:
            if os.path.isdir(dir_path):
                print(f"DELETE {dir_path}")
                shutil.rmtree(dir_path)

    def clean(self):
        if self.operation_arg == "-F" or self.operation_arg == "--frontend":
            self._cleanFrontend()
        elif self.operation_arg == "-B" or self.operation_arg == "--Backend":
            self._cleanBackend()
        elif self.operation_arg == "-A" or self.operation_arg == "--all":
            self._runProcesses(self._cleanFrontend, self._cleanBackend)
        elif self.operation_arg == None:
            self._runProcesses(self._cleanFrontend, self._cleanBackend)
    # --------------------------------------------------------------- clean

    # install dependencies -------------------------------------------------
    def _installFrontend(self):
        os.chdir(FRONTEND_PATH)
        os.system("npm install")

    def _installBackend(self):
        os.chdir(BACKEND_PATH)
        os.system("python -m pip install -r requirements.txt")

    def install(self):
        if self.operation_arg == "-F" or self.operation_arg == "--frontend":
            self._installFrontend()
        elif self.operation_arg == "-B" or self.operation_arg == "--Backend":
            self._installBackend()
        elif self.operation_arg == "-A" or self.operation_arg == "--all":
            self._runProcesses(self._installFrontend, self._installBackend)
        elif self.operation_arg == None:
            self._runProcesses(self._installFrontend, self._installBackend)
    # --------------------------------------------------------------- install

    # build project  --------------------------------------------------------
    def _buildFrontend(self):
        os.chdir(FRONTEND_PATH)
        os.system("ng build --prod")

    def _buildBackend(self):
        os.chdir(BACKEND_PATH)
        os.system("pip freeze > requirements.txt")

    def build(self):
        if self.operation_arg == "-F" or self.operation_arg == "--frontend":
            self._buildFrontend()
        elif self.operation_arg == "-B" or self.operation_arg == "--Backend":
            self._buildBackend()
        elif self.operation_arg == "-A" or self.operation_arg == "--all":
            self._runProcesses(self._buildFrontend, self._buildBackend)
        elif self.operation_arg == None:
            self._runProcesses(self._buildFrontend, self._buildBackend)
    #  ------------------------------------------------------------------ build

    # run project  ------------------------------------------------------------
    def _runFrontend(self):
        os.chdir(FRONTEND_PATH)
        os.system("ng serve --open")

    def _runBackend(self):
        os.chdir(BACKEND_PATH)
        os.system("python manage.py runserver")

    def run(self):
        if self.operation_arg == "-F" or self.operation_arg == "--frontend":
            self._runFrontend()
        elif self.operation_arg == "-B" or self.operation_arg == "--Backend":
            self._runBackend()
        elif self.operation_arg == "-A" or self.operation_arg == "--all":
            self._runProcesses(self._runFrontend, self._runBackend)
        elif self.operation_arg == None:
            self._runProcesses(self._runFrontend, self._runBackend)
    #  ------------------------------------------------------------------ run


    def operate(self):
        if self.operation_kind == "install":
            self.install()
        if self.operation_kind == "run":
            self.run()
        if self.operation_kind == "clean":
            self.clean()
        if self.operation_kind == "build":
            self.clean()
            self.install()
            self.build()
        if self.operation_kind == "all":
            self.clean()
            self.install()
            self.build()
            self.run()
        return None

if __name__ == "__main__":
    OperateObj = Operate(OPERATION_KIND, OPERATION_ARG)
    OperateObj.operate()
