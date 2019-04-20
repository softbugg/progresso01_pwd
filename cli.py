from typing import List, Any

from program import computer
import sys

params = sys.argv


if len(params) > 1:
    if params[1] == "--os" or params[1] == "--system":
        print("Sistema Operacional: ", computer.os())
        print("Versao: ", computer.version())

    elif params[1] == "--name":
        print("Node de Rede:", computer.name())

    elif params[1] == "--distro":
        print("Distribuição: ", computer.distro())

    elif params[1] == "--process" or params[1] =="--cpu":
        print("Processador: ", computer.cpu())

    elif params[1] == "--arc":
        print("Arquitetura da Maquina: ", computer.arch())

    else:
        print('Erro! Parametro desconhecido')

else:
    print("Sistema Operacional", computer.os())

