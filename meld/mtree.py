import sys

__author__ = 'alberto'

### Clase multi arbol

class MTree():

    def __init__(self, name):
        self.name = name
        self.childs = []

    def getName(self):
        return self.name

    def getChilds(self):
        return self.childs

    def addChild(self, node):
        self.childs.append(node)
        self.childs.sort()

    def hasChild(self, node):
        result = False
        for item in self.childs:
            if item.getName() == node:
                result = True
                break
        return result

    def countChilds(self):
        return len(self.childs)

    def getChild(self, node):
        for item in self.childs:
            if item.getName() == node:
                return item
        return None

    def imprimir(self, space=""):
        if self.countChilds():
            hijos = ""
            for item in self.childs:
                hijos += item.getName() + ", "
            hijos = hijos[:-2]
            name = space + self.name + ": "
            print name + hijos
            space = ""
            for i in range(len(name)):
                space += " "
            
            for item in self.childs:
                item.imprimir(space)
        else:
            print space + self.name

    def contains_path(self, path):
        resultado = False
        path_items = path.split("/")
        tree = self;
        for pit in path_items:
            resultado = tree.countChilds()
            if resultado:
                resultado = tree.hasChild(pit)
                if resultado:
                    tree = tree.getChild(pit)
                else:
                    break
            else:
                break
        return resultado

def print_rsync_file(filename):

    """Imprime el archivo"""
    rsync_file = open(filename, "r")
    print rsync_file.read()
    rsync_file.close()

def parse_rsync_file(filename):

    """Construye un arbol de directorios a partir de la lista pasada en el archivo"""
    rsync_file = open(filename, "r")
    rsync_paths = rsync_file.readlines()
    rsync_file.close()
    root = MTree("inicio")
    tree = root
    for file in rsync_paths:
        path_items = file.split("/")
        tree = root
        for item in path_items:
            item = item.replace("\n","")
            if not len(item):
                continue
            if tree.hasChild(item):
                tree = tree.getChild(item)
            else:
                item_tree = MTree(item)
                tree.addChild(item_tree)
                tree = item_tree
    return root

def main():
    print_rsync_file(sys.argv[1])
    tree = parse_rsync_file(sys.argv[1])
    tree.imprimir()

    def contiene(tree, path):

        """Utileria para test"""
        if tree.contains_path(path):
           print path + " EXISTE"
        else:
            print path + " NO CONTENIDO"

<<<<<<< HEAD
    contiene(tree, "Integralia/trunk/base/maestros/comunes/MaeDatosLogisticos.java")
    contiene(tree, "Integralia/trunk/base/objetosbd/Set.java")
    contiene(tree, "Integralia/trunk/base/objetosbd/Usuario.java")
    contiene(tree, "Integralia/trunk/base/objetosbd/logistica/")
    contiene(tree, "Integralia/trunk/base/objetosbd/logistica/PrioridadProvLog.java")
    contiene(tree, "Integralia/trunk/base/procesos/configuracion/ComboBoxAutoCompLaunchEnter.java")
    contiene(tree, "Integralia/trunk/base/procesos/configuracion/ConfiguracionTablas.java")
    contiene(tree, "Integralia/trunk/base/ui/actions/OpenKeyFormAction.java")
    contiene(tree, "Integralia/trunk/base/ui/dialog/LoginDialog.java")
    contiene(tree, "Integralia/trunk/base/util/ConstantesIntegra.java")
    contiene(tree, "Integralia/trunk/base/util/ConversorFormato.java")

    contiene(tree, "Integralia/trunk/base/maestros/comunes/MaeDatosLosticos.java")
    contiene(tree, "Integralia/trunk/base/objetosbd")
    contiene(tree, "Integralia/trunk/base/objetosbd/")
    contiene(tree, "Integralia/trunk/bas")
    contiene(tree, "Integralia/trunk/base/objetosbd/logistica/PrioridadProvLog.java")
    contiene(tree, "Integralia/trunk/procesos/configuracion/ComboBoxAutoCompLaunchEnter.java")
    contiene(tree, "Integralia/trunk/base/procesos/configuracion/ConfiguracionTablas.java")
    contiene(tree, "Integralia/trunk/base/ui/actions/OpenKeyFormAction.ja")
    contiene(tree, "base/ui/dialog/LoginDialog.java")
=======
>>>>>>> 4f00fb3... Cambios para utilizar las diferencias detectadas por rsync (y evitar una
    contiene(tree, "hola")
    contiene(tree, "adios/eco")

if __name__ == "__main__":
    main()

