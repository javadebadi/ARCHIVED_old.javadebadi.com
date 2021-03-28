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

# INDENT UNIT
INDENT = "    "       
# top directory
ROOT_PATH = os.getcwd()
# Frontend directory
FRONTEND_PATH = os.path.join(ROOT_PATH, "frontend")
# path for directory where js files after build will be placed there
DIST_PATH = os.path.join(FRONTEND_PATH, "dist")
# backend directory
BACKEND_PATH = os.path.join(ROOT_PATH, "backend")
# backend settings directory path
BACKEND_SETTINGS_DIRECTORY_NAME = "backend_project" 
BACKEND_SETTINGS_PATH = os.path.join(BACKEND_PATH, BACKEND_SETTINGS_DIRECTORY_NAME)
# frontend ROOT string to use inside django settings
FRONTEND_ROOT_STRING = """FRONTEND_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend", "dist", "frontend"))"""
# string to add to urls of django to direct all requests to frontend
URL_PATTERNS_FOR_FRONTEND_STRING ="""re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.FRONTEND_ROOT}),"""
# string to import backend settings
IMPORT_BACKEND_SETTINGS_STRING = f"""from {BACKEND_SETTINGS_DIRECTORY_NAME} import settings"""

class PythonScriptWriter:
    """A class to write into .py files"""
    def appendToPythonList(self, file_path, new_items, list_name):
        lines = []
        items = []
        list_end_line = 0
        list_started = False
        list_ended = False
        with open(file_path, "r") as f:
            for line_num, line in enumerate(f.readlines()):
                if (list_name in line):
                    if (r"[" in line):
                        list_started = True
                    if (r"]" in line):
                        raise ValueError("the list in python script must be in two lines at least")
                if (list_started is True) and (list_ended is False):
                    items.append(line)
                    if r"]" in line:
                        list_ended = True
                        list_end_line = line_num
                    
                lines.append(line)
        for i, elem in enumerate(items):
            new_elem = elem.replace(INDENT,"").strip() + "\n"
            items[i] = new_elem

        with open(file_path, "w") as f:
            for item in new_items:
                if item.endswith("\n"):
                    item = item[:len(item)-1]
                if not item.endswith(","):
                    item = item + ","
                item = item + "\n"
                    
                if not(item in items):
                    print(items)
                    lines.insert(list_end_line, INDENT + item)
                    list_end_line += 1
                        
            lines = "".join(lines)
            f.write(lines)

    def addImport(self, file_path, new_import_stmts=[]):
        "adds an import statement into a python scirpt"
        lines = []
        imports_current = 0
        imports_stmts = []
        with open(file_path, "r") as f:
            for line_num, line in enumerate(f.readlines()):
                if ("import" in line):
                    imports_current = line_num
                    imports_stmts.append(line)
                lines.append(line)

        with open(file_path, "w") as f:
            for import_stmt in new_import_stmts:
                if not(import_stmt in imports_stmts) and not(import_stmt+"\n" in imports_stmts) :
                    imports_current += 1
                    if import_stmt.endswith("\n"):
                        lines.insert(imports_current, import_stmt)
                    else:
                        lines.insert(imports_current, import_stmt+"\n")
                        
            lines = "".join(lines)
            f.write(lines)


class Operate:

    def __init__(self, operation_kind, operation_arg):
        self.pywriter = PythonScriptWriter()
        self.operation_kind = operation_kind
        self.operation_arg = operation_arg
        if self.operation_kind not in ["create", "build", "run", "all", "clean", "install"]:
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


    # create project ----------------------------------------------------
    def _createProxyConfJsonString(self):
        proxy_conf_json = "{\n"
        proxy_conf_json += '\t"/api": {\n'
        proxy_conf_json += '\t\t"target": "http://localhost:8000/",\n'
        proxy_conf_json += '\t\t"secure": false\n'
        proxy_conf_json += '\t},\n'
        proxy_conf_json += '\t"/oauth": {\n'
        proxy_conf_json += '\t\t"target": "http://localhost:8000/",\n'
        proxy_conf_json += '\t\t"secure": false\n'
        proxy_conf_json += '\t}\n'
        proxy_conf_json += "}\n"
        return proxy_conf_json
    
    def _addFrontendRootToBackendSettings(self):
        os.chdir(BACKEND_SETTINGS_PATH)
        lines = []
        with open("settings.py") as f:

            for line in f.readlines():
                if line.startswith("FRONTEND_ROOT"):
                    continue
                lines.append(line)
            lines.append("\n\n")
            lines.append(FRONTEND_ROOT_STRING)
        lines = "".join(lines)
        while "\n\n\n" in lines:
            lines = lines.replace("\n\n\n", "\n\n")
        with open("settings.py", "w") as f:
            f.write(lines)

    def _addFrontendURLtoBackendURLPatterns(self):
        os.chdir(BACKEND_SETTINGS_PATH)
        self.pywriter.addImport("urls.py", 
                          new_import_stmts=[
                                "from django.urls import include",
                                "from django.urls import re_path",
                                "from django.conf.urls.static import static",
                                "from django.conf.urls.static import serve",
                                IMPORT_BACKEND_SETTINGS_STRING,
                        ])
        self.pywriter.appendToPythonList("urls.py", [URL_PATTERNS_FOR_FRONTEND_STRING], "urlpatterns")

    def _createFrontend(self):
        os.chdir(FRONTEND_PATH)
        proxy_conf_json = self._createProxyConfJsonString()
        with open("proxy.conf.json", "w") as f:
            f.write(proxy_conf_json)

    def _createBackend(self):
        os.chdir(BACKEND_PATH)
        self._addFrontendRootToBackendSettings()
        self._addFrontendURLtoBackendURLPatterns()

    def create(self):
        if self.operation_arg == "-F" or self.operation_arg == "--frontend":
            self._createFrontend()
        elif self.operation_arg == "-B" or self.operation_arg == "--Backend":
            self._createBackend()
        elif self.operation_arg == "-A" or self.operation_arg == "--all":
            self._runProcesses(self._createFrontend, self._createBackend)
        elif self.operation_arg == None:
            self._runProcesses(self._createFrontend, self._createBackend)
    # --------------------------------------------------------------- create

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
        if self.operation_kind == "create":
            self.create()
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
