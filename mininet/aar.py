from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.link import TCLink, TCULink, OVSLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info

import time

def aar():
    net = Mininet(controller=RemoteController, link=TCULink)

    node_num = 10

    # Create switches
    for i in range(1, node_num + 1):
        net.addSwitch('s%d' %i)

    # Create nodes
    for i in range(1, node_num + 1):
        net.addHost('h%d' %i, ip = '10.0.0.%d' %i)

    print "*** Creating host-switch links"
    for i in range(1, node_num + 1):
        net.addLink('h%d'%i, 's%d' %i, bw=20)

    print "*** Creating switch-switch links"
    link_from = [1,2,2,3,3,5,4,8,9,]
    link_to =   [2,3,4,5,7,6,8,9,10]

    #create links between switches with bandwidth (bw)
    for lf, lt in zip(link_from, link_to):
        if lf == 1 and lt == 2: # link's capacity from sw1 to sw2 need to be larger to prevent bottle necks
            net.addLink('s%d' % int(lf), 's%d' % int(lt), bw=40)
        elif (lf == 2 and lt == 3) or (lf == 2 and lt == 4):
            net.addLink('s%d' % int(lf), 's%d' % int(lt), bw=15)
        else:
            net.addLink('s%d' % int(lf), 's%d' % int(lt), bw=10)
    # Add Controllers
    c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    net.start()
    CLI( net )

    for host in net.hosts:
        print(host)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    aar()
    